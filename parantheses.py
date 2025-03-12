open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


def check_parantheses(my_str):
    Stack = []
    for i in open_list:
        if i in open_list:
            Stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if len(Stack) > 0 and open_list[pos] == Stack[len(Stack) - 1]:
                Stack.pop()
            else:
                return "UNBALANCED"
    if len(Stack) == 0:
        return "BALANCED"
    else:
        return "UNBALANCED"
    
string = "{[]{()}}"
print(string, check_parantheses(string))
string = ((()))
print(string, check_parantheses(string))