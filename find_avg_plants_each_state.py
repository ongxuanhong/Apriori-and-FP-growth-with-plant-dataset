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

def find_avg_plants(states, num_instances):
	num_plants = []

	# calculate avg plants for each state
	for s in states:
		num_plants.append(states[s])

	# calculate avg plants of each state
	result = sum(num_plants)/len(states)
	return result

def main():
	states, num_instances = count_num_plant_each_state()
	result = find_avg_plants(states, num_instances)
	print "Average plants each state: ", result


if __name__ == "__main__":
	sys.exit(main())		