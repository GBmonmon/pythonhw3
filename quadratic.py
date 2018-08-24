class Quadratic:
    #ax^2 + bx + c
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        a = self.a
        b = self.b
        c = self.c

        if a == 0: a = ''
        elif a == -1: a = '-x^2'
        elif a == 1: a = 'x^2'
        elif a < -1: a = '%sx^2'%a
        elif a > 1: a = '%sx^2'%a

        if a == '' and b == 1: b = 'x'
        elif a == '' and b > 1: b = '%sx'%b
        elif b == 1: b = '+x'
        elif b ==-1: b = '-x'
        elif b == 0: b = ''
        elif b < -1: b = '%sx'%b
        elif b > 1: b = '+%sx'%b

        if c == 0: c = ''
        elif c>0:
            if a == '' and b == '': c = str(c)
            else: c = '+%s'%c
        else:
            c = str(c)

        if a == '' and b == '' and c == '': return '0'
        else: return a+b+c







    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        c = self.c + other.c

        if a == 0: a = ''
        elif a == -1: a = '-x^2'
        elif a == 1: a = 'x^2'
        elif a < -1: a = '%sx^2'%a
        elif a > 1: a = '%sx^2'%a

        if a == '' and b == 1: b = 'x'
        elif a == '' and b > 1: b = '%sx'%b
        elif b == 1: b = '+x'
        elif b ==-1: b = '-x'
        elif b == 0: b = ''
        elif b < -1: b = '%sx'%b
        elif b > 1: b = '+%sx'%b

        if c == 0: c = ''
        elif c>0:
            if a == '' and b == '': c = str(c)
            else: c = '+%s'%c
        else:
            c = str(c)

        if a == '' and b == '' and c == '': return '0'
        else: yield a+b+c


    def __sub__(self, other):
        a = self.a - other.a
        b = self.b - other.b
        c = self.c - other.c

        if a == 0: a = ''
        elif a == -1: a = '-x^2'
        elif a == 1: a = 'x^2'
        elif a < -1: a = '%sx^2'%a
        elif a > 1: a = '%sx^2'%a

        if a == '' and b == 1: b = 'x'
        elif a == '' and b > 1: b = '%sx'%b
        elif b == 1: b = '+x'
        elif b ==-1: b = '-x'
        elif b == 0: b = ''
        elif b < -1: b = '%sx'%b
        elif b > 1: b = '+%sx'%b

        if c == 0: c = ''
        elif c>0:
            if a == '' and b == '': c = str(c)
            else: c = '+%s'%c
        else:
            c = str(c)

        if a == '' and b == '' and c == '': return '0'
        else: yield a+b+c




Q1 = Quadratic(-5,10,7)
print('Q1 > ',Q1)
Q2 = Quadratic(6,-10,-7)
print('Q2 > ',Q2,'\n')

addQ1Q2 = Q1 + Q2
subQ1Q2 = Q1 - Q2
print('Q1 + Q2(Sum) > ',addQ1Q2)
print([ i for i in addQ1Q2])
print('Q1 - Q2(Difference) > ',subQ1Q2)
print([i for i in subQ1Q2],'\n')

print('Q1 == Q1 ',Q1 == Q1)
print('Q1 == Q2',Q1 == Q2)
