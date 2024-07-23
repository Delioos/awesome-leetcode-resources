# Problems related lessons

## Reverse a linked list
I used to think in a naive way that I would just browse through nodes, store the data in a vector and build a new list from a reversed vector.

This induced a time complexity of O(2n) (I think)

But the correct way is to reverse the pointers during the traversal. This is done in a single pass, so the time complexity is O(n) (and the code is way more understandable).
