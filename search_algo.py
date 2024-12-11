
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#                        BREADTH FIRST SEARCH #
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


graph = {
    'S': ['A','B','D'],
    'A': ['C'],
    'B': ['D'],
    'D': ['G'],
    'C': ['D','G'],
    'G': [],
}

def bfs(graph, start, goal):
    visited = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adgacent_node = graph.get(node, [])
            for newnode in adgacent_node:
                newpath = path.copy()
                newpath.append(newnode)
                queue.append(newpath)








# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#                          DEPTH FIRST SEARCH #
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def dfs(graph, start, goal):
    visited = []
    stack = [[start]]
    while stack:
        path = stack.pop(-1)
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            for newnode in graph.get(node, []):
                newpath = path.copy()
                newpath.append(newnode)
                stack.append(newpath)







# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#                        depth limited SEARCH #
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


def dls(graph, start, goal, limited=100):
    visited = []
    stack = [[start]]
    while stack:
        path = stack.pop(-1)
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        if len(path) > limited:
            break
        if node == goal:
            return path
        else:
            adgacent_node = graph.get(node, [])
            for new_node in adgacent_node:
                new_path = path.copy()
                new_path.append(new_node)
                stack.append(new_path)
    return None








# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#                        Iterative deepening search #
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


def ids(graph, start, goal):
    def dls(graph, start, goal, limit):
        limited = 0
        visited = []
        stack = [[start]]
        while stack:
                path = stack.pop(-1)
                node = path[-1]
                if node in visited:
                    continue
                visited.append(node)
                if node == goal:
                    return path
                if limit < len(path):
                    continue
                else:
                    adgacent_node = graph.get(node, [])
                    for new_node in adgacent_node:
                        new_path = path.copy()
                        new_path.append(new_node)
                        stack.append(new_path)
    depth = 0
    while True:
        result = dls(graph, start, goal, depth)
        if result != None:
            return result
        depth += 1









# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#                        uniform cost SEARCH #
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

graph = {
    'S': [('A',2),('B',3),('D',5)],
    'A': [('C',4)],
    'B': [('D',4)],
    'D': [('G',5)],
    'C': [('D',1),('G',2)],
    'G': [],
}

def cost_path_uniform(path):
    total_cost = 0
    for (node, cost) in path:
        total_cost += cost
        path = node
    return total_cost, path       

def ucs(graph, start, goal):
    visited = []
    queue = [[(start,0)]]
    while queue:
        queue.sort(key = cost_path_uniform)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adgacent_node = graph.get(node, [])
            for new_node in adgacent_node:
                new_path = path.copy()
                new_path.append(new_node)
                queue.append(new_path)
            
  








# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#                           Greedy Best first search #
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# heuristic function => (h(n),n)
# give a number to any node 
graph = {
    'S': [(2,'A'),(3,'B'),(5,'D')],
    'A': [(4,'C')],
    'B': [(5,'D')],
    'D': [(0,'G')],
    'C': [(5,'D'),(0,'G')],
    'G': [],
}

def gbfs(graph, start, goal, heuristic_fun = None):
    visited = []
    queue = [[(0, start)]]
    while queue:
        queue.sort()
        path = queue.pop(0)
        node = path[-1][-1]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adgacent_node = graph.get(node)
            for new_node in adgacent_node:
                new_path = path.copy()
                new_path.append(new_node)
                queue.append(new_path)








# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#                                 A* search #
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


graph = {
    'S': [('A',1),('B',4)],
    'A': [('B',2),('C',5),('G',12)],
    'B': [('C',2)],
    'C': [('G',3)],
    'G': [],
}

nodes = {
    'S':7,
    'A':6,
    'B':4,
    'C':2,
    'G':0,
}

def cost_path(path):
    total_cost = 0
    for (node, cost) in path:
        total_cost += cost
        last_node = node
# f(n) = g(n) + h(n)
    f_fun = total_cost + nodes[last_node]
    return f_fun, last_node

def a_star_search(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key = cost_path)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adgacent_node = graph.get(node,[])
            for new_node in adgacent_node:
                new_path = path.copy()
                new_path.append(new_node)
                queue.append(new_path)

  









# APlus
