import random

class Genotype:
	def __init__(self, size):
		self.size = size

	def generate(self):
		chromosome = []
		for i in range(self.size):
			chromosome.append(random.uniform(-1, 1))
		return chromosome
