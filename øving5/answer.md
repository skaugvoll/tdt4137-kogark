# Kogarg Exercise 5
## Sigve Skaugvoll

__Good book: https://books.google.com/books?id=80FXUtF5kRoC&pg=PA307&lpg=PA307&dq=soar+%22i-support%22&source=bl&ots=j3fji_17hZ&sig=sY76HYef90V4LoK8CBF2DfGInCA&hl=no&sa=X&ved=0ahUKEwjPu4X324_XAhWj14MKHU-rCy4Q6AEIUjAF#v=onepage&q&f=false__


## Task 1: The Soar processing cycle
**Input phase**
See stuff in the real world, and store in working memory

**Operation Selection**
Productions fire (and retract) to interpret new data (state elaboration), propose operators for the current situation (operator proposal), and compare proposed operators (operator comparison). All of the actions of these productions are I-supported. All matched productios fire in parallel (and all retractions occure in parallel), and matching and firing continues until there are no more additional complete matches or retractions of productions (quiescence).

__Decision__ A new operator is selected, or an impass is detected and a new state is created.


**Operation Application**
The new state created goes through the operation selcetion elaboration, then it goes to the application state. **application**, Productions fire to apply the operator (operator application). The actions of these productions will be O-supported. Because of changes from operator application productions, other productions with I-supported actions may also match or retract. Just as during proposal, productions fire and retract in parallel until quiescence.

**Output** Output commands are sent to the external environment.

The cuycles continue until the halt ction is issued from the Soar program (as the action of a production) or until Soar is interrupted by the user.

## Task 2
### a)
The notion of I- and O-support in Soar is an importatn and fundamental concept. It distinguish between different types of support.

I-support means instantiation and its; Once an operator is proposed, its  preference persists until working memory no longer supports the operator preference.

Operator actions that changes working memory, and are persistent over subsequent working memory changes are said to have `operator` or `O-support`

### b)
Impass means do the same rule evaluation approach as before, but now the goal is to choose between two operators for the original state,. and is the learning process. It means that there is no rule that is choosen and thus an branch off happens and a new rule is created from the state that did not have an action, with a new action that was created in the impasse. Thus the agent learns.

An event happens, and we doent know what to do. We have to choose one operator, but we cannot decide on one. Thus we need to create a new rule that indicates what rule / operator that we need to choose if such an event occures again.
Summed up; remember what happened, and what we did.

## Task 3: Representation

