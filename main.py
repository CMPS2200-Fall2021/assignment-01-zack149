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
    
   
def longest_run_recursive(mylist, key):
    # Base Case
    if (len(mylist) == 1):
        if (mylist[0]==key):
            return 1
        else:
            return 0

    # Recursive Case
    mid = len(mylist)//2 # This is as far as I got, though not for lack of trying

    # This is roughly what the recursion would look like, I could not figure out the last two parameters:
    #res = Result(longest_run_recursive(mylist[:mid],key), longest_run_recursive(mylist[mid:],key), None, 0)

    # This is how it would end:
    #return res.longest_size


## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12) == 3


