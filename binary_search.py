#!/usr/bin/env python
# coding: utf-8

# In[4]:


def binary_search(A, key, f=lambda x: x):
    """
    Iterative binary search. Returns -1 if key is not in A.
    
    Parameters
    ----------
    A : array_like
    key : comparable
    f : This function will be applied to the elements of A before comparing them with key.
    """
    l = 0
    r = len(A) - 1
    
    while (l <= r):
        mid = l + (r - l) // 2
        
        if (key < f(A[mid])):
            r = mid - 1
        elif (key > f(A[mid])):
            l = mid + 1
        else:
            return mid
    return -1


# In[75]:


def bisect_left(A, key, f=lambda x: x):
    """
    Find the left-most point where inserting key to A would keep it sorted.
    
    Parameters
    ----------
    A : array_like
    key : comparable
    f : This function will be applied to the elements of A before comparing them with key.
    
    Intuition
    ---------
    We want to find the left-most point, so we should shrink from right as long as key <= A[mid].
    Since key <= A[mid], we can't set r = mid - 1, otherwise we could skip the insertion point.
    """
    l = 0
    r = len(A)
    
    while (l < r):
        mid = l + (r - l) // 2
        
        if (key <= f(A[mid])):
            r = mid
        else:
            l = mid + 1
    return l


# In[6]:


def bisect_right(A, key, f=lambda x: x):
    """
    Find the right-most point where inserting key to A would keep it sorted.
    
    Parameters
    ----------
    A : array_like
    key : comparable
    f : This function will be applied to the elements of A before comparing them with key.
    
    Intuition
    ---------
    We want to find the right-most point, so we should shrink from left as long as key >= A[mid].
    Unlike bisect_left, we will set l = mid + 1 (instead of l = mid), because we want to find an insertion point, 
    and not find the actual element.
    
    For instance,
    >>> a = [1, 2, 3, 4]
    >>> bisect_right(a, 2)
    3
    """
    l = 0
    r = len(A)
    
    while (l < r):
        mid = l + (r - l) // 2
        
        if (key >= f(A[mid])):
            l = mid + 1
        else:
            r = mid
    return r


# In[7]:


def binary_search_left(A, key, f=lambda x: x):
    """
    Find the left-most occurence of key in A. Returns -1 if key is not in A.
    
    Parameters
    ----------
    A : array_like
    key : comparable
    f : This function will be applied to the elements of A before comparing them with key.
    """
    p = bisect_left(A, key, f)
    if (p < len(A) and f(A[p]) == key):
        return p
    return -1


# In[172]:


def binary_search_right(A, key, f=lambda x: x):
    """
    Find the right-most occurence of key in A. Returns -1 if key is not in A.
    
    Parameters
    ----------
    A : array_like
    key : comparable
    f : This function will be applied to the elements of A before comparing them with key.
    
    Intuition
    ---------
    Unlike what you'd expect, the first part of this algorithm is the counterpart of bisect_left.
    We want to find the right-most point, so we should shrink from left as long as key >= A[mid].
    We don't set l = mid + 1 because we could miss a match.
    
    Notice the initial value of r, compared to bisect_right.
    Notice the ceil operation when finding mid.
    """
    l = 0
    r = len(A) - 1
    
    while (l < r):
        mid = l - ((l - r) // 2) # equivalent to math.ceil((r - l) / 2)
        
        if (key >= f(A[mid])):
            l = mid
        else:
            r = mid - 1
            
    if (f(A[r]) == key):
        return r
    return -1

