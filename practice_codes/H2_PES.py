import re
import os
import sys
from mpi4py import MPI
import numpy as np
import matplotlib.pyplot as plt

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

start_timer = MPI.Wtime()
def generate_nwchem_input(file_name,molecule_name,basis_set,xc,coordinates,task):
    '''
    Parameters
    ----------
    file_name : type = string, name of the input file
    molecule_name : type = string, name of the molecule
    basis : type = string, the basis set to be used(default = lda)
    xc : type = string, the exchange-correlation functional to be used (default = None)
    coordinates : type = list, list of coordinates for each atom
    task : type = string, task to be performed

    Output
    ------
    Generates an NWCHEM input file
    '''
    #naming the file
    file_name = ("{}.nw".format(file_name))
    file = open(file_name,"w+")

    #writing some starting lines in standard NWCHEM input file
    file.write("start {}\n".format(molecule_name))
    file.write('title "{} in {} basis set"\n\n'.format(molecule_name,basis_set))

    #writing the coordinates of the atoms
    file.write("geometry units au\n")
    for i in atoms:
        file.write("  {}      {}      {}      {}\n".format(i[0],i[1],i[2],i[3]))
    file.write("end\n")

    #writing the basis set
    file.write("basis\n")
    file.write("  H library {}\n".format(basis_set))
    file.write("end\n")

    #writing the xc functional
    file.write("dft\n")
    file.write("  xc {}\nend\n".format(xc))

    #writinf the DFT task
    file.write("task {}".format(task))

#Defining the molecule
basis_set = '6-31g'
xc = 'b3lyp'
atoms = [['H',0.0,0.0,0.0],['H',0.0,0.0,1.0]]
task = 'DFT energy'
n_distances = int(sys.argv[1])

#Generating and delegating works to different processes
distance_array = np.linspace(1.3,1.5,n_distances)
workload = np.array([(n_distances//size)*i for i in range(size)])
work_start = workload[rank]
work_end = workload[rank] + (n_distances//size)

#Arrays to store PES data
Energies = np.zeros(work_end-work_start)
Distances = np.zeros(work_end-work_start)

for dist in range(work_start,work_end):
    input_file_name = 'h2_test{}'.format(rank)
    molecule_name = 'h2{}'.format(rank)
    atoms[1][3] = round(distance_array[dist],8)
    #print("Calculating energy for d = {} au".format(atoms[1][3]))
    generate_nwchem_input(input_file_name,molecule_name,basis_set,xc,atoms,task)
    os.system("nwchem {}.nw > {}.out".format(input_file_name,input_file_name))

    out_file = input_file_name+'.out'
    file = open(out_file)
    for line in file:
        line_ = line.strip()
        e_line = re.findall("^Total DFT energy =       (\S+[0-9]+)",line_)
        if len(e_line) >0:
            Energies[dist-work_start] = float(e_line[0])
            Distances[dist-work_start] = atoms[1][3]

if rank == 0:
    pes = {Distances[i]:Energies[i] for i in range(len(Energies))}
    for i in range(1,size):
        comm.Recv(Distances,source=i)
        comm.Recv(Energies,source=i)
        for j in range(len(Energies)):
            pes[Distances[j]] = Energies[j]
else:
    comm.Send(Distances,dest=0)
    comm.Send(Energies,dest=0)

if rank == 0:
    #writng the PES generated to a file
    PES_data = open("PES_curvature_{}.txt".format(len(Energies)),'w+')
    PES_data.write("Distance(au)                    Energy(au)\n")
    for i in list(pes.keys()):
        PES_data.write("{}                    {}\n".format(i,pes[i]))
    end_timer = MPI.Wtime()
    time_taken = end_timer-start_timer
    print("Time taken = {} seconds".format(time_taken))

    Dis = list(pes.keys())
    En = [pes[i] for i in Dis]
    plt.figure()
    plt.xlabel("R ----->")
    plt.ylabel("E ----->")
    plt.title("PES of H2")
    plt.plot(Dis,En)
    plt.savefig("H2_PES_{}_t_{}.pdf".format(len(Dis),time_taken))
    plt.show()
