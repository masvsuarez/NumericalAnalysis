from itertools import combinations
import pickle


# Vector definition
class Vector():
    def __init__(self, i1,i2):
        self.x = i1
        self.y = i2

    def __add__(self,other):
        return (Vector(self.x+other.x,self.y+other.y))

    def __sub__(self,other):
        return (Vector(self.x-other.x,self.y-other.y))

    def __mul__(self,other):
        return Vector(self.x*other,self.y*other)

    def __truediv__(self,other):
        return Vector(self.x/other,self.y/other)

    def __pow__(self,other):
        return Vector(self.x**other,self.y**other)

    def __repr__(self):
        return '{x} {y}'.format(x=self.x, y=self.y)

    def dot(self,other):
        return self.x*other.x + self.y*other.y

    def norm(self):
        return (self.x**2+self.y**2)**0.5

# Particle definition

class Particle():
    def __init__(self, position, momentum, radius, mass):
        self.position = position
        self.momentum = momentum
        self.radius = radius
        self.mass = mass
      
    def velocity(self):
        lala = self.copy()
        return lala.momentum / lala.mass
   
    def copy(self):
        return Particle(self.position, self.momentum, self.radius, self.mass)
    
    #taking into account theoretical particle overlap and discarding it
    def overlap(self, other_particle):
        allowed_distance = self.radius + other_particle.radius
        vector1 = self.copy()
        distancevec = vector1.position - other_particle.position
        actual_distance = distancevec.norm()
        return allowed_distance > actual_distance

# Simulation of particle collisions. 
    
class Simulation():
    def __init__(self, particles, box_length, dt):
        self.particles = particles
        self.box_length = box_length
        self.timestep = dt
        self.trajectory = []

    def apply_box_collisions(self, particle):
        # right
        if particle.position.x + particle.radius >= self.box_length and particle.momentum.x >= 0:
            particle.momentum.x = - particle.momentum.x
        # left
        elif particle.position.x - particle.radius <= 0 and particle.momentum.x <= 0:
            particle.momentum.x = - particle.momentum.x
        # top
        elif particle.position.y + particle.radius >= self.box_length and particle.momentum.y >= 0:
            particle.momentum.y = - particle.momentum.y
        # bottom
        elif particle.position.y - particle.radius <= 0 and particle.momentum.y <= 0:
            particle.momentum.y = - particle.momentum.y

    def apply_particle_collision(self, particle1, particle2):
        if particle1.overlap(particle2):
            normal = particle2.position - particle1.position
            # normalised normal between particles
            normalaxis = normal/normal.norm()
            momentum_norm1 = normalaxis * particle1.momentum.dot(normalaxis)
            momentum_tang1 = particle1.momentum - momentum_norm1 
            momentum_norm2 = normalaxis * particle2.momentum.dot(normalaxis)
            momentum_tang2 = particle2.momentum - momentum_norm2
            # checking whether particles collide
            totalmom = particle1.momentum - particle2.momentum
            if totalmom.dot(normalaxis) >= 0:
                #including difference in mass in the normal component
                momentum_mass1 = (momentum_norm1*(particle1.mass - particle2.mass) + momentum_norm2*(2*particle1.mass))/(particle1.mass + particle2.mass)
                momentum_mass2 = (momentum_norm2*(particle2.mass - particle1.mass) + momentum_norm1*(2*particle2.mass))/(particle1.mass + particle2.mass)
                particle1.momentum = momentum_tang1 + momentum_mass1
                particle2.momentum = momentum_tang2 + momentum_mass2

    def update_position(self, particle):
        particle.position = particle.position + (particle.velocity() * self.timestep)
            
    def step(self):
        for particle in self.particles:
            self.update_position(particle)
            self.apply_box_collisions(particle)
        for p1,p2 in combinations(self.particles,2):
            self.apply_particle_collision(p1,p2)
        self.record_state()

    def record_state(self):
        positions = []
        for particle in self.particles:
            positions.append(particle.copy())
        self.trajectory.append(positions)


















