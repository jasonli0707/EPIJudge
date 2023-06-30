import random

# ref: https://realpython.com/sorting-algorithms-python/#measuring-efficiency-with-big-o-notation

def bubble_sort(A):
    """
    Time: O(n^2)
    Space: O(1)
    """
    n = len(A)
    for j in range(n):
        for i in range(n-j-1): # j elements sorted
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]

                
def selection_sort(A):
    """
    Time: O(n^2)
    Space: O(1)
    """
    n = len(A)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if A[j] < A[min_idx]:
                min_idx = j
                
        A[i], A[min_idx] = A[min_idx], A[i]

    
def insertion_sort(A):
    """
    Time: O(n^2) , best case O(n) for sorted array
    Space: O(1)
    """
    n = len(A)
    for i in range(1, n):
        key_element = A[i]
        j = i - 1 # insert from the right
        while j >= 0 and  key_element < A[j]:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key_element 

    
def merge_sort(A):
    """
    Time: O(nlogn)
    Space: not in-place
    """

    def merge(left, right):
        if not left:
            return right
        
        if not right:
            return left 

        result = []
        l = r = 0
        while len(result) < len(left) + len(right):
            if l == len(left):
                result.extend(right[r:])
                return result

            if r == len(right):
                result.extend(left[l:])
                return result

            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1

        return result

    def recursive_helper(A):
        if len(A) <= 1:
            return A

        mid = len(A)//2

        return merge(recursive_helper(A[:mid]), recursive_helper(A[mid:]))

    return recursive_helper(A)


def quick_sort(A):
    """
    Time: O(nlogn)
    Space: O(1)
    """
    def recursive_helper(left, right):
        if left >= right:
            return

        pivot = random.randint(left, right)
        A[pivot], A[right] = A[right], A[pivot] # move pivot to the right

        pivot = left
        for i in range(left, right):
            if A[i] < A[right]:
                A[pivot], A[i] = A[i], A[pivot]
                pivot += 1

        A[pivot], A[right] = A[right], A[pivot]

        recursive_helper(left, pivot)
        recursive_helper(pivot+1, right)

    l, r = 0, len(A)-1

    return recursive_helper(l, r)


if __name__ == '__main__':
    a = [random.randint(1, 100) for _ in range(10)]
    ans = sorted(a)
    print(ans)
    quick_sort(a)
    print(a)
    print(a == ans)
    

