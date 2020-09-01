## 26/08/2020

#### Task1 - "Nonadiabatic dynamics within the time dependent density functional theory:Ultrafast photodynamics in pyrazine" by Werner et al.
#### Aim of paper:
Treatment of radiationless transitions in Pyrazine involving all degrees of freedom, in particular, study of ultrafast relaxation of S2 excited state in Pyrazine.

#### Computational details :
- Functionals used - B3LYP
- Basis set - Triple zeta valence plus (TZVP)
- Software used - Turbomole
- Also compared accuracy of TDDFT with highgly correlted EOM-CCSD(T)
- Number of states - Ground state + four lowest excited states
- \Delta = 0.1 fs , \delta = 1e-5 fs
- RK-4 used for integration of electronic time steps
- Number of for theoretical absorption spectra by TDDFT = 650

#### Task2 - TSH discussion with Chakri bhaiya and shubhojit
- Path of NWCHEM directory must be specified at the beginning of fssh.py
- Number of processors for NWCHEM jobs can be changed in the NWCHEM input file fssh.nw by the user by
    np_opt np
    np_norm np
    np_tddft np
  np = number of processors, and some(or all) of the above lines can be included in the TSH block of fssh.nw
- For running the TSH simulation, we need to type the following command in terminal:
   python main.py ../input_files/fssh.nw (python main.py PATH-TO-fssh.nw)
   This runs a single trajectory for now
   *For parallelisation over trajectories we need to distribute the trajectories (ntraj) in the main.py file to different processes
- In the NAC calculation, to interpolate and extrapolate for the first time step, we also calculate the NAC a -\Delta (just for the initial time step) and then we propagate by interpolation and extrapolation of further time steps.
- Also look for density matrices, some doubt is there anout its correctness (although it satiesfies the its properties)

#### Task3 - Checking and learning to use the TSH code
- Encountered some errors related to specification of NWCHEM path (error - Directory not found)
- Changed the NWCHEM path.... but still the same error persist
- Tried the command:
   module load nwchem/7.0
   and then ran a test H2 calculation (NWCHEM worked)
   The TSH code also started running. BUt every time I logout, I have to module load nwchem again before running the any tests (*I have to find the correct NWCHEM path and specify that in fssh.py file)
- TSH simulation for a trajectory-0 showed error (in interpolation step of NAC calculation) at the 8th time step simulation. (*To be     fixed)
- Wrote some lines of code in the fssh.py file to generate an output file and wrtie to it, at each nuclear propagation step, the positions, momentum',Kinetic energy, Potential energy, Density matrices and the current elecronic state.
(*No precision limit set for the values written in the file -> code must be modified later to do this.)  


## 27/08/2020

#### Task1 - Werener et al.(2008)
#### Results:
- There is a strong pi-pi* transition at 5.3eV from 1A_g ground state to the 1B_2u S2 state.  
- A weak npi* transition to 1B_3u S1 state is at 3.9eV.
- Two dark states (optical transition not allowed) with 1A_u and 1B_2g symmetry at 4.6eV and 6.3eV are also considered in the TSH simulations.
- Number of trajectories for TDDFT-TSH simulation = 60
- S2 state decays approximately exponentially with (approx)lifetime = 21.1 fs
#### The story:
- They did a TDDFT calculation to obtain the excited states. The excited states are nearly around:
    3.9eV, 4.6eV, 5.3eV, 6.4eV.
- They calculated the theoretical absorption spectrum by eqn(16), doing the TDDFT simulation of 650 structures around the equilibrium grometry by sampling with wigner distribution, and found the absorption peak to be around 3.9eV and 5.3eV(strong peak), and compared it with the experiment which shows similar results(~3.9eV and ~4.8eV).
- Thus, they labelled 3.9eV as S1 and 5.3eV as S2. The bands which showed no absorption were labelled dark bands (the ones at 4.6eV and 6.3eV)
- Now they did TDDFT-TSH simulation with 60 trajectories (sampled by wigner distribution) and looked for the decay of S2 excited state (into all the other states considered above)
- They obtained theoretical lifetime to be 21.1 fs, experimental is 20 fs. (Good disagreement?)
- Also the nature of the curve (somewhat) matches to the full Quantum mechanical result (TDDVR-whats this?)

#### Task2 - Discussion with sir and Chakri bhaiya
- Discussion on inclusion of coherence correction in TSH code -> Read the paper *Nelson, T.; Fernandez-Alberti, S.; Roitberg, A.; Tretiak, S. Nonadiabatic excited-state molecular dynamics: Treatment of electronic decoherence. J. Chem. Phys. 2013, 138,224111–224124
- Discussion on the floating point error occuring in the code:
    a) maybe roundoff at the RK4 level to the required precision
    b) take as input, the precision required by the user for tprime
- Try the TSH simulations DEF2-TZVP and CD(Charge Density Fitting) basis
- Try to implement excited state MD

#### Task3 - Running TSH code temporary fix
- Replaced dt -> np.round(dt,7) in RK4 function in util_functions file as a temporary hack.
- The code now works even for the time step which showed error earlier. We should try to apply this hack in a more effective way and also try to make this more general such that the user can specify how much precision they want in their results.

#### Task4 - Discussion with Chakradhar bhaiya and shubhojit
- Some modifications required in TSH output file:
    - Print x,y z in position and momentum
    - Don't print brackets in the printed arrays
    - Print out the results in units specified by the user along with unit itself
    - Print trace of the density matrix
- Discussion on CD basis and DEF2-TZVP -> We just need to put an extra block below the basis block in NWCHEM input file, specifying:
```
    basis
       "cd basis" spherical
    end
```
- In NWCHEM output file:
    - Bfn - basis function
    - coefficients printed out for each bfn used in the order of atoms specified in  NWCHEM input file


## 28/08/2020

#### Task1 - Making modifications in output file
- Using 16 processes for NWCHEM, the speed for simulation of each time step reduced from ~104s to ~70s.
- Trace of the matrix added to the output file
- Created a fuction to carry out the task of printing to an output file
- Modified the output file containing x,y,z labels in position and momentum

#### Task2 - electronic.py and fssh.py part in TSH code

#### Task3 - Reading about decoherence (*Pending)
#### Task4  - lectures of the Deep learning course (*Pending)
#### Task6 - Discussion with Chakri bhaiya
- Add atoms to the position and momentum list
- Add some printing information at the beginning of file.
- change after cd basis :
    - 8 processes ~ 150s per time step
    - 16 processes ~ 300s per time step


## 29/08/2020

#### Task1 - TSH simulations
- Rerun with CD basis, 8 processes -> The time taker for each delta ~ 150sec. This is due to improper communication due to less availability of processes (only 4 were free and I submitted jobs for 8 and 16)
- Simulating for 10 fs -> simulation done till 8.6 fs (my net cut off) -> file size~298Kb
- Error occured when the simulation started from 3rd excited state -> error in checking the number of electrons from tddft.out file.
- Error in taking temperature input. Error corrected by putting float outside temperature.
- Error occured when putting temp = 260

#### Task2 - Reading SHARC (*pending)


## 30/08/2020

#### Task1 - TSH simulations (decay testing)
- temperature to au conversion done and the error was correced.
- Error occuring in a hopping step (maybe), in particular in the self.hopping_check(self.decide_hopping()). -> To be corrected
- Temperature conversion function added.
- Density matrix will now be printed to output file in real and imaginary components seperately.
- Fixed broadcasting error in hopping_check in fssh.py -> the broadcasting term changed to be a tuple.
- Hop oocured for the first time at around 3fs for a trajectory (running in Heisenberg). Hop also occured in Bose.
- Plotted the hopping between states for the trajectory obtained from heisenberg

## 31/08/2020

#### Task1 - Extract data out of the two trajectories
- Hopping between states plotted between both trajectories
- Trace of densities plotted for both trajectories
  - With the electronic time step as 0.00005 fs, the trace of the density matrix was not conserved.
  - With electronic time step as 1e-6 fs, the error in the trace reduced significantly.

#### Task2 - Modify the files to implement parallelisation
- Created a parallel version of main.py
  - workloads divided to ranks depending on the the number of trajectories
  - extra workloads are created if the number of trajectories is not a multiple of the number of processes
- Each trajectory output will be labelled by an index which is incorporated by an extra parameter for the trajectory class in fssh.py

#### Task3 - Test parallelisation over the two trajectories
- Initial testing started for 2 trajectories distributed over 2 processes
- We have to also generate the optimization input files with different index for each trajectory.
