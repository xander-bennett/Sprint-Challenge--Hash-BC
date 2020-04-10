#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # if the number of packages is less than 2
    # return None. It's impossible to get a pair of unique packages

    if len(weights) < 2:
        return None

    #across the length of the table
    #insert the index and the weight into a hash table
    for i in range(0, length):
        hash_table_insert(ht, weights[i],i)


    #with all values inserted into the hash table
    #we can look through the remaining indexes and weights of packages
    #to find a valid condition

    # with everything now inserted in the hash map
    # lets look through the remaining indexes to find a solution
    
    for(index,weight) in enumerate(weights):
        #with the limit condition defined and the known weight of the first package
        #the companion target weight is set by taking limit-weight
        companion_target = limit - weight
        #with that target weight known, we can look up that weight in the hash table at constant time!
        companion_index = hash_table_retrieve(ht,companion_target)

        #if we were able to find the value
        if companion_index is not None:
            #The documentation in the readme states that we want the largest value in the 0th index
            #this sorts based on which index is value, the initial package or the companion retreived
            #from the hash table
            return (index,companion_index) if index > companion_index else (companion_index,index)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
