from output_ways import print_list


def list_practice():
    num_list = [i for i in range(1, 4)]
    num_list.append([4])
    num_list.append([5, 6])
    num_list.extend([7, 8])
    num_list.insert(0, 0)
    print_list(num_list)
    num_list[2:4] = num_list[4:6]
    print_list(num_list)
    num_list[4] = [10]
    print_list(num_list)
    return num_list
