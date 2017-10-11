# Lab ecercise 4 - Artifical Neural Networks

## Task a)

### Questions:
1. What are `step` in activation function (step 2)
2. are `X` and `W` functions, since in `step 2 (activation)` they take in iteration `p`
3. Should `Y` be a list holding all calculated Y's since Y also takes in P?
4. What is `p` is it the same as `x` ? I need help to understand how to do step 2, activation.

### Notes from reading

#### Sign function
Sign is one of many activation functions. It's also a hard limit function.
All it actually does is;
Computes the weighted sum of the input signals and compares the result with a threshold value, 𝜭.

If the net unout is less than the threshold, the neuron outpus is -1. But if the net input is greater than or equal to the threshold, the neouron becomes activated and itis output attains a vaue +1.

_func_:

X = ∑<sub>i=1</sub><sup>n</sup> X<sub>i</sub>\* W<sub>i</sub>

Y = +1 if X >= 𝜭 OR Y = -1 if X < 𝜭

Another way of writing the function is

Y = sign[ ∑<sub>i=1</sub><sup>n</sup> X<sub>i</sub>\* W<sub>i</sub> - 𝜭 ]


#### X<sub>i</sub>, W<sub>i</sub> and n
X<sub>i</sub> is the value of input i
W<sub>i</sub> is the weight of input i
n is the number of neuron inputs
y = is the output of the neuron


#### P - iteration
`P` represents the pth training example presented to the perceptron.


#### Error function:
`e(P) = Y<sub>d</sub>(P) - Y(P)`, where P = 1,2,3,....




### Perceptron Learning Rule
w<sub>i</sub>(p + 1) = w<sub>i</sub>(p) + 𝛂 * x<sub>i</sub>(p) * e(p)

### 𝛂
The learning rate a positive constant less than unity.


Epcoh, en iterasjon gjennom treningsettet
