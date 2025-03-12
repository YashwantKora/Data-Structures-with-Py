graph = {'a':['b','d','e','f'],'d':['a'],'b':['a','f','c'],'f':['b','a'],'c':['b'],'e':['a']}
print(graph)

def dfs(graph, source):
    Stack = list()
    visited_list = list()
    Stack.append(source)
    visited_list.append(source)

    while Stack:
        vertex = Stack.pop()
        print(vertex, end=" ")

        for visited in graph:
            if visited not in visited_list:
                Stack.append(visited)
                visited_list.append(visited)
dfs(graph, "a")
