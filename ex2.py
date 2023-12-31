############### USER INPUT ############

# name = input('Enter your name here: ')

############### LISTS ############

countries = ['Rwanda','uganda','Kenya','Tanzania','Rwanda','Burundi','Morocco','Rwanda']
fruits = ['Avocado','banana','melon','passion']
numb = [3,5,2,8,7,1,6,4,9]
print(type(countries))                      # it checks the datatype of the variable
print(countries[2:])                        # it prints elements of a list that comes after a specified index
print(countries[:2])                        # it prints elements of a list that comes prior to a specified index
print(countries[0:3])                       # it prints elements of a list that are between the specified indexes
countries[6] = 'DRC'                        # it changes the value of that index
print(countries[-1])                        # prints the last nth Element in the list
print(len(countries))                       # prints the total number of elements in the list
countries.extend(fruits)                    # it joins the second list to the first one
print(countries)
countries.append('South sudan')             # it adds or appends an element to the of the list
countries.insert(3,'Edwin')                 # it inserts an element before a specified index in the list
print(countries)
countries.remove('Edwin')                   # it removes an element from the list
print(countries)
indexNo = countries.index('Burundi')        # it checks the index of a given element inside a list
print(indexNo)
number = countries.count('Rwanda')          # it returns the number of times a given element appears in the list
print(number)
numb.sort()
print(numb)                                 # it sorts the list in the ascending order
print(fruits)
fruits.reverse()                            # it reverses the order of elements in the list
print(fruits)
numb2 = numb.copy()                         # it duplicates a list 
print(numb2)  
numb2.pop()                                 # it removes (or pops out) the last element in the list                               
numb2.pop(2)                                 # it removes the element in the list with the specified index same as writting ( del numb2[2] )                             
print(numb2)

# numb2.clear() =! del numb2      (the clear method deletes every element from the list but the list remains to exist while the del removes everything the variable itself included )


########################### TUPLES ##############################

# A TUPLE IS SIMPLY AN IMMUTABLE LIST BUT INSTEAD OF USING SQUARE BRAQUETS [] WE USE PARANTHESIS ()

tuple1 = (3,'Hello', True, 4)
print(type(tuple1))


########################### FUNCTIONS ##############################

print('this is an example of a function')
name = input('Enter your name here: ')
age = input('Enter your age here: ')

def function_example(name, age):                        # function definition with 2 parameters
    print('Your name is '+name+'. And You are ',age, 'years old')

def friends_list(*friends):                             # (*friends) means that we are going to be passing an uknown number of parameters in form of a tuple
    print('here are your friends: ', friends)
    print('The last one of them is ',friends[-1])

function_example(name, age)                             # function calling & passing 2 arguments
friends_list('Jerome','John','Jeremy','Khalifa','Benjamin')   # function calling



########################### IF STATEMENT ##############################

print('This is an example of If statement')
a = input('Enter a number to compare: ')
b = input('Enter a second number to compare: ')

if a>b:
    print(a, 'Is greater' )
elif b>a: 
    print(b, 'Is greater')
else :
    print('these numbers are equal')