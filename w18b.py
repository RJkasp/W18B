# Setup a GitHub repository and local git repository
# We don't have a script that will do this for python, so you have 2 options:
# Create a copy of the projectStarter script and modify the copy to work for a simple python file
# Do the steps manually (create the repo, clone it, create the python inside of that cloned repo)
# Create a python script that achieves the following:
# Have a function that takes in one number as an argument
# This function will:
# print "Fizz" if the number is divisible by 3
# print "Buzz" if the number is divisible by 5
# print "FizzBuzz" if the number is divisible by both 3 and 5
# The function should only ever print once per number!
# Hard code a list of random numbers with at least 15 numbers inside
# Run the function created for each number in your list.
# Once the script is working git add, commit and push your code

def num(number):
    if number %3 == 0:
        print('fizz')
    elif number %5 == 0:
        print('buzz')
    elif number %5 == 0 and number %3 == 0:
        print('fizzbuzz')
    else:
        print('not divisable by either')        

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for x in numbers:
    num(x)

