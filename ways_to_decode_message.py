import os
# print(os.environ['PYTHONPATH'])

def num_ways(data):
    def valid(d1, d2):
        assert len(d1) == 1 and len(d2) == 1, "Character should have length of 1"
        num_string = d1 + d2
        if d1 == "0":
            return False
        elif 26 >= int(num_string) >= 10:
            return True

        return False

    def solve(data):
        nonlocal count
        if len(data) <= 1:
            return
        else:
            for i in range(0,len(data)-1):
                if valid(data[i], data[i+1]):
                    count += 1
                    truncated_data = data[i+2:]
                    solve(truncated_data)


    # decoder = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12,
    #            'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23,
    #            'x':24, 'y':25, 'z':26
    #            }

    count = 1
    solve(data)
    print(count)

def num_ways_ds_dojo(data):
    def solve(data):
        if len(data) == 0: # aka. data = ""
            return 1
        elif data[0] == "0":
            return 0
        elif len(data) == 1:
            try:
                if 9 >= int(data[0]) > 0:
                    return 1
                else:
                    return 0
            except ValueError:
                return 0
        else:
            result = solve(data[1:])
            if (9 >= int(data[0]) > 0) and (26 >= int(data[0] + data[1]) >= 10):
                result += solve(data[2:])
            # memo = result
            return result

    print(solve(data))

def main():
    # rs = num_ways_ds_dojo("1110")
    num_ways("1110")

if __name__ == '__main__':
    main()