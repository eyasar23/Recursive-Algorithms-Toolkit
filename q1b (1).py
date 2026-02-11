import math
from q1a import calculate

def derivative(f, x):
    if f == 'sin(x)':
        return math.cos(x) 
    if f == 'cos(x)':
        return -math.sin(x)         
    if '+' in f:
        parts = f.split('+')       
        return derivative(parts[0], x)+derivative(parts[1], x)
          
    if '*' in f:                  
        parts = f.split('*',1) 
        return calculate(parts[0], x) * derivative(parts[1], x) + calculate(parts[1], x) * derivative(parts[0], x)
    if f.startswith('sin(') and f.endswith(")"):       
        return derivative(f[4:-1], x)* math.cos(calculate(f[4:-1], x))
    
    if f.startswith('cos(')and f.endswith(")"):   
         return  derivative(f[4:-1], x)*-math.sin(calculate(f[4:-1], x))    
        