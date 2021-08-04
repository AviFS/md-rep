arr = [1,2,3,4]
demo1 = ".{*arr} .."
demo2 = "[.{*arr}, ..]"
demo3 = "| .{*arr} | .. |"
demo4 = "echo '.{*arr} ..' | python jelly.py"
demo5 = "python jelly.py .-{*arr} .."

rep = ""
is_rep = True

out = ""

inp = demo1

lst1 = ["", "*arr", " ", ""]
lst2 = ["[", "*arr", ", ", "]"]
lst3 = ["| ", "*arr", " | ", " |"]

lst = lst2

out+=str(lst[0])

for i in range(len(arr)):
    out += str(arr[i])
    if i!=len(arr)-1:
        out += str(lst[2])

out+=str(lst[3])

print(out)
# i=0
# while i < len(inp):
#     if inp[i]=="." and not is_rep:
#         rep += inp[i]
#         is_rep = True
#     elif inp[i]=="." and is_rep:
#         i+=1
    
#     elif 
    

#     i+=1
