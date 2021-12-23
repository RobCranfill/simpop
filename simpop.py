#!/usr/bin/python3
# sim of population growth - does 1 person having 1 child really lead to a stable population?

REPRO_AGE = 2
DEATH_AGE = 8
STARTING_POP = 100
MAX_GEN = 100   # how long to run the sim

class Person:
    def __init__(self):
        self.age = 0
    def getOlder(self):
        self.age += 1

print(f'Running for {MAX_GEN} generations with starting population of {STARTING_POP}')
print(f'Reproduction age is {REPRO_AGE}; death age is {DEATH_AGE}')

# initial population
peeps  = []
for i in range(STARTING_POP):
    peeps.append(Person())

# run each generation
for i in range(MAX_GEN+1):
    # print(f'Starting generation {i}...')
    for p in peeps:
        p.getOlder()
        if p.age == DEATH_AGE:
            peeps.remove(p) # die
        elif p.age == REPRO_AGE:
            peeps.append(Person()) # add a new person
    print(f' - At end of generation {i}, population is {len(peeps)}')
