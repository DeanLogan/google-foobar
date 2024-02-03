
# times can be used as a graph times[i] is the node and times[i][j] is the weight of the edge between node times[i] to node times[j]

from itertools import permutations

def solution(times, time_limit):
    # Apply Floyd-Warshall algorithm
    shortest_paths = floyd_warshall(times)

    num_bunnies = len(times) - 2
    all_bunnies = range(num_bunnies)

    for i in range(0, len(shortest_paths)):
        # if there is a negative path then all bunnies can be saved 
        if shortest_paths[i][i] < 0:
            return list(all_bunnies)
        
    # Try all permutations of bunnies
    for num_to_save in range(num_bunnies, -1, -1):
        for bunnies_to_save in permutations(all_bunnies, num_to_save):
            # Calculate the total time to save these bunnies
            total_time = shortest_paths[0][bunnies_to_save[0] + 1] + shortest_paths[bunnies_to_save[-1] + 1][-1]
            total_time += sum(shortest_paths[bunnies_to_save[i-1] + 1][bunnies_to_save[i] + 1] for i in range(1, num_to_save))
            if total_time <= time_limit:
                return sorted(list(bunnies_to_save))  # Return the indices of the bunnies to save

    return []  # No bunnies can be saved


def floyd_warshall(graph):
    num_vertices = len(graph)

    distance_matrix = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])

    return distance_matrix


if __name__ == "__main__":
    print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
    print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))