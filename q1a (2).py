import math
def calculate(f, x):
    if '+' in f:
        parts = f.split('+')       
        return calculate(parts[0], x)+calculate(parts[1], x)
    if '*' in f:
        parts = f.split('*')  
        return calculate(parts[0], x)*calculate(parts[1], x)    
    if f == 'x':
        return x
    if f.startswith('sin('):       
        return math.sin(calculate(f[4:-1], x))
    elif f.startswith('cos('):     
        return math.cos(calculate(f[4:-1], x))       

