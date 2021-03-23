Ab-inito Numerical Analysos for particles as Molecular Dynamics simulation

From scratch coding and simulations of particles and interactions in a 2 D box. 

Using cython for frequently called functions and classes as acceleration of python


base_functions.py contains the Classes "Vector" (2D coordinate input), "Particle" (position, momentum, radius, mass) and "Simulation" (particles, box_dims, timesteps)

The position however will change. In a small amount of time $\Delta t$ the position will change via:

$$\vec{r}(t+\Delta t)=\vec{r}(t)+\vec{v}(t)\times \Delta t$$

where $\vec{r}(t)$ is the position at time $t$, $\vec{v}(t)$ is velocity and $\Delta t$ is the time step.


See the python notebook for details.
I have subsequently implemented from scratch:
- Particle Definitions
- 1D and 2D Collisions based on the dot product
- Account for difference of particles masses
- Implemented Physical quantities in terms of particle speeds and found it agrees with Maxwell-Boltzmann's distribution