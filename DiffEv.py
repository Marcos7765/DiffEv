import numpy as np

class DiffEvolver:
    def __init__(self, objective, popSize, limits, maxGen, 
        mutationFactor, CR, _max):
        
        self.popSize = popSize
        self.limits = limits
        self.maxGen = maxGen
        self.mf = mutationFactor
        self.fobj = objective
        self.max = _max
        self.CR = CR

        resizeScale = [x[1]-x[0] for x in limits]
        resizeOffset = [x[0] for x in limits]
        resizeVec = lambda vec : vec*resizeScale + resizeOffset

        self.pop = np.random.random((popSize, len(limits)))
        self.bestVal = None
        self.bestPos = np.empty
        self.pop[:] = np.apply_along_axis(resizeVec, axis=1, arr=self.pop)
        

        temp = np.apply_along_axis(self.fobj,axis=1, arr=self.pop)

        self.bestPos = self.pop[np.argmax(temp)] if _max else self.pop[
            np.argmin(temp)]
        
        self.bestVal = self.fobj(self.bestPos)
        #print(self.pop)

    
    
    def mutate(self):
        '''overload this to change the candidate-creating function'''
        donor = np.empty(self.pop.shape, self.pop.dtype)
        indexes = np.random.randint(0, self.popSize, size=self.popSize*2 )
        
        for i in range(self.popSize):
            while indexes[2*i] == i:
                indexes[2*i] = np.random.randint(0, self.popSize)
            while indexes[2*i +1] == i or indexes[2*i +1] == indexes[2*i]:
                indexes[2*i +1] = np.random.randint(0, self.popSize)

            donor[i] = self.bestPos + self.mf*(self.pop[indexes[2*i]] - self.pop[indexes[2*i +1]])
        def __normP(vec):
            newVec = np.copy(vec)
            for index, elemento in enumerate(vec):
                if self.D[index][1] < elemento:
                    newVec[index] = self.D[index][1]
                    continue
                if self.D[index][0] > elemento:
                    newVec[index] = self.D[index][0]
            return newVec
        donor = np.apply_along_axis(__normP, axis=1, arr=donor)
        return donor
    
    def recombine(self, donor):

        ndims = self.pop.shape[1]
        candidates = np.empty(self.pop.shape, self.pop.dtype)        
        for i in range(self.popSize):
            rand = np.random.rand(ndims)
            Irand = np.random.randint(ndims)
            for j in range(ndims):
                if rand[j] <= self.CR or j == Irand:
                    candidates[i][j] = donor[i][j]
                else:
                    candidates[i][j] = self.pop[i][j]
        #print(candidates)
        return candidates

    def select(self, candidates):
        
        if self.max:
            cmp = lambda i : True if self.fobj(candidates[i]) >= self.fobj(self.pop[i]) else False
        else:
            cmp = lambda i : True if self.fobj(candidates[i]) <= self.fobj(self.pop[i]) else False
        
        for i in range(self.popSize):
            if cmp(i):
                self.pop[i] = candidates[i]

        #print(self.pop)

    def updateBest(self):
        temp = np.apply_along_axis(self.fobj,axis=1, arr=self.pop)

        self.bestPos = self.pop[np.argmax(temp)] if self.max else self.pop[np.argmin(temp)]
        
        self.bestVal = self.fobj(self.bestPos)