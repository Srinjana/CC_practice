# Henry is extremely keen on history and every one of the ages of his family. He does a ton of exploration and understands that he has plummeted from the incomparable Amaya line. After a ton of looking through old records and the most recent records of the general public, he can discover all the parent-kid connections in his family right from the extraordinary ruler Ming of the tradition to himself.

# These connections are given in the structure a direct exhibit where emperor is at the main position and his kids are at pos (2i + 1) and (2i + 2)

# This is the pattern followed throughout.

# Henry needs to sort out every one of the kin of individual X from the information.

# Write a program for Henry to figure out all the siblings of person X from the data.
# Return the sorted list of all of Henry’s siblings.

# If no sibling return {-1}

# input 1: N, the length of the array
# input2: An array representing the ancestral tree
# input 3 : X, the person whose siblings are sought.
# output – return the array of all siblings in increasingly sorted order.
# Example 1 :

# input 1 : 5
# input 2 : {1,2,3,4,5}
# input 3 : 1
# output : {-1}
# Explanation : x is the root of the tree and has no siblings

# Example 2 :
# input 1 : 6
# input 2 : {1,2,3,4,5,6}
# input 3 : 5
# output : {4,6}
# Explanation : {2,3 } are the children of {1}.
# {4,5,6 } are the children of {2,3}, thus the siblings of x= 5 are {4,6}


def identify_siblings(tree_array, x):
    
    tree_len = len(tree_array)
    index = tree_array.index(x)
    level = 0
    start_index = level
    number_of_nodes = 0

    while start_index < tree_len:
    	end_index = pow(2, level) + start_index

    	if x in tree_array[start_index:end_index]:
    		break

    	level += 1
    	start_index = (2 * start_index) + 1
    final_array = tree_array[start_index:end_index]
    final_array.remove(x)

    return final_array if final_array else [-1]