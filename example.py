
def example1():
    return 3
    
def example2():
    while True: print("loop...")
    return 3

def loop_forever():
    while True: print("loop...")
    return 3



def example3():  # TODO: clearer becuase of for loop? less clear becuase of range
    #TODO: check that that does what I think it does
    out = 0
    for i in range(0, 10):
        out += i
    return out
    
    
#TODO: example 4

# when n is a natural number
def example4(n):
    if n == 0 :
        return 0
    elif n % 2 == 0 :
        return n / 2
    else :
        return 3 * n + 1
        
        
# when n is a natural number
def collatz(n):
    if n == 0 :
        return 0
    elif n % 2 == 0 :
        return n / 2
    else :
        return 3 * n + 1



# def does_it_halt(program, aruments):
#     # left as an exercise to the reader
#     return True

import inspect

def does_it_halt(program, aruments):
    program_source = inspect.getsourcelines(program)[0]
    lines_forever = [line for line in program_source 
                              if " while True: " in line]
    if lines_forever:
        return False
    #TODO: left as an exercise to the reader
    return True

does_it_halt(loop_forever, "")


#TODO show arguments don't matter
def does_ever_halt(program):
    program_source = inspect.getsourcelines(program)[0]
    lines_forever = [line for line in program_source 
                              if " while True: " in line]
    if lines_forever:
        return False
    #TODO: left as an exercise to the reader
    return True


def good(program, aruments):
    if not does_it_halt(program, aruments):
        print("this program runs forever, sorry")
    return program(aruments)


def bad(program):
    if does_it_halt(program, program):
        loop_forever()
    else:
        return True

# bad(bad)


print(example4())

    
    
