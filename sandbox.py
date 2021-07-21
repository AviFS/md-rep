from lark import Lark

def pprint(text='["{arr[i]}, "...]', file_name="rep.lark"):
    with open(file_name,'r') as file:
        grammar = file.read()
    parser = Lark(grammar, start='prog')
    print(parser.parse(text).pretty())
