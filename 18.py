graph = {'A' : ['B', 'D'], 'B' : ['C', 'F'], 'C' : ['E', 'G', 'H'], 'G' : ['E', 'H'], 'E' : ['B', 'F'], 'F' : ['A'], 'D' : ['F'], 'H' : ['A']}
print("Given graph: ")
print(graph)

def dfs(graph, root):
    stack = []
    visited_list = []

    stack.append(root)
    visited_list.append(root)

    while stack:
        vertex = stack.pop()
        print(vertex, end=" ")

        for node in graph[vertex]:
            if node not in visited_list:
                stack.append(node)
                visited_list.append(node)

print("DFS traversal with A being the root is: ")
dfs(graph, 'A')