import random

# regular
# [5, 4, 3, 1, 0]
# [4, 5, 3, 1, 0] 
# [4, 3, 5, 1, 0]
# [3, 4, 5, 1, 0]
# [3, 4, 1, 5, 0]
# [3, 1, 4, 5, 0]
# [1, 3, 4, 5, 0]

# enhanced
# [5, 4, 3, 1, 0]
# [4, 5, 3, 1, 0]
# [4, 3, 5, 1, 0]
# [4, 3, 1, 5, 0]
# [4, 3, 1, 0, 5]
# [3, 1, 0, 4, 5]

def bubbleSort(input_list):
    print(f"Initial sequence for bs: {input_list}")

    if len(input_list) == 0:
        print("Cannot sort an empty list!")
        return 
    
    if len(input_list) == 1:
        print("Only one element, cannot sort!") 
        return
    
    if len(input_list) == 2:
        if input_list[0] > input_list[1]:
            return [input_list[1], input_list[0]]
        else:
            print("Already sorted list!")
    
    index = 0
    current = 0
    swaps = 0       #DEBUG
    restarts = 0    #DEBUG

    while True:

        if index + 1 == len(input_list):
            print(f"Final sequence: {input_list}")
            print(f"Number of swaps: {swaps}")
            print(f"Total passes/restarts: {restarts}")
            return input_list
        
        previous = input_list[index]
        current = input_list[index + 1]

        if previous > current:
            # print(input_list)
            input_list[index + 1] = previous
            input_list[index] = current
            swaps += 1
            restarts += 1
            index = 0
            continue
        
        index += 1
        
#Worst order would be an inverted list: [5, 4, 3, 1, 0]

def enhancedbubbleSort(input_list):
    print(f"Initial sequence for ebs: {input_list}")

    if len(input_list) == 0:
        print("Cannot sort an empty list!")
        return 
    
    if len(input_list) == 1:
        print("Only one element, cannot sort!") 
        return
    
    if len(input_list) == 2:
        if input_list[0] > input_list[1]:
            return [input_list[1], input_list[0]]
        else:
            print("Already sorted list!")
    
    index = 0
    current = 0
    new_swaps = 0
    passes = 0
    swaps_made = False

    while True:

        if index + 1 == len(input_list):
            if swaps_made == False:
                print(f"Final sequence: {input_list}")      #DEBUG
                print(f"Number of swaps: {new_swaps}")          #DEBUG
                print(f"Total passes/restarts: {passes}")
                return input_list
            elif swaps_made == True:
                # print(f"New pass starting. Input_list: {input_list}")                           #DEBUG
                index = 0
                swaps_made = False
                passes += 1
                continue
        
        previous = input_list[index]
        current = input_list[index + 1]

        if previous > current:
            input_list[index + 1] = previous
            input_list[index] = current
            # print(f"Swapped: {previous} and {current}, {input_list}")   #DEBUG

            new_swaps += 1
            swaps_made = True
            index += 1
        else:
            # print(f"No Swap {previous} and {current}, {input_list}")    #DEBUG
            index += 1

seq_1 = [5, 4, 3, 2, 1]
seq_2 = [5, 4, 3, 2, 1]
#enhancedbubbleSort(seq_1)

test_arr = list(range(999, 0, -1))
other_test = list(range(999, 0, -1))
# rand_size = 1000
# for i in range(999, 0, -1):
#     test_arr.append(i)
#     other_test.append(i)

bubbleSort(test_arr)
enhancedbubbleSort(other_test)
