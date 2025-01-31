par = int(input())
strokes = int(input())
eagle = par - 2
birdie = par - 1
bogey = par + 1

if par == 3 or par == 4 or par == 5:
    if par == strokes:
        print('Par')
    elif strokes == eagle:
        print('Eagle')
    elif strokes == birdie:
        print('Birdie')
    elif strokes == bogey:
        print('Bogey')
    else:
        print('Error')
else:
    print('Error')