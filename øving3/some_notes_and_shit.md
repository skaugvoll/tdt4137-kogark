## Mamdani-reasoner

 `Mamdani` is a way to do `Fuzzy logic reasoning`

 Mamdani Fuzzy Inference : simple `two-input one-output` problem, that includes rules.
 The inference process is performed in four steps:
 1. Fuzzification of the input variables.
 2. Rule evaluation (inference).
 3. Aggregation of the rule outputs (composition).
 4. Defuzzification.


### Defuzzification:

 TOP = (BH* actionValue<sub>BH</sub>)  (SD * actionValue<sub>SD</sub>)  (N* actionValue<sub>N</sub>)  (SU* actionValue<sub>SU</sub>)  (F* actionValue<sub>F</sub>)

 Bottom = (Number of of x values for BH * actionValue<sub>BH</sub>)  (Number of of x values for SD * actionValue<sub>SD</sub>)  (Number of of x values for N * actionValue<sub>N</sub>)  (Number of of x values for SU * actionValue<sub>AV</sub>)  (Number of of x values for F * actionValue<sub>F</sub>)


 COG = T / B
