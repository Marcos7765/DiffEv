import numpy as np
import DiffEv

f64_5 = np.float64(5)
limits = [(-f64_5, f64_5), (-f64_5, f64_5)]
popSize = 10
maxGen = 100
mf = 0.5
CR = 0.1
maximize = False
fobj = lambda x : 20+ np.e - 20*np.exp(-0.2 * np.sqrt((x[0]**2 + x[1]**2)/2)) - np.exp((np.cos(2*np.pi*x[0]) + np.cos(2*np.pi*x[1]))/2 )

otimizer = DiffEv.DiffEvolver(fobj, popSize, limits, maxGen, mf, CR, maximize)


for i in range(otimizer.maxGen):
    otimizer.select(otimizer.recombine(otimizer.mutate()))
    otimizer.updateBest()
    print(f"{otimizer.bestPos}\t{otimizer.bestVal}")

print(f"Resultado final:\n{otimizer.bestPos}\t{otimizer.bestVal}")