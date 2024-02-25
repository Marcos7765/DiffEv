from mpi4py import MPI
rank = 0
size = 1
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

import numpy as np
import DiffEv

f64_5 = np.float64(5)
limits = [(-f64_5, f64_5), (-f64_5, f64_5)]
popSize = 10//size + (1 if rank<10%size else 0)
maxGen = 50
mf = 0.5
CR = 0.1
maximize = False
fobj = lambda x : 20+ np.e - 20*np.exp(-0.2 * np.sqrt((x[0]**2 + x[1]**2)/2)) - np.exp((np.cos(2*np.pi*x[0]) + np.cos(2*np.pi*x[1]))/2 )

otimizer = DiffEv.DiffEvolver(fobj, popSize, limits, maxGen, mf, CR, maximize)

def sync():
    info = np.array([*otimizer.bestPos, otimizer.bestVal])
    recBuff = None if rank!=0 else np.empty((size, len(otimizer.bestPos)+1), dtype=np.float64)
    comm.Gather([info, MPI.DOUBLE], [recBuff, MPI.DOUBLE], 0)
    if rank==0: info[:] = recBuff[np.argmin(recBuff[:,-1])]
    comm.Bcast([info, MPI.DOUBLE], 0)
    otimizer.bestPos = info[:-1]
    otimizer.bestVal = info[-1]

for i in range(otimizer.maxGen):
    otimizer.select(otimizer.recombine(otimizer.mutate()))
    otimizer.updateBest()
    sync()
    #print(f"{otimizer.bestPos}\t{otimizer.bestVal} [rank {rank}]\n")

if rank==0: print(f"Final result:\n{otimizer.bestPos}\t{otimizer.bestVal}")

MPI.Finalize()