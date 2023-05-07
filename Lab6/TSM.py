import itertools

# Given graph with 4 edges
graph = {
    1: {2: 42, 3: 88, 4: 20},
    2: {1: 30, 3: 35, 4: 24},
    3: {1: 55, 2: 35, 4: 50},
    4: {1: 60, 2: 25, 3: 70},
}

# Starting Edge
start_edge = 1


def TSP(graph, start_edge):
    # Generate all permutations of cities
    cities = list(graph.keys())
    cities.remove(start_edge)
    permutations = list(itertools.permutations(cities))

    # Add start_edge to each permutation and calculate the total distance
    min_distance = float("inf")
    optimal_route = None
    for permutation in permutations:
        distance = graph[start_edge][permutation[0]]
        for i in range(len(permutation) - 1):
            distance += graph[permutation[i]][permutation[i + 1]]
        distance += graph[permutation[-1]][start_edge]

        # Update the minimum distance and optimal route
        if distance < min_distance:
            min_distance = distance
            optimal_route = (start_edge,) + permutation + (start_edge,)

    return optimal_route, min_distance


# Find the optimal route and minimum distance
optimal_route, min_distance = TSP(graph, start_edge)

# Print the results
print("Optimal route:", optimal_route)
print("Minimum distance:", min_distance)
