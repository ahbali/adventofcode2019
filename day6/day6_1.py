from collections import deque

search_queue = deque()

world_map = {}
world_map["COM"] = ["B"]
world_map["B"] = ["C", "G"]
world_map["C"] = ["D"]
world_map["D"] = ["E", "I"]
world_map["E"] = ["F", "J"]
world_map["G"] = ["H"]
world_map["J"] = ["K"]
world_map["K"] = ["L"]
world_map["K"] = ["YOU"]
world_map["I"] = ["SAN"]

# world_map["H"] = []
# world_map["I"] = []
# world_map["L"] = []
# world_map["F"] = []

# a = 1 + 2 * 2 + 3 * 2 + 4 * 2 + 5 * 2 + 6 + 7
# d_d = [(x, 1) for x in world_map["B"]]


# d = world_map["B"]
# f = zip(d, [1 for i in d])
# for i in f:
#     print(i)
def depth_sum(w_map={}):
    queue = deque()
    total_depth = 0
    queue.extend(zip(w_map["COM"], [1 for i in w_map["COM"]]))

    while queue:
        node, depth = queue.popleft()
        # print(node, " depth = ", depth)
        total_depth += depth
        queue.extend([(x, depth + 1) for x in w_map.get(node, [])])

        # queue.extend(
        #     zip(w_map.get(node, []), [depth + 1 for i in w_map.get(node, [])]))
    return total_depth


def search_node(w_map={}, s_node=""):
    # queue = deque()
    # searched_nodes = []
    # queue.extend(w_map.get("COM"))
    # while queue:
    #     node = queue.popleft()
    #     children = w_map.get(node, [])
    #     if children == []:
    #         continue
    #     queue.extend(children)
    path = []
    parent = s_node
    while parent != "COM":
        for node in w_map:
            if parent in w_map.get(node, []):
                parent = node
                path.append(node)
                break
    return path


graph = {}
with open("day6/input.txt") as file:
    for line in file:
        node, child = line.strip().split(")")
        children = graph.get(node, [])
        children.append(child)
        graph[node] = children

# sum_ = depth_sum(graph)
# print("depth = ", sum_)

you_path = search_node(graph, "YOU")
san_path = search_node(graph, "SAN")
# result_set = (set(you_path) & set(san_path)) - (set(you_path) - set(san_path))
result_set = set(you_path).symmetric_difference(set(san_path))
# print(you_path)
# print(san_path)
print(len(result_set))