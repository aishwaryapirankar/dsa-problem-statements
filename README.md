# Problem Solutions: Graphs, Hashing, and DP

This repository contains Python implementations for three problem statements.

## Problem Logic Explanations

### P015: Graphs - Depth-First Search (DFS)

**Approach:**

1. Initialize an empty set 'visited' to keep track of explored nodes and a 'stack' starting with the initial vertex.
2. In each iteration, pop a vertex from the stack.
3. If it hasn't been visited, add it to the 'result' and push all its neighbors onto the stack.

### P016: Contains Duplicate

**Approach:**

1. Initialized set called 'seen' and iterate through the array once.
2. For each number, we check if it already exists in the 'seen' set.
3. If found, we return 'True'. If the loop finishes, we return 'False'.

### P017: Longest Increasing Subsequence (LIS)

**Approach:**

1. Every element starts with a default LIS length of 1.
2. For every element at 'i', we scan all previous elements at 'j'.
3. If 'nums[i] > nums[j]', we update 'lis[i]' to be the maximum of its current value or 'lis[j] + 1'.

## How to Run

In terminal:
python solution_code.py > output.txt
