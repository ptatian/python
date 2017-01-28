import copy

class cState:

    def __init__(self):
        self.labels = []
        self.values = []

    def readout(self):
        b = len(self.labels)
        for a in range( b ):
            print( self.labels[a], self.values[a] )
        print( )

    def set(self, n ):
        self.values[n] = 1
        self.readout()

    def reset(self, n):
        self.values[n] = 0
        self.readout()
        
class cRod:

    def __init__(self,l,c):
        self.logic = l
        self.clock = c

class cProgram:
    
    def __init__(self):
        self.title = ""
        self.description = ""
        self.initstate = cState()
        self.rods = []

def initstate():

    state = cState()
    b = len(program.initstate.labels)
    for a in range( b ):
        state.labels.append( program.initstate.labels[a] )
        state.values.append( program.initstate.values[a] )
    return state

def readout():
    b = len(state.labels)
    for a in range( b ):
        print( state.labels[a], state.values[a] )
    print( )

def clock():
    bits = len(program.initstate.labels)
    rods = len(program.rods)
    newstate = cState()
    newstate.labels = copy.deepcopy( state.labels )
    newstate.values = copy.deepcopy( state.values )
    for i in range( rods ):
        eval = 0
        for a in range( bits ):
            if program.rods[i].logic[a] == None:
                pass
            elif state.values[a] != program.rods[i].logic[a]:
                eval = 0
                break
            else:
                eval = 1
        if eval:
            for a in range( bits ):
                if program.rods[i].clock[a] == 1:
                    newstate.values[a] = 1
                elif program.rods[i].clock[a] == 0:
                    newstate.values[a] = 0
    state.values = copy.deepcopy( newstate.values )
    state.readout()

def print_program():
    bits = len(program.initstate.labels)
    rods = len(program.rods)
    stubsize = len(program.initstate.labels[0])

    print( program.title )

    ### Header
    stub = stubsize * " "

    print( stub, end='' )
    for i in range(rods):
        print( "   ", i + 1, end=' ' )
    print()

    print( stub + " ", end='' )
    for i in range(rods):
        print( " T F| ", end='' )
    print()

    for j in range(bits):
        print( program.initstate.labels[j], end='  ' )
        for i in range(rods):
            if program.rods[i].logic[j] == None:
                print( " | |", end='' )
            elif program.rods[i].logic[j] == 0:
                print( " |L|", end='' )
            else:
                print( "L| |", end='' )
            if program.rods[i].clock[j] == None:
                print( "  ", end='' )
            else:
                print( "C ", end='' )
        print()

    print()
        
    
    

program = cProgram()

''' CHECKOUT '''
program.title = "Checkout"
program.initstate.labels = [ "A", "B", "C" ]
program.initstate.values = [ 0, 0, 0 ]
program.rods.append( cRod( [ None, 0, None ], [ 0, None, None ] ) )
program.rods.append( cRod( [ None, 1, None ], [ 1, None, None ] ) )
program.rods.append( cRod( [ None, None, 0 ], [ None, 0, None ] ) )
program.rods.append( cRod( [ None, None, 1 ], [ None, 1, None ] ) )
program.rods.append( cRod( [ 1, None, None ], [ None, None, 0 ] ) )
program.rods.append( cRod( [ 0, None, None ], [ None, None, 1 ] ) )
''' '''

''' FINAL COUNT DOWN 
program.title = "Final Count Down"
program.initstate.labels = [ "A", "B", "C" ]
program.initstate.values = [ 1, 1, 1 ]
program.rods.append( cRod( [ 1, None, None ], [ 0, None, None ] ) )
program.rods.append( cRod( [ 0, None, None ], [ 1, None, None ] ) )
program.rods.append( cRod( [ 0, 1, None ], [ None, 0, None ] ) )
program.rods.append( cRod( [ 0, 0, None ], [ None, 1, None ] ) )
program.rods.append( cRod( [ 0, 0, 1 ], [ None, None, 0 ] ) )
program.rods.append( cRod( [ 0, 0, 0 ], [ None, None, 1 ] ) )
'''

''' AUTOMATIC ELEVATOR
program.title = "Automatic Elevator"
program.initstate.labels = [ "2nd floor", "1st floor", "Up/Down  " ]
program.initstate.values = [ 0, 1, 0 ]
program.rods.append( cRod( [ None, None, 0 ], [ 0, None, None ] ) )
program.rods.append( cRod( [ None, None, 1 ], [ 1, None, None ] ) )
program.rods.append( cRod( [ None, None, 1 ], [ None, 0, None ] ) )
program.rods.append( cRod( [ None, None, 0 ], [ None, 1, None ] ) )
'''

state = initstate()
readout()

print_program()
