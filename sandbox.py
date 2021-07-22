A = [1,2,3,4]


class StringWrapper:
    def __init__(self, s):
        self._s = s

    def __repr__(self):
        return self._s

    def __str__(self):
        return self._s


from lark import Lark
import lark

def pprint(text, file_name="arrs.lark"):
    with open(file_name,'r') as file:
        grammar = file.read()
    parser = Lark(grammar, start='prog')
    return parser.parse(text)

def a():
    print(pprint('[.{A[i]}, ...]'))

def pretty(text):
    print(pprint(text).pretty())



# ---------------------------

def parseRepX(tree):
    res = ""
    start_slice, end_slice, step_slice = 0, len(A), 1
    dots = list(tree.find_data('dots'))[0].children
    
    for token in dots:
        if token.data == 'start_slice':
            start_slice = int(token.children[0].value)
        if token.data == 'end_slice':
            end_slice = int(token.children[0].value)
        if token.data == 'step_slice':
            step_slice = int(token.children[0].value)

    #Tree('repx', [Tree('curlies', [Token('CHAR', 'A[i]')]), Tree('dots', [Tree('start_slice', [Token('DIGIT', '0')])])])
    """
    Tree('repx',
        [
            Tree('curlies', 
                [
                    Token('CHAR', 'A[i]')
                ]), 
            Tree('dots', [])
        ])
    ]
    """
    #  for res**y** it should be `for **j** in ...`
    for i in range(start_slice, end_slice, step_slice):
        for subtree in tree.children:
            if subtree.data == 'curlies':
                for token in subtree.children:
                    res += eval("f'{"+ token.value +"}'") 

            if subtree.data == 'static_beg':
                # UNCOMMENT TO INCLUDE. FOR NOW I DON'T WANT A STATIC BEGINNING
                # if i != start_slice: # skip the first iteration  
                for token in subtree.children:
                        res += token.value
            if subtree.data == 'static_mid':
                for token in subtree.children:
                        res += token.value
            if subtree.data == 'static_end':
                if i != end_slice-step_slice:
                    for token in subtree.children:
                            res += token.value
            if subtree.data == 'dots':
                continue
                # should remove from parse tree
    return res

def parseHeadX(tree):
    res = ""
    for token in tree.children:
        res += token.value
    return res

def parseFootX(tree):
    res = ""
    for token in tree.children:
        res += token.value
    return res

def parseLine(line = '[.{A[i]}, ...]'):
    res = ""
    parsed = pprint(line)
    for tree in parsed.children:
        if tree.data == 'headx':
            res += parseHeadX(tree)

        if tree.data == 'repx':
            res += parseRepX(tree)
            
                    
        if tree.data == 'footx':
            res += parseFootX(tree)
            
    return res

"""
%load sandbox.py
%clear
parseLine()

"""

f = parseLine

"""
f('[.{A[i]}, .::2.]')
'[1, 3, ]'

f('[.{A[i]}, .:2:.]')
'[1, 2, ]'

f('[.{A[i]}, .2::.]')
'[3, 4]'
"""
if __name__ == '__main__':
    print(f("[.{A[i]}, ...]"))
    print(f("| .{A[i]} | ... |"))
    print(f("|.{A[i]}|...|"))
    print(f("|.{A[i]}|...|"))
    print(pprint(".{A[i]}..."))

