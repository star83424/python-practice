
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    param = (1, 2, (4, 5))
    print('x:{0}, y:{1}, z:{2}'.format(*param))

    param2 = {'latitude': '37.24N', 'longitude': '-115.81W'}
    print(*param2)

    # print('lat:{latitude}, lng:{longitude}'.format(*param2))


def print_list(num_list):
    print(f'list: {num_list}')
