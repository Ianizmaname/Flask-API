# create a function
def print_5_times(parameter = 'loop', loop_amount = 5):
    counter = 0
    print(global_var)
    while counter < loop_amount:
        print(counter, parameter)
        counter += 1
    return 'something else'

 def hypotenuse_calculator(side_a =1, side_b =1):
    hypotenuse = (side_a ** 2 + side_b ** 2) ** (1/2)
    return round(hypotenuse, 2)

def shout(output_string = 'hello', repitition_amount = 2):
    if repitition_amount <= 10:
        for i in range(repitition_amount):
            print(output_string.upper())
    else:
        print('you are too loud')
    return 'done'

# call
# print('print')
# global_var = 'global variable'
# test = print_x_times('something', 4)
# print(test)

# print(hypotenuse_calculator(side_a = 4, side_b = 5))

# exercise
status = shout('test', 5)
print(status)