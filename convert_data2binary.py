import sys

state_file = "stateabbr.txt"
plants_data = "plants.data"
plants_binary = "plants.csv"

def load_stateabbr():
	dict_state = {}
	f = open(state_file)
	for line in f:
		state = line.strip().split(" ")[0]
		dict_state[state] = "?"
	
	f.close()
	return dict_state

def convert2binary():
	# load states abbriviate
	states_origin = load_stateabbr()
	states = states_origin.copy()

	# prepare write plants binary file
	f_bin = open(plants_binary, "w")
	# write header
	header = "name"
	for s in states:
		header += "," + s

	f_bin.write(header + "\n")

	# read plants.data
	f = open(plants_data, "r")
	for line in f:
		plant = line.strip().split(",")
		plant_name = plant[0]
		new_line = plant_name

		# set bit 1 for states in current line
		for i in range(1, len(plant)):
			if plant[i] in states:
				states[plant[i]] = "y"

		# write to plant binary file
		for s in states:
			new_line += "," + str(states[s])

		# reset state value
		f_bin.write(new_line + "\n")
		states = states_origin.copy()

	f.close()
	f_bin.close()

def main():
	convert2binary()


if __name__ == "__main__":
	sys.exit(main())		