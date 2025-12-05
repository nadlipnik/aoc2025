def read_input_file(file_path: str):
    lines = []
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.read().splitlines()
    return lines
        
def solve_part1( lines: list ):
    joltage = 0
    for line in lines:
        a = '0'
        b = '0'
        length = len(line)
        for idx in range(0,length):
            if( line[idx] > a and idx < length-1 ):
                a = line[idx]
                b = '0'
            elif( line[idx] > b and idx < length ):
                b = line[idx]
#            else: # already at end
#                if( line[idx] > b ):
#                    b = line[idx]
        joltage += pow(10,1)*int(a) + int(b)
    
    print( 'joltage ', joltage )
    
def solve_part2( lines: list ):
    joltage = 0
    for line in lines:
        a = '0' #1
        b = '0' #2
        c = '0' #3
        d = '0' #4
        e = '0' #5
        f = '0' #6
        g = '0' #7
        h = '0' #8
        i = '0' #9
        j = '0' #10
        k = '0' #11
        l = '0' #12
        length = len(line)
        
        for idx in range(0,length):
            if( line[idx] > a and idx < length-11 ):
                a = line[idx]
                b=c=d=e=f=g=h=i=j=k=l = '0'
            elif( line[idx] > b and idx < length-10 ):
                b = line[idx]
                c=d=e=f=g=h=i=j=k=l = '0'
            elif( line[idx] > c and idx < length-9 ):
                c = line[idx]
                d=e=f=g=h=i=j=k=l = '0'
            elif( line[idx] > d and idx < length-8 ):
                d = line[idx]
                e=f=g=h=i=j=k=l = '0'
            elif( line[idx] > e and idx < length-7 ):
                e = line[idx]
                f=g=h=i=j=k=l = '0'
            elif( line[idx] > f and idx < length-6 ):
                f = line[idx]
                g=h=i=j=k=l = '0'
            elif( line[idx] > g and idx < length-5 ):
                g = line[idx]
                h=i=j=k=l = '0'
            elif( line[idx] > h and idx < length-4 ):
                h = line[idx]
                i=j=k=l = '0'
            elif( line[idx] > i and idx < length-3 ):
                i = line[idx]
                j=k=l = '0'
            elif( line[idx] > j and idx < length-2 ):
                j = line[idx]
                k=l = '0'
            elif( line[idx] > k and idx < length-1 ):
                k = line[idx]
                l = '0'
            elif( line[idx] > l and idx < length ):
                l = line[idx]

        joltage += pow(10,11)*int(a) + pow(10,10)*int(b) + pow(10,9)*int(c) + pow(10,8)*int(d) + pow(10,7)*int(e) + pow(10,6)*int(f) + pow(10,5)*int(g) + pow(10,4)*int(h) + pow(10,3)*int(i) + pow(10,2)*int(j) + pow(10,1)*int(k) + pow(10,0)*int(l)
    
    print( 'joltage ', joltage )
        
if __name__ == "__main__":
    lines = read_input_file( "input.txt" )
    solve_part1( lines )
    solve_part2( lines )