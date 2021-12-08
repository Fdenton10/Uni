import random
# Create individual class
class individual:
        gene = []
        fitness = 0

population = []

P = 50
# 10-bit binary string
N = 10

for x in range(0,P):
        tempgene = []
        for x in range (0, N):
                # Creates random 10 bit strint of floating point numbers
                tempgene.append(random.random())
        newind = individual()
        newind.gene = tempgene.copy()
        print(newind.gene)
        population.append(newind)


for x in range(0,N):
        if newind.gene[x] == 1:
                newind.fitness +=1

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

temp = individual()
for i in range (0,P, 2):
        temp = offspring[i]
        crosspoint= random.random()
        j = crosspoint
        for j in range (j, N):
                offspring[i].gene[j] = offspring[i+1].gene[j]
                offspring[i+1].gene[j] = temp.gene[j]           

#Mutation
MUTRATE = 0.1
for i in range(0,P):
        newind = individual()
        newind.gene = []
        for j in range (0, N):
                gene = offspring[i].gene[j]
                mutprob = random.random()
                if mutprob< (100*MUTRATE):
                        if (gene == 1):
                                gene = 0
                        else:
                                gene = 1
                newind.gene.append(gene)