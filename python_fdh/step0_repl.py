

def read(x):
    return x

def _eval(x):
    return x

def _print(x):
    # print("x = %s" % x)
    return x

def rep(x):
    rres = read(x)
    eres = _eval(rres)
    pres = _print(eres)
    return pres

if __name__ == "__main__":
    try:
        while True:
            rep_res = rep(input('user> '))
            print(rep_res)
    except EOFError:
        print("\ngood talking to you")
        # pass  # just end it
