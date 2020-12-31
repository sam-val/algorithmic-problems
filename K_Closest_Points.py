import math
import functools


def further_point(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dis1 = abs(x1) + abs(y1)
    dis2 = abs(x2) + abs(y2)
    if dis1 > dis2:
        return p1
    else:
        return p2


def find_max_points(closest_points_heap):
    closest_points_heap.sort(key=lambda x: x[0]*x[0] + x[1]*x[1], reverse=True)
    return closest_points_heap[0]

def k_closest_points(points, k=1):

    # points is a sequence of tuples containing pointX and pointY

    # calculate sum of pointX and pointY of each element in 'points'
    if len(points) <= k:
        return points
    closest_points_heap = []
    for p in points:
        if len(closest_points_heap) < k:
            closest_points_heap.append(p)
        else:
            # find the furthest point in the closest points, can optimize by using better sort-algorithm that is log-n
            furthest = find_max_points(closest_points_heap)

            # then just replace the furthest point with a new point that is closer (if)
            if further_point(furthest, p) == furthest:
                closest_points_heap[closest_points_heap.index(furthest)] = p


    return closest_points_heap


def make_distances(l):
    rs = []
    for p in l:
        dict = {}
        dict['points'] = p
        dict['distance_squared'] = p[0] * p[0] + p[1] * p[1]
        rs.append(dict)
    return rs


def sorting_technique(points, k =1):

    points_with_d = make_distances(points)
    points_with_d.sort(key=lambda x: x['distance_squared'], reverse=False)
    import itertools
    rs = []
    for i in itertools.islice(points_with_d,k):
        rs.append(i['points'])
    return rs

if __name__ == '__main__':
    points = [(2,-1), (-1,-3), (0,0), (4,-1), (-1,-1)]
    rs = k_closest_points(points, k=2)
    # rs = further_point((2,-1), (-1,-3))
    rs2 = sorting_technique(points,k = 2)
    print(rs)
    print(rs2)