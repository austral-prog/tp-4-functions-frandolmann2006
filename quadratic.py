# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    r1= (-b + (b**2-4*a*c)**1/2)/2*a
    r2=(-b - (b**2-4*a*c)**1/2)/2*a
    if r1==r2:
        return f"({r1})"
    elif r1!=r2:
        return f"({r1,r2})"
    else:
        return "( )"


def value_y(a, b, c, x):
    valor_y= a*x**2+b*x+c
    return valor_y


def to_string(a, b, c):
    if a==0 and b==0 and c==0:
        return f"f(x)= 0"
    elif a==0 and b==0:
        return f"f(x)= {c}"
    elif a==0:
        return f"f(x)= {b}*x+{c}"
    elif b==0:
        return f"f(x)= {a}*x**2+{c}"
    elif c==0:
        return f"f(x)= {a}*x**2+{b}*x"
    elif b==0 and c==0:
        return f"f(x)= {a}*x**2"
    elif a==0 and c==0:
        return f"f(x)= {b}*x"
    else:
        return f"f(x)= {a}*x**2+{b}*x+{c}"


def derivation(a, b, c):
    if a==0 and b==0:
        return f"f'(x)= 0"
    elif a==0:
        return f"f'(x)= {b}"
    elif b==0:
        return f"f'(x)= {2*a}*x"
    else:
        return f"f'(x)= {2*a}*x+{b}"
