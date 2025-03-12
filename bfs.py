from queue import Queue
graph = {'a':['b','d','e','f'],'d':['a'],'b':['a','f','c'],'f':['b','a'],'c':['b'],'e':['a']}
print ("Given Graph is:")
print(graph)

def BFS(input_graph,source):
    Q=Queue()
    visited_vertices = list()
    Q.put(source)
    visited_vertices.append(source)
    while not Q.empty():
        vertex = Q.get()
        print(vertex,end=" ")
        for u in input_graph[vertex]:
            if u not in visited_vertices:
                Q.put(u)
                visited_vertices.append(u)

print("BFS traversal of graph with source A is: ")
BFS(graph, "a")