from game import Directions
import random, util
from util import manhattanDistance

from game import Agent

class NewAgent(Agent):
    def __init__(self):
        super().__init__()
        self.lastMove = 'Stop'
        self.oppositeMove = {
            'East': 'West',
            'West': 'East',
            'North': 'South',
            'South': 'North',
            'Stop': 'Stop'
        }
        self.plan = ['Stop']
        self.planScore = 0

    def getAction(self, gameState):
        """
        getAction chooses among the best options according to the evaluation function.
        Code provided by environment requires us to use this function.

        getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        #print(self.planScore)
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        #print(legalMoves)
        #print(scores)
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best
        #print(legalMoves[chosenIndex] != self.plan[0])
        if(legalMoves[chosenIndex] != self.plan[0]):
            self.plan = ['Stop']
            self.planScore = 0
        else :
            self.plan.pop()
        self.lastMove = legalMoves[chosenIndex]
        return self.lastMove

    def evaluationFunction(self, currentGameState, action):
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        #newPos = successorGameState.getPacmanPosition()
        #newFood = successorGameState.getFood()
        #print(newFood)
        #newGhostStates = successorGameState.getGhostStates()
        #newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        #print(successorGameState.getScore())
        #A*
        #f(n) = g(n) + h(n) : total cost = cost of successor + cost to goal by heuristic
        #best score of successor -> lowest cost, lowest score -> highest cost
        #thus in our case f(n) is the highest score possible, h(n) is greatest amount of points possible per state.
        #h(n) = remaining pellets*10, heuristic is the highest amount pellets possible to collect
        #gets best action (highest score)
        
        
        #initial total with initial state score
        #total = successorGameState.getScore() + successorGameState.getNumFood()*10
        actions = []
        total = 0
        count = 0
        curplan = []
        curplan.append(action)
        #check if goal node has been reached
        goalReached = False
        newGS = successorGameState
        oldpos = currentGameState.getPacmanPosition()
        pos = newGS.getPacmanPosition()
        ghostState = newGS.getGhostStates()
        fud = newGS.getFood()
        #for x in range(fud.width):
        #    for y in range(fud.height):
        #        if fud[x][y] :
        #            nd = abs(pos[0] - x)
        #            nd = nd + abs(pos[1] - y)
        #            od = abs(oldpos[0] - x)
        #            od = od + abs(oldpos[1] - y) 
        #            if(nd < od):
        #                total += 1
        #                break
        for ghost in ghostState:
            gp = ghost.getPosition()
            d = abs(pos[0] - gp[0])
            d = d + abs(pos[1] - gp[1])
            if(d <= 1 and ghost.scaredTimer < 1): 
                total -= 1000
                goalReached = True
        if oldpos == pos:
            total -= 10
            goalReached = True
        if fud[pos[0]][pos[1]]:
            total += 500
        if action == self.oppositeMove[self.lastMove] :
            total -= 50
        if newGS.isWin():
                    return 1000000
        chosenAction = 'Stop'
        #print("search for goal state: pellets = 0")
        #If goal node has not been reached, find next node. Else return score
        while (goalReached == False and count < 20):
                       
            legalMoves = successorGameState.getLegalActions()

            # Choose one of the best actions
            scores = []
            for action in legalMoves:
                newGS = successorGameState.generatePacmanSuccessor(action)
                score = newGS.getScore() - (newGS.getNumFood() - currentGameState.getNumFood())
                if(newGS.getPacmanPosition() == successorGameState.getPacmanPosition() 
                or action == self.oppositeMove[chosenAction] 
                or newGS.getPacmanPosition() == oldpos):
                    score -= 50
                #print(score)
                if(newGS.isWin()):
                    return 100000/(count+1)
                scores.append(score) 
                actions.append(action)
            if not scores: break
            bestScore = max(scores)
            bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
            chosenIndex = random.choice(bestIndices)
            chosenAction = legalMoves[chosenIndex]
            curplan.append(chosenAction)
            #actions.remove(legalMoves[chosenIndex])
            total+=scores.pop(chosenIndex)
            if(total > self.planScore):
                #print(self.planScore)
                #print("Replaced by")
                #print(total)
                self.plan = curplan
                self.planScore = total
            successorGameState=successorGameState.generatePacmanSuccessor(legalMoves[chosenIndex])
            
            
            if successorGameState.getNumFood() == 0:
                goalReached = True
            count+= 1
            
        #print("goal state reached.")
        #return total score
        if(len(self.plan) > 0 and action == self.plan[0] and not goalReached):
            total = self.planScore
        return total/(count+1)
        #return successorGameState.getScore()
        
class RandomReflexAgent(Agent):
    def getAction(self, gameState):
        """
        getAction chooses among the best options according to the evaluation function.
        Code provided by environment requires us to use this function.

        getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        #print(self.planScore)
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        #print(legalMoves)
        #print(scores)
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best
        #print(legalMoves[chosenIndex] != self.plan[0])
        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        #newPos = successorGameState.getPacmanPosition()
        #newFood = successorGameState.getFood()
        #print(newFood)
        #newGhostStates = successorGameState.getGhostStates()
        #newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        #print(successorGameState.getScore())
        #A*
        #f(n) = g(n) + h(n) : total cost = cost of successor + cost to goal by heuristic
        #best score of successor -> lowest cost, lowest score -> highest cost
        #thus in our case f(n) is the highest score possible, h(n) is greatest amount of points possible per state.
        #h(n) = remaining pellets*10, heuristic is the highest amount pellets possible to collect
        #gets best action (highest score)
        
        
        #initial total with initial state score
        #total = successorGameState.getScore() + successorGameState.getNumFood()*10
        actions = []
        total = 0
        count = 0
        #check if goal node has been reached
        goalReached = False
        newGS = successorGameState
        fud = currentGameState.getFood()
        oldpos = currentGameState.getPacmanPosition()
        pos = newGS.getPacmanPosition()
        ghostState = newGS.getGhostStates()
        
        #for x in range(fud.width):
        #    for y in range(fud.height):
        #        if fud[x][y] :
        #            nd = abs(pos[0] - x)
        #            nd = nd + abs(pos[1] - y)
        #            od = abs(oldpos[0] - x)
        #            od = od + abs(oldpos[1] - y) 
        #            if(nd < od):
        #                total += 1
        #                break
        for ghost in ghostState:
            gp = ghost.getPosition()
            d = abs(pos[0] - gp[0])
            d = d + abs(pos[1] - gp[1])
            if(d <= 1 and ghost.scaredTimer < 1): 
                total -= 1000
                goalReached = True
        if fud[pos[0]][pos[1]]:
            total += 500
        if action == 'Stop':
            total -= 10
        if newGS.isWin():
                return 1000000
            
        #print("goal state reached.")
        total += newGS.getScore()
        return total
        #return successorGameState.getScore()

class RandomMemoryAgent(Agent):
    def __init__(self):
        super().__init__()
        self.lastMove = 'Stop'
        self.oppositeMove = {
            'East': 'West',
            'West': 'East',
            'North': 'South',
            'South': 'North',
            'Stop': 'Stop'
        }

    def getAction(self, gameState):
        """
        getAction chooses among the best options according to the evaluation function.
        Code provided by environment requires us to use this function.

        getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        #print(self.planScore)
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        #print(legalMoves)
        #print(scores)
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best
        self.lastMove = legalMoves[chosenIndex]
        return self.lastMove

    def evaluationFunction(self, currentGameState, action):
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        #newPos = successorGameState.getPacmanPosition()
        #newFood = successorGameState.getFood()
        #print(newFood)
        #newGhostStates = successorGameState.getGhostStates()
        #newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        #print(successorGameState.getScore())
        #A*
        #f(n) = g(n) + h(n) : total cost = cost of successor + cost to goal by heuristic
        #best score of successor -> lowest cost, lowest score -> highest cost
        #thus in our case f(n) is the highest score possible, h(n) is greatest amount of points possible per state.
        #h(n) = remaining pellets*10, heuristic is the highest amount pellets possible to collect
        #gets best action (highest score)
        
        
        #initial total with initial state score
        #total = successorGameState.getScore() + successorGameState.getNumFood()*10
        actions = []
        total = 0
        count = 0
        #check if goal node has been reached
        goalReached = False
        newGS = successorGameState
        oldpos = currentGameState.getPacmanPosition()
        pos = newGS.getPacmanPosition()
        ghostState = newGS.getGhostStates()
        fud = newGS.getFood()
        #for x in range(fud.width):
        #    for y in range(fud.height):
        #        if fud[x][y] :
        #            nd = abs(pos[0] - x)
        #            nd = nd + abs(pos[1] - y)
        #            od = abs(oldpos[0] - x)
        #            od = od + abs(oldpos[1] - y) 
        #            if(nd < od):
        #                total += 1
        #                break
        for ghost in ghostState:
            gp = ghost.getPosition()
            d = abs(pos[0] - gp[0])
            d = d + abs(pos[1] - gp[1])
            #print(d)
            #print(d < 2 and ghost.scaredTimer < 1)
            if(d < 2 and ghost.scaredTimer < 1): 
                #print("TESTING VAR")
                return -1000
                goalReached = True
        if oldpos == pos:
            total -= 10
            goalReached = True
        if fud[pos[0]][pos[1]]:
            total += 500
        if action == self.oppositeMove[self.lastMove] :
            total -= 50
        if newGS.isWin():
                    return 1000000
        total += successorGameState.getScore()
        #print("search for goal state: pellets = 0")
        #If goal node has not been reached, find next node. Else return score
        
            
        #print("goal state reached.")
        #return total score
        return total
        #return successorGameState.getScore()