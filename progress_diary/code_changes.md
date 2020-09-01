## Bugs and fixes
- #### Simulations at 0 Kelvin
  - Floating point error encountered always at 8th time step
    - Temporary Correction done by putting a limit to the precision (Replaced dt -> np.round(dt,7)) of the electronic time step in RK4 function
    - For future change, the precision is to be taken as input from the user and this precision is to incorporated as global precision value.
  - Error in reading the number of electron from tddft.out file, when the simulation started for the 3rd excited state.
  - the re.search_pattern was changed in line 231 of parse_nwchem.py file:
    "No. of electrons" -> "No. of electrons :"

- #### Simulations at 260 Kelvin
  - Error in reading of temperature as float.
    - temp was convrted to float in line 32 of molecules.py file.
  - Error occured in convergence of TTDFT. This occured as the we didn't convert it from Kelvin to atomic-units of temperature.
    - correction made : kelvintoau function added in the conversion library and temp converted to au units in line 32 of molecule.py file.
  - Error occured hopping was supposed to occur for the first time
    - Error was in self.hopping_check(self.decide_hopping())
    - This is due to broadcasting error in line 137
    - correction made : the 2nd element of np.broadcast_to must be a tuple
  np.broadcast_to(self.molecule.masses,len(self.molecule.masses),3) -> np.broadcast_to(self.molecule.masses,(len(self.molecule.masses),3))

## Additions to the code

- #### Functions added to fssh.py
  - #### write_output()
    - Writes to an output file at each nuclear time step:
      - Positions of atoms
      - Momenta of atoms
      - Kinetic energy of system
      - Potential energy of ground and excited states
      - Real and imaginary part of Density matrix seperately
      - Trace of the density matrix
      - The current electronic state of the system
      - Time requied to evaluate the present nuclear time step
      - Time elasped till now in the TSH simulation
    - Additions to be made in the future
      - Number of trajectory, stopping criterion at the starting of the file
      - Atomic symbols beside the positions and momenta
      - Making the density matrix in tabular format
      - The electronic time step
      - Embellishing the output file.
  - #### print_output()
  Same as the write_output() function, but prints out the information to screen at each nuclear time step.

- #### Parallelisation of the main.py function
  - Added python MPI communicator (mpi4py)
  - Divided the workload among ranks
  - Divided the extra workloads to some ranks
  - Added extra parameter to the trajectory class containing the trajectory index. So each trajectory will have its own output file.
    - Error occured in the output trajectory files. They were empty. This occured as the different trajectories should read different normal_mode and tddft_inputs. So these must also be indexed for the parallalisation over just the trajectories.

- #### Functions to extract datat from the output file
  - extract states
  - extract density matrix traces
  - extract coefficients of the 3rd elecronic state
