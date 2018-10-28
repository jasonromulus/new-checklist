# print("Hello World")
# checklist = list()
# print (checklist)
# checklist.append('blue')
# print (checklist)
# checklist.append('ornage')
# print (checklist)

# def my_fun_function(say_this):
#     print(say_this)

# my_fun_function('Hello World')

#Start of CRUD part of checklist project
checklist = list()

# create
def create (item):
    checklist.append (item)

# read
def read (index):
    return checklist [index]

# checklist = ['blue', 'orange']
# checklist [1] = 'cats'
# print (checklist)

# update
#
def update (index, item):
    checklist [index] = item

# checklist = ['blue', 'cats']
# checklist.pop (1)
# print (checklist)

# destory
def destroy (index):
    checklist.pop (index)

# list all items in list
def list_all_items ():
    index = 0
    for list_item in checklist:
        print ("{} {}".format (index, list_item))
        index += 1

#mark completed
def mark_completed(index):
    update(index, "√" + checklist[int(index)])
    #update (0, "purple socks")


def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")

        # Remember that item_index must actually exist or our program will crash.
        read(int(item_index))

    # Print all items
    elif function_code == "P":
        list_all_items()

    #stop the loop
    elif function_code == "Q":
        return False

    # Catch all
    else:
        print("Unknown Option")
    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input


# make test function
def test ():
    create ("purple sox")
    create ("red cloak")

    print (read(0))
    print (read(1))

    update (0, "purple socks")
    destroy (1)

    print (read(0))
    # print (read(1))

    mark_completed (0)
    list_all_items ()

    # Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run
    select("P")
    #View results
    list_all_items()

    user_value = user_input("Please Enter a value:")
    print(user_value)
    

# this will run my tests
test ()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit")
    running = select(selection)