from core.dna import Individual
import random

# Configurações
TARGET = "Python Genetico 2026"
POP_SIZE = 200
MUTATION_RATE = 0.01

def main():
    # 1. População Inicial
    population = [Individual(TARGET) for _ in range(POP_SIZE)]
    generation = 0
    found = False

    while not found:
        # 2. Calcular Fitness
        for ind in population:
            ind.calculate_fitness()
        
        # Ordenar por melhor fitness
        population.sort(key=lambda x: x.fitness, reverse=True)
        best = population[0]

        print(f"Geracao {generation:4} | Melhor: {best.get_phrase()} | Fitness: {best.fitness:.2%}")

        if best.get_phrase() == TARGET:
            found = True
            break

        # 3. Seleção (Mating Pool - pegamos os 50% melhores)
        next_gen = population[:10] # Elitismo: mantém os 10 melhores
        
        while len(next_gen) < POP_SIZE:
            parent_a = random.choice(population[:50])
            parent_b = random.choice(population[:50])
            
            # 4. Crossover e 5. Mutação
            child = parent_a.crossover(parent_b)
            child.mutate(MUTATION_RATE)
            next_gen.append(child)

        population = next_gen
        generation += 1

if __name__ == "__main__":
    main()
