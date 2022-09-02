############
############ ALTHOUGH I GIVE YOU THIS TEMPLATE PROGRAM WITH THE NAME 'skeleton.py', 
############ YOU CAN RENAME IT TO ANYTHING YOU LIKE. HOWEVER, FOR THE PURPOSES OF 
############ THE EXPLANATION IN THESE COMMENTS, I ASSUME THAT THIS PROGRAM IS STILL 
############ CALLED 'skeleton.py'.
############
############ IF YOU WISH TO IMPORT STANDARD MODULES, YOU CAN ADD THEM AFTER THOSE BELOW.
############ NOTE THAT YOU ARE NOT ALLOWED TO IMPORT ANY NON-STANDARD MODULES! TO SEE
############ THE STANDARD MODULES, TAKE A LOOK IN 'validate_before_handin.py'. DO NOT
############ INCLUDE ANY COMMENTS ON A LINE WHERE YOU IMPORT A MODULE.
############

import os
import sys
import time
import random

############
############ NOW PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS.
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############ BY 'DO NOT TOUCH' I REALLY MEAN THIS. EVEN CHANGING THE SYNTAX, BY
############ ADDING SPACES OR COMMENTS OR LINE RETURNS AND SO ON, COULD MEAN THAT
############ CODES WILL NOT RUN WHEN I RUN THEM!
############

def read_file_into_string(input_file, ord_range):
    the_file = open(input_file, 'r') 
    current_char = the_file.read(1) 
    file_string = ""
    length = len(ord_range)
    while current_char != "":
        i = 0
        while i < length:
            if ord(current_char) >= ord_range[i][0] and ord(current_char) <= ord_range[i][1]:
                file_string = file_string + current_char
                i = length
            else:
                i = i + 1
        current_char = the_file.read(1)
    the_file.close()
    return file_string

def remove_all_spaces(the_string):
    length = len(the_string)
    new_string = ""
    for i in range(length):
        if the_string[i] != " ":
            new_string = new_string + the_string[i]
    return new_string

def integerize(the_string):
    length = len(the_string)
    stripped_string = "0"
    for i in range(0, length):
        if ord(the_string[i]) >= 48 and ord(the_string[i]) <= 57:
            stripped_string = stripped_string + the_string[i]
    resulting_int = int(stripped_string)
    return resulting_int

def convert_to_list_of_int(the_string):
    list_of_integers = []
    location = 0
    finished = False
    while finished == False:
        found_comma = the_string.find(',', location)
        if found_comma == -1:
            finished = True
        else:
            list_of_integers.append(integerize(the_string[location:found_comma]))
            location = found_comma + 1
            if the_string[location:location + 5] == "NOTE=":
                finished = True
    return list_of_integers

def build_distance_matrix(num_cities, distances, city_format):
    dist_matrix = []
    i = 0
    if city_format == "full":
        for j in range(num_cities):
            row = []
            for k in range(0, num_cities):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    elif city_format == "upper_tri":
        for j in range(0, num_cities):
            row = []
            for k in range(j):
                row.append(0)
            for k in range(num_cities - j):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    else:
        for j in range(0, num_cities):
            row = []
            for k in range(j + 1):
                row.append(0)
            for k in range(0, num_cities - (j + 1)):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    if city_format == "upper_tri" or city_format == "strict_upper_tri":
        for i in range(0, num_cities):
            for j in range(0, num_cities):
                if i > j:
                    dist_matrix[i][j] = dist_matrix[j][i]
    return dist_matrix

def read_in_algorithm_codes_and_tariffs(alg_codes_file):
    flag = "good"
    code_dictionary = {}   
    tariff_dictionary = {}  
    if not os.path.exists(alg_codes_file):
        flag = "not_exist"  
        return code_dictionary, tariff_dictionary, flag
    ord_range = [[32, 126]]
    file_string = read_file_into_string(alg_codes_file, ord_range)  
    location = 0
    EOF = False
    list_of_items = []  
    while EOF == False: 
        found_comma = file_string.find(",", location)
        if found_comma == -1:
            EOF = True
            sandwich = file_string[location:]
        else:
            sandwich = file_string[location:found_comma]
            location = found_comma + 1
        list_of_items.append(sandwich)
    third_length = int(len(list_of_items)/3)
    for i in range(third_length):
        code_dictionary[list_of_items[3 * i]] = list_of_items[3 * i + 1]
        tariff_dictionary[list_of_items[3 * i]] = int(list_of_items[3 * i + 2])
    return code_dictionary, tariff_dictionary, flag

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY!
############
############ THE RESERVED VARIABLE 'input_file' IS THE CITY FILE UNDER CONSIDERATION.
############
############ IT CAN BE SUPPLIED BY SETTING THE VARIABLE BELOW OR VIA A COMMAND-LINE
############ EXECUTION OF THE FORM 'python skeleton.py city_file.txt'. WHEN SUPPLYING
############ THE CITY FILE VIA A COMMAND-LINE EXECUTION, ANY ASSIGNMENT OF THE VARIABLE
############ 'input_file' IN THE LINE BELOW iS SUPPRESSED.
############
############ IT IS ASSUMED THAT THIS PROGRAM 'skeleton.py' SITS IN A FOLDER THE NAME OF
############ WHICH IS YOUR USER-NAME, E.G., 'abcd12', WHICH IN TURN SITS IN ANOTHER
############ FOLDER. IN THIS OTHER FOLDER IS THE FOLDER 'city-files' AND NO MATTER HOW
############ THE NAME OF THE CITY FILE IS SUPPLIED TO THIS PROGRAM, IT IS ASSUMED THAT 
############ THE CITY FILE IS IN THE FOLDER 'city-files'.
############

input_file = "AISearchfile012.txt"

############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS.
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############

if len(sys.argv) > 1:
    input_file = sys.argv[1]

##### BEGIN CHANGE 1 #####
##### (IGNORE THESE COMMENTS BUT DON'T TOUCH ANYTHING!)
the_particular_city_file_folder = "city-files"
path_for_city_files = "../" + the_particular_city_file_folder
##### END CHANGE 1   #####
    
if os.path.isfile(path_for_city_files + "/" + input_file):
    ord_range = [[32, 126]]
    file_string = read_file_into_string(path_for_city_files + "/" + input_file, ord_range)
    file_string = remove_all_spaces(file_string)
    print("I have found and read the input file " + input_file + ":")
else:
    print("*** error: The city file " + input_file + " does not exist in the folder '" + the_particular_city_file_folder + "'.")
    sys.exit()

location = file_string.find("SIZE=")
if location == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
comma = file_string.find(",", location)
if comma == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
num_cities_as_string = file_string[location + 5:comma]
num_cities = integerize(num_cities_as_string)
print("   the number of cities is stored in 'num_cities' and is " + str(num_cities))

comma = comma + 1
stripped_file_string = file_string[comma:]
distances = convert_to_list_of_int(stripped_file_string)

counted_distances = len(distances)
if counted_distances == num_cities * num_cities:
    city_format = "full"
elif counted_distances == (num_cities * (num_cities + 1))/2:
    city_format = "upper_tri"
elif counted_distances == (num_cities * (num_cities - 1))/2:
    city_format = "strict_upper_tri"
else:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()

dist_matrix = build_distance_matrix(num_cities, distances, city_format)
print("   the distance matrix 'dist_matrix' has been built.")

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY!
############
############ YOU NOW HAVE THE NUMBER OF CITIES STORED IN THE INTEGER VARIABLE 'num_cities'
############ AND THE TWO_DIMENSIONAL MATRIX 'dist_matrix' HOLDS THE INTEGER CITY-TO-CITY 
############ DISTANCES SO THAT 'dist_matrix[i][j]' IS THE DISTANCE FROM CITY 'i' TO CITY 'j'.
############ BOTH 'num_cities' AND 'dist_matrix' ARE RESERVED VARIABLES AND SHOULD FEED
############ INTO YOUR IMPLEMENTATIONS.
############

############
############ THERE NOW FOLLOWS CODE THAT READS THE ALGORITHM CODES AND TARIFFS FROM
############ THE TEXT-FILE 'alg_codes_and_tariffs.txt' INTO THE RESERVED DICTIONARIES
############ 'code_dictionary' AND 'tariff_dictionary'. DO NOT AMEND THIS CODE!
############ THE TEXT FILE 'alg_codes_and_tariffs.txt' SHOULD BE IN THE SAME FOLDER AS
############ THE FOLDER 'city-files' AND THE FOLDER WHOSE NAME IS YOUR USER-NAME.
############

##### BEGIN CHANGE 2 #####
##### (IGNORE THESE COMMENTS BUT DON'T TOUCH ANYTHING!)
the_particular_alg_codes_and_tariffs = "alg_codes_and_tariffs.txt"
path_for_alg_codes_and_tariffs = "../" + the_particular_alg_codes_and_tariffs
##### END CHANGE 2   #####

code_dictionary, tariff_dictionary, flag = read_in_algorithm_codes_and_tariffs(path_for_alg_codes_and_tariffs)

if flag != "good":
    print("*** error: The text file 'alg_codes_and_tariffs.txt' does not exist.")
    sys.exit()

print("The codes and tariffs have been read from 'alg_codes_and_tariffs.txt':")

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY! SORRY TO GO ON ABOUT THIS BUT YOU NEED TO BE 
############ AWARE OF THIS FACT!
############
############ YOU NOW NEED TO SUPPLY SOME PARAMETERS.
############
############ THE RESERVED STRING VARIABLE 'my_user_name' SHOULD BE SET AT YOUR
############ USER-NAME, E.G., "abcd12"
############

my_user_name = "cvhm34"

############
############ YOU CAN SUPPLY, IF YOU WANT, YOUR FULL NAME. THIS IS NOT USED AT ALL BUT SERVES AS
############ AN EXTRA CHECK THAT THIS FILE BELONGS TO YOU. IF YOU DO NOT WANT TO SUPPLY YOUR
############ NAME THEN EITHER SET THE STRING VARIABLES 'my_first_name' AND 'my_last_name' AT 
############ SOMETHING LIKE "Mickey" AND "Mouse" OR AS THE EMPTY STRING (AS THEY ARE NOW;
############ BUT PLEASE ENSURE THAT THE RESERVED VARIABLES 'my_first_name' AND 'my_last_name'
############ ARE SET AT SOMETHING).
############

my_first_name = "Zhenhao"
my_last_name = "Zhao"

############
############ YOU NEED TO SUPPLY THE ALGORITHM CODE IN THE RESERVED STRING VARIABLE 'algorithm_code'
############ FOR THE ALGORITHM YOU ARE IMPLEMENTING. IT NEEDS TO BE A LEGAL CODE FROM THE TEXT-FILE
############ 'alg_codes_and_tariffs.txt' (READ THIS FILE TO SEE THE CODES).
############

algorithm_code = "GA"

############
############ DO NOT TOUCH OR ALTER THE CODE BELOW! YOU HAVE BEEN WARNED!
############

if not algorithm_code in code_dictionary:
    print("*** error: the algorithm code " + algorithm_code + " is illegal")
    sys.exit()
print("   your algorithm code is legal and is " + algorithm_code + " -" + code_dictionary[algorithm_code] + ".")

############
############ YOU CAN ADD A NOTE THAT WILL BE ADDED AT THE END OF THE RESULTING TOUR FILE IF YOU LIKE,
############ E.G., "in my basic greedy search, I broke ties by always visiting the first 
############ city found" BY USING THE RESERVED STRING VARIABLE 'added_note' OR LEAVE IT EMPTY
############ IF YOU WISH. THIS HAS NO EFFECT ON MARKS BUT HELPS YOU TO REMEMBER THINGS ABOUT
############ YOUR TOUR THAT YOU MIGHT BE INTERESTED IN LATER.
############

added_note = ""

############
############ NOW YOUR CODE SHOULD BEGIN.
############

""" 

This is the genetic algorithm enhancement by combing with greedy search algorithm.
1: Initializing the population.
2: Select parents according proportional selection algorithm
3: Choose children by applying two crossover methods and swap to muate it.
4: Choose the best score and route
5: Loop 2-4 until the time stop at 30s.
6: use the result from genetic algorithm and put it into the 2-opt
7: until the time stop at 20s.

"""

# initializing the population with random city
# cities: a sample of city list.
# num: the numer of population
# return: population -> list of list 
def InitGroup(cities,num):
    population = []
    for each in range(num):
        random.shuffle(cities)
        population.append(cities[:])
    return population

# Get cost(distance)
# each_tour: the route -> list
# return: cost -> int
def GetCost(each_tour):
    cost = 0
    for i in range(-1,len(each_tour)-1):
        cost += dist_matrix[each_tour[i]][each_tour[i+1]]
    return cost

# Get the each cost in population
# population: population -> list of list
# return fitness -> list
def fit(population):
    fitness = []
    for each_tour in population:
        cost = 0
        cost = GetCost(each_tour)
        fitness.append(cost)
    return fitness

# Get the best fitness in population
# population: population -> list of list
# return: score -> int, best:best route -> list
def getBest(population):
    fitness = fit(population)
    score = min(fitness)
    best = population[fitness.index(score)]
    return score,best

# Get the probality list base on the fitness
# prob = (max_fitness - current_fitness) / total fitness
# return: prob_list
def evaluate(population):
    fitness = fit(population)
    max_fitness = max(fitness)
    prob_list = []
    for each in fitness:
        new_prob = (max_fitness - each)/sum(fitness)
        if new_prob == 0:
            new_prob = 0.1 ** 20
        prob_list.append(new_prob)
    return prob_list

# Select parents base on the probability list.
# The way to choose is to choose the highest probality one.
# return: parents -> list
def select(k,population):
    prob_list = evaluate(population)
    parents = []
    while len(parents) < k:
        new_parent = random.choices(population,weights=prob_list)[0]
        parents.append(new_parent) 
    return parents

# Swap two gene part in one route
# return: each_route -> list
def swap(each_route):
    a = b = -1
    while a == b:
        a = random.randint(0,len(each_route) - 1)
        b = random.randint(0,len(each_route) - 1)
        
    each_route[a],each_route[b] = (
        each_route[b],
        each_route[a],
    )
    return each_route
# Standard Crossover: create children base on the parents
# Two parents -> One child
# Generate same amount of parents for children
# If random number is smaller than p_mute, then copy one of the parents.
# Otherwise, generate two random number, indicating the part of the individual chromosome to be exchanged.
# Firstly, put parent1's part inside the child
# Secondly, fill in child with parent2's part which not in child
# return: children -> list of list
def crossover2(parents,p_cross,population,n_cities):
    children = []
    while len(children) < len(parents):
        child = []
        if random.random() < p_cross:
            parent1 = random.choice(parents)
            child.append(parent1)
            continue
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        start = random.randint(0,len(parent1)-1)
        if start == len(parent1) - 1:
            child.append(parent2)
        else:
            end = random.randint(start+1,len(parent1)-1)
            child = parent1[start:end]
            for each in parent2:
                if each in child:
                    continue
                child.append(each)
            children.append(child)
    return children

# Greedy based CrossOver: create children base on the parents
# Two parents -> One child
# Generate same amount of parents for children
# If random number is smaller than p_mute, then copy one of the parents.
# Otherwise:
# 1: a parent is chosen at random, and assuming the choice of parent1, 
# a city is chosen at random as the current city in the chosen parent,
# and assuming the choice of place_parent1, a gene palce_parent2 is found from parent2 that is equivalent to palce_parent1 and current city
# is added to the child as the first gene in the individual child.

# 2: if next_city_parent1 and next_city_parent2 not in the child,
#    then calculate the distance from the current city for each of them, 
#    and add the minimum distance one.

#    elif next_city_parent1 or next_city_parent2 in the child,
#    then add the city not in the child.

#    elif next_city_parent1 and next_city_parent2 in the child,
#    then go to next city and loop until child has enough city.
# 3: add child into the children
# return children -> list of list
def crossover1(parents,p_cross,population,n_cities):
    children = []
    while len(children) < len(parents):
        child = []
        if random.random() < p_cross:
            parent1 = random.choice(parents)
            child.append(parent1)
            continue
        parent1 = random.choice(parents)
        random_city = random.choice(parent1)
        child.append(random_city)
        parent2 = random.choice(parents)
        place_parent2 = parent2.index(random_city)
        place_parent1 = parent1.index(random_city)
        next_city_parent1 = (place_parent1 + 1) % (n_cities)
        next_city_parent2 = (place_parent2 + 1) % (n_cities)
        while len(child) < n_cities:
            if next_city_parent1 not in child and next_city_parent2 not in child:
                current_city = child[-1]
                distance_parent1 = dist_matrix[current_city][next_city_parent1]
                distance_parent2 = dist_matrix[current_city][next_city_parent2]
                if distance_parent1 > distance_parent2:
                    child.append(next_city_parent2)
                else:
                    child.append(next_city_parent1)
            elif next_city_parent1 in child and next_city_parent2 not in child:
                child.append(next_city_parent2)
            elif next_city_parent1 not in child and next_city_parent2 in child:
                child.append(next_city_parent1)
            elif next_city_parent1 in child and next_city_parent2 in child:
                next_city_parent1 = (next_city_parent1 + 1) % (n_cities)
                next_city_parent2 = (next_city_parent2 + 1) % (n_cities)
                continue
        children.append(child)
    return children

# 2-opt Swap method
# new_route -> list, i: start -> int, j: end -> int
# return new_route -> list
def Swap(new_route,i,j):
    new_route[i:j] = new_route[j-1:i-1:-1]
    return new_route

# 2-opt improve route method
# if improved twice, will finish the program
# the aim of that is to make faster
# if not improved, will finish the program
# return best: best route -> list, improved -> boolean 
def GetNewRoute(route,improved):
    best = []
    improved_count = 0
    for i in range(1,len(route)-2):
        for j in range(i+1,len(route)):
            if j-i == 1:
                continue
            new_route = route[:]
            old_route = route[:]
            new_route = Swap(new_route,i,j)
            new_route_cost = GetCost(new_route)
            old_route_cost = GetCost(old_route)
            if new_route_cost < old_route_cost:
                best = new_route
                improved_count += 1
                if improved_count == 2:
                    improved = False
                    break
                else:
                    improved = True
                    continue
            else:
                break
    if best == []:
        best = route
    return best,improved

# 2-opt method
def two_opt(initial_tour):
    best = initial_tour
    improved = True
    while improved:
        improved = False
        new_route,improved = GetNewRoute(best,improved)
        best = new_route
    return best

# Keep the best children in last population
# and bring it into this generation
# if worst child in the children is not good as the best one in population
# then repalce it.
# return: children -> list of list
def keepBest(children,population):
    new_gener_cost = fit(children)
    min_gener_cost = min(new_gener_cost)
    index = new_gener_cost.index(min_gener_cost)
    best_cost,best_gener = getBest(population)
    if best_cost < min_gener_cost:
        children[index] = best_gener
    return children

# Do the mutation.
# if random number is less than 0.1, then do greedy based crossover.
# Otherwise, then do standard crossover.
# if random number is less than p_mut, then do swap.
# Otherwise, do nothing
# Keep the best one from the last popualtion
# return: next_gener: next generation -> list of list
def mutate(parents,p_cross,p_mut,population,n_cities):
    next_gener = []
    if random.random() > 0.07 :
        children = crossover2(parents,p_cross,population,n_cities)
    else:
        children = crossover1(parents,p_cross,population,n_cities)
    for child in children:
        if random.random() < p_mut:
            child = swap(child)
            next_gener.append(child)
        else:
            next_gener.append(child)
    next_gener = keepBest(next_gener,population)
    return next_gener

# Main genetic algorithm
def genetic(
    p_cross=0.01,
    p_mut=0.01,
    n_pop = 100,
    num_parent = 10
):
    end = start = time.time()
    cities = list(range(0,len(dist_matrix)))
    population = InitGroup(cities,n_pop)
    score,best = getBest(population)
    n_cities = len(population[0])
    while end - start < 25:
        all_children = []
        parents = select(num_parent,population)
        while len(all_children) < n_pop:
            children = mutate(parents,p_cross,p_mut,population,n_cities)
            all_children = all_children + children
        population = all_children
        currentScore,currentBest = getBest(population)
        if currentScore < score:
            best = currentBest
            score = currentScore
        end = time.time()
    # 2-opt
    end = start = time.time()
    while end - start < 15:
        improved = False
        new_route,improved = GetNewRoute(best,improved)
        best = new_route
        score = GetCost(best)
        end = time.time()
    score = GetCost(best)
    return best,score

tour,tour_length = genetic(p_cross=0.05, p_mut=0.05,n_pop = 100,num_parent = 30)   

############
############ YOUR CODE SHOULD NOW BE COMPLETE AND WHEN EXECUTION OF THIS PROGRAM 'skeleton.py'
############ REACHES THIS POINT, YOU SHOULD HAVE COMPUTED A TOUR IN THE RESERVED LIST VARIABLE 'tour', 
############ WHICH HOLDS A LIST OF THE INTEGERS FROM {0, 1, ..., 'num_cities' - 1} SO THAT EVERY INTEGER
############ APPEARS EXACTLY ONCE, AND YOU SHOULD ALSO HOLD THE LENGTH OF THIS TOUR IN THE RESERVED
############ INTEGER VARIABLE 'tour_length'.
############

############
############ YOUR TOUR WILL BE PACKAGED IN A TOUR FILE OF THE APPROPRIATE FORMAT AND THIS TOUR FILE'S,
############ NAME WILL BE A MIX OF THE NAME OF THE CITY FILE, THE NAME OF THIS PROGRAM AND THE
############ CURRENT DATE AND TIME. SO, EVERY SUCCESSFUL EXECUTION GIVES A TOUR FILE WITH A UNIQUE
############ NAME AND YOU CAN RENAME THE ONES YOU WANT TO KEEP LATER.
############

############
############ DO NOT TOUCH OR ALTER THE CODE BELOW THIS POINT! YOU HAVE BEEN WARNED!
############

flag = "good"
length = len(tour)
for i in range(0, length):
    if isinstance(tour[i], int) == False:
        flag = "bad"
    else:
        tour[i] = int(tour[i])
if flag == "bad":
    print("*** error: Your tour contains non-integer values.")
    sys.exit()
if isinstance(tour_length, int) == False:
    print("*** error: The tour-length is a non-integer value.")
    sys.exit()
tour_length = int(tour_length)
if len(tour) != num_cities:
    print("*** error: The tour does not consist of " + str(num_cities) + " cities as there are, in fact, " + str(len(tour)) + ".")
    sys.exit()
flag = "good"
for i in range(0, num_cities):
    if not i in tour:
        flag = "bad"
if flag == "bad":
    print("*** error: Your tour has illegal or repeated city names.")
    sys.exit()
check_tour_length = 0
for i in range(0, num_cities - 1):
    check_tour_length = check_tour_length + dist_matrix[tour[i]][tour[i + 1]]
check_tour_length = check_tour_length + dist_matrix[tour[num_cities - 1]][tour[0]]
if tour_length != check_tour_length:
    flag = print("*** error: The length of your tour is not " + str(tour_length) + "; it is actually " + str(check_tour_length) + ".")
    sys.exit()
print("You, user " + my_user_name + ", have successfully built a tour of length " + str(tour_length) + "!")

local_time = time.asctime(time.localtime(time.time()))
output_file_time = local_time[4:7] + local_time[8:10] + local_time[11:13] + local_time[14:16] + local_time[17:19]
output_file_time = output_file_time.replace(" ", "0")
script_name = os.path.basename(sys.argv[0])
if len(sys.argv) > 2:
    output_file_time = sys.argv[2]
output_file_name = script_name[0:len(script_name) - 3] + "_" + input_file[0:len(input_file) - 4] + "_" + output_file_time + ".txt"

f = open(output_file_name,'w')
f.write("USER = " + my_user_name + " (" + my_first_name + " " + my_last_name + "),\n")
f.write("ALGORITHM CODE = " + algorithm_code + ", NAME OF CITY-FILE = " + input_file + ",\n")
f.write("SIZE = " + str(num_cities) + ", TOUR LENGTH = " + str(tour_length) + ",\n")
f.write(str(tour[0]))
for i in range(1,num_cities):
    f.write("," + str(tour[i]))
f.write(",\nNOTE = " + added_note)
f.close()
print("I have successfully written your tour to the tour file:\n   " + output_file_name + ".")
    
    











    


