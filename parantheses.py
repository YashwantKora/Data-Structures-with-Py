open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


# def check_parantheses(string):
#     Stack = []
#     for i in string:
#         if i in open_list:
#             Stack.append(i)
#         elif i in close_list:
#             pos = close_list.index(i)
#             if len(Stack) > 0 and open_list[pos] == Stack[len(Stack) - 1]:
#                 Stack.pop()
#             else:
#                 return "UNBALANCED"
#     if len(Stack) == 0:
#         return "BALANCED"
#     else:
#         return "UNBALANCED"

def check_parantheses(string):
    stack = []
    for i in string:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if len(stack) > 0 and open_list[pos] == stack[len(stack) -1]:
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
    
string = "{[]{()}}"
print(string, check_parantheses(string))
string = ((()))
print(string, check_parantheses(string))