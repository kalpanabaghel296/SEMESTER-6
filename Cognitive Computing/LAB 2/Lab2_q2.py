import heapq

def best_first_search(graph, heuristic, start, goal):
    
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))

    parent = {start: None}

    visited = set()

    while open_list:
        h, current = heapq.heappop(open_list)

        print(f"Node Expanded: {current}")

        if current == goal:
            # Reconstruct path
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        visited.add(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                parent[neighbor] = current
                heapq.heappush(
                    open_list,
                    (heuristic[neighbor], neighbor)
                )

    return None
