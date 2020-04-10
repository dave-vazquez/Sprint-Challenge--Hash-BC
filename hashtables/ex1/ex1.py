#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)

    # O(n) --> loop through the 'length' of 'weights' at linear run-time
    for i in range(0, length):
        # insert into the new table
        # the weights will be the key, since the indices are what we
        # care about storing
        # O(1) --> insert for each iteration
        hash_table_insert(ht, weights[i], i)

    # O(n) --> loop through the 'length' of 'weights' at linear run-time
    for i in range(0, length):

        # grab the weight using the index
        current_weight = weights[i]

        # the trial weight is just the difference of
        # the limit and the current weight
        # we're trying to add the current weight
        # to a weight they may or may not exist in the
        # list of weights to see if we hit the limit
        trial_weight = limit-current_weight

        # grab the index of the trial_weight
        # (if it exists)
        trial_weight_index = hash_table_retrieve(
            ht, trial_weight)

        # if the trial weight index was returned from the HT
        if trial_weight_index is not None:
            print(f"{current_weight}, {trial_weight}")
            # check if the summation of the current_weight and the trial_weight
            # add up to the limit
            if current_weight + trial_weight == limit:
                # if they're equal, be sure to order the trial_weight_index first
                if current_weight == trial_weight:
                    return (trial_weight_index, i)
                # else, order the weight indices by largest to smallest
                # and return
                elif i >= trial_weight_index:
                    return (i, trial_weight_index)
                else:
                    return (trial_weight_index, i)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
