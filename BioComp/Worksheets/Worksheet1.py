import random
# Create individual class

class individual:
        gene = []
        fitness = 0

population = []

#Population Size and Size of Binary String.
P = 50
N = 10

for x in range(0,P):
        tempgene = []
        for x in range (0,N):
                # Creates random 10 bit binary string
                tempgene.append(random.random())
        newind = individual()
        newind.gene = tempgene.copy()
        population.append(newind)
        for x in range(0,N):
                newind.fitness = newind.fitness + newind.gene[x]

for x in range (0,P):
        print(population[x].fitness)


offspring = []
for i in range (0,P):
        parent1 = random.randint(0, P-1)
        off1 = population[parent1]
        parent2 = random.randint(0, P-1)
        off2 = population[parent2]
        if off1.fitness > off2.fitness:
                offspring.append( off1 )
        else: 
                offspring.append( off2 )
               
