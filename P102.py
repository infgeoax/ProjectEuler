

def cross_product(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]

def contains_origin(triangle):
    c1 = cross_product(triangle[0], triangle[1])
    c2 = cross_product(triangle[1], triangle[2])
    c3 = cross_product(triangle[2], triangle[0])
    return (c1>=0 and c2>=0 and c3>=0) or (c1<=0 and c2<=0 and c3<=0)

if __name__ == '__main__':
    count = 0
    with open('triangles.txt') as f:
        for l in f:
            x1,y1,x2,y2,x3,y3 = [int(s) for s in l.strip().split(',')]
            if contains_origin(((x1, y1), (x2, y2), (x3, y3))):
                print l
                count += 1
    print count