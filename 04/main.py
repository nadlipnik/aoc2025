def read_input_file(file_path: str):
    lines = []
    with open(file=file_path, mode="r") as input_file:
        #for line in input_file:
        #    str1 = list(line)
        #    lines.append(str1) # Add the "row" to your list.
        for line in input_file:
            chars = []
            for char in line:
                if( char != '\n' ):
                    chars.append(char)
                    #print(char)
            lines.append( chars )
    return lines


def solve_part1( lines ):
    len1 = len( lines )
    len2 = len(lines[0] )
    count = 0
    for idx_line in range(0, len1 ):
        for idx_char in range(0, len2 ):
            if lines[idx_line][idx_char] == '@':
                neighbours = 0
                for idx1 in range(-1, 2):
                    for idx2 in range(-1, 2):
                        if( idx_line+idx1 < 0 or idx_line + idx1 >= len1 or idx_char + idx2 < 0 or idx_char + idx2 >= len1 or ( idx1 == 0 and idx2 == 0 )):
                            pass
                        else:
                            if( lines[idx_line+idx1][idx_char+idx2] == '@' ) :
                                neighbours += 1
                if( neighbours < 4 ):
                    count += 1
    print( count )

# this is actually part 1 with an extension
def get_current_solution( lines ):
    len1 = len( lines )
    len2 = len(lines[0] )
    count = 0
    removed = []
    for idx_line in range(0, len1 ):
        for idx_char in range(0, len2 ):
            if lines[idx_line][idx_char] == '@':
                neighbours = 0
                for idx1 in range(-1, 2):
                    for idx2 in range(-1, 2):
                        if( idx_line+idx1 < 0 or idx_line + idx1 >= len1 or idx_char + idx2 < 0 or idx_char + idx2 >= len1 or ( idx1 == 0 and idx2 == 0 )):
                            pass
                        else:
                            if( lines[idx_line+idx1][idx_char+idx2] == '@' ) :
                                neighbours += 1
                if( neighbours < 4 ):
                    count += 1
                    removed.append([idx_line, idx_char])
    print( count )
    return count, removed

def solve_part2( lines ):
    count = 0
    while( 1 ):
        c,r = get_current_solution(lines)
        if( c == 0 ):
            break
        count += c
        # now correct the lines
        for element in r:
            lines[ element[0]][element[1]] = '.'
    print(count)


if __name__ == "__main__":
    lines = read_input_file( "input.txt" )
    #solve_part1( lines )
    solve_part2( lines )