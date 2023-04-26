##########################################################################
# Raegan Sweeney
# CS 162
# Assignment 3 (Queues in Python)

# ---------------------------------------------------------------------- #
# STEP ONE
# enter queue list

# Input packets as a string, P=Priority, S=Standard, E=Economy
input_packets = ["S Mary", "P Dee", "P Dee", "P Dee", "E Eileen",
                 "E Mike", "E Joe", "P Dee", "E Vicky", "E George",
                 "P Dee", "P Joe", "E Sally", "P Joe", "S Pete",
                 "P Dee", "S Bill", "S Chase", "E Price", "P Dee",
                 "E Sue"]

# ---------------------------------------------------------------------- #
# STEP TWO
# make priority/standard/economy lists

priority = []
standard = []
economy = []
final_queue = []

# ---------------------------------------------------------------------- #
# STEP THREE
# make sorter

# define function


def packet_sorter():
    # confirm first letter and sort
    for x in input_packets:
        if x[0] == 'P':
            priority.append(x)
        elif x[0] == 'S':
            standard.append(x)
        elif x[0] == 'E':
            economy.append(x)
        else:
            print('your packet does not have a priority level, try again')


# call function
# packet_sorter()

# ---------------------------------------------------------------------- #
# STEP FOUR
# make packet reshuffler for final queue

# define function


def packet_reallocate():
    # first, make main loop as well as set important variables
    total_packets = len(priority) + len(standard) + len(economy)
    processed_packets = 0
    # this process adds them to final queue list and increments counter
    while processed_packets < total_packets:
        # process priority
        for i in range(3):
            if priority.__len__() > 0:
                final_queue.append(priority[0])
                priority.pop(0)
                processed_packets += 1
        # now standard
        for i in range(2):
            if standard.__len__() > 0:
                final_queue.append(standard[0])
                standard.pop(0)
                processed_packets += 1
        # now economy
        if economy.__len__() > 0:
            final_queue.append(economy[0])
            economy.pop(0)
            processed_packets += 1


# call function
# packet_reallocate()

# ---------------------------------------------------------------------- #
# STEP FIVE
# call main and print

# define function
def main():
    # call sorter
    packet_sorter()
    # call shuffler
    packet_reallocate()
    # print final queue
    print('---------------------------------')
    print('final queue:')
    print(final_queue)
    print('---------------------------------')


# call main
main()
