def read_input_file(file_path: str):
    with open(file=file_path, mode="r") as input_file:
        line = input_file.readline()
        return line.strip().split(',')
    
def solve_part1():
    lines = read_input_file( 'input.txt' )

    sum = 0
    
    for line in lines:
        start,end = line.split('-')
        
        for i in range( int(start), int(end)+1 ):
            number = str(i)
            length = len(number)
            #print(length)
            # check if all the same
            
            # check if has repeat twice
            if( length % 2 == 0 ) :
                #print( length/2-1)
                #print( 'length ', length, 'first half ', number[:int(length/2)], 'second half ', number[int(length/2):] )
                if( number[:int(length/2)] == number[int(length/2):] ):
                    #print(number)
                    sum += i
    print('sum ', sum)
    
def solve_part2():
    lines = read_input_file( 'input.txt' )

    sum = 0

    for line in lines:
        start,end = line.split('-')
        
        for i in range( int(start), int(end) + 1):
            number = str(i)
            length = len(number)
            
            # loop through characters of number
            for j in range(1, length//2+1):
                # now create a string of same length
                my_str = number[:j]
                new_str = ''
                for k in range(1, length//j+1):
                    new_str += my_str
                if( new_str == number ):
                    #print( 'ID is ', i, ' new_str ', new_str, ' my_str ', my_str )
                    sum += i
                    break
                #print('number ', number, ' my_str ', my_str, ' new_str ', new_str)
    print( sum )

if __name__ == "__main__":
    #solve_part1()
    solve_part2()