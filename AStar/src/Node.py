

class Node:

    def __init__(self, pos, toGoal, parent, cost, stringValue):
        #As the error only happens once, faster to use try except than if/else
        try:
            self.g = parent.getG() + cost
        except:
            self.g = 0
        #An estimation (heuristic) from this node to goal, using manhattan distance
        self.h = toGoal
        #Estimated cost of getting to goal through this node
        self.f = self.g + self.h

        self.cost = cost

        #1 means the node is open, 0 is closed
        self.status = True

        #Parent is the parent of this node with the lowest cost path
        self.parent = None
        self.kids = []
        self.pos = pos

        #Not needed but nice to have. String value in board
        self.value = stringValue


    def getParent(self):
        return self.parent
    def getCost(self):
        return self.cost

    def getG(self):
        return self.g

    def setStatus(self):
        self.status = False

    def makeLoveChild(self, node):
        self.kids.append(node)

    def getString(self):
        return self.value

    def getPos(self):
        return self.pos

    def getKids(self):
        return self.kids

    def updatef(self):
        self.f = self.h + self.g

    #Gets called if the newly found parent is a better parent choice for the path.
    def kidnappedBy(self, parent):
        self.parent = parent
        self.g = parent.getG() + self.cost
        self.updatef()

    def getF(self):
        return self.f
