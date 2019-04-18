# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    start = problem.getStartState()
    stack = util.Stack()
    stack.push((start, list()))
    visited_nodes = list()
    while not stack.isEmpty():
        # print "a"
        curr_coord, next_coords = stack.pop()
        for xy, comp, _ in problem.getSuccessors(curr_coord):
            if problem.isGoalState(xy):
                return next_coords + [comp]
            #     raise Exception("Illegal action " + str(action))
            # Exception: Illegal action South

            if xy not in visited_nodes:
                stack.push((xy, next_coords + [comp]))
                visited_nodes.append(curr_coord)
    return list()


# BFS = Queue
# Return a list of Directions


def breadthFirstSearch(problem):
    # from game import Directions as dir
    # TODO "Exception: Illegal action South"
    # (35, 1)
    start = problem.getStartState()
    queue = util.Queue()
    # queue = (Current COORD, [Next COORD(S)])
    queue.push((start, list()))
    visited_nodes = list()
    # print queue.list
    while not queue.isEmpty():
        curr_coord, next_coords = queue.pop()  # Tuple and a List
        # next_coords == None ?!?!
        # getSuccessors returns available coords to visit
        for xy, comp, _ in problem.getSuccessors(curr_coord):
            if problem.isGoalState(xy):
                # Does it 1 block early? how to fix?!
                return next_coords + [comp]
            if xy not in visited_nodes:
                # Compass is a direction NORTH, SOUTH, etc.
                visited_nodes.append(xy)
                # queue.push((xy, next_coords.append(comp)))

                # order of concatanation matters
                queue.push((xy, next_coords + [comp]))
                #    queue.push((xy, next_coords.append(comp)))
                # AttributeError: 'NoneType' object has no attribute 'append'
    # return [dir.NORTH, dir.NORTH, dir.WEST]
    return list()


def uniformCostSearch(problem):
    # from game import Directions as dir

    p_queue = util.PriorityQueue()
    visited_nodes = list()
    start = problem.getStartState()
    # PriorityQueue = (Item, Priority)
    p_queue.push((start, list(), 0), 0)

    while not p_queue.isEmpty():
        curr_coord, next_coords, cost = p_queue.pop()

        for xy, comp, price in problem.getSuccessors(curr_coord):
            if problem.isGoalState(xy):
                return next_coords + [comp]
            if xy not in visited_nodes:
                visited_nodes.append(xy)
                p_queue.push(
                    (xy, next_coords + [comp], cost + price), cost + price)

    return list()


def nullHeuristic(state, problem=None):
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    p_queue = util.PriorityQueue()
    visited_nodes = list()
    start = problem.getStartState()
    p_queue.push((start, list(), 0), 0 + heuristic(start, problem))
    while not p_queue.isEmpty():
        curr_coord, next_coords, cost = p_queue.pop()
        for xy, comp, price in problem.getSuccessors(curr_coord):
            if problem.isGoalState(xy):
                return next_coords + [comp]
            if xy not in visited_nodes:
                visited_nodes.append(xy)
                p_queue.push(
                    (xy, next_coords + [comp], cost + price),
                    cost + price + heuristic(xy, problem))

    return list()


# Abbreviations
dfs = depthFirstSearch
bfs = breadthFirstSearch
ucs = uniformCostSearch
astar = aStarSearch
