####### UNWEIGHTED #######

graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C']
}


####### WEIGHTED #######

weighted_graph = {
    'A': [('B', 1), ('C', 2)],
    'B': [('C', 3), ('D', 4)],
    'C': [('D', 2)],
    'D': [('C', 2)]
}        


####### FIND PATH #######

def find_path(graph, start, end, path=None):
    if not path:
        path = []
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


####### FIND ALL PATHS (DFS) #######

def find_all_paths(graph, start, end, path=None):
    if not path:
        path = []
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
    