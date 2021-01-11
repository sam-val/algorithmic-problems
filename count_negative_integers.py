"""
Count negative integers in a
sorted 2-d matrix, sorted row-wise, column-wise

"""
import os


def solve_native(m):
    # loop through the row(y) and columns(x)
    rs = []
    for row in m:
        for column in row:
            if column < 0:
                rs.append(column)

    return len(rs)

def solve_optimal(m):
    """
    for sorted matrix
    """
    if not len(m) > 0:
        return 0
    # traverse from top right
    rs = 0
    walk = len(m[0]) - 1 # top right
    for row in m:
        while walk >= 0:
            if row[walk] < 0:
                rs += (walk + 1)
                break
            walk -= 1 
    return rs
    
def main():
    matrix = [[-3,-2,-1,1],[-2,2,3,4],[4,5,7,8]]
    rs = solve_optimal(matrix)
    print(rs)

if __name__ == "__main__":
    main()