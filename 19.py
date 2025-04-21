from queue import Queue
graph = {'a':['b','d','e','f'],'d':['a'],'b':['a','f','c'],'f':['b','a'],'c':['b'],'e':['a']}

print ("Given Graph is:")
print(graph)

def BFS(graph,source):
    Q = Queue()
    visited_vertices = []

    Q.put(source)
    visited_vertices.append(source)

    while not Q.empty():
        vertex = Q.get()
        print(vertex,end=" ")

        for i in graph[vertex]:
            if i not in visited_vertices:
                Q.put(i)
                visited_vertices.append(i)

print("BFS traversal of graph with source A is: ")
BFS(graph, "a")