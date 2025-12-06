def read_input_file(file_path: str):
    operations = []
    values = []
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.read().splitlines()
        for line in lines:
            values.append( line.split() )
    #print( values )
    operations = values[-1]
    values = values[:-1]
    return values,operations

def transpose( values ):
    val1 = list(map(list, zip(*values)))
    return val1


def solve_part1( values, operations ):
    sum = 0
    # columns
    for i in range(0, len(operations) ):
        if( operations[i] == '*' ):
            current_sum = 1
        else:
            current_sum = 0
        # each line in column
        #print(values[i])
        for j in range( 0, len( values[i] ) ):
            if( operations[i] == '*' ):
                current_sum *= int(values[i][j] )
            else:
                current_sum += int(values[i][j] )
        #print( current_sum )
        sum += current_sum
    print(sum)
    
def read_part2( file ):
    values = []
    with open( file ) as fileobj:
        for line in fileobj:
            lin = []
            for ch in line:
                lin.append( ch )
                #print(ch)
            values.append( line[:-1] )
    return values[:-1]

def solve_part2( values, operations ):
    lines = []
    lin = []
    for line in values:
        
        chars = ''
        for char in line:
            chars += char
        if( chars == '   ' or chars == '    '):
            lines.append(lin)
            lin = []
        else:
            lin.append( int(chars) )
    lines.append( lin )
    print( lines )
    print( operations )
    
    sum = 0
    for i in range(0, len( lines ) ):
        if( operations[i] == '*' ):
            current_sum = 1
        else:
            current_sum = 0
        for j in range( 0, len( lines[i] ) ):
            if( operations[i] == '*' ):
                current_sum *= int(lines[i][j] )
            else:
                current_sum += int(lines[i][j] )
        #print( current_sum )
        sum += current_sum
    print(sum)
    

if __name__ == "__main__":
    values, operations = read_input_file( 'input.txt' )
    #values=transpose(values)
    #print( values )
    #print( operations )
    #solve_part1( values, operations )
    
    values = read_part2( 'input.txt' )
    values = transpose( values )
    #print( values )
    #print( operations )
    solve_part2( values, operations )
