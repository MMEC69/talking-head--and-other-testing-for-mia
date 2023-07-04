#lets illustrate threading
import threading

import threading

def print_cube(num):
    print("Cube: {}" .format(num*num*num))
    #this is function to print cube of a given number

def print_square(num):
    #function to print square of a given number
    print("Square: {}" .format(num*num))

if __name__ == "__main__":
    #creating a thread
    t1 = threading.Thread(target = print_square, args = (10,))
    t2 = threading.Thread(target = print_cube, args = (10,))

    #starting thread 1
    t1.start()

    #starting thread 2
    t2.start()

    #wait until thread 1 is completly executed
    t1.join()

    #wait until thread 2 is completly executed
    t2.join()
    #both done correctly
    print("Done!")