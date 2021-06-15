import re 

def parse(s):
    x = re.search("^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IV|XV|V?I{0,3})$", s)
    x = bool(x)
    if x == True:
        return True
    else:
        raise Exception("No es romano")

if __name__ == '__main__':
    parse("CCC")