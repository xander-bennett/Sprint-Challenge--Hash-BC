#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    #first, we need to insert all of the tickets into the hash table

    for ticket in tickets:
        #within the hash table, we are inserting the source and destinations of each ticket
        hash_table_insert(hashtable, ticket.source,ticket.destination)

    #the first flight is the one where the source is None
    #we could also count it the city we are currently in as the day starts
    #but lets ignore that for now :)

    city = hash_table_retrieve(hashtable, "NONE")

    #walking across the route list
    for i in range(0,len(route)-1):
        #retrieve the city value and add it to the next element in the route list
        route[i] = city
        #once added, retrieve the next city where it is the origin
        city = hash_table_retrieve(hashtable, city)
        #this city will be added to the next part of the route at the top of the loop
    


    #COME BACK HERE
    #always adds a "None" at the end, for now this gets around teh solution
    #but i need to think through how to do this better to remove the None value
    return route[:-1]

    pass