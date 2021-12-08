import math
import random
import matplotlib.pyplot as plt
import numpy as np


# Create individual class

# Population Size and Size of Binary String.
P = 50
N = 10

population = []
offspring = []


class individual:
    gene = []
    fitness = 0


class network:
    hweights = []
    oweights = []
    error = 0.0


def create_population():
    tempgene = []
    for x in range(0, P):
        for x in range(0, N):
            # Creates random 10 bit binary string
            tempgene.append(random.random())
    newind = individual()
    newind.gene = tempgene.copy()
    population.append(newind)


#for x in range(0, N):
    #newind.fitness = newind.fitness + newind.gene[x]


def tournamentselection(population):
    offspring = []
    for i in range(0, P):
        parent1 = random.randint(0, P-1)
        off1 = population[parent1]
        parent2 = random.randint(0, P-1)
        off2 = population[parent2]
        if off1.fitness > off2.fitness:
            offspring.append(off1)
        else:
            offspring.append(off2)


def crossover():
    for i in range(0, P, 2):
        temp = offspring[i]
        crosspoint = random.randint(0, N)
        j = crosspoint
        for j in range(j, N):
            offspring[i].gene[j] = offspring[i+1].gene[j]
            offspring[i+1].gene[j] = temp.gene[j]
        print('After Crossover', offspring[0].gene)

# Mutation


MUTRATE = 0.1
for i in range(0, P):
    newind = individual()
    newind.gene = []
    for j in range(0, N):
        mutprob = random.random()
        if (mutprob < MUTRATE):
            alter = random.uniform(0, mutprob)
            if (random.random() % 2):
                #print("Before Mutation: ", offspring[i].gene[j])
                offspring[i].gene[j] = offspring[i].gene[j] + alter
                #print("After Mutation: ", offspring[i].gene[j])
            else:
                #print("Before Mutation: ", offspring[i].gene[j])
                offspring[i].gene[j] = offspring[i].gene[j] - alter
                #print("After Mutation: ", offspring[i].gene[j])
        newind.gene.append(offspring[i].gene[j])
        print('After Mutation', newind.gene)
