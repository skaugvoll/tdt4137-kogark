# NGOMSL - A branch of GOMSL
Has certain properties that make it unique. NGOMSL inherits the ability to not only give estimations for execution times but it can also estimate the time taken to learn how to use the system. It also, however, shares one of the major disadvantages all of the previous methods. NGOMSL models user interaction as a serial operation. One operation occupies the user completely, there is no multitasking, which makes NGOMSL inappropriate for analyzing tasks where the users are under time pressure, highly practiced and, in reality, do act in a parallel fashion.

Based on CCT (Cognitive Complexity Theory) research
results, but suitable for practical use.

## Goals:
The recipe is referred to as a "top-down, breadth-first" expansion. The user's high-level goals are unfolded until only operators remain. Generally operators are considered to be keystroke-level operations, but that is not a rigid requirement.

## Unit tasks - user goals:
Unit tasks are naturla user goals at the conceptual level. Example of unit tasks for A Text editor: save document, new document, delete document, find text, delete word, delete line, etc.

Unit tasks may be decomposed / broken into sub-taks or sub goals.
- moving text in an editor decoposed into; cut text and paste text.

Insert picture [Mae a list of the top-level user's goals]


***Model the top-level***

- Top level is a unit-task / user goal top level. i.e Edit the document. This task has several unit tasks : move text, delete text, etc.

    ELLER

- Top level er super abstract / generelt.
 - eksempel : få en oppgave, utfør oppgave, hent neste oppgave, hvis ikke flere oppgaver avbryt.


## Structure:
- User goals
- Unit taks
- Method
 - Steps
- Selection rule set

## Operators:
KLM-operators: K,P,B,H and M (time estimates)
- K - Keystroke
 - Pressing a key or button on the keyboard
 - Different experience levels have different times
 - Good typist (90 wpm): .12 sec
 - Average skilled typist (55 wpm): .20 sec
 - Average nonsecretarial typist (40 wpm): .28sec
 - Worst typist (unfamilar with keyboard): 1.2 sec
 - Pressing SHIFT or CONTROL key is a separate keystroke
- P - Point with mouse to a target on the display
 - Follows Fitts’ law ( T = a + b log2 (D/S + 1) Shannon )
 - Typically ranges from .8 to 1.5 sec Average is 1.1 sec
- B - Press mouse button
 - Highly practiced, simple reaction Use .1 sec
 - Mouse button click (BB) takes .2 sec
- H - Home hands to the keyboard or mouse Takes .4 sec
- M - Mental act of thinking Estimates ranges from .6 to 1.35 sec. Use 1.2 sec

## Syntax
###  NGOMSL Syntax: Operators
Built-in Primitive operators (cognitive processor related)
- Accomplish subgoals:
 - ① Accomplish the goal of <goal description>
 - ② Return with goal accomplished
- Flow of control:
 - ① Decide: If <operator ...> Then <operator>
 - ② Decide: If <operator ...> Then <operator> Else <operator>
 - ③ Go to …
- Memory storage and retrieval:
 - ① Recall that <WM-object-description>
 - ② Retain that <WM-object-description>
 - ③ Retrieve-LTM that <LTM-object-description>
- Mental ”arithmetic”:
 - ① Think of ……
 - ② Make …..

Notice that we write ”Decide: if …” to
not confuse with the parallel-if used in selection rules.
”Decide:if …” is sequential.

Typical Primitive external operators:
- ① Press-key <key name>
- ② Hold <button>
- ③ Release <button>
- ④ Type <string>
- ⑤ Move-mouse to <target coordinates>
- ⑥ Find-cursor-is-at <returned cursor coordinates>
- ⑦ Locate <object>
- ⑧ …………etc

Examples typical Analyst-defined operators (varies from domain to domain):
- ① Get-from-task <name>
- ② Look in the task description for the information
 tagged with <name> and put it into working memory
- ③ Verify-result
 Determine whether the result of an operation is
 correct
- ④ Get-next-edit-location
 Get the next edit location from the task description
- ⑤ Most-recent
 Determine the most recent of two time-stamped items
- ⑥ ……..etc


## THE METHOD:
- Make a list of the top-level user's goals (unit-tasks)
- Do the following recursively (breadth-first):
 - Write a step-by-step method for accomplishing each goal in the list based on:
  - how the system is operated
  - Judgment calls on how user views the task in terms of subgoals.
- Examine each step in each method:
 - If a step is NOT a keystroke-level operator:
  - reqrite the steps as invoking a subgoal
  - add this subgoal to a new list of goals
 - If all the steps involve only eystroke-level operators the method is finished

- repeat for the new list of goals until all methods are finished.
- if there are multiple methods for a goal, supply a set of selection rules to choose which method to invoke.


### The method once more.
- make a list of unit taks and then the unit task sub goals.

- Sketch the top-level method for handling unit tasks.
 - the reqrite sketch, in NGOMSL (conduct a top-down breadth-first expansio).

- Write top-level unit tasks handling in NGOMSL (main program loop).
