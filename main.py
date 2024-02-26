"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x-1)
        rb = foo(x-2)
        return ra + rb

def longest_run(mylist, key):
    longest_run = 0
    current_run = 0
    for i in range(len(mylist)):
        if mylist[i] == key:
            current_run += 1
        else:
            if current_run > longest_run:
                longest_run = current_run
            current_run = 0   
          
    if current_run > longest_run:
        longest_run = current_run
      
    return longest_run



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
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
  if len(mylist) == 0:
      return Result(0, 0, 0, True)

  result_if_key_present = longest_run_recursive(mylist[1:], key)

  left_size = result_if_key_present.left_size + (mylist[0] == key)
  right_size = result_if_key_present.right_size + (mylist[0] != key)
  longest_size = max(left_size, right_size)
  is_entire_range = left_size + right_size == len(mylist)

  return Result(left_size, right_size, longest_size, is_entire_range)


