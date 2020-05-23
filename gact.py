#!/usr/bin/python

infile = input('which file do you wanna open? ')

gen = open(infile, 'r')

c = 0;
g = 0;
t = 0;
a = 0;

gen.readline()

for line in gen:

    line = line.lower()

    for char in line:
        
        if char == 'g':

            g+=1

        if char == 'a':

            a+=1

        if char == 'c':

            c+=1

        if char == 't':

            t+=1

print('your file has {0} guanines'.format(g))
print('your file has {0} adenines'.format(a))
print('your file has {0} cytosines'.format(c))
print('your file has {0} thymines'.format(t))

