def alternativeMain():
    # [x, y] coordinates. Want to classify all positive x as a group, and all negative as one group
    numberOfFeatures = 2

    testSet = [   [-1,2], [1,2], [8,2], [-4,7], [9,1], [-1,9], [-9,1], [6,6], [6,1], [-5,1]]
    testValidation = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0]

    trainingSet = [
        [2,0],
        [3,7],
        [-1,5],
        [-2,4],
        [4,4],
        [-9,9],
        [5,3],
        [-4,0]
    ]
    training_validation_set = [1,1,0,0,1,0,1,0]

    per = Percepton(
        training_set=trainingSet,
        training_validation_set=training_validation_set,
        test_set=testSet,
        test_validation=testValidation,
        numberOfFeatures=numberOfFeatures
    ) # number of weights = number of features (X1,...Xn)
    print(per)

    per.initialisation()
    print(per)
