# P015 Graphs - Implement depth-first search (DFS) for an undirected graph.
from typing import Dict, List

def dfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    visited = set()
    stack = [start]
    result = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            stack.extend(graph[vertex])
    return result

# P016 Check if any value appears at least twice in the array.
def contains_duplicate(nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# P017 Longest Increasing Subsequence using DP
def length_of_LIS(nums: List[int]) -> int:
    if not nums:
        return 0
    lis = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    return max(lis)

# Testing
if __name__ == "__main__":
    print("Testing P015: Graphs")
    g1 = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
    print(f"Standard Case (Start 2): {dfs(g1, 2)}")
    g2 = {0: []} 
    print(f"Base Case (Single Node): {dfs(g2, 0)}")
    g3 = {0: [1], 1: [2], 2: []} 
    print(f"Linear Case (Start 0): {dfs(g3, 0)}")

    print("\nTesting P016: Hashing")
    print(f"Duplicates exist: {contains_duplicate([1,2,3,1])}") 
    print(f"Base Case (Empty): {contains_duplicate([])}")
    print(f"Edge Case (Unique): {contains_duplicate([1,2,3,4])}")

    print("\nTesting P017: Dynamic Programming")
    print(f"Length of LIS: {length_of_LIS([10,9,2,5,3,7,101,18])}")
    print(f"Base Case(One Element): {length_of_LIS([7])}")
    print(f"Edge Case(Decreasing): {length_of_LIS([5, 4, 3, 2, 1])}")
