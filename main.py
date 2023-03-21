import numpy as np
from random import choices
import statistics
from typing import List


def calculate_difference(
    mean_total_trees_burned: float,
    all_simulations: List[float],
    num_simulations: int
) -> float:
    """Calculate the proportion of simulations that had a 25-tree difference from the mean total trees burned.

    Args:
    - mean_total_trees_burned (float): The mean total trees burned across all simulations.
    - all_simulations (List[float]): A list of the total trees burned in each simulation.
    - num_simulations (int): The total number of simulations.

    Returns:
    - float: The proportion of simulations that had a 25-tree difference from the mean total trees burned.
    """
    num_different = sum(1 for trees_burned in all_simulations
                        if abs(trees_burned - mean_total_trees_burned) > 25)
    prop_different = num_different / num_simulations
    return prop_different


def total_trees_on_fire(forest: np.ndarray) -> int:
    """Calculate the total number of trees on fire in the forest.

    Args:
    - forest (np.ndarray): A 2D numpy array representing the forest. 
      A value of 0 means a tree is not on fire, while a value of 1 means a tree is on fire.

    Returns:
    - int: The total number of trees on fire in the forest.
    """
    return np.sum(forest)


def spreads_fire(spread_fire_probability: int = 35):
    """
    Generate a weighted uniform random number to determine if a tree will catch on fire.

    Args:
        spread_fire_probability (int): Probability of a tree catching fire. Default value is 35.

    Returns:
        int: 0 if the tree does not catch fire, 1 if it does.
    """
    return choices([0, 1], [100 - spread_fire_probability, spread_fire_probability])[0]


def run_simulation(rows: int = 30, columns: int = 40, simulations: int = 38416):
    """Run a Monte Carlo simulation of a forest fire.

    Args:
    - rows (int): The number of rows in the forest. The default value is 30.
    - columns (int): The number of columns in the forest. The default value is 40.
    - simulations (int): The number of simulations to run. The default value is 38416.

    Returns:
    - tuple: A tuple containing four parts:
        - Part a: The proportion of simulations where more than 40% of the forest burned.
        - Part b: The mean total number of trees burned across all simulations.
        - Part c: The standard deviation of the total number of trees burned across all simulations.
        - Part d: The proportion of simulations where the total number of trees burned differed from the mean 
          by more than 25 trees.
    """
    all_simulations = []
    total_trees_caught_fire = 0
    more_than_fourty_percent_burning = 0
    for simulation in range(simulations):
        forest = np.zeros((rows, columns))
        forest[0][0] = 1

        for row in range(rows):
            for column in range(columns):
                current_tree_on_fire = forest[row][column]
                west, north, east, south = 0, 0, 0, 0

                if column > 0:
                    west = forest[row][column-1]
                if row > 0:
                    north = forest[row-1][column]
                if column < columns - 1:
                    east = forest[row][column+1]
                if row < rows - 1:
                    south = forest[row + 1][column]

                if not current_tree_on_fire:
                    if west and spreads_fire(85):
                        forest[row][column] = 1
                    elif north and spreads_fire():
                        forest[row][column] = 1
                    elif south and spreads_fire():
                        forest[row][column] = 1
                    elif east and spreads_fire():
                        forest[row][column] = 1
                    else:
                        forest[row][column] = 0

        num_trees_on_fire = total_trees_on_fire(forest)
        if (num_trees_on_fire >= 480):
            more_than_fourty_percent_burning += 1
        total_trees_caught_fire += num_trees_on_fire
        all_simulations.append(num_trees_on_fire)

    part_a = more_than_fourty_percent_burning / simulations
    part_b = total_trees_caught_fire/simulations
    part_c = str(statistics.pstdev(all_simulations))
    part_d = calculate_difference(part_b, all_simulations, simulations)
    return (part_a, part_b, part_c, part_d)


if __name__ == "__main__":
    simulations_executed = run_simulation()
    print(simulations_executed)
