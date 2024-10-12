#!/usr/bin/python3

"""demo of code that checks to see if any lock can be unlocked
"""


def canUnlockAll(boxes):
    """ Method that determines if all boxes can be opened """

    for key in range(1, len(boxes)):
        # create loop to iterate through all the boxes

        flag = False  # variable that checks state of the lock

        for box in range(len(boxes)):
            # for each box in the loop check if the key opens it
            if key in boxes[box] and box != key:
                flag = True
                break
        if not flag:
            return False

    return True
