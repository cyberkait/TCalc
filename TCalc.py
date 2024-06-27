"""
My calculator project
"""

#imports
from menus import get_menu_choice
import calc_funcs as cf
import sys


# Creating necessary variables.
result = 0
memory = 0
menu = ["add", "add to memory", "subtract", "subtract from memory", "multiply", "multiply by memory", "divide", "divide by memory", "store value in memory", "clear memory", "quit"]


# Running the program.
while True:
    print(f"Current memory: {memory}")
    choice = get_menu_choice(menu)
    match choice:
        case "add":
            nums = cf.two_nums()
            result = cf.add(nums[0], nums[1])
            print(f"{nums[0]}+{nums[1]} = {result}")
        case "add to memory":
            num = cf.get_num("Enter number to add to memory: ")
            old_memory = memory
            memory += num
            print(f"{old_memory}+{num} = {memory}")
        case "subtract":
            nums = cf.two_nums()
            result = cf.subtract(nums[0], nums[1])
            print(f"{nums[0]}-{nums[1]} = {result}")
        case "subtract from memory":
            num = cf.get_num("Enter number to subtract from memory: ")
            old_memory = memory
            memory -= num
            print(f"{old_memory}-{num} = {memory}")
        case "multiply":
            nums = cf.two_nums()
            result = cf.multiply(nums[0], nums[1])
            print(f"{nums[0]}×{nums[1]} = {result}")
        case "multiply by memory":
            num = cf.get_num("Enter a number to multiply by memory: ")
            old_memory = memory
            memory *= num
            print(f"{old_memory}×{num} = {memory}")
        case "divide":
            nums = cf.two_nums()
            result = cf.divide(nums[0], nums[1])
            print(f"{nums[0]}÷{nums[1]} = {result}")
        case "divide by memory":
            num = cf.get_num("Enter a number to divide by memory: ")
            old_memory = memory
            memory /= num
            print(f"{old_memory}÷{num} = {memory}")
        case "store value in memory":
            num = cf.get_num("Enter number to store: ")
            memory = num
            print(f"Number in memory is now {num}")
        case "clear memory":
            memory = 0
            print("Memory cleared.")
        case "quit":
            print("Exiting.")
            sys.exit()