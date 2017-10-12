import re

from pyfdh_types import Symbol


class Reader:

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def next(self):
        curr_token = self.peek()
        if curr_token:
            self.position += 1
        return curr_token

    def peek(self):
        if self.position >= len(self.tokens):
            return None
        return self.tokens[self.position]


def read_str(_in):
    reader = Reader(tokenizer(_in))
    return read_form(reader)


TOKEN_RE = re.compile("[\s,]*(~@|[\[\]{}()'`~^@]|\"(?:\\.|[^\\\"])*\"|;.*|[^\s\[\]{}('\"`,;)]*)")


def tokenizer(_in):
    return TOKEN_RE.findall(_in)


def read_form(reader):
    token = reader.peek()
    # print("token = %s" % token)
    if not token:
        return None
    if token[0] == '(':
        list_res = read_list(reader)
        # print("list = %s" % list_res)
        return list_res
    elif token[0] == ')':
        return None
    atom_res = read_atom(reader)
    # print("atom = %s" % atom_res)
    return atom_res
    # returns some kind of mal type


def read_list(reader):
    result = []
    while True:
        reader.next()
        form_res = read_form(reader)
        if not form_res:
            break
        result.append(form_res)
    return result


def read_atom(reader):
    token = reader.peek()

    def represents_int(val):
        try:
            int(val)
            return True
        except ValueError:
            return False

    if represents_int(token):
        return int(token)
    return Symbol(token)
