graph = {}
costs = {}
parents = {}
processed = []


def find_lowest_cost_node(costs):
    lowest_node = None
    lowest_cost = float('inf')
    for key, value in costs.items():
        if value < lowest_cost and key not in processed:
            lowest_node = key
            lowest_cost = value
    return lowest_node


node = find_lowest_cost_node(costs)
while node:
    cost = costs[node]
    for key, value in graph[node].items():
        if cost + value < costs[key]:
            costs[key] = cost + value
            parents[key] = node
        processed.append(node)
    node = find_lowest_cost_node(costs)
