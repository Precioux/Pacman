# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
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
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):

    #Defining a stack for DFS traverse
    forDFS = util.Stack()

    #Getting starting point
    startLocation = problem.getStartState()

    # Defining Root Node => (location, path)
    rootNode = (startLocation, [])

    #Pushing root to stack
    forDFS.push(rootNode)

    #Defining a set for visited nodes
    visitedLocations = set()

    while not forDFS.isEmpty():
        # node[0] : location, node[1] : path(NEWS)

        #pop latest node as current node
        node = forDFS.pop()

        #adding current node to visited ones
        visitedLocations.add(node[0])

        #check whether current node is goal or not
        if problem.isGoalState(node[0]):
            return node[1]

        #find successors of current node
        successors = problem.getSuccessors(node[0])

        for item in successors:
            #checking whether successor has been visited or not
            if item[0] in visitedLocations:
                continue
            #pushining unvisited ones as nodes to stack
            forDFS.push((item[0], node[1] + [item[1]]))

    return None


def breadthFirstSearch(problem):
    #Defining a Queue for applying BFS
    forBFS = util.Queue()

    # Getting starting node
    startLocation = problem.getStartState()
    print(f'Statrting point is {startLocation}')

    #Setting Root Node
    rootNode = (startLocation, [])

    #adding root node to queue
    forBFS.push(rootNode)

    #Defining a set for visited nodes
    visitedLocations = set()

    #adding starting point to that set
    visitedLocations.add(startLocation)

    while not forBFS.isEmpty():
        # node[0] : location, node[1] : path (NEWS)

        #Setting latest node as current one
        node = forBFS.pop()
        #print(f'Current node is {node}')

        #checking whether current node is goal
        if problem.isGoalState(node[0]):
            return node[1]

        #getting current node successors
        successors = problem.getSuccessors(node[0])
        #print(f'Successors to current node are {successors}')
        #adding successors to queue if they are not visited
        for item in successors:
            if item[0] in visitedLocations:
                continue
            visitedLocations.add(item[0])
            #print(f'visited locations are {visitedLocations}')
            forBFS.push((item[0], node[1] + [item[1]]))
            #print(f'added to Q => node[0]={item[0]} , node[1]={node[1]} + {item[1]}')

    return None

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
