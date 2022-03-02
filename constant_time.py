"""  Constant Time -- O(1)
An algorithm is said to have a constant time when it is 
not dependent on the input data (n). No matter the size 
of the input data, the running time will always be the same. 

For example:

    if a > b:
        return True
    else:
        return False

Now, lets implement this in a function get_first which returns
the first element of a list

"""

def get_first(item):
    return item[0]

if __name__ == '__main__':
    data = [1,2,3,4,5,6,7,8,9]
    print(get_first(data))