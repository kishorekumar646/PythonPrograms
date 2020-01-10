

open_list = ["[","{","("]
close_list = ["]","}",")"]

def check(myStr):
    stack = []
    for i in myStr:
        print("i : ",i)
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            print("Close_list : ",i)
            pos = close_list.index(i)
            print("pos : ",pos)
            if ((len(stack)) > 0) and (open_list[pos] == stack[len(stack)-1]):
                stack.pop()
            else:
                return False
    return True



string = str(input("Enter the brackets : "))
print(string," is ","Balanced" if check(string) else "Not Balanced")