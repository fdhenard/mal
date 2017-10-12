import reader
import printer


def read(x):
    return reader.read_str(x)


def _eval(x):
    return x


def _print(x):
    # print("x = %s" % x)
    return printer.pr_str(x)


def rep(x):
    # import pdb; pdb.set_trace()
    rres = read(x)
    # print("read res = %s" % rres)
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
