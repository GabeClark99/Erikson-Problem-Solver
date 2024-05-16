class Node: 
    def __init__(self, solution, equation, potentialOperands):
        self.children = []
        self.solution = solution
        self.equation = equation
        self.potentialOperands = potentialOperands
        return
    
    def Insert(self, newNode):
        self.children.append(newNode)
        return

    def Reproduce(self):
        for i in range(len(self.potentialOperands)):
            curOperand = self.potentialOperands[i]
            remainingPotentialOperands = self.potentialOperands[:i] + self.potentialOperands[i+1:]

            #---add---
            #HACK
            if self.solution is not None: 
                newSolution = self.solution + curOperand
            else:
                newSolution = curOperand
            
            #HACK
            if self.equation is not None: 
                newEquation = "(" + str(self.equation) + ") + " + str(curOperand)
            else:
                newEquation = str(curOperand)
            
            newNode = Node(newSolution, newEquation, remainingPotentialOperands)
            newNode.Reproduce()
            self.Insert(newNode)
            
            #---mul---
            if self.solution is not None:
                newSolution = self.solution * curOperand
            else:
                newSolution = curOperand

            if self.equation is not None: 
                newEquation = "(" + str(self.equation) + ") * " + str(curOperand)
            else:
                newEquation = str(curOperand)
            
            newNode = Node(newSolution, newEquation, remainingPotentialOperands)
            newNode.Reproduce()
            self.Insert(newNode)
            
            #---sub1---
            #TODO
            
            #---sub2---
            #TODO
            
            #---div1---
            #TODO
            
            #---div2---
            #TODO
    
    def PrintTree(self, padding):
        i = 0
        for child in self.children:
            print(padding + "child" + str(i) + ":")
            print(padding + "\tsolution: " + str(child.solution))
            print(padding + "\tequation: " + child.equation)
            print(padding + "\tpotentialOperands: " + str(child.potentialOperands))
            child.PrintTree(padding + "\t")#
            i += 1
            
def FindSolution(n:Node, solution):
    if len(n.children) < 1:
        if n.solution == solution:
            return n.equation
        else:
            return ""
    else:
        for child in n.children:
            curEquation = FindSolution(child, solution)
            if curEquation != "":
                return curEquation
        return ""

desired = 42
operands = [1,3,4,6]

root = Node(None, None, operands)
root.Reproduce()
equation = FindSolution(root, desired)
print("equation: " + equation)