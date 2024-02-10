

def bfs(corridors, source, parent, sink):
    visited = [False]*len(corridors)
    queue = [source]
    visited[source] = True
    while queue:
        room_num = queue.pop(0)
        for ind, val in enumerate(corridors[room_num]):
            if not visited[ind] and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = room_num
                if ind == sink:
                    return True
    return False

# This function implements the Ford-Fulkerson algorithm to find the maximum flow
# from the source to the sink, which represents the maximum number of bunnies that can escape.
def ford_fulkerson(corridors, source, sink):
    parent = [-1]*(sink+1)
    bunnies_saved = 0
    while bfs(corridors, source, parent, sink):
        path_flow = float('inf')
        current_node = sink
        while current_node != source:
            path_flow = min(path_flow, corridors[parent[current_node]][current_node])
            current_node = parent[current_node]
        bunnies_saved += path_flow
        path_end = sink
        while path_end != source:
            parent_node = parent[path_end]
            corridors[parent_node][path_end] -= path_flow
            corridors[path_end][parent_node] += path_flow
            path_end = parent[path_end]
    return bunnies_saved

def solution(entrances, exits, path):
    source = len(path)
    sink = source + 1
    corridors = [[0]*(sink+1) for _ in range(sink+1)]
    for i in range(len(path)):
        for j in range(len(path[i])):
            corridors[i][j] = path[i][j]
    for entrance in entrances:
        corridors[source][entrance] = float('inf')
    # Add infinite capacity corridors from each exit to the sink. 
    # This represents the fact that any number of bunnies can leave the system at the exits.
    for exit in exits:
        corridors[exit][sink] = float('inf')
    return ford_fulkerson(corridors, source, sink)


if __name__ == "__main__":
    print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))
    print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))