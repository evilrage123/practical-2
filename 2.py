#perimeters of ractangles
l=int(input('Enter length of rectangal:'))
b=int(input('Enter breth of rectangal:'))
a = 2 * ( l + b )
c = l * b
fh = open('pactical2.txt','w')
fh.write(f'perimeters of ractangle is {a}')
fh.write('\n')
fh.write(f'Area of ractangle is {c}')
fh.close()