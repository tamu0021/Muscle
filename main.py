# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import BigThree

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # input big3 data
    print('Please teach me your weight')
    weight = int(input())
    print('Please teach me your bench-press weight')
    bench_press = int(input())
    print('Please teach me your squat weight')
    squat = int(input())
    print('Please teach me your dead lift weight')
    dead_lift = int(input())

    # Instance BigThree Class
    big_three = BigThree.BigThree(weight, bench_press, squat, dead_lift)

    # output big3 data
    big_three.output_big_three_weight_ratio()
    big_three.output_big_three_weight_total()
    big_three.output_big_three_weight_total_ratio()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
