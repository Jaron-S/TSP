import heapq


def solve_tsp(G):
    n = len(G)
    visited = set()
    result = [0]
    visited.add(0)

    for i in range(n-1):
        # find the min of the current node's neighbors
        neighbors = []
        for j in range(n):
            heapq.heapify(neighbors)
            if G[i][j] > 0 and j not in visited:
                node = (G[i][j], j)     # (edge weight, node index)
                heapq.heappush(neighbors, node)
        min_node = heapq.heappop(neighbors)

        # move to that node
        result.append(min_node[1])
        visited.add(min_node[1])

    result.append(0)

    return result


# ----------------- TESTS --------------------
if __name__ == '__main__':
    G = [
        [0, 2, 3, 0, 1],
        [2, 0, 15, 2, 20],
        [3, 15, 0, 20, 13],
        [0, 2, 20, 0, 0],
        [1, 20, 13, 0, 0],
    ]
    print(solve_tsp(G))

