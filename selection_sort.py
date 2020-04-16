from collections import deque

search_queue = deque()

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

mango_sellers = ["jonny", "anuj"]

graph2 = {}
graph2["wake_up"] = ["exercise", "brush_teeth", "pack_luch"]
graph2["exercise"] = ["shower"]
graph2["brush_teeth"] = ["eat_breakfast"]
graph2["shower"] = ["get_cressed"]

dij_graph = {}
dij_graph["book"] = [("rare_lp", 5), ("poster", 0)]
dij_graph["rare_lp"] = [("bass_guitar", 15), ("drum_set", 20)]
dij_graph["poster"] = [("bass_guitar", 30), ("drum_set", 35)]
dij_graph["bass_guitar"] = [("piano", 20)]
dij_graph["drum_set"] = [("piano", 10)]
dij_graph["piano"] = []

graph_dijk_book = {}
graph_dijk_book["start"] = {"a": 6, "b": 2}
graph_dijk_book["a"] = {"fin": 1}
graph_dijk_book["b"] = {"a": 3, "fin": 5}
graph_dijk_book["fin"] = {}

graph_dijk_book_tuple = {}
graph_dijk_book_tuple["start"] = [("a", 6), ("b", 2)]
graph_dijk_book_tuple["a"] = [("fin", 1)]
graph_dijk_book_tuple["b"] = [("a", 3), ("fin", 5)]
graph_dijk_book_tuple["fin"] = []

# *** bellman-ford ***
# algorithm for graph with negative edges


def findlowest_cost(nodes_list):
    if not nodes_list:
        return (None, -1)
    lowest_cost = nodes_list[0][1]
    lowest_node = nodes_list[0][0]
    for (node, cost) in nodes_list:
        if cost < lowest_cost:
            lowest_cost = cost
            lowest_node = node
    return (lowest_node, lowest_cost)


def dijkstra_search(graph={}):
    infinity = float("inf")
    processed = []
    parents = {}
    costs = {}

    for node in graph:
        costs[node] = infinity
        parents[node] = None

    root = find_graph_root(graph)

    for (node, cost) in graph[root]:
        parents[node] = root
        costs[node] = cost

    current_node = findlowest_cost_node(costs, processed)
    while current_node is not None:
        children = graph[current_node]
        for (child_node, cost) in children:
            new_cost = costs[current_node] + cost
            if new_cost < costs[child_node]:
                costs[child_node] = new_cost
                parents[child_node] = current_node

        processed.append(current_node)
        current_node = findlowest_cost_node(costs, processed)

    return (costs, parents)


def find_graph_root_tuple(graph={}):
    for node in graph.keys():
        exist = False
        for comp_node in graph:
            for (name, cost) in graph[comp_node]:
                if node == name:
                    exist = True
        if not exist:
            return node
        else:
            return None


def find_graph_root(graph={}):
    for node in graph.keys():
        exist = False
        if node not in graph.values():
            return node
    return None


def dijkstra_book(graph={}):
    infinity = float("inf")
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = infinity

    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None

    processed = []

    node = findlowest_cost_node(costs, processed)

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = findlowest_cost_node(costs, processed)
    return (costs, parents)


def findlowest_cost_node(costs={}, processed=[]):
    lowest = None
    low_cost = float("inf")
    for node in costs:
        if node not in processed:
            if costs[node] < low_cost:
                lowest = node
                low_cost = costs[node]
    return lowest


def path_from_dict(parents={}, exit_node=""):
    path = exit_node
    parent = parents[exit_node]
    while parent is not None:
        path = parent + " -> " + path
        parent = parents[parent]
    return path


(costs, parents) = dijkstra_search(dij_graph)
# print(costs)
# print(parents)
print(path_from_dict(parents, "piano"))

(costs, parents) = dijkstra_search(graph_dijk_book_tuple)
# print(costs)
# print(parents)
print(path_from_dict(parents, "fin"))

# for node in dij_graph:
#     print(findlowest_cost(dij_graph[node]))

# print(graph_dijk_book)
# (costs, parents) = dijkstra_book(graph_dijk_book)
# print(costs)
# print(parents)
# dijkstra_search(dij_graph)
# def person_is_seller(name):
#     return name in mango_sellers

# def breath_first_search():
#     search_queue = deque()
#     search_queue += graph["you"]
#     while search_queue:
#         person = search_queue.popleft()
#         if person_is_seller(person):
#             print(person, " is a mango seller!")
#             return True
#         else:
#             search_queue += graph[person]
#     return False

# def search_breadth_first(name=""):
#     search_queue = deque()
#     search_queue += graph[name]
#     searched = []
#     while search_queue:
#         person = search_queue.popleft()
#         if not person in searched:
#             if person_is_seller(person):
#                 print(person, " is a mango seller!")
#                 return True
#             else:
#                 search_queue += graph[person]
#                 searched.append(person)
#     return False

# def breadth_search(name):
#     queue = deque()
#     seen = []
#     queue += graph[name]
#     while queue:
#         node = queue.popleft()
#         if node in seen:
#             continue
#         if person_is_seller(node):
#             print(node, " is mango seller!")
#             return True
#         else:
#             seen.append(node)
#             queue += graph[node]
#     return False

# breadth_search("you")

# breath_first_search()

# search_breadth_first("you")

# def find_smallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index

# def selection_sort(arr):
#     new_array = []
#     for i in range(len(arr)):
#         smallest = find_smallest(arr)
#         new_array.append(arr.pop(smallest))
#     return new_array

# def recursive_sum(myarray):
#     if len(myarray) == 0:
#         return 0
#     if len(myarray) == 1:
#         return myarray[0]
#     else:
#         return myarray[0] + recursive_sum(myarray[1:])

# def recursive_max(my_array):
#     if len(my_array) == 1:
#         return my_array[0]
#     temp_max = recursive_max(my_array[1:])
#     return temp_max if my_array[0] < temp_max else my_array[0]

# def euclidian_division(a, b, step=0):
#     if a <= b:
#         return euclidian_division(b, a)
#     elif b == 0:
#         # print("step = ", step)
#         return (a, step)
#     return euclidian_division(b, a % b, step + 1)

# def recursive_binary_search(element, array=[]):
#     if len(array) == 1 and element == array[0]:
#         return True
#     if len(array) == 1 and element != array[0]:
#         return False

#     middle_index = len(array) // 2
#     middle_element = array[middle_index]
#     if element == middle_element:
#         return True
#     return recursive_binary_search(
#         element, array[middle_index:]
#     ) if element > middle_element else recursive_binary_search(
#         element, array[:middle_index])

# def quick_sort(array):
#     if len(array) < 2:
#         return array
#     pivot = array[0]
#     left = [i for i in array[1:] if i < pivot]
#     right = [i for i in array[1:] if i > pivot]
#     return quick_sort(left) + [pivot] + quick_sort(right)

# # print(recursive_max([1, 2, 3, 4, 5, 6, 7]))
# print(quick_sort([3, 5, 1, 0, 14, 4]))