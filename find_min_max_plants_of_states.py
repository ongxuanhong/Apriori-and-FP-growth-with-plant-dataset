import sys

plants = "plants.csv"
state_file = "stateabbr.txt"

def init_states():
	dict_state = {}
	f = open(state_file)
	for line in f:
		state = line.strip().split(" ")[0]
		dict_state[state] = 0
	
	f.close()
	return dict_state

def count_num_plant_each_state():
	f = open(plants, "r")
	states = init_states()

	# read header file
	header = f.readline().strip().split(",")
	
	# counting number of plant in each state
	num_instances = 0
	for line in f:
		num_instances += 1
		plant = line.strip().split(",")

		# get state column
		num_state = len(plant)
		for i in range(1, num_state):
			# add up number of plant in current state
			if plant[i] == "y":
				states[header[i]] += 1

	f.close()
	return states, num_instances

def find_min_max(states, num_instances):
	result = {"state_max":"", "state_min":"", 
				"num_max":0, "num_min":35000,
				"percent_max":0.0, "percent_min":0.0}

	# find min max in states
	for s in states:
		# find min
		if states[s] < result['num_min']:
			result['num_min'] = states[s]
			result['state_min'] = s

		# find max
		if states[s] > result['num_max']:
			result['num_max'] = states[s]
			result['state_max'] = s

	result['percent_max'] = float(result['num_max'])/num_instances * 100
	result['percent_min'] = float(result['num_min'])/num_instances * 100
	return result

def main():
	states, num_instances = count_num_plant_each_state()
	result = find_min_max(states, num_instances)
	print result


if __name__ == "__main__":
	sys.exit(main())		