arr = [1,2,3,4]
demo1 = ".{*arr} .."
demo2 = "[.{*arr}, ..]"
demo3 = "| .{*arr} | .. |"
demo4 = "echo '.{*arr} ..' | python jelly.py"
demo5 = "python jelly.py .-{*arr} .."


dots, is_dots = "", False
# bracks, is_bracks = "", False
parsed = []
i = 0

demo = demo4

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
        if is_dots:
            dots += demo[i]
        else:
            parsed += [demo[i]]
    i+=1

print(parsed)

        # if demo[i]=='{' and not is_bracks:
        #     is_bracks = True
        # if demo[i]=='}' and is_bracks:
        #     is_bracks = False

        
    



rep = ""
is_rep = True

out = ""

inp = demo1

lst1 = ["", ("", "*arr", " "), ""]
lst2 = ["[", ("", "*arr", ", "), "]"]
lst3 = ["| ", ("", "*arr", " | "), " |"]
lst4 = ["echo '", ("", "*arr", " "), "' | python jelly.py"]
lst5 = ["python jelly.py ", ("-", "*arr", " ")]

lst = lst4


lst = parsed
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

print(out)

# out+=str(lst[0])

# for i in range(len(arr)):
#     out += str(arr[i])
#     if i!=len(arr)-1:
#         out += str(lst[2])

# out+=str(lst[3])

# print(out)
# i=0
# while i < len(inp):
#     if inp[i]=="." and not is_rep:
#         rep += inp[i]
#         is_rep = True
#     elif inp[i]=="." and is_rep:
#         i+=1
    
#     elif 
    

#     i+=1
