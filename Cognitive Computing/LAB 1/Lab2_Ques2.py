from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A','D', 'E'],
    'C': ['A','F','G'],
    'D': ['B'],
    'E': ['B','H'],
    'F': ['C'],
    'G' : ['C','I'],
    'H' : ['E'],
    'I' : ['G']
}


# DFS 
def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        print(node, end=' ')
        visited.add(node)

        for neighbor in graph[node]:
            stack.append(neighbor)




# BFS

def bfs(graph, start):
    visited = {start}
    queue = [start]

    while queue:
        node = queue.pop(0)
        print(node, end=' ')

        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                queue.append(n)




if __name__ == "__main__":
   
    print("DFS : ")
    dfs(graph, 'A')
    print("\n")

    print("BFS : ")
    bfs(graph, 'A')
    print()
