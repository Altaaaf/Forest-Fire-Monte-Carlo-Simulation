# Forest-Fire-Monte-Carlo-Simulation
This script simulates a forest fire in a perfect 40x30 rectangular forest consisting of 1,200 trees. The top-left corner tree catches fire, and wind blows from the west. The probability that any tree catches fire from its burning left neighbor is 0.85. The probabilities of catching fire from trees immediately to the right, above, or below are all equal to 0.35.

The script conducts a Monte Carlo study to estimate the probability that more than 40% of the forest will eventually be burning. It also estimates the total number of affected trees X and the standard deviation of X. Finally, it calculates the probability that the actual number of affected trees differs from the estimator by more than 25 trees.

## Technologies Used

* Python
* numpy
* statistics
* random

## Get started
To get started, follow these steps:

1. Clone the repository to your local machine.
``` {.sourceCode}
git clone https://github.com/Altaaaf/Forest-Fire-Monte-Carlo-Simulation
```
2. Install the required packages by running the following command:
``` {.sourceCode}
pip install -r requirements.txt
```
## Question

A forest consists of 1,200 trees forming a perfect 40×30 rectangle. The top-left corner tree catches fire. Wind blows from the west, therefore, the probability that any tree catches fire from its burning left neighbor is 0.85. The probabilities to catch fire from trees immediately to the right, above, or below are all equal 0.35.

1. Conduct a Monte Carlo study to estimate the probability that more than 40% of the forest will eventually be burning. With probability 0.95, your answer should differ from the true value by no more than 0.005.
2. Based on the same study, predict the total number of affected trees X.
3. Estimate the standard deviation of X and comment on the accuracy of your estimator of X.
4. What is the probability that the actual number of affected trees differs from your estimator by more than 25 trees?
