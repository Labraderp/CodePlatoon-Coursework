# Balanced Parentheses

For this assignment, we will do it on leetcode. This is both to help you get more familiar with leetcode (which is becoming a standard tool in the technical interview-prep process) and because leetcode describes this problem particularly well and has excellent tests for it.

https://leetcode.com/problems/valid-parentheses/

**You should complete the assignment in leetcode above, to get familiar with the platform.** That said, if it helps, don't be afraid to prototype code locally (on your own computer) in VS Code. 

If you have not we recommend creating free account with leetcode.

**Once you are done be sure to check out other submitted solutions on leetcode and the problem discussion!**

Also - **only once you are done** -- [check out the problem analysis here](https://redquark.org/leetcode/0020-valid-parentheses/)

Below is the problem description from leetcode 

----

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
```
Input: s = "()"
Output: true
```

Example 2:
```
Input: s = "()[]{}"
Output: true
```

Example 3:
```
Input: s = "(]"
Output: false
```
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

### Write an algorithm that takes in a string and returns a string with balanced parentheses only. The string will contain letters, numbers, and parentheses only.

```python
balanceParens("()") # should return "()"
balanceParens("a(b)c)") # should return "a(b)c"
balanceParens("(a)(bdd)c)") # should return "(a)(bdd)c"
balanceParens("a(dbvb)c)") # should return "a(dbvb)c"
balanceParens("a(b)(c)())") # should return "a(b)(c)()"
balanceParens(")(") # should return ""
balanceParens("(((((") # should return ""
balanceParens(")(())(") # should return "(())"
balanceParens("(()()(") # should return "()()"
balanceParens(")())(()()(") # should return "()()()"
```

### Challenge - Nested Parentheses
```python
balanceParens(")(())(")) # should return "(())"
```
