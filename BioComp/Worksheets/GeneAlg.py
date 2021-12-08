'''
Biocomputation Assignment
Francis Denton 
Student Number - 18024097
'''
#Imports
import math
import random
import matplotlib.pyplot as plt
import numpy as np
import copy


# Parameters changed for experiments
P = 50
N = 10
MUTRATE = 0.05
genesize = 32
population = []
offspring = []

random.seed(1)
# Class of an Individual
class individual():
    gene = []
    fitness = 0


# Function to initialise the first population
def generate_population(P, N):
    for x in range(0, P):
        tempgene = []
        for i in range(0, N):
            # Creates a random 10 gene string between two values
            random1 = random.uniform(-genesize, genesize)
            tempgene.append(random1)
        #Calculates the fitness on the created gene
        fitness = minimization_function(tempgene)
        newind = individual()
        newind.gene = tempgene.copy()
        newind.fitness = fitness
        #Adds the set of created individual to create the first populatioin
        population.append(newind)

# Fitness Function for floats from worksheets
def fitness_function(pop):
    for i in range(0, P):
        pop[i].fitness = 0
        for x in range(0, N):
            pop[i].fitness = pop[i].fitness + pop[i].gene[x]

# Coursework Minimilisation function
def minimization_function(gene):
    # Minimisation function, optimal value expected to be around -20
    geneSquared = 0
    cosSum = 0
    for i in gene:
        geneSquared += i * i
        cosSum += math.cos(2.0 * math.pi * i)
    fitness = -20.0 * math.exp(-0.2 * math.sqrt(geneSquared) / N) - math.exp(cosSum / N)
    return fitness


def tournament_selection(population):
    offspring = []
    for x in range(0, P):
        #Select 2 random parents in the population and compare the fitnesses.
        parent1 = random.randint(0, P-1)
        off1 = population[parent1]
        parent2 = random.randint(0, P-1)
        off2 = population[parent2]
        #Add which individual had the better fitness to the new offspring
        if off1.fitness < off2.fitness:
            offspring.append(off1)
        else:
            offspring.append(off2)
        
    return offspring

# Function to Calculate the total fitness of the population
def total_fitness(pop):
    total_fitness = 0
    for x in range(0, len(pop)):
        total_fitness += pop[x].fitness
    return total_fitness

def roulettewheelselection(population):  # Roulette wheel selection
    offspring = []
    # Call function to grab total fitness value
    fitnessSum = total_fitness(population)
    for i in range(0, len(population)):
        #Generate a random point between the total fitness and 0 since we are using negative numbers
        selection_point = np.random.uniform(fitnessSum, 0)
        running_total = 0
        j = 0
        #At the fitness values of each individiual together until it is greater then the selection point
        #Add that value to the offspring population
        while running_total >= selection_point:
            running_total += population[j].fitness
            j += 1
        offspring.append(population[j-1])
    
    return offspringpopulation

#Function to calculate mean fitness
def mean_fitness(population):
    total_fitness = 0
    mean_fitness = 0
    #Sum all the fitness values together and divide it by the size of the population
    for x in range(0, len(population)):
        total_fitness += population[x].fitness
    mean_fitness = total_fitness / P
    return mean_fitness

#Function to calculate best fitness
def best_fitness(population):
    gene_fit = 0.0
    best_fit = 0.0
    for i in range(0,len(population)):
        gene_fit = population[i].fitness
        if gene_fit < best_fit:
            best_fit = gene_fit
    return best_fit

def single_point_crossover(offspring): 
    children_after_crossover = []
    for i in range(0, len(offspring), 2):
        #Create two children which will be born for a set of parents
        child1,child2 = individual(), individual()

        # Pick a point in the string of genes.
        Xpoint = random.randint(0, N)
        child1head, child1tail = [], []
        child2head, child2tail = [], []

        #Find the midpoints of the genes, and adds the heads and tails to the respective child lists.
        for h in range(0, Xpoint):
            child1head.append(offspring[i].gene[h])
            child2head.append(offspring[i + 1].gene[h])
        for j in range(Xpoint, len(offspring[0].gene)):
            child2head.append(offspring[i].gene[j])
            child2tail.append(offspring[i + 1].gene[j])

        #Swap genes between the two parents and call the fitness function to calculcate fitness value of new child.
        child1.gene = child1head + child2tail 
        child2.gene = child2head + child1tail
        child1.fitness = minimization_function(child1.gene)
        child2.fitness = minimization_function(child2.gene)  # 4th dec
        children_after_crossover.append(child1)
        children_after_crossover.append(child2)
    
    #Return list of updated children after crossover
    return children_after_crossover

#Mutation Function
def mutation(offspring, MUTRATE):
    offspring_after_mutation = []
    for i in range(0, P):
        newind = individual()
        newind.gene = []
        for j in range(0, N):
            gene = offspring[i].gene[j]
            mutprob = random.randint(0, 100)
            if mutprob < (100 * MUTRATE):
                #Generate a random value between these two points which will be how large the mutation is.
                alter = random.uniform(-2,2)
                #Make sure the gene values stay within the upper and lower bounds set at the beginning.
                if gene + alter > 32:
                    gene = 32
                elif gene + alter < -32:
                    gene = -32
                else:
                    gene = gene + alter
            newind.gene.append(gene)
            newind.fitness = minimization_function(newind.gene)
        #Add the updated offsrping after mutation to the list.
        offspring_after_mutation.append(newind)
    #Return the list of offspring after mutation.
    return offspring_after_mutation

#Function to update the initial population with the newly created offspring each cycle
def update_pop(population, offspring):
    population = copy.deepcopy(offspring)

    return population

#Call generate population function
generate_population(P, N)
#Create lists to store best and mean fitness for each generation and the number of generations
mean = []
best = []
generation = []
for i in range(0,400):
    '''
    Initial population is created outside of the loop of generations
    Step 1. - Call Selection Function (tournament or roulette wheel)
    Step 2. - Call Crossover Function
    Step 3. - Call Mutation Function
    Step 4. - Calculate Mean and Best fitness of generation and append it to the list
    Step 5. - Call Update population to update intial population with created offspring for next generation
    '''
    offspring = tournament_selection(population)
    offspring = single_point_crossover(offspring)
    offspring = mutation(offspring, MUTRATE)
    mean1 = mean_fitness(offspring)
    best1 = best_fitness(offspring)
    mean.append(mean1)
    best.append(best1)
    population = update_pop(population, offspring)
    generation.append(i)

#Plot Graph of Mean and Best Fitnesses
plt.xlabel("Number of Generations")
plt.ylabel("Fitness")
plt.title("Genetic Algorithm")
plt.ylim([-25, 0])
plt.xlim([0, len(generation)])
plt.plot(mean, label = "Mean fitness")
plt.plot(best, label = "Best fitness")
plt.legend()
plt.show()


