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
def create(item):
    checklist.append (item)

# read
def read(index):
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

def destroy (index):
    checklist.pop (index)

def test ():
    create ("purple sox")
    create ("red cloak")

    print (read(0))
    print (read(1))

    update (0, "purple socks")
    destroy (1)

    print (read(0))
    # print (read(1))

test ()

def list_all_items():
    for list_item in checklist:
        print (list_item)