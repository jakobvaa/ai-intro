import Util
import math
from Node import Node
import heapq

# Should make the project by using a min-heap as the open list. Sort on node.for
# But it works this way too.

class AStar():

    #Initialize everything
    def __init__(self, board, goal):

        # Dictionary with cost of the different path choices
        self.COST = {".": 1, "A": 1, "B": 1, "w": 100, "m": 50, "f": 10, "g": 5, "r": 1}

        # Should have made a board class
        # Board is a list of strings
        self.board = board
        self.nodeBoard = []
        self.boardHeight = len(board) - 1
        self.boardWidth = len(board[0]) - 1
        for x in range(self.boardHeight + 1):
            list = []
            for y in range(self.boardWidth + 1):
                list.append(None)
            self.nodeBoard.append(list)

        self.goalPos = self.findLetter(board, "B")

        self.startPosition = self.findLetter(board, "A")
        self.startNode = self.makeNode(self.startPosition, None, 0, "A")

        self.open = []
        self.closed = []
        self.finalNode = None
        self.open.append(self.startNode)

    # Solves the board given to the algorithm
    def solve(self):
        goalFound = False
        while not goalFound:
            goalFound = self.iteration()

    #Does one iteration of the algorithm on the board in the AStar object.
    #Similar to the Agenda loop in A* pseudocode given in assigment.
    def iteration(self):
        if self.open:
            node = self.open.pop(0)
            self.closed.append(node)
        #Should have made a board class
            if node.getString() == "B":
                print("Mission accomplished, yeaas!")
                self.finalNode = node
                return True
            successors = self.generateFriends(node)
            for child in successors:
                node.makeLoveChild(child)
                if child not in self.open and child not in self.closed:
                    self.attachEval(child, node)
                    self.open.append(child)
                elif node.getG() + child.getCost() < child.getG():
                    self.attachEval(child, node)
                    if child in self.closed:
                        self.propagateImprovement(child)
        else:
            print("No solution for problem")
            return True

    #If it is found a better path, for parent node: It checks if this path is a
    #better choice for the children.
    def propagateImprovement(self, node):
        for child in node.getKids():
            if node.getG() + child.getCost() < child.getG():
                child.kidnappedBy(node)
                self.propagateImprovement(child)

    #Sets childs parent variable to parent
    def attachEval(self, child, parent):
        child.kidnappedBy(parent)


    #Hehe, could be done prettier
    #Checks if the slots around the node is nodeworthy (hah) and should be made
    #into a child of the node.
    def generateFriends(self,node):
        pos = node.getPos()
        board = self.board
        friends = []
        if pos[0] + 1 <= self.boardWidth:
            pos1 = [pos[0] + 1, pos[1]]
            nodeAtPos = self.nodeAtPos(pos1,node)
            if nodeAtPos and nodeAtPos not in node.getKids():
                friends.append(nodeAtPos)
        if pos[0] - 1 >= 0:
            pos2 = [pos[0] - 1, pos[1]]
            nodeAtPos = self.nodeAtPos(pos2,node)
            if nodeAtPos and nodeAtPos not in node.getKids():
                friends.append(nodeAtPos)
        if pos[1] + 1 <= self.boardHeight:
            pos3 = [pos[0], pos[1] + 1]
            nodeAtPos = self.nodeAtPos(pos3,node)
            if nodeAtPos and nodeAtPos not in node.getKids():
                friends.append(nodeAtPos)
        if pos[1] - 1 >= 0:
            pos4 = [pos[0], pos[1] - 1]
            nodeAtPos = self.nodeAtPos(pos4,node)
            if nodeAtPos and nodeAtPos not in node.getKids():
                friends.append(nodeAtPos)
        # Adopsjon
        return friends

    # Returns a new node if a node should be made, node at position if not
    def nodeAtPos(self, pos, parent):
        if not (self.board[pos[1]][pos[0]] == "#"):
            string = self.board[pos[1]][pos[0]]
            if not self.nodeBoard[pos[1]][pos[0]]:
                new = self.makeNode(pos, parent, self.COST[string], string)
                self.insertNodeBoard(new, pos[0], pos[1])
                return new
            else:
                return self.nodeBoard[pos[1]][pos[0]]
        return None

    #Creates a board with all nodes. Used this to return node at given position
    def insertNodeBoard(self, node, x, y):
        self.nodeBoard[y][x] = node

    def findLetter(self, board, letter):
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == letter:
                    return [x, y]

    def makeNode(self, pos, parent, cost, stringValue):
        man = self.findManhattan(pos, self.goalPos)
        node = Node(pos, man, parent, cost, stringValue)
        return node

    def findManhattan(self, start, end):
        return abs(start[0] - end[0]) + abs(start[1] - end[1])

    def getNodeBoard(self):
        return self.nodeBoard



for e in range(2):
    for r in range(4):
        board = Util.makeBoard("board-"+ str(e + 1) + "-" + str(r + 1) + ".txt")
        algo = AStar(board, "B")
        algo.solve()

        algo.getNodeBoard()

        #Only runs if there is a solution for problem, prints solution
        if algo.finalNode:
            x = algo.finalNode
            liste = []
            for y in board:
                liste.append(list(y))

            while x.getString() != "A":
                x = x.getParent()
                pos = x.getPos()
                if x.getString() != "A":
                    liste[pos[1]][pos[0]] = "@"

            list2 = []
            for z in liste:
                list2.append("".join(z))

            for x in list2:
                print(x)
            print("\n")
