import csv

def strip(new_list, old_list):
    for x in old_list:
        y = str(x).strip('[]')[1:]
        new_list.append(y[:len(y)-1].replace(' ',''))
    return new_list

# open company_states.csv,  every thing start from here
LOCATIONS_O = open('CS123/COMPANY_STATES.csv','rU')
LOCATIONS_R = csv.reader(LOCATIONS_O)
LOCATIONS = []
for x in LOCATIONS_R:
     LOCATIONS.append(x)

# creates a dictionary of key = head, value = list of states in which the head has operation
company_state_dict = {}
for x in LOCATIONS[1:]:
    company = x[0]
    company_state_dict[company] = []
    for i in range(1,len(x)-1):
        if x[i] == '1':
            state = LOCATIONS[0][i]
            company_state_dict[company].append(state)

# retrieve a state list from LOCATIONS
state_list = LOCATIONS[0][1:]

# creates a state_city_list dictionary
state_city_dict = {}
for x in state_list:
    # open state/city files
    STATE_O = open('CS123/STATES/'+x+'.csv','rU')
    # read in state/city files
    STATE_R = csv.reader(STATE_O)
    # strip all items in the read_list into state_name_list
    STATE = []
    strip(STATE, STATE_R)
    state_city_dict[x] = STATE

# reads test file
TEST_O = open('test.csv','rU')
# read test csv
TEST_R = csv.reader(TEST_O)
# strip items in test_r list
TEST = []
for x in TEST_R:
    y = str(x).strip('[]')[1:]
    TEST.append(y[:len(y)-1])

# returns to how many characters that city is matched to tail
def get_score(tail, city):
    score = 0
    L = len(tail)
    for i in range(0,L):
        if i < len(city):
            if tail[i] == city[i]:
                score = score + 1
    return score

# search_city: search a city for an operation's tail in a list of states, return '' if not found
def search_city(operation_tail, state_list, state_city_dict):
    top_match = ''
    top_score = 0
    for state in state_list:
        for city in state_city_dict[state]:
            score = get_score(operation_tail, city)
            if score > top_score:
                top_match = state + ' ' + city
                top_score = score
    return top_match
    
# get_header_tail: if operation is 'UPPC.AZ', return 'UPPC' as header and 'AZ' as tail 
def get_header_tail(operation):
    header = ''
    for c in operation:
        if c != '.':
            header = header + c
        else:
            break
    tail = operation[len(header)+1:]
    return [header, tail]

#for every thing in TEST search a city for it, store in dictionary 
op_city_dict = {}
for operation in TEST:   # for instance 'UPPC.AZ'
    [header, tail] = get_header_tail(operation) # header = 'UPPC' , tail = 'AZ'
    if company_state_dict.has_key(header):     # if UPPC is in file LOCATIONS.csv 
        states = company_state_dict[header]    # then we know the states where UPPC has operation
        op_city_dict[operation] = search_city(tail, states, state_city_dict) # and we search only in those states with the state_city_dictionary
    else:
        op_city_dict[operation] = ''            #if UPPC is not in file LOCATIONS.csv, then we can not find the location of UPPC, just give an empty string 


Writer = csv.writer(open('CS123/NODE_CITY.csv', 'wb'))
for x in op_city_dict:
    Writer.writerow([x, op_city_dict[x]])






