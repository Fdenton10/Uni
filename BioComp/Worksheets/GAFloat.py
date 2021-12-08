import math
import random
import matplotlib.pyplot as plt
import numpy as np
import copy


# Population Size and Size of Binary String.
P = 50
N = 10
MUTRATE = 0.1
genesize = 5.12
random.seed(1)

population = []
offspring = []


class individual():
    gene = []
    fitness = 0

# Initialise the first population
 
def generate_population(P, N):
    for x in range(0, P):
        tempgene = []
        for x in range(0, N):
            # Creates random 10 bit binary string            
            tempgene.append(random.uniform(-genesize, genesize))
        newind = individual()
        newind.gene = tempgene.copy()
        population.append(newind)

# Calculate the fitness of each member of the population. Floating point adds together all the gene values per individual


def fitness_function(pop):
    for i in range(0, P):
        pop[i].fitness = 0
        for x in range(0, N):
            pop[i].fitness = pop[i].fitness + pop[i].gene[x]
        #print('Individual ',i,'Fitness: ',pop[i].gene,pop[i].fitness)

# Select 2 Parents
# Compare the fitness of the parents
# Create offspring based on which parent has higher fitness


def tournament_selection(population):
    for x in range(0, P):
        parent1 = random.randint(0, P-1)
        off1 = population[parent1]
        parent2 = random.randint(0, P-1)
        off2 = population[parent2]
        if off1.fitness > off2.fitness:
            offspring.append(off1)
        else:
            offspring.append(off2)
    
    return offspring
    

# Calculate mean fitness of individuals


def mean_fitness(pop):
    total_fitness = 0
    mean_fitness = 0
    for x in range(0, P):
        total_fitness += pop[x].fitness
    mean_fitness = total_fitness / P
    print(mean_fitness)

    return mean_fitness

def best_fitness(pop):
    gene_fit = 0.0
    best_fit = 0.0
    for i in range(0,len(pop)):
        gene_fit = pop[i].fitness
        if gene_fit > best_fit:
            best_fit = gene_fit
    #print('Current best fit is',best_fit)
    
    return best_fit

# Perform Crossover
# Select a point in two offspring and swap gene values


def crossover(offspring):
    for i in range(0, P, 2):
        temp = offspring[i]
        j = random.randint(0, N)  # Random Crosspoint
        for j in range(j, N):
            offspring[i].gene[j] = offspring[i+1].gene[j]
            offspring[i+1].gene[j] = temp.gene[j]


def mutation(offspring, MUTRATE):
    for i in range(0, P):
        newind = individual()
        newind.gene = []
        #print('Individual ', i, 'Before Mutation', offspring[i].gene)
        for j in range(0, N):
            gene = offspring[i].gene[j]
            mutprob = random.randint(0, 100)
            if (mutprob < 100 * MUTRATE):
                alter = random.uniform(0.0, 0.1)
                if (random.random() % 2):
                    print("Before Mutation: ", offspring[i].gene[j])
                    gene = gene + alter
                    print("After Mutation: ", offspring[i].gene[j])
                else:
                    print("Before Mutation: ", offspring[i].gene[j])
                    gene = gene - alter
                    print("After Mutation: ", offspring[i].gene[j])
            newind.gene.append(gene)
        offspring.append(newind)
        #print('Individual ', i, 'After Mutation', newind.gene)

    return offspring

def update_pop(population, offspring):
    population = copy.deepcopy(offspring)

    return population

generate_population(P, N)
mean = []
best = []
generation = []
for i in range(0,20):
    fitness_function(population)
    offspring = tournament_selection(population)
    crossover(offspring)
    offspring = mutation(offspring, MUTRATE)
    fitness_function(offspring)
    mean1 = mean_fitness(offspring)
    best1 = best_fitness(offspring)
    mean.append(mean1)
    best.append(best1)
    print('Mean Fitness of Offspring Population', mean_fitness(offspring))
    population = update_pop(population, offspring)
    generation.append(i)
    print('Best fitness in current generation is:', best_fitness(offspring))

plt.xlabel("Number of Generations")
plt.ylabel("Total Fitness")
plt.title("Genetic Algorithm")
plt.axis([0,len(generation),0,max(best) + 5])
plt.plot(mean, label = "Mean fitness")
plt.plot(best, label = "Best fitness")
plt.legend()
plt.show()


