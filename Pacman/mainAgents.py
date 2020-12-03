from game import Directions
import random, util
from util import manhattanDistance

from game import Agent

class NewAgent(Agent):
    """
      An A* search agent

      Don't touch the method headers.
    """


    def getAction(self, gameState):
        """
        getAction chooses among the best options according to the evaluation function.
        Code provided by environment requires us to use this function.

        getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        print(scores)
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best
        
        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
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
        pos = newGS.getPacmanPosition()
        ghostPos = newGS.getGhostPositions()
        for gp in ghostPos:
            d = abs(pos[0] - gp[0])
            d = d + abs(pos[1] - gp[1])
            if(d <= 1): 
                total -= 1000
                goalReached = True
        if(newGS.isWin()):
                    return 1000000
        print("search for goal state: pellets = 0")
        #If goal node has not been reached, find next node. Else return score
        while (goalReached == False):
                       
            legalMoves = successorGameState.getLegalActions()

            # Choose one of the best actions
            scores = []
            for action in legalMoves:
                newGS = successorGameState.generatePacmanSuccessor(action)
                score = newGS.getScore() - (newGS.getNumFood() - currentGameState.getNumFood())
                #print(score)
                if(newGS.isWin()):
                    return 100000/(count+1)
                scores.append(score) 
                actions.append(action)
            if not scores: break
            bestScore = max(scores)
            bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
            chosenIndex = random.choice(bestIndices)
            actions.remove(legalMoves[chosenIndex])
            total+=scores.pop(chosenIndex)
            successorGameState=successorGameState.generatePacmanSuccessor(legalMoves[chosenIndex])
            
            
            if successorGameState.getNumFood() == 0 or count == 20:
                goalReached = True
            count+= 1
            
        print("goal state reached.")
        #return total score
        return total/(count+1)
        #return successorGameState.getScore()
        
    