# 1. Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return **indices** of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

### Example
#### Input
```text
nums = [2, 7, 11, 15]
target = 9
```
#### Output
```text
[0, 1]
```

#### Explanation
`nums[0] + nums[1] = 2 + 7 = 9`

---

## Approach 1: Brute Force

### Algorithm
1. Iterate through all pairs of numbers in the array using two nested loops.
2. Check if their sum equals the `target`.
3. Return their indices if a match is found.

### Complexity
- **Time Complexity:** \(O(n^2)\), due to nested loops.
- **Space Complexity:** \(O(1)\), as no additional space is used.

### Code
```python
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

---

## Approach 2: Using a Hash Map (Optimal)

### Algorithm
1. Create an empty dictionary (hash map) to store numbers and their indices.
2. Traverse the array:
   - Calculate the `complement` as `target - nums[i]`.
   - If the `complement` exists in the hash map, return the indices.
   - Otherwise, store `nums[i]` in the hash map with its index.
3. This ensures a single pass through the array.

### Complexity
- **Time Complexity:** \(O(n)\), as we traverse the array once.
- **Space Complexity:** \(O(n)\), for storing elements in the hash map.

### Code
```python
def two_sum(nums, target):
    num_map = {}  # Dictionary to store number and index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
```

---

## Key Insights
- **Brute Force** works but is inefficient for larger arrays.
- **Hash Map** drastically reduces the time complexity by using extra space to store indices.

---

## Test Cases
| nums               | target | Output  |
|--------------------|--------|---------|
| [2, 7, 11, 15]     | 9      | [0, 1]  |
| [3, 2, 4]          | 6      | [1, 2]  |
| [3, 3]             | 6      | [0, 1]  |
| [-1, -2, -3, -4]   | -6     | [1, 3]  |

---

## Edge Cases
1. **Negative Numbers:** Handles negative values correctly.
2. **Duplicate Numbers:** Ensures the same element isn't reused for the solution.

---

## Conclusion
The hash map approach is optimal for this problem, with a linear time complexity. It efficiently handles large inputs and edge cases.
