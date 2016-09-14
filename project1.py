__author__ = 'kurt'
import sys


def main():
    """This is the main function of the Module, designed to give statistics on a batch of imported numbers"""
    try:
        read_file = open(sys.argv[1], "r")
    except IndexError:
        read_file = sys.stdin

    try:
        write_file = open(sys.argv[2], "w")
    except IndexError:
        write_file = sys.stdout
    try:
        number_array = read_int(read_file)
        write_file.write("number = " + str(num_count(number_array)) + "\n")
        write_file.write("minimum = " + str(min_num(number_array)) + "\n")
        write_file.write("maximum = " + str(max_num(number_array)) + "\n")
        write_file.write("sum = " + str(sum_num(number_array)) + "\n")
        write_file.write("product = " + str(prod_num(number_array)) + "\n")
        write_file.write("average = " + str(avg_num(number_array)) + "\n")
        write_file.write("median = " + str(med_num(number_array)) + "\n")
        write_file.write("modes = " + str(mode_num(number_array)) + "\n")
    except IndexError:
        write_file.write("minimum = none\n")
        write_file.write("maximum = none\n")
        write_file.write("sum = 0\n")
        write_file.write("product = 1\n")
        write_file.write("average = none\n")
        write_file.write("median = none\n")
        write_file.write("modes = []\n")


def read_int(read_file):
    """This reads in the file and exports a list of all the numbes combined in the list"""
    numbers = read_file.read()
    totalarray = numbers
    second_array = totalarray.split()
    new_array = []
    for i in range(len(second_array)):
        if second_array[i] == ' ':
            pass
        elif second_array[i] == '\n':
            pass
        else:
            new_array.append(second_array[i])

    new_array = [int(i) for i in new_array]
    return new_array


def sum_num(num_list):
    """Sums the batch of numbers and returns this num as an integer"""
    total = 0
    for i in range(len(num_list)):
        total += num_list[i]
    return total


def num_count(num_list):
    """Counts how many numbers are presented and returns that value"""
    total = 0
    for i in range(len(num_list)):
        total += 1
    # if total == 0:
    #     return "none"
    return total


def min_num(num_list):
    """Goes through a list of numbers and returns the smallest number"""
    sort_list = sorted(num_list)
    return sort_list[0]


def max_num(num_list):
    """Goes through a list of numbers and returns the smallest number"""
    sort_list = sorted(num_list)
    return sort_list[len(num_list) - 1]


def prod_num(num_list):
    """Takes a list of numbers and returns their product"""
    total = num_list[0]
    for i in range(1, len(num_list)):
        total = total * num_list[i]
    return total


def avg_num(num_list):
    """Takes a list of numbers and reutrns their average"""
    return sum_num(num_list) / num_count(num_list)


def med_num(num_list):
    """Takes in a list and returns the median of that list, averaging if even"""
    sort_list = sorted(num_list)
    if len(num_list) % 2 == 0:
        index = int(len(num_list) / 2)
        index2 = int(index - 1)
        average = ((sort_list[index] + sort_list[index2]) / 2)
        return average
    else:
        index = int(len(num_list) / 2)
        return sort_list[index]


def mode_num(num_list):
    """Takes in a list and very complicatedly returns the mode"""
    sort_list = sorted(num_list)
    duplicate_list = []
    holder = 0
    third_list = []
    last_list = []
    for number in sort_list:
        switcher = False
        count = 0
        for i in range(len(sort_list)):
            if number == sort_list[i]:
                count += 1
                switcher = True
        if switcher == True:
            duplicate_list.append(number)
            duplicate_list.append(count)
    for i in range(1, len(duplicate_list), 2):
        if duplicate_list[i] >= holder:
            holder = duplicate_list[i]
    for i in range(1, len(duplicate_list), 2):
        if duplicate_list[i] == holder:
            third_list.append(duplicate_list[i - 1])
    for i in third_list:
        if i not in last_list:
            last_list.append(i)
    return sorted(last_list)


if __name__ == "__main__":
    main()