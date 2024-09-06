# Problems related lessons

## Linked list
### Reverse a linked list
I used to think in a naive way that I would just browse through nodes, store the data in a vector and build a new list from a reversed vector.

This induced a time complexity of O(2n) (I think)

But the correct way is to reverse the pointers during the traversal. This is done in a single pass, so the time complexity is O(n) (and the code is way more understandable).

### Cycle detection
Again, I focused on a naive approach but I should have thought about the pointers.

The correct way is to traverse the list and check if the next pointer is pointing to the current node by using two pointers.
One that goes faster than the other one. if they are equal, then we have a cycle. And if one pointer.Next is null (nil in go), 
then we have finished traversing the list and can return false 

## Binary tree
## Tree inversion
Nothing much to say. Found the solution on my own on the first time. I built my solution on two main parts:
- tree traversal
- node leafs inversion
Thats pretty much it. The code speaks for itself. 
I just had a hard time with rust borrow checker  / rc / cell and it would be great to be able to get it on a whiteboard without any external help (neither net nor compiler hardcarrying me. 

## Backtracking
### Permutations
