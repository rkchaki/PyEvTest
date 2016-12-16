from pyevolve import Util
from pyevolve import GTree
from pyevolve import GSimpleGA
from pyevolve import Consts
import math

def gp_and(a,b):
	p = bool(a)
	q = bool(b)
	if p and q:
		return 1
	else:
		return 0
		
def gp_or(a,b):
	p = bool(a)
	q = bool(b)
	if p or q:
		return 1
	else:
		return 0
		
def gp_xor(a,b):
	p = bool(a)
	q = bool(b)
	if ((p or q) and (not (p and q))):
		return 1
	else:
		return 0
		
def gp_not(a):
	p = bool(a)
	if not p:
		return 1
	else:
		return 0
		
def gp_nand(a,b):
	p = bool(a)
	q = bool(b)
	if not (p and q):
		return 1
	else:
		return 0
		
def gp_nor(a,b):
	p = bool(a)
	q = bool(b)
	if not (p or q):
		return 1
	else:
		return 0
		
def gp_xnor(a,b):
	p = bool(a)
	q = bool(b)
	if not ((p or q) and (not (p and q))):
		return 1
	else:
		return 0
		
def eval_func(chromosome):
	return 0

genome = GTree.GTreeGP()
genome.setParams(max_depth=4, method="ramped")
genome.evaluator += eval_func

ga = GSimpleGA.GSimpleGA(genome)
ga.setParams(gp_terminals       = ['a', 'b'],
             gp_function_prefix = "gp")

ga.setMinimax(Consts.minimaxType["minimize"])
ga.setGenerations(50)
ga.setCrossoverRate(1.0)
ga.setMutationRate(0.25)
ga.setPopulationSize(800)
   
ga(freq_stats=10)
best = ga.bestIndividual()
print best

