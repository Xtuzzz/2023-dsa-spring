import time
import re

def f2(a:str,string:str):
    b=[]
    i=0
    while i<len(string)-3:
        if string[i:i+4]==a:
            b.append(i)
            i+=4
        else:
            i+=1
    return b

t1 = time.time()
read = open('pi50.4.bin', 'rb').read()
string = ''.join([hex(x)[2:].zfill(2) for x in read])
# starts = [each.start() for each in re.finditer('2021', string)]
starts = f2('2021',string)
t3 = time.time()
a = {'01': 31, '02': 28, '03': 31, '04': 30,
     '05': 31, '06': 30, '07': 31, '08': 31,
     '09': 30, '10': 31, '11': 30, '12': 31
     }
b = ['2021' + x + str(y + 1).zfill(2) for x in a for y in range(a[x])]
if starts:
    i = 0
    c = [string[x:x + 8] for x in starts]
    for x in b:
        if x in c:
            i += 1
    t2 = time.time()
    print(i)
    print(t2 - t1)
    print(t3 - t1)
else:
    print(0)
