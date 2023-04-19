import matplotlib.pyplot as plt

def parse_file(file_name):
	#Read the input file and parse to get si, a, b, and x values
	f = open(file_name, "r")
	lines = f.read()
	x = lines.split(',')
	si = int(x[0])
	a = int(x[1])
	b = int(x[2])
	x = x[3::]
	#Convert the string values to float
	for i in range(len(x)):
	    x[i] = float(x[i])

	return (x, si, a, b)


def shifted_scaled(x, si, a, b):
	y = {}

	#Either shrink or expand and then shift the signal
	for i in range(si, si+len(x)):
		val = (i/abs(a))-(b/abs(a))

		if (val == int(val)):
			y[int(val)] = x[i-si]

	#Store the values of keys corresponding to shifted scaled version
	keys = [k for k in y]
	values = [val for val in y.values()]
	#Store initial and final keys to be used in range for plotting
	initial = keys[0]
	final = keys[-1]


	for i in range(len(keys)):
		keys[i] = abs(initial - keys[i])

	#Store the shifted keys
	shifted_indices = [0] * (keys[-1]+1)


	for i in range(len(keys)):
		shifted_indices[keys[i]] = values[i]

	#Plotting the graph depending on value of a

	#NPositive a does not cause reflection
	if (a > 0):
		n_range = range(initial, final+1)
		plt.stem(n_range, shifted_indices, linefmt='red', markerfmt='ro', label='y[n]')
	#If a is negative, the graph is reflected over y-axis
	else:
		n_range = range(-final, -initial+1)
		shifted_indices.reverse()
		plt.stem(n_range, shifted_indices, linefmt='red', markerfmt='ro', label='y[n]')


	#Add title and labels to the graph
	plt.xlabel('n')
	plt.ylabel('x[n] / y[n]')
	plt.title('Shifted and Scaled Signal')
	plt.legend()
	plt.show()
	




input_list = ["chirp_part_b.csv", "shifted_sawtooth_part_b.csv", "sine_part_b.csv"]

for file_name in input_list:
    my_input = parse_file(file_name)
    shifted_scaled(my_input[0], my_input[1], my_input[2], my_input[3])


