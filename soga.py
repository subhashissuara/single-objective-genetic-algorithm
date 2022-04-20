# ------------------------------------------------------------
#   Author: Subhashis Suara
#   Roll No.: UCSE19012
#   Problem: Solving OneMax Problem using Genetic Algorithm
# ------------------------------------------------------------


from numpy.random import randint
from numpy.random import rand

# --------------- EDIT BELOW THIS LINE ---------------------

# Number of Bits
number_of_bits = 20

# Total Number of Iterations
number_of_iterations = 100

# Total Population Size
population_size = 100

# Crossover Rate
crossover_rate = 0.9

# Mutation Rate
mutation_rate = 1.0 / float(number_of_bits)

# OneMax Objective Function (Change as required)
def objective_function(x):
	return -sum(x)

# --------------- EDIT ABOVE THIS LINE ---------------------

def tournament_selection(population, scores, num_of_candidates = 3):
	first_random_player = randint(len(population))
	for player in randint(0, len(population), num_of_candidates - 1):
		if scores[player] < scores[first_random_player]:
			first_random_player = player
	return population[first_random_player]

def crossover(parent_one, parent_two, crossover_rate):
    child_one = parent_one.copy()
    child_two = parent_two.copy()

    if rand() < crossover_rate:
        crossover_point = randint(1, len(parent_two) - 2)
        child_one = parent_one[:crossover_point] + parent_two[crossover_point:]
        child_two = parent_one[:crossover_point] + parent_two[crossover_point:]

    return [child_one, child_two]

def mutation(chromosome, mutation_rate):
	for i in range(len(chromosome)):
		if rand() < mutation_rate:
			chromosome[i] = 1 - chromosome[i]

def single_objective_genetic_algorithm(objective, number_of_bits, number_of_iterations, population_size, crossover_rate, mutation_rate):
    initial_population = [randint(0, 2, number_of_bits).tolist() for _ in range(population_size)]
    best_candidate, best_evaluation = 0, objective(initial_population[0])

    for generation in range(number_of_iterations):
        candidate_scores = [objective(c) for c in initial_population]
        
        for candidate in range(population_size):
            if candidate_scores[candidate] < best_evaluation:
                best_candidate, best_evaluation = initial_population[candidate], candidate_scores[candidate]
                print(f"Generation: {generation + 1} | New Best: {initial_population[candidate]} = {candidate_scores[candidate]:.3f}")
        
        selected_parents = [tournament_selection(initial_population, candidate_scores) for _ in range(population_size)]
        next_generation_children = list()

        for i in range(0, population_size, 2):
            parent_one, parent_two = selected_parents[i], selected_parents[i+1]
            
            for child in crossover(parent_one, parent_two, crossover_rate):
                mutation(child, mutation_rate)
                next_generation_children.append(child)
        initial_population = next_generation_children
    return [best_candidate, best_evaluation]

def main():
    best_candidate, score = single_objective_genetic_algorithm(objective_function, number_of_bits, number_of_iterations, population_size, crossover_rate, mutation_rate)
    print(f"\nOptimized!\nBest Candidate: {best_candidate} | Score: {score:.3f}")

if __name__ == '__main__':
    main()