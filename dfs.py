graph = {'a':['b','d','e','f'],'d':['a'],'b':['a','f','c'],'f':['b','a'],'c':['b'],'e':['a']}
print(graph)

# def dfs(graph, source):
#     Stack = list()
#     visited_list = list()
#     Stack.append(source)
#     visited_list.append(source)

#     while Stack:
#         vertex = Stack.pop()
#         print(vertex, end=" ")

#         for i in graph:
#             if i not in visited_list:
#                 Stack.append(i)
#                 visited_list.append(i)

def dfs(graph, source):
    stack = []
    visited = []
    stack.append(source)
    visited.append(source)

    while stack:
        vertex = stack.pop()
        print(vertex, end=" ")

        for i in graph:
            if i not in visited:
                stack.append(i)
                visited.append(i)

dfs(graph, "a")
