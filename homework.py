from re import S


var1 = input('Type object:')

if var1 == 'Circle' or var1 == 'circle':
    radius = int(input('Type circle radius:'))
    perimeter = 2*3.14*radius
    area = 3.14*(radius**2)
    print(f'Your circles perimeter is:{perimeter}')
    print(f'Your circles area is:{area}')
elif var1 == 'Rectangle' or var1 == 'rectangle':
    x = int(input('Type the long edge:'))
    y = int(input('Type the short edge:'))
    perimeter = 2*(x+y)
    area = x*y
    print(f'Your rectangles perimeter is:{perimeter}')
    print(f'Your rectangles area is:{area}')
else:
    print('sorry not yet fully capable')