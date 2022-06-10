"""This module has phrases only."""
def hello():
    """Print "Hello!"."""
    print("Hello!")

def hi():
    """Print "Hi!"."""
    print("Hi!")

def morning():
    """Print "Good morning!"."""
    print("Good morning!")
    
def request_num():
    """Print "Please, entered number: " and read line in console."""
    try:
    	num = float(input("Please, enter a floating point number: "))
    except ValueError:
    	print("Could not convert data to an type 'float'. Please, enter a floating point number.")
    	num = 0
    
    return num
