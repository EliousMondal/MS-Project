###26/08/2020

##Task1 - Read "Nonadiabatic dynamics within the time dependent density functional theory:Ultrafast photodynamics in pyrazine" by Werner et al.
#Aim of paper:
Treatment of radiationless transitions in Pyrazine involving all degrees of freedom, in particular, study of ultrafast relaxation of S2 excited state in Pyrazine.

#Computational details :
1) Functionals used - B3LYP
2) Basis set - Triple zeta valence plus (TZVP)
3) Software used - Turbomole
4) Also compared accuracy of TDDFT with highgly correlted EOM-CCSD(T)
5) Number of states - Ground state + four lowest excited states
6) \Delta = 0.1 fs , \delta = 1e-5 fs
7) RK-4 used for integration of electronic time steps
8) Number of for theoretical absorption spectra by TDDFT = 650

##Task2 - TSH discussion with Chakri bhaiya and Shubhojit
1) Path of NWCHEM directory must be specified at the beginning of fssh.py
2) Number of processors for NWCHEM jobs can be changed in the NWCHEM input file fssh.nw by the user by
    np_opt np
    np_norm np
    np_tddft np
  np = number of processors, and some(or all) of the above lines can be included in the TSH block of fssh.nw
3) For running the TSH simulation, we need to type the following command in terminal:
   python main.py ../input_files/fssh.nw (python main.py PATH-TO-fssh.nw)
   This runs a single trajectory for now
   *For parallelisation over trajectories we need to distribute the trajectories (ntraj) in the main.py file to different processes
4) In the NAC calculation, to interpolate and extrapolate for the first time step, we also calculate the NAC a -\Delta (just for the initial time step) and then we propagate by interpolation and extrapolation of further time steps.
5) Also look for density matrices, some doubt is there anout its correctness (although it satiesfies the its properties)

##Task3 - Checking and learning to use the TSH code
1) Encountered some errors related to specification of NWCHEM path (error - Directory not found)
2) Changed the NWCHEM path.... but still the same error persist
3) Tried the command:
   module load nwchem/7.0
   and then ran a test H2 calculation (NWCHEM worked)
   The TSH code also started running. BUt every time I logout, I have to module load nwchem again before running the any tests (*I have to find the correct NWCHEM path and specify that in fssh.py file)
4) TSH simulation for a trajectory-0 showed error (in interpolation step of NAC calculation) at the 8th time step simulation. (*To be     fixed)
5) Wrote some lines of code in the fssh.py file to generate an output file and wrtie to it, at each nuclear propagation step, the positions, momentum',Kinetic energy, Potential energy, Density matrices and the current elecronic state.
(*No precision limit set for the values written in the file -> code must be modified later to do this.)  


###27/08/2020

##Task1 - Remaining portion of Werener et al.(2008) paper
#Results:
1) There is a strong pi-pi* transition at 5.3eV from 1A_g ground state to the 1B_2u S2 state.  
2) A weak npi* transition to 1B_3u S1 state is at 3.9eV.
3) Two dark states (optical transition not allowed) with 1A_u and 1B_2g symmetry at 4.6eV and 6.3eV are also considered in the TSH simulations.
4) Number of trajectories for TDDFT-TSH simulation = 60
5) S2 state decays approximately exponentially with (approx)lifetime = 21.1 fs
#The story:
1) They did a TDDFT(maybe at equilibrium geometry) calculation to obtain the excited states. The excited states are nearly around:
    3.9eV, 4.6eV, 5.3eV, 6.4eV.
2) They calculated the theoretical absorption spectrum by eqn(16), doing the TDDFT simulation of 650 structures around the equilibrium grometry by sampling with wigner distribution, and found the absorption peak to be around 3.9eV and 5.3eV(strong peak), and compared it with the experiment which shows similar results(~3.9eV and ~4.8eV).
3) Thus, they labelled 3.9eV as S1 and 5.3eV as S2. The bands which showed no absorption were labelled dark bands (the ones at 4.6eV and 6.3eV)
4) Now they did TDDFT-TSH simulation with 60 trajectories (sampled by wigner distribution) and looked for the decay of S2 excited state (into all the other states considered above)
5) They obtained theoretical lifetime to be 21.1 fs, experimental is 20 fs. (Good disagreement?)
6) Also the nature of the curve (somewhat) matches to the full Quantum mechanical result (TDDVR-whats this?)

##Task2 - Discussion with sir and Chakri bhaiya regarding the project
1) Discussion on inclusion of coherence correction in TSH code -> Read the paper *Nelson, T.; Fernandez-Alberti, S.; Roitberg, A.; Tretiak, S. Nonadiabatic excited-state molecular dynamics: Treatment of electronic decoherence. J. Chem. Phys. 2013, 138,224111–224124
2) Discussion on the floating point error occuring in the code:
    a) maybe roundoff at the RK4 level to the required precision
    b) take as input, the precision required by the user for tprime
3) Try the TSH simulations DEF2-TZVP and CD(Charge Density Fitting) basis
4) Try to implement excited state MD

##Task3 - Running TSH code
1) Replaced dt -> np.round(dt,7) in RK4 function in util_functions file as a temporary hack.
2) The code now works even for the time step which showed error earlier. We should try to apply this hack in a more effective way and also try to make this more general such that the user can specify how much precision they want in their results.
