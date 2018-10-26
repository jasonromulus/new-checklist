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
def mark_completed(index)


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

    list_all_items ()

test ()