import matplotlib.pyplot as plt

def parse_file(file_name):
    f = open(file_name, "r")
    lines = f.read()
    x = lines.split(',')
    si = int(x[0])
    x = x[1::]

    #Converting string values to float
    for i in range(len(x)):
        x[i] = float(x[i])

    return (si, x)


def plot_even_odd_parts(x, si):


    x_original = x
    #Reverse the list to get x[-n]
    x_reverse = x[::-1]

    #Append zeros to the beginning because of the starting index
    x = ([0] * abs(si) + x)
    x_reverse = ([0] * abs(si) + x_reverse)


    #Calculate even (xe) and odd (xo) parts of the signal x
    xe = [(x[n] + x_reverse[n])/2 for n in range(abs(si), abs(si)+len(x_original))]
    xo = [(x[n] - x_reverse[n])/2 for n in range(abs(si), abs(si)+len(x_original))]

    xe = [0] * 2 + xe + [0] * 2
    xo = [0] * 2 + xo + [0] * 2

    # Plotting the even part
    plt.stem(range(si-2, si+len(x_original)+2), xe, linefmt='b-', markerfmt='bo', label='Even part')

    # Plotting the odd part
    plt.stem(range(si-2, si+len(x_original)+2), xo, linefmt='r-', markerfmt='ro', label='Odd part')

    #Adding title and labels for the graph
    plt.title('Even and Odd Parts of Signal a Discrete Signal')
    plt.xlabel('n')
    plt.ylabel('Odd and Even Parts')
    plt.legend()
    plt.show()


input_list = ["chirp_part_a.csv", "shifted_sawtooth_part_a.csv", "sine_part_a.csv"]

for file_name in input_list:
    my_input = parse_file(file_name)
    plot_even_odd_parts(my_input[1], my_input[0])

