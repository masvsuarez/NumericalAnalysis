Ab-inito Numerical Analysos for particles as Molecular Dynamics simulation

From scratch coding and simulations of particles and interactions in a 2 D box. 

Using cython for frequently called functions and classes as acceleration of python


base_functions.py contains the Classes "Vector" (2D coordinate input), "Particle" (position, momentum, radius, mass) and "Simulation" (particles, box_dims, timesteps)

The position however will change. In a small amount of time <img src="https://render.githubusercontent.com/render/math?math=\Delta t"> the position will change via:

<img src="https://render.githubusercontent.com/render/math?math=\vec{r}(t+\Delta t)=\vec{r}(t)+\vec{v}(t)\times \Delta t">

where <img src="https://render.githubusercontent.com/render/math?math=\vec{r}(t)"> is the position at time <img src="https://render.githubusercontent.com/render/math?math=t">, <img src="https://render.githubusercontent.com/render/math?math=\vec{v}(t)"> is velocity and <img src="https://render.githubusercontent.com/render/math?math=\Delta t"> is the time step.


See the python notebook for details.
I have subsequently implemented from scratch:
- Particle Definitions
- 1D and 2D Collisions based on the dot product
- Account for difference of particles masses
- Implemented Physical quantities in terms of particle speeds and found it agrees with Maxwell-Boltzmann's distribution
