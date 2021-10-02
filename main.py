"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if (x<=1):
        return x
    else:
        return foo(x-1) + foo(x-2)

def longest_run(mylist, key):
    """
    Sequential Implementation
    """
    curRun = 0
    maxRun = 0

    for e in mylist:
        if (e==key):
            curRun += 1
        elif (maxRun<curRun):
            maxRun = curRun
            curRun = 0
        else:
            curRun = 0
    return maxRun


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))


def combine(mylist, mid, l_size, r_size, key):
    """
    Helper function to combine results in O(1) time.
    """
    if (mylist[mid] != key):
        return max(l_size, r_size)
    elif (len(mylist) == 2): # Avoids out-of-bounds errors from next step
        if (mylist[0] == mylist[1] == key):
            return 2
        else:
            return 1
    else:
        if ((mylist[mid-1] != key) and (mylist[mid+1] != key)):
            return max(l_size, r_size, 1)
        elif (mylist[mid-1] == mylist[mid+1] == key):
            return 3
        elif (mylist[mid-1] == key):
            if (mylist[mid-l_size] == mylist[mid-l_size+1] == key):
                return l_size + 1
            else:
                return max(l_size, r_size, 2)
        else:
            if (mylist[mid+r_size] == mylist[mid+r_size-1] == key):
                return r_size + 1
            else:
                return max(l_size, r_size, 2)


def longest_run_recursive(mylist, key):
    
    res = Result(None, None, None, None)

    # Base Case
    if (len(mylist) == 1):
        res.left_size = None
        res.right_size = None
        res.longest_size = res.is_entire_range = (mylist[0] == key)
        return (int(mylist[0] == key))

    # Recursive Case
    mid = len(mylist)//2
    res.left_size = longest_run_recursive(mylist[:mid], key)
    res.right_size = longest_run_recursive(mylist[mid:], key)
    res.is_entire_range = ((res.left_size + res.right_size) == len(mylist))
    if (res.is_entire_range):
        res.longest_size = len(mylist)
    else:
        res.longest_size = combine(mylist, mid, res.left_size, res.right_size, key)

    return res.longest_size


## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run_recursive([0], 1) == 0
    assert longest_run_recursive([3,1,3], 3) == 1
    assert longest_run_recursive([5,5,5,5], 5) == 4

"""
def main():
    test_longest_run()
    return

main()
"""
