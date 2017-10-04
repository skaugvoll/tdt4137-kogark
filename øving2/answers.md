# Assignment Two - TDT4137 - Kogark
## NGOMSL and Mental Programming.
***Sigve Skaugvoll, 2017***

### Task 1.
Unit tasks are just top level users goals. This means that the goals are at a conceptual level.

#### A) Name some typical unit-task for a telephone app and model the top-level i NGOMSL
Typical examples of 'User goals' for the typical "telephone" app are

- Call x
- Send x a text message
- Add x to contact list
- Delete x from contact list

Some Unit tasks level goals are for instance if we want to call x;
If we remember x's number.

- Open app.
- Navigate to numpad.
- Enter number.
- Press call button.

Or if x is one of my "stared" contacts.

- Navigate to my favorites.
- Find person.
- Press on persons tile.

__Sketch of top-level method__:

- Find the numpad
- Find the number of a piece of paper
- Enter the number on the numpad
- Hit the call button

### Model top level in NGOMSL
__Method to accomplish calling__

- Step 1. Get next unit task information from marked-up manuscript
- Step 2. Decide: If no more unit tasks, then return with goal accomplished
- Step 3. Accomplish the goal of moving to the unit task location
- Step 4. Accomplish the goal of **performing the unit task**
- Step 5. Goto 1.

__Selection rule set for the goal of **performing the unit task**__

- If the task is call x using numpad, then accomplish the goal of **call number**
- If the task is call x using favorite, then accomplish the goal of **select favorite**
- Return with goal accomplished.


#### B) Model the unit task / goal : Call x.

Assumptions

- Number and name is written on a piece of paper.
- Person is also stored in contacts as a favorite.
- I assume recall / retain is act of M (mental act of thinking).
- I assume decide is a function of CP

Method to accomplish call number:

- Step 1. recall number
- Step 2. Retain number // retain so that we can use it when enter digits.
- Step 3. Accomplish the goal of enter digits.
- Step 4. Move finger to call button
- Step 5. Push call button.
- Step 6. Return with goal accomplished.

Method to accomplish enter digits:

- Step 1. Decide: if whole number is entered. return with goal accomplished.
- Step 2. Recall next digit.
- Step 3. Move finger to digit location on screen.
- Step 4. Press digit.
- Step 5. Go to step 1.

Method to accomplish call using favorite:

- Step 1. Recall name.
- Step 2. Locate name on screen.
- Step 3. Move finger to name.
- Step 4. Push name to call.
- Step 5. Return with goal accomplished.


#### C) Calculate execution time for the given alternatives:

- CP = 1.2 sec # see something
- B = 0.1 sec (Tap/push button)
- H = 0.4 sec (Home hands to the keyboard or mouse)
- K = 0.2 sec (Keystroke)
- M = 1.2 sec (verify that task is done)
- P = 1.1 sec (Point move to location)

Τ = Σ KLM-operator-times + 0.1 sec * NGOMSL statements executed


***Top level***

Total statements including "headers" : 6

- #CB : 1
- #B :
- #H :
- #K :
- #M :
- #P :

Operator time = (1 * CP)
Operator time = (1 * 1.2) = 1.2 sec

Total time  = Operator time + (0.1 * steps)
            = 1.2 + (0.1 * 6)
            = 1.2 + 0.6
            = 1.8 sec

***Rule set***

Total statements including "headers and returns" : 3 (since all "if"s happen in parallel, all counts as one together)

***call number***

Total statements including "headers" : 7

- #CB :
- #B : 1
- #H :
- #K :
- #M : 2
- #P : 1

Operator time = (1 * B) + (2 * M) + (1 * P)

Operator time = (1 * 0.1) + (2 *  1.2) + (1 * 1.1)  = 3.6 sec

***enter digits***

Total statements including "headers" : 6
> (Since a number has 8 digits we have to repeat each "action" 8 times)

- #CB : 1 (decide) * 8 = 8
- #B : 1 * 8 = 8
- #H :
- #K :
- #M : 1 (recall) * 8 = 8
- #P : 1 * 8 = 8

Operator time = (8 * CP) +  (8 * B) +    (8 * M) +    (8 * P)

Operator time = (8 * 1.2) + (8 * 0.1) + (8 *  1.2) + (8 * 1.1)  = 28.8sec

***Using numpad***

Total statements including "headers" : 13 (call number + enter digits)

- #CB : 8 = (0 + 9.6) = 9.6 sec
- #B : 9 = (0.1 + 0.8) = 0.9 sec
- #H :
- #K :
- #M : 9 = (1.2 + 9.6) = 10.8 sec
- #P : 9 = (1.1 + 8.8) = 9.9 sec

Total Operator time = (9.6 + 0.9 + 10.8 + 9.9)sec = 31.2 sec

Total time  = Total Operator time + (0.1 * steps)
            = 31.2 + (0.1*13)
            = 31.2 + 1.3
            = 32.5 sec

Execution time with top level: 32.5 + 1.8 = 34.3 sec

***Using favorites***

Total statements including "headers" : 6

- #CB : 1 (locate)
- #B : 1
- #H :
- #K :
- #M : 1 (recall)
- #P : 1

Operator time = (1 * CP) +  (1 * B) +    (1 * M) +    (1 * P)

Operator time = (1 * 1.2) + (1 * 0.1) + (1 *  1.2) + (1 * 1.1)  = 3.6sec

Total time  = Operator time + (0.1 * number of statements)
            = 3.6sec + (0.1 * 6)sec
            = 4.2 sec

Execution time with top level: 4.2 sec + 1.8 = 6 sec
