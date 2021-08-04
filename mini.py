##### NOTES

### It'd be nice for debuggin if parse() kept all
### literal chars together, rather than separate

### Can also add to parse() eventually:
# bracks, is_bracks = "", False
# if demo[i]=='{' and not is_bracks:
#     is_bracks = True
# if demo[i]=='}' and is_bracks:
#     is_bracks = False

# Test cases as is
demo1 = ".{*arr} .."
demo2 = "[.{*arr}, ..]"
demo3 = "| .{*arr} | .. |"
demo4 = "echo '.{*arr} ..' | python jelly\.py"
demo5 = "python jelly\.py .-{*arr} .."

# Test cases preparsed
lst1 = ["", ("", "*arr", " "), ""]
lst2 = ["[", ("", "*arr", ", "), "]"]
lst3 = ["| ", ("", "*arr", " | "), " |"]
lst4 = ["echo '", ("", "*arr", " "), "' | python jelly.py"]
lst5 = ["python jelly.py ", ("-", "*arr", " ")]

def parse(demo):

    parsed = []
    dots, is_dots = "", False

    i = 0
    while i < len(demo):
        if demo[i] in '.': # should be if demo[i] in '.{}'
            if demo[i]=='.' and not is_dots:
                is_dots = True
            elif demo[i]=='.' and is_dots:
                is_dots = False
                beg, end = dots.index('{'), dots.index('}')
                parsed += [(dots[:beg], dots[beg+1:end], dots[end+1:])]
                dots = ""
                i+=1 # skip second dot
        else:
            if demo[i] == '\\':
                i+=1
            if is_dots:
                dots += demo[i]
            else:
                parsed += [demo[i]]
        i+=1

    return parsed


def render(demo, arr):
    out = ""
    lst = parse(demo)
    for elem in lst:

        if isinstance(elem, tuple):
            for i in range(len(arr)):
                out += elem[0]
                # assumes elem[1] == *arr
                assert elem[1] == "*arr"
                out += str(arr[i])
                if i!=len(arr)-1:
                    out += elem[2]

        else:
            out += elem

    return out


# Array to use in test cases
arr = [1,2,3,4]

# Try it out
print(render(demo5, ["2", "3", "5"]))