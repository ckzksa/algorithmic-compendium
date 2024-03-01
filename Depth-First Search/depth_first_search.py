
#      1
#    /   \
#   2     5
#  / \   / \
# 3   4 6   7
graph = {
    "1": ["2", "5"],
    "2": ["1", "3", "4"],
    "3": ["2"],
    "4": ["2"],
    "5": ["1", "6", "7"],
    "6": ["5"],
    "7": ["5"],
}

def dfs(graph, starting_node, visited=None):
    if visited is None:
        visited = []
    
    visited.append(starting_node)
    result = [starting_node]
    
    for neighbor in graph[starting_node]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    return result

if __name__ == "__main__":
    print(dfs(graph, "1"))