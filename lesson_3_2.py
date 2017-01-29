"""

A zero-indexed array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

    def solution(A)

that, given a zero-indexed array A, returns the value of the missing element.

For example, given array A such that:
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5

the function should return 4, as it is the missing element.

Assume that:

        N is an integer within the range [0..100,000];
        the elements of A are all distinct;
        each element of array A is an integer within the range [1..(N + 1)].

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.

test:
1. empty list and single element
2. the first or the last element is missing
3. single element
4. two elements
5. range sequence, length = ~100,000

"""

def solution(A):
    if len(A)==0 or len(A)==1:
        return 0
    elif len(A)==2:
        A.sort()
        if A[0]!=A[1]:
            return A[0]+1
    else:
        A.sort()
        for i in range(len(A)):
            key=A[i+1]
            if (key-A[i])!=1:
                return A[i]+1
