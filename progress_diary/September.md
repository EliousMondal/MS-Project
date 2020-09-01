## 01/09/2020

#### Task1 - Summarize all changes made to TSH-code last month
Created a new file (code_changes.md) to track the changes in the codes. Bugs and fixes will contain the fixes to the existing code and additions will contain the files created as addtion to the existing code.

#### Task2 - Bechmarking the TSH simulations with dt = 0.000005fs
- for dt = 0.000005fs, the error in trace was less than 1% for total simulation time = 5fs
- on 2 processes, ~355 sec for each nuclear time step (Shalini Di's jobs were were also running on 16 processes)
- on 2 processes, ~250 sec per nuclear time step
- on 4 processes, ~205 sec per nuclear time step
- on 8 processes, ~150 sec per nuclear time step
- on 16 processes, ~120 sec per nuclear time step
- Wrote a function to extract the coefficients at each nuclear time step

#### Task3 - Bechmarking the TSH simulations with dt = 0.000001fs on hisenberg
- on 1 process, ~400 sec per nuclear time step
- on 2 processes, ~430 sec per nuclear time step
- on 4 processes, ~400 sec per nuclear time step
- on 8 processes, ~330 sec per nuclear time step
- on 16 processes, ~300 sec per nuclear time step

#### Task4 - Decoherence
At the region of strong coupling, the trajectory can branch into multiple wavepackets and the trajectory may hop from one PES to another. If a hop occurs, the branched nuclear wavepackets remain adiabatically coupled in the strong coupling region and continue exchanging populations. But as they move sufficiently far away in the phase space, they should evolve independently of each other. This is Decoherence.

#### Task5 - SHARC(*Pending)
