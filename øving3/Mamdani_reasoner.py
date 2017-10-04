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
            "Perfect": ['T', [3.75, 5, 6.75]],
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
    def RuleEvaluation(self, position=0, set_={}):

        return



    ########
    # Meta
    #######


    def printResult(self, directionPos, deltaPos, action):
        print("Distance position is: %s \nDelta position is: %s\nAction position: %s\n" %(directionPos, deltaPos, action))

    def getIntersection(self,set,value):
        dict = {}
        for key in set:
            if set[key][1][0] <= value and value <= set[key][1][-1]:
                if set[key] == 'RG':
                    dict[key] = self.reverse_grade(value,set[key][1][0],set[key][1][1],100)
                elif set[key] == 'T':
                    dict[key] = self.triangle(value,set[key][1][0],set[key][1][1],set[key][1][2],100)
                else:
                    dict[key] = self.grade(value,set[key][1][0],set[key][1][1],100)
        return dict


    def reasoning(self):
        #Step 1: Fuzzication (Find values for each set in fuzzyset)
        print(self.getIntersection(self.distance_set(),self.distancePos))
        return

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



def main(distancePos, deltaPos):
    '''
     Assignment values: $ python Mamdani_reasoner.py 3.7 1.7
    '''

    distancePos = float(distancePos) # convert sys args to float, not string
    deltaPos = float(deltaPos) # convert sys args to float, not string
    m = Mamdani(distancePos, deltaPos)

    print(str(m) + "\n")



    action = m.reasoning()
    print("Action crisp value is: " + str(action))



main(sys.argv[1], sys.argv[2])
