
myfile = open('myfile.txt', 'w')
myfile.write('hello text file\n')

myfile.write('goodbye text file\n')

myfile.close()

myfile = open('myfile.txt')
F = myfile.readline()
F += myfile.readline()
F += myfile.readline()

F = open('myfile.txt').read()

# for line in open('myfile'):
#     print

myfile2 = open('data.bin', 'w')
myfile2.write('spam')
myfile2.close()

data = open('data.bin', 'rb').read()

F = bin(data[0])

X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a': 1, 'b': 2}
L =[1,2,3]

F = open('datafile.txt', 'w')
F.write(S + '\n')
F.write('%s,%s,%s\n' % (X, Y, Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()

F = open('datafile.txt')
line = F.readline()
line.rstrip()

line = F.readline()
line

parts = line.split(',')
parts
int(parts[1])
numbers = [int(P) for P in parts]
numbers

line = F.readline()
line

parts = line.split('$')
parts

eval(parts[0])

objects = [eval(P) for P in parts]
objects

D = {'a':1, 'b': 2}
F = open('datafile.pk1', 'wb')
import pickle
pickle.dump(D, F)
F.close()

F = open('datafile.pk1', 'rb')
E = pickle.load(F)
E

open('datafile.pk1', 'rb').read()

F = open('data1.bin', 'wb')
import struct
data = struct.pack(b'>i4sh', 7, b'spam', 8)
data
F.write(data)
F.close()

values = struct.unpack('>i4sh', data)
values



print(F)

# myfile.write()