#  Hint:  You may not need all of these.  Remove the unused functions.
import os
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)
os.system('clear')


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __str__(self):
        return f"{{ source: {self.source}, destination: {self.destination} }}"


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * (length-1)

    # add all the tickets to the HT
    # O(n) run-time
    for ticket in tickets:
        hash_table_insert(ht, ticket.source, ticket.destination)

    # add the value of 'NONE' to route index 0
    route[0] = hash_table_retrieve(ht, 'NONE')
    # O(n) run-time
    for i in range(1, length-1):
        # use the previous route values as keys for the next route
        # and the values into route[i]
        route[i] = hash_table_retrieve(ht, route[i - 1])

    return route


# ticket_1 = Ticket("PIT", "ORD")
# ticket_2 = Ticket("XNA", "SAP")
# ticket_3 = Ticket("SFO", "BHM")
# ticket_4 = Ticket("FLG", "XNA")
# ticket_5 = Ticket("NONE", "LAX")
# ticket_6 = Ticket("LAX", "SFO")
# ticket_7 = Ticket("SAP", "SLC")
# ticket_8 = Ticket("ORD", "NONE")
# ticket_9 = Ticket("SLC", "PIT")
# ticket_10 = Ticket("BHM", "FLG")

# tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
#            ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]


# reconstruct_trip(tickets, len(tickets))
