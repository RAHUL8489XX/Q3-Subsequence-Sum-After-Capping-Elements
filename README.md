# 🎯 Subsequence Sum After Capping Elements

Accepted solution for LeetCode Weekly Contest 467 problem:  
[Subsequence Sum After Capping Elements](https://leetcode.com/contest/weekly-contest-467/problems/subsequence-sum-after-capping-elements/description/)

✅ [View Accepted Submission](https://leetcode.com/contest/weekly-contest-467/problems/subsequence-sum-after-capping-elements/submissions/1776018059/)

---

## 📘 Problem Description

You're given:
- An integer array `nums` of size `n`.
- A positive integer `k`.

For each integer `x` from `1` to `n`, you:
1. Cap the array by replacing each element `nums[i]` with `min(nums[i], x)`.
2. Check if it's possible to choose a subsequence from the capped array whose sum is exactly `k`.

Return a boolean array `answer` of size `n`, where `answer[i]` is `True` if it's possible when using `x = i + 1`, and `False` otherwise.

---

## 🧪 Example

```python
Input: nums = [4,3,2,4], k = 5
Output: [False, False, True, True]
