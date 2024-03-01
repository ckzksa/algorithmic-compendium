
#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7
graph = {
    "1": ["2", "3"],
    "2": ["1", "4", "5"],
    "3": ["1", "6", "7"],
    "4": ["2"],
    "5": ["2"],
    "6": ["3"],
    "7": ["3"],
}

def bfs(graph, starting_node):
    if starting_node not in graph:
        return None
    
    visited = []
    queue = []
    
    visited.append(starting_node)
    queue.append(starting_node)
    
    while queue:
        node = queue.pop(0)
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return visited

if __name__ == "__main__":
    print(bfs(graph, "1"))