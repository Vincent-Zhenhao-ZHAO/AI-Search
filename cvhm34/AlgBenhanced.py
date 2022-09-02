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
import math

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

algorithm_code = "AC"

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
    This is the enhancement of the Ant Colony Optimization:
    1: Use greedy search to find one optimal route, and set it as global best.
    2: Calculate the inital pheremone value: t = num_cities / global best(knn_cost)
    3: Change the beta value, beta = num_cities // 10
    Aim: make search more greedy so it can reduce the time needs.
    4: We have updated the the way to update the pheremone matrix and here are the details:
    pharameters:
        Q: multipler constant and means how many rewards should be given
        update_value: the reward for any path match the best path. 
        update_value = Q / current best cost
        maximum pheremone: the maximum pheremone should be -> (1/(1-rho) * (Q/global_best))
        minimum pheremone: the minimum pheremone should be  
        -> max_pheremone*(1-prob_best ** 1/n_city) / ((n_city/2 - 1) * (prob_best ** (1/n_city)))
        stagnation_value: this stagnation value is to find if the pheremone at the max or min point
        -> stagnation_value = min(max_pheremone-pheromne[row][column],pheromne[row][column]-min_pheremone) / (n_cities ** 2))
    knnUpdatePheromne: after the greedy search, we give rewards to these path, to encourange ants to follow these path.
    5: Get ant route according to the probablities.
    6: store the local search best in to the local cost.
    7: change current cost frequently.
        Aim: encourage ants to the ants to choose the path that has 
        been demonstrated to be accurate (global best), while also learning from their
        experiences (local best) and thereby improve the algorithm.
    8: calculate maximum and minimum pheremone, and update_value.
    9: Update phereomone matrix in general, with smoothing, and reward to some ants who follow best route.
        Aim: 
        1: Set the maximum and minimum pheromones values as a way of ensuring that pheromones do not overflow or become severely underused,
        and avoid situations where some pathways are abandoned or overused.
        2: Award some ants to help them to find path more easier.
    10: repeat 5-9 until time stop.  
         
"""

# Nearest neighter algorithm
# 1: Random choose a city to start
# 2: Choose and add a city which has the minimum distance with the current city
# 3: Repeat until one tour finished
# return knn_cost -> int, knn_ant: knn_route -> list
def Knn(n_city):
    knn_ant = []
    start_city = random.randint(0,n_city-1)
    knn_ant.append(start_city)
    for _each_ in range(n_city-1):
        current_city = knn_ant[-1]
        rest_city = list(set(range(n_city)) - set(knn_ant))
        shorest_dis = float('inf')
        next_city = rest_city[0]
        for each_city in rest_city:
            current_distance = dist_matrix[current_city][each_city]
            if  current_distance < shorest_dis:
                shorest_dis = current_distance
                next_city = each_city
        knn_ant.append(next_city)
    knn_cost = GetCost(knn_ant)
    return knn_cost,knn_ant

# initializing the pheremone matrix
# return: list in list
def InitPheremone(n_cities,t):
    return [[t for x in range(n_cities)] for y in range(n_cities)]

# Get probablity according the formula.
# if the current distance is 0, then make current distance to 0.0000001, as close as 0.
# if the current probablity is too big, then set it back a large number.
# return: prob -> list
def GetProb(current_city,potential_cities,pheremone,beta,alpha):
    prob = []
    for each_city in potential_cities:
        current_distance = dist_matrix[current_city][each_city]
        current_pheremone = pheremone[current_city][each_city]
        if current_distance == 0: 
            current_prob = (1/0.0000001) ** beta * (current_pheremone ** alpha)
        else:
            current_prob = math.pow(1/current_distance,beta) * math.pow(current_pheremone,alpha)
        if current_prob > 10 ** 20:
            current_prob = 10 ** 20
        prob.append(current_prob)
    return prob

# Get every route according to the probablity.
# 1: Choose a random city to start
# 2: Choose next city from rest of the city base on the potential cities.
# 3: Loop until each_ant finish its route
# return: each_ant: each ant route -> list
def GetEveryRoute(n_cities,each_ant,pheremone,beta,alpha):
    each_ant = [random.randint(0,n_cities-1)]
    for _each_choice_ in range(n_cities-1):
        current_city = each_ant[-1]
        potential_cities = list(set(range(n_cities)) - set(each_ant))
        prob = GetProb(current_city,potential_cities,pheremone,beta,alpha)
        next_city = random.choices(potential_cities,weights=prob)[0]
        each_ant.append(next_city)
    return each_ant

# Get the total ant route.
# return: ant: ant route -> list of list
def GetRoute(n_ants,alpha,beta,n_cities,pheremone):
    ant = []
    each_ant = []
    for _each_ant_ in range(n_ants):
        each_ant = GetEveryRoute(n_cities,each_ant,pheremone,beta,alpha)
        ant.append(each_ant)
    return ant

# Get each route cost
# return cost -> list
def GetCost(each_ant):
    cost = 0
    for each_city in range(-1,len(each_ant)-1):
        each_cost = dist_matrix[each_ant[each_city]][each_ant[each_city+1]]
        cost += each_cost
    return cost

# Check if the some part of the route is part of the best ant.
# And add every part of route into the result.
# return: result -> list
def CheckIfGoodPath(each_ant,aim_ant):
    result = []
    for each in range(-1,len(each_ant)-1):
        if each_ant[each] in aim_ant:
            index_aim = aim_ant.index(each_ant[each])
            if index_aim + 1 > len(aim_ant) - 1:
                index_aim = len(aim_ant) - 2
            if each_ant[each+1] == aim_ant[index_aim+1]:
                result.append(each)
    return result

# update the pheromne matrix after the knn.
# return: pheromne: pheromne matrix -> list of list
def knnUpdatePheromne(pheromne,RHO,knn_route,n_cities,knn_cost,update_value):
                
    for each_city in range(-1,n_cities-1):
        pheromne[knn_route[each_city]][knn_route[each_city+1]] += update_value
    return pheromne

# update pheromne in gerenal.
# 1: Every update, will reduce all pheremone.
# 2: Calculate the stagnation value, this stagnation value is to find if the pheremone at the max or min point
# 3: if the stagnation value is below than 1 ** -12, will smooth it by using formula.
# 4: if part of route is part of the best route, then give awards to the route part.
# return: pheromne: pheremone matrix -> list of list
def UpdatePheromne(pheromne,RHO,ant_route,n_cities,ant_cost_hash,max_pheremone,min_pheremone,update_value,real_best_route,smoothing_parameter):
                
    for row in range(len(pheromne)):
        for column in range(len(pheromne)):
            pheromne[row][column] *= (1-RHO)
            stagnation_value = min(max_pheremone-pheromne[row][column],pheromne[row][column]-min_pheremone) / math.pow(n_cities,2)
            if stagnation_value < math.pow(0.1,10):
                pheromne[row][column] += smoothing_parameter*(max_pheremone-pheromne[row][column])
    
    for each_ant in ant_route:
        good_path = CheckIfGoodPath(each_ant,real_best_route)
        if good_path == []:
            continue
        else:
            for each_path in good_path:
                pheromne[each_ant[each_path]][each_ant[each_path+1]] += update_value
    return pheromne

# Get all cost and store in the hashtable
# return cost_hashtable -> hashtable
def GetAllCost(ant_route):
    cost_hashtable = {}
    for num_each_ant in range(len(ant_route)):
        cost_hashtable[num_each_ant] = GetCost(ant_route[num_each_ant])
    return cost_hashtable

# Get the maximum pheremone value
def GetMaxPheremone(rho,Q,global_best):
    return (1/(1-rho) * (Q/global_best))

# Get the minimum pheremone value
def GetMinPheremone(max_pheremone,prob_best,n_city):
    return (max_pheremone*(1-math.pow(prob_best,1/n_city))) / ((n_city/2 - 1) * (math.pow(prob_best,1/n_city)))

# AOC algorithm:
def AOC(
    alpha=1,
    beta=3,
    rho=0.3,
    n_ants=20,
    smoothing_parameter = 0.99,
    prob_best = 0.005,
    Q = 100
):
    n_cities = len(dist_matrix[0])
    start_time = time.time()
    knn_cost,knn_route = Knn(n_cities)
    t = n_cities / knn_cost
    beta = n_cities // 10
    if beta > 55:
        beta = 55
    pheremone_matrix = InitPheremone(n_cities,t)
    global_best_cost = knn_cost
    global_best_route = knn_route
    update_value = Q/knn_cost
    pheremone_matrix = knnUpdatePheromne(pheremone_matrix,rho,knn_route,n_cities,knn_cost,update_value)
    interaction = 0
    while time.time() - start_time < 40:
        ant_route = GetRoute(n_ants,alpha,beta,n_cities,pheremone_matrix)
        ant_cost_hash = GetAllCost(ant_route)
        local_cost = min(ant_cost_hash.values())
        place_best_route = [key for key in ant_cost_hash if ant_cost_hash[key] == local_cost][0]
        local_route = ant_route[place_best_route]
        current_best_cost = global_best_cost
        current_best_route = global_best_route
        
        if interaction % 5 == 0:
            current_best_cost = local_cost
            current_best_route = local_route
        else:
            current_best_cost = global_best_cost
            current_best_route = global_best_route
        if global_best_cost > local_cost:
            global_best_cost = local_cost
            global_best_route = local_route
            
        max_pheremone = GetMaxPheremone(rho,Q,current_best_cost)
        min_pheremone = GetMinPheremone(max_pheremone,prob_best,n_cities)
        update_value = Q/current_best_cost
        pheremone_matrix = UpdatePheromne(pheremone_matrix,rho,ant_route,n_cities,ant_cost_hash,max_pheremone,min_pheremone,update_value,current_best_route,smoothing_parameter)
        interaction += 1
    return global_best_route,global_best_cost

tour,tour_length = AOC(alpha=1,beta=3,rho=0.3,n_ants=20,smoothing_parameter = 0.99,prob_best = 0.005,Q = 100)

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
    
    











    


