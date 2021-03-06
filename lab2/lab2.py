# Fall 2012 6.034 Lab 2: Search
#
# Your answers for the true and false questions will be in the following form.
# Your answers will look like one of the two below:
#ANSWER1 = True
#ANSWER1 = False

# 1: True or false - Hill Climbing search is guaranteed to find a solution
#    if there is a solution
ANSWER1 = False

# 2: True or false - Best-first search will give an optimal search result
#    (shortest path length).
#    (If you don't know what we mean by best-first search, refer to
#     http://courses.csail.mit.edu/6.034f/ai3/ch4.pdf (page 13 of the pdf).)
ANSWER2 = False

# 3: True or false - Best-first search and hill climbing make use of
#    heuristic values of nodes.
ANSWER3 = True

# 4: True or false - A* uses an extended-nodes set.
ANSWER4 = True

# 5: True or false - Breadth first search is guaranteed to return a path
#    with the shortest number of nodes.
ANSWER5 = True

# 6: True or false - The regular branch and bound uses heuristic values
#    to speed up the search for an optimal path.
ANSWER6 = False

# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph

## Optional Warm-up: BFS and DFS
# If you implement these, the offline tester will test them.
# If you don't, it won't.
# The online tester will not test them.

def bfs(graph, start, goal):
    queue = [[start]]

    while(len(queue) > 0):
        #pop
        cur_path = queue[0]
        queue = queue[1:]

        end_node = cur_path[-1]

        if(end_node == goal):
            return cur_path

        for neigh in graph.get_connected_nodes(end_node):
            if(not neigh in cur_path):
                queue.append(cur_path + [neigh])

    return []


## Once you have completed the breadth-first search,
## this part should be very simple to complete.
def dfs(graph, start, goal):
    queue = [[start]]

    while(len(queue) > 0):
        #pop
        cur_path = queue[0]
        queue = queue[1:]

        end_node = cur_path[-1]

        if(end_node == goal):
            return cur_path

        for neigh in graph.get_connected_nodes(end_node):
            if(not neigh in cur_path):
                queue.insert(0, cur_path + [neigh])

    return []


## Now we're going to add some heuristics into the search.
## Remember that hill-climbing is a modified version of depth-first search.
## Search direction should be towards lower heuristic values to the goal.
def hill_climbing(graph, start, goal):
    queue = [[start]]

    while(len(queue) > 0):
        #pop
        cur_path = queue[0]

        queue = queue[1:]

        end_node = cur_path[-1]

        if(end_node == goal):
            return cur_path

        new_paths = []
        for neigh in graph.get_connected_nodes(end_node):
            if(not neigh in cur_path):
                new_paths.append(cur_path + [neigh])

        new_paths = sorted(new_paths, key=(lambda x: graph.get_heuristic(x[-1], goal)))
        queue = new_paths + queue

    return []

## Now we're going to implement beam search, a variation on BFS
## that caps the amount of memory used to store paths.  Remember,
## we maintain only k candidate paths of length n in our agenda at any time.
## The k top candidates are to be determined using the
## graph get_heuristic function, with lower values being better values.
def beam_search(graph, start, goal, beam_width):
    queue = []
    next_level = [[start]]

    while(len(next_level) > 0):
        queue = sorted(next_level, key=(lambda x: graph.get_heuristic(x[-1], goal)))
        queue = queue[:beam_width] #keep only beam_width nuber of paths
        next_level = []

        while(len(queue) > 0):
            #pop
            cur_path = queue[0]
            queue = queue[1:]

            end_node = cur_path[-1]

            if(end_node == goal):
                return cur_path

            for neigh in graph.get_connected_nodes(end_node):
                if(not neigh in cur_path):
                    next_level.append(cur_path + [neigh])

    return []

## Now we're going to try optimal search.  The previous searches haven't
## used edge distances in the calculation.

## This function takes in a graph and a list of node names, and returns
## the sum of edge lengths along the path -- the total distance in the path.
def path_length(graph, node_names):
    if(len(node_names) < 2):
        return 0

    return graph.get_edge(node_names[0],node_names[1]).length + path_length(graph, node_names[1:])

def branch_and_bound(graph, start, goal):
    queue = [[start]]

    while(len(queue) > 0):
        #pop
        cur_path = queue[0]
        queue = queue[1:]

        end_node = cur_path[-1]

        if(end_node == goal):
            return cur_path

        for neigh in graph.get_connected_nodes(end_node):
            if(not neigh in cur_path):
                queue.append(cur_path + [neigh])

        queue = sorted(queue, key=(lambda x: path_length(graph, x)))

    return []

def a_star(graph, start, goal):
    queue = [[start]]
    extended = []

    while(len(queue) > 0):
        #pop
        cur_path = queue[0]
        queue = queue[1:]

        end_node = cur_path[-1]

        if(end_node == goal):
            return cur_path
        elif(not end_node in extended):
            extended.append(end_node)

            for neigh in graph.get_connected_nodes(end_node):
                if(not neigh in cur_path):
                    queue.append(cur_path + [neigh])

            queue = sorted(queue, key=(lambda x: path_length(graph, x) + graph.get_heuristic(x[-1], goal)))

    return []

## It's useful to determine if a graph has a consistent and admissible
## heuristic.  You've seen graphs with heuristics that are
## admissible, but not consistent.  Have you seen any graphs that are
## consistent, but not admissible?

def is_admissible(graph, goal):
    controls = [(graph.get_heuristic(node, goal) <= path_length(graph, a_star(graph, node, goal))) for node in graph.nodes]
    return reduce((lambda x, y: x and y), controls)

def is_consistent(graph, goal):
    controls = [(edge.length >= abs(graph.get_heuristic(edge.node1, goal) - graph.get_heuristic(edge.node2, goal))) for edge in graph.edges]
    return reduce((lambda x, y: x and y), controls)

HOW_MANY_HOURS_THIS_PSET_TOOK = '1'
WHAT_I_FOUND_INTERESTING = '1'
WHAT_I_FOUND_BORING = '1'
