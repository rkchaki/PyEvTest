from pyevolve import G1DList
from pyevolve import GSimpleGA
import math

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    
def fitness_func(chromosome): #count how many primes in chromosome
	score = 0
	primes = []
	for value in chromosome:
		if isPrime(value):
			if value not in primes:
				score += 1
				primes.append(value)
	return score

genome = G1DList.G1DList(20)
genome.evaluator.set(fitness_func)
ga = GSimpleGA.GSimpleGA(genome)
ga.evolve(freq_stats=1)
print ga.bestIndividual()
