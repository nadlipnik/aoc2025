

''' part 1 
count = 0
value = 50
with open('input.txt') as file:
    for line in file:
        if line[0] == 'L' :
            value = value - int( line[ 1: ] )
        else:
            value = value + int( line[ 1: ] )
        if( value % 100 == 0 ):
            value = 0
            count += 1
        
print( count )
'''

''' part 2 '''
count = 0
value = 50
steps = 0
valueOld = 0
with open('input.txt') as file:
    for line in file:
        if line[0] == 'L' :
            dir = -1
            steps = int( line[ 1: ] )
        else:
            dir = 1
            steps = int( line[ 1: ] )

        #print( 'steps ', steps )

        # for 100 steps
        count += int(steps / 100 )
            
        #if( (value + steps % (100*dir)) < 0 or (value + steps % (100*dir) > 100) ):
        #    count += 1
        for k in range( steps % 100 ):
            value += dir
            if( value == 100 ):
                value = 0
                count += 1
            elif( value == 0 ):
                count += 1
            elif( value == -1 ):
                value = 99
        
        #if( value == 0):
        #    count += 1
            #print( 'HERE 2')
            
        print( 'value ', value, ' steps ', steps, ' count ', count)
            
            
            
print( count )
