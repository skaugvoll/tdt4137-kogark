import sys
import random as r

class Mamdani:
    def __init__(self, disPos, delPos):
        self.distancePos = disPos
        self.deltaPos = delPos
        self.distanceValues = {}
        self.deltaValues = {}
        self.actionValues = {}
        self.clipSet = {}

    def __repr__(self):
        return "I'm Mamdani!\nWho are you?"


    ########
    # Rules
    #######

    def AND_rule(self, *args):
        return min(*args)

    def OR_rule(self, *args):
        return max(*args)

    def NOT_rule(self, value):
        return 1 - value


    ########
    # Sets
    #######

    def distance_set(self):
        setValues = {
            "VerySmall": ['RG', [1.5, 2.75]],
            "Small": ['T', [1.75, 3, 4.75]],
            "Perfect": ['T', [3.75, 5 ,6.75]],
            "Big": ['T', [5.75, 7, 8.75]],
            "VeryBig": ['G', [7.75, 9]]
        }
        return setValues

    def delta_time_set(self):
        setValues = {
            "ShrinkingFast": ['RG', [-3.5,-2.25]],
            "Shrinking": ['T', [-3.25,-1.75,-0.25]],
            "Stable": ['T', [-1.25,-0.25,1.75]],
            "Growing": ['T', [0.75,2.25,3.75]],
            "GrowingFast": ['G', [2.75,4.25]]
        }
        return setValues

    def action_set(self):
        setValues = {
            "BrakeHard": ['RG', [-7.5,-5]],
            "SlowDown": ['T', [-7,-4,-1]],
            "None": ['T', [-3,0,3]],
            "SpeedUp": ['T', [1,4,7]],
            "FloorIt": ['G', [5,7.5]]
        }
        return setValues


    ########
    # Membership functions
    #######

    def triangle(self, position, x0, x1, x2, clip):
        value = 0.0

        if position >= x0 and position <= x1:
            value = (position - x0) / (x1 - x0)

        elif position >= x1 and position <= x2:
            value = (x2 - position) / (x1 - x0)

        if value > clip:
            value = clip

        return value


    def grade(self, position, x, y, clip):
        value = 0.0

        if position >= y:
            value = 1.0
        elif position <= x:
            value = 0.0
        else:
            value = (position - x) / (y - x)

        if value > clip:
            value = clip

        return value

    def reverse_grade(self, position, x, y, clip):
        value = 0.0

        if position <= x:
            value = 1.0
        elif position >= y:
            value = 0.0
        else:
            value = (y - position) / (y - x)

        if value > clip:
            value = clip

        return value

    def getAggregation(self, set_={}):
        s = 0
        for k in set_:
            s += set_[k]

        print("*********Sum Aggregation: " + str(s))
        return s



    ########
    # ACTIONS
    #######

    def AND_TRIANGLE(self, distKey, deltKey, clip):
        dix0,dix1,dix2 = self.distance_set()[distKey][1]
        dex0,dex1,dex2 = self.delta_time_set()[deltKey][1]

        value = self.AND_rule(self.triangle(self.distancePos, dix0, dix1, dix2, clip), self.triangle(self.deltaPos, dex0, dex1, dex2, clip))
        return value



    ########
    # Testing
    #######

    '''
    Basically, find the sub-set the position belongs to, in a given fuzzy set.
    '''
    def testFuzzySetValue(self, position=0, set_={}):
        s = set_
        heighestVal = 0.0
        heighestBelonging = ""
        pos = position
        setValues = {}
        for k in s:
            dist = s[k]
            # print(k)
            # print(dist, len(dist), k)
            if(dist[0] == "RG"):
                tempval = self.reverse_grade(pos, dist[1][0], dist[1][1], 100)

            elif(dist[0] == "G"):
                tempval = self.grade(pos, dist[1][0], dist[1][1], 100)
            else:
                tempval = self.triangle(pos, dist[1][0], dist[1][1], dist[1][2], 100)

            setValues[k] = tempval
            # print(k,tempval)

            if(tempval > heighestVal):
                heighestVal = tempval
                heighestBelonging = k

        # print(heighestVal, heighestBelonging)
        return setValues



    ########
    # Meta
    #######


    def printResult(self, directionPos, deltaPos, action):
        print("Distance position is: %s \nDelta position is: %s\nAction position: %s\n" %(directionPos, deltaPos, action))


    def reasoning(self):
        # Step 1: Fuzzication (Find values for each set in fuzzyset)
        self.distanceValues = self.testFuzzySetValue(self.distancePos, set_=self.distance_set())
        self.deltaValues = self.testFuzzySetValue(self.deltaPos, set_=self.delta_time_set())

        print("distance values: ", self.distanceValues)
        print("delta values: ", self.deltaValues)

        diPos = self.getNonZeroSubSets(self.distanceValues)
        dePos = self.getNonZeroSubSets(self.deltaValues)

        print ("DI pos: ", diPos )
        print ("DE pos: ", dePos)

        # Step 2: Rule evaluation

        self.printResult(self.distancePos, self.deltaPos, actionPosition)


        # Step 3: Aggregation (finding output/action)
        '''
        - Process of unification of the outputs of all rules
        - Take membership functions of all rule consequents (etterledd) prev. clipped and combine them into a single single fuzzy set
        - The input of the aggregation process is the list of clipped or scaled consequent membership functions,
          and the output is one fuzzy set for each output variable.
          - Basically just sum up all the rule values. (getAction, just sum up instaed of find heighest)
        '''

        self.actionValues = self.testFuzzySetValue(actionPosition, set_=self.action_set())
        print("ActionValues is: ", self.actionValues)

        # a = getHeighest(self.actionValues)
        # print("Action to take is: " + str(a))


        # Step 4: Defuzzification

        # TODO: Regn sammen COG!
            # regn COGt
        w = {**self.distance_set(), **self.delta_time_set()}
        COGt = 0

        for ss in self.action_set():
            setValues = self.action_set()[ss][1]
            print(setValues)

            x = 0 # legg sammen alle x verdiene
            print(setValues[-1])
            for i in range(int(setValues[0]), int(setValues[-1]+1)):
                x += i
            y = self.actionValues[ss] # actionValue for dette sub settet
            print("*****X and Y: ", x, y)
            COGt += x * y
            print("***********COGt", COGt)
        print(COGt)



            # regn COGb
        COGb = None
        for hvertSubSet in hvertFuzzySet:
            x = hvertSubSet[1][0] - hvertSubSet[1][-1] # antall x-steg ( x verdier subsettet strekker seg over) x1 - x2 =>  [(-3) - 3] = 6 steps
            y = 0 # actionValue for dette sub settet
            COGb += x * y

        sumCOG = COGt / COGb

        print("Sum COG: ", sumCOG)

        return sumCOG


    def getNonZeroSubSets(self, s):
        sets = []
        for k in s:
            # print(k)
            tempval = 0.01
            if s[k] > tempval:
                sets.append(k)
        print("*********: " + str(sets))
        return sets

########
# Running this badboy
#######

def getHeighest(s):
    action = ""
    tempval = -1000000
    for k in s:
        if s[k] > tempval:
            tempval = s[k]
            action = k

    return action



def main(directionPos, deltaPos):
    '''
     Assignment values: $ python Mamdani_reasoner.py 3.7 1.7
    '''

    directionPos = float(directionPos) # convert sys args to float, not string
    deltaPos = float(deltaPos) # convert sys args to float, not string
    m = Mamdani(directionPos, deltaPos)

    print(str(m) + "\n")



    action = m.reasoning()
    print("Action crisp value is: " + str(action))



main(sys.argv[1], sys.argv[2])
