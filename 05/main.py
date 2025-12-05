def read_input_file(file_path: str):
    ranges = []
    values = []
    new_val = []
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.read().splitlines()
        for line in lines:
            if line == '\n' or line == '':
                pass
            if line.find('-') != -1 :
                val1,val2 = line.split('-')
                ranges.append([int(val1), int(val2)])
            else:
                values.append( line )
        for val in values[1:]:
            new_val.append( int(val) )
    return ranges,new_val



def solve_part1( ranges, values ):
    fresh = 0
    for val in values: # each instance
        for rng in ranges: # range of good
            if( val >= rng[0] and val <= rng[1] ):
                fresh += 1
                break
    print( fresh )
    
def solve_part2( ranges ):
    # sort the list first
    ranges.sort(key = lambda x:x[0])
    #print(ranges)
    vals = []
    vals.append( ranges[0] )
    idx = 0
    for i in range(1, len(ranges)):
        broken = False
        for j in range( 0, len(vals) ):
            # one range is inside another range -> extend
            if( vals[j][0] >= ranges[i][0] and vals[j][1] <= ranges[i][1] ):
                vals[j][0] = ranges[i][0]
                vals[j][1] = ranges[i][1]
                broken = True
                break
            
            # range starts in, but ends after -> extend
            elif( vals[j][0] <= ranges[i][0] and vals[j][1] >= ranges[i][0] and vals[j][1] < ranges[i][1] ):
                vals[j][1] = ranges[i][1]
                broken = True
                break

            # range starts before, but ends in -> extend
            elif( vals[j][0] > ranges[i][0] and vals[j][0] <= ranges[i][1] and vals[j][1] >= ranges[i][1] ):
                vals[j][0] = ranges[i][0]
                broken = True
                break
            # range inside
            elif( vals[j][0] <= ranges[i][0] and vals[j][1] >= ranges[i][1]):
                broken = True
                break

        # none of the above in the loop, need to extend
        if( not broken ):
            vals.append( ranges[i] )
    
    count = 0
    
    for value in vals:
        count += value[1]-value[0]+1
    print( count )
    
if __name__ == "__main__":
    ranges, values = read_input_file( 'input.txt' )
    #print( ranges )
    #print( values )
    #solve_part1( ranges, values )
    solve_part2( ranges )