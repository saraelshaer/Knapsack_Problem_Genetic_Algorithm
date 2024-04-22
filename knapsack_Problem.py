import random
from turtle import *
import time

population_size = 10
knapsack_limit = random.randint(20, 60)
items = []
for _ in range(18):
    items.append((random.randint(1, 50), random.randint(1, 100)))
length = len(items)


def get_parent(length):
    genes = []
    for _ in range(length):
        genes.append(random.randint(0, 1))
    return genes


def initialize_population(population_size, length):
    population = []
    for _ in range(population_size):
        population.append(get_parent(length))
    return population


def get_fitness(individual):
    fitness = 0
    total_weight = 0
    for i in range(length):
        if individual[i] == 1:
            total_weight += items[i][0]
            fitness += items[i][1]
    if total_weight > knapsack_limit:
        fitness = 0
    return fitness


def crossover(parent1, parent2):
    point1 = random.randint(1, length - 2)
    child1 = parent1[:point1] + parent2[point1:]
    child2 = parent2[:point1] + parent1[point1:]
    return child1, child2


def mutate(individual):
    child = individual[:]
    mutation_chromosome = get_parent(length)
    for i in range(length):
        if mutation_chromosome[i] == 1:
            if child[i] == 1:
                child[i] = 0
            else:
                child[i] = 1
    return child


population = initialize_population(population_size, length)
Generation = 0
fitness = 0
num_of_generations = 10000

for generation in range(num_of_generations):
    fitness_scores = [get_fitness(individual) for individual in population]
    max_fitness = sorted(fitness_scores, reverse=True)[0]
    second_max_fitness = sorted(fitness_scores, reverse=True)[1]
    max_fitness_index = fitness_scores.index(max_fitness)
    second_max_fitness_index = fitness_scores.index(second_max_fitness)
    best_individual = population[max_fitness_index]
    best_fitness = get_fitness(best_individual)
    if best_fitness > fitness:
        fitness = best_fitness
        Generation = generation

    # print(f"Generation : {generation} best individual : {best_individual} with {best_fitness}")
    parent1 = population[max_fitness_index]
    parent2 = population[second_max_fitness_index]
    child1, child2 = crossover(parent1, parent2)
    child1 = mutate(child1)
    child2 = mutate(child2)

    min_fitness_index = fitness_scores.index(min(fitness_scores))
    if get_fitness(child1) > min(fitness_scores):
        population[min_fitness_index] = child1
    if get_fitness(child2) > min(fitness_scores):
        min_fitness_index = fitness_scores.index(min(fitness_scores))
        population[min_fitness_index] = child2

best_individual = max(population, key=get_fitness)
print(
    f" Generation: {Generation} best individual : {best_individual} ->> fitness : {get_fitness(best_individual)} "
)
# ----------------------------------------------------------------------
win = Screen()
win.title("knapsack problem")
win.setup(width=840, height=700)

pen = Turtle()
pen.speed(0)
pen.hideturtle()
pen.shape("circle")


def write(
    tr, str, x, y, color="black", align_text="center", font_prop=("Arial", 15, "bold")
):
    tr.color(color)
    tr.penup()
    tr.goto(x, y)
    tr.write(str, align=align_text, font=font_prop)


write(
    pen, "Knapsack Problem 🤔", -30.0, 300.0, "green", "center", ("Courier", 40, "bold")
)
write(
    pen,
    "-------------------------",
    -30.0,
    260.0,
    "#e65c00",
    "center",
    ("Courier", 30, "bold"),
)
write(
    pen,
    f"🛑 Knapsack's limit (W) = {knapsack_limit} kg",
    500.0,
    200.0,
    "#e65c00",
    "center",
)
write(pen, "💼", 500.0, 10.0, "brown", "center", ("Courier", 150, "bold"))

p = Turtle()
p.hideturtle()
current_weight = 0
write(
    p,
    f"Current Weight = {current_weight} kg",
    500.0,
    -10.0,
    "#990000",
    "center",
    ("Courier", 18, "bold"),
)


def update_current_weight():
    p.clear()
    write(
        p,
        f"Current Weight = {current_weight} kg",
        500.0,
        -10.0,
        "#990000",
        "center",
        ("Courier", 18, "bold"),
    )


# -------------------------------
def print_pos(x, y):
    print(x, y)


# win.onclick(print_pos)
# ----------------------------
t = Turtle()
t.hideturtle
t.speed(0)
t.penup()
t.goto(-730.0, 200.0)


def polygon(tr, n, lenght, width, color1="#544f54", color2="white"):
    tr.pendown()
    tr.begin_fill()
    tr.color(color1, color2)
    for i in range(n):
        tr.fd(lenght)
        tr.lt(90)
        tr.fd(width)
        tr.lt(90)
    tr.end_fill()


def go_lt(d):
    t.lt(90)
    t.fd(d)
    t.lt(90)
    t.fd(60 * 10)


def go_rt(d):
    t.rt(90)
    t.fd(d)
    t.rt(90)
    t.fd(60 * 10)


directons = [
    (-650.0, 160.0),
    (-650.0, 100.0),
    (-650.0, 40.0),
    (-650.0, -20.0),
    (-650.0, -80.0),
    (-650.0, -140.0),
    (-650.0, -200.0),
    (-650.0, -260.0),
    (-650.0, -320.0),
    (-200.0, 160.0),
    (-200.0, 100.0),
    (-200.0, 40.0),
    (-200.0, -20.0),
    (-200.0, -80.0),
    (-200.0, -140.0),
    (-200.0, -200.0),
    (-200.0, -260.0),
    (-200.0, -320.0),
]


def write_items_in_table():
    t.hideturtle()
    for i in range(18):
        t.penup()
        t.goto(directons[i][0], directons[i][1])
        t.color("#000080")
        t.write(f"Item {i+1}", align="center", font=("Courier", 20, "bold"))
        t.fd(190)
        t.write(
            f"         {items[i][0]}       {items[i][1]}     ",
            align="center",
            font=("Courier", 20, "bold"),
        )


def drow_table(width):
    t.pensize(2)
    t.pencolor("#544f54")
    for i in range(10):
        polygon(t, 2, 2 * 450, 60)
        t.penup()
        if i != 9:
            t.rt(90)
            t.fd(width)
            t.lt(90)
        t.pendown()
    t.fd(450)
    t.lt(90)
    t.fd(60 * 10)

    go_lt(150)
    go_rt(150)
    go_rt(450)
    go_lt(150)
    write(t, "Profit", 85.0, 220.0, "#000080", "center", ("Courier", 20, "bold"))
    write(t, "Weight", -50.0, 220.0, "#000080", "center", ("Courier", 20, "bold"))
    write(t, "Profit", -360.0, 220.0, "#000080", "center", ("Courier", 20, "bold"))
    write(t, "Weight", -500.0, 220.0, "#000080", "center", ("Courier", 20, "bold"))

    t.lt(90)
    t.fd(750)
    t.lt(90)
    t.fd(60 + 30)
    t.lt(90)
    write_items_in_table()


drow_table(60)

# ---------------------------------------------------------------------
# start button
t.goto(420.0, -91.0)
polygon(t, 2, 120, 60, "#990000", "#990000")
write(t, "Start", 479, -76, "white", "center", ("Courier", 20, "bold"))
x_min = 419.0
x_max = 537.0
y_min = -85.0
y_max = -28.0
cnt = 0
# -----------------------------------------------------------------------


def start(x, y):
    global current_weight
    global cnt
    if x >= x_min and x <= x_max and y >= y_min and y <= y_max and cnt == 0:
        cnt += 1
        if fitness > 0:
            for i in range(length):
                if best_individual[i] == 1:
                    t.penup()
                    t.goto(directons[i][0], directons[i][1])
                    t.color("green")
                    t.write(f"Item {i+1}", align="center", font=("Courier", 20, "bold"))
                    t.fd(190)
                    t.write(
                        f"         {items[i][0]}       {items[i][1]}     ",
                        align="center",
                        font=("Courier", 20, "bold"),
                    )
                    current_weight += items[i][0]
                    update_current_weight()
                    time.sleep(0.5)
            write(
                t,
                f"🛑 Found at Generation:  {Generation} \n\n🛑 Total profit = ${fitness}",
                450.0,
                -199.0,
                "green",
                "center",
                ("Courier", 20, "bold"),
            )
        else:
            write(
                t,
                f"🛑 Could not find solution in {num_of_generations} generations ",
                450.0,
                -175.0,
                "#990000",
                "center",
                ("Courier", 15, "bold"),
            )


# ------------------------------------------------------------------
win.onclick(start, 1, True)
done()
