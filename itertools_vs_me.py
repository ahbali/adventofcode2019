import datetime
from itertools import permutations


def phase_generator(iterable):
    sequence_set = set()
    for i in iterable:
        sequence_set.add(i)

    temp_set = set()
    for phase_one in sequence_set:
        temp_set.add(phase_one)
        for phase_two in sequence_set.difference(temp_set):
            temp_set.add(phase_two)
            for phase_three in sequence_set.difference(temp_set):
                temp_set.add(phase_three)
                for phase_four in sequence_set.difference(temp_set):
                    temp_set.add(phase_four)
                    for phase_five in sequence_set.difference(temp_set):
                        sequence = (phase_one, phase_two, phase_three,
                                    phase_four, phase_five)
                        yield sequence
                        # temp_set.discard(phase_five)
                    temp_set.discard(phase_four)
                temp_set.discard(phase_three)
            temp_set.discard(phase_two)
        temp_set.discard(phase_one)


a1 = datetime.datetime.now()

sequence = permutations(range(5, 10))
count1 = 0
for i in sequence:
    count1 += 1

a2 = datetime.datetime.now()

sequence = phase_generator(range(5, 10))
count2 = 0
for i in sequence:
    count2 += 1

a3 = datetime.datetime.now()

exp1 = (a2 - a1).total_seconds()
exp2 = (a3 - a2).total_seconds()
print("itertools time for ", count1, " items = ", exp1)
print("my algo time for ", count2, " items = ", exp2)

"""Final Verdict: itertools wins"""