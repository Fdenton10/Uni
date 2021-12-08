import math
import random
import matplotlib.pyplot as plt
import numpy as np
import copy
import pandas as pd

# Population Size and Size of Binary String.
P = 50
N = 32
MUTRATE = 0.02
hidden_nodes = 3
input_nodes = 6
output_nodes = 1

np.random.seed(0)

data1 = pd.read_csv('data/data1.txt', sep=" ", header=None)
data2 = pd.read_csv('data/data2.txt', sep=" ", header=None)
data4 = pd.read_csv('data/data4.txt', sep=" ", header=None)
 
population = []
offspring = []
hOutput = [0.0,0.0,0.0]
Output = [0.0]

def get_input(data,index,split):
    test1 = []
    test2 = []
    train1 = []
    train2 = []
    outputs1 = []
    outputs2 = []
    for i in range(0, split):
        for j in range(0,index):
            train1.append(data[j][i])
        outputs1.append(data[index][i])
        train2.append(train1)
        train1 = []
    for i in range(split, split * 2):
        for j in range(0,index):
            test1.append(data[j][i])
        outputs2.append(data[index][i])
        test2.append(test1)
        test1 = []


    return np.array(train2),np.array(outputs1),np.array(test2),np.array(outputs2)

def sigmoid(x):
        return 1 / (1 + np.exp(-x))
#training_input(data2,6)
#print(data2)

training_inputs1, training_outputs1, test_inputs1, test_outputs1  = get_input(data1,6,20) 
training_inputs2, training_outputs2, test_inputs2, test_outputs2  = get_input(data2,6,1000) 
training_inputs3, training_outputs3, test_inputs3, test_outputs3  = get_input(data4,10,874) 

class individual():
    hiddenWeights = []
    outputWeights = []
    fitness = 0.0
    error = 0.0

# Initialise the first population

class network_layer():
    def calc(self,ind,data,outputdata):
        for t in range(0, len(data)):
            for i in range(0, hidden_nodes):
                hOutput[i] = 0
                for j in range(0,input_nodes):
                    #print('Individual',j,':',ind.hiddenWeights)
                    #print(data[t][j])
                    hOutput[i] += (ind.hiddenWeights[i][j] * data[t][j])
                #Add bias
                hOutput[i] += ind.hiddenWeights[i][input_nodes]
                #print('hidden output before sigmoid',t,': ',hOutput)
                #Apply Sigmoid Activation Function
                hOutput[i] = sigmoid(hOutput[i])
                #print('hidden output after sigmoid',t,': ',hOutput)
            for i in range(0, output_nodes):
                Output[i] = 0
                for j in range(0,hidden_nodes):
                    Output[i] += (ind.outputWeights[i][j] * hOutput[j])
                Output[i] += ind.outputWeights[i][hidden_nodes]
                #print('Bias',t,': ',Output[i])
                Output[i] = sigmoid(Output[i])
                #print('output after sigmoid',t,': ',Output[i])
            #print('Output',Output[0])
            if (outputdata[t] == 1 and Output[0] < 0.5):
                ind.error += 1.0
                print('Output 1 and below 0.5',t,outputdata[t],Output[0],ind.error)
            if (outputdata[t] == 0 and Output[0] >= 0.5):
                ind.error += 1.0
                print('Individual Output 0 and above 0.5',t,outputdata[t],Output[0],ind.error)
                #print('Training Output: ',data[t],outputdata[t], 'Output 0 and above 0.5: ',ind.error)
        return ind.error
        
            

def generate_population(pop, pop_size):
    pop = []
    for x in range(0, pop_size):
        ind = individual()
        ind.hiddenWeights, ind.outputWeights = generate_gene(input_nodes,hidden_nodes,output_nodes,-1 ,1)
        pop.append(ind)
        #print('Individual',x + 1,': \n',pop[x].outputWeights)
    
    return pop

def generate_gene(input_nodes, hidden_nodes, output_nodes,min,max):
    hiddenWeights = []
    for h in range(0, hidden_nodes + 1):
        tempgene = []
        for i in range(0, input_nodes + 1):
            random1 = np.random.uniform(min,max)
            tempgene.append(random1)
        hiddenWeights.append(tempgene)
    outputWeights = []
    for h in range(0, output_nodes):
        tempgene = []
        for i in range(0,hidden_nodes + 1):
            random1 = np.random.uniform(min,max)
            tempgene.append(random1)
        outputWeights.append(tempgene)
    return hiddenWeights, outputWeights

def fitness_function(pop):
    for i in range(0, len(pop)):
        pop[i].fitness = 0
        for j in range(0, N):
            pop[i].fitness =  pop[i].fitness + pop[i].gene[j]
        #print('Individual ',i,'Fitness: ',pop[i].gene[j])


def tournament_selection(population):
    offspring = []
    for x in range(0, P):
        parent1 = random.randint(0, P-1)
        off1 = population[parent1]
        parent2 = random.randint(0, P-1)
        off2 = population[parent2]
        if off1.error < off2.error:
            offspring.append(off1)
        else:
            offspring.append(off2)
    
    return offspring


def mean_fitness(pop):
    total_error = 0.0
    mean_error = 0.0
    for i in range(0, len(pop)):
        total_error += pop[i].error
    mean_error = total_error / P
    mean_error = mean_error / 1000
    #print('Current mean fit',mean_fitness)

    return mean_error

def best_fitness(pop):
    gene_fit = 0.0
    best_fit = 0.0
    for i in range(0,len(pop)):
        gene_fit = pop[i].fitness
        if gene_fit > best_fit:
            best_fit = gene_fit
    #print('Current best fit is',best_fit)
    
    return best_fit


def crossover(offspring):
    for i in range(0, len(offspring), 2):
        temp = offspring[i]
        j = random.randint(0, hidden_nodes)
        k = random.randint(0, input_nodes)  # Random Crosspoint
        for j in range(j,hidden_nodes):
            offspring[i].hiddenWeights[j][k] = offspring[i+1].hiddenWeights[j][k]
            offspring[i+1].hiddenWeights[j][k] = temp.hiddenWeights[j][k]
        x = random.randint(0, output_nodes)
        y = random.randint(0,hidden_nodes)
        for x in range(x, output_nodes):
            offspring[i].outputWeights[x][y] = offspring[i+1].outputWeights[x][y]
            offspring[i+1].outputWeights[x][y] = temp.outputWeights[x][y]


    return offspring

def mutation(offspring, MUTRATE):
    for i in range(0, P):
        newind = individual()
        newind.gene = []
        #print('Individual ', i, 'Before Mutation', offspring[i].gene)
        for j in range(0, hidden_nodes):
            for k in range(0,input_nodes):
                mutprob = random.randint(0, 100)
                if (mutprob < 100 * MUTRATE):
                    alter = random.uniform(0.0, 0.2)
                    if (mutprob % 2):
                        #print("Before Mutation (when random % 2):" , offspring[i].hiddenWeights[j][k])
                        offspring[i].hiddenWeights[j][k] = offspring[i].hiddenWeights[j][k] + alter
                        #print("After Mutation: (when random % 2)", offspring[i].hiddenWeights[j][k])
                    else:
                        #print("Before Mutation: ", offspring[i].hiddenWeights[j][k])
                        offspring[i].hiddenWeights[j][k] = offspring[i].hiddenWeights[j][k] - alter
                        #print("After Mutation: ", offspring[i].hiddenWeights[j][k])
    
    return offspring

def update_pop(population, offspring):
    population = copy.deepcopy(offspring)

    return population
'''
def printNN(ind):
    print('Individual 1: Hidden Weights\n',ind1.hweights)
    print('Individual 1: Hidden Bias: \n',ind1.hbiases)
    print('Individual 1: Output Weights: \n',ind1.oweights)
    print('Individual 1: Output Bias: \n',ind1.obiases)
    '''

'''
def best_fit(pop):
    for i in range(0, len(pop)):

        maxfit = max(pop[i].fitness)
    
    return maxfit
'''

population = generate_population(population, P)
layer1 = network_layer()
for j in range(0,1):
    for i in range(0, 1): 
        population[i].error = layer1.calc(population[i],training_inputs1,training_outputs1)
        print(population[i].error)
    offspring = tournament_selection(population)               
    offspring = crossover(offspring)
    #print('Offspring: ',1,'Gene After Crossover: ', offspring[0].outputWeights)
    offspring = mutation(offspring, MUTRATE)
    #for k in range(0, 1): 
     #   population[k].error = layer1.calc(offspring[k],training_inputs1,training_outputs1)
        #print(offspring[k].error)
#ind1.hforward(training_inputs1[0])
#ind1.oforward(ind1.houtput)



#generate_population(input_nodes,hidden_nodes, output_nodes)
mean = []
best = []

'''
generation = []
for i in range(0,1):
    fitness_function(population)
    offspring = tournament_selection(population)
    crossover(offspring)
    offspring = mutation(offspring, MUTRATE)
    fitness_function(offspring)
    mean1 = mean_fitness(offspring)
    best1 = best_fitness(offspring)
    mean.append(mean1)
    best.append(best1)
    #print('Mean Fitness of Offspring Population', mean_fitness(offspring))
    population = update_pop(population, offspring)
    generation.append(i)
    #print('Best fitness in current generation is:', best_fit(offspring))



plt.xlabel("Number of Generations")
plt.ylabel("Total Fitness")
plt.title("Genetic Algorithm")
plt.axis([0,len(generation),0,max(best) + 5])
plt.plot(mean, label = "Mean fitness")
plt.plot(best, label = "Best fitness")
plt.legend()
#plt.show()
'''
