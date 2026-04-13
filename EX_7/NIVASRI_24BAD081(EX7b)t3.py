# Strategy Counter-Proof: Duration vs Finish Time
print("NIVASRI T | 24BAD081")
class Activity:
    def __init__(self, act_id, start, finish):
        self.id = act_id
        self.start = start
        self.finish = finish

# Correct Greedy (Sort by Finish Time)
def select_by_finish(activities):
    activities.sort(key=lambda x: x.finish)
    selected = []
    last_finish = 0

    for act in activities:
        if act.start >= last_finish:
            selected.append(act)
            last_finish = act.finish

    return selected

# Wrong Strategy (Sort by Shortest Duration)
def select_by_duration(activities):
    activities.sort(key=lambda x: x.finish - x.start)
    selected = []
    last_finish = 0

    for act in activities:
        if act.start >= last_finish:
            selected.append(act)
            last_finish = act.finish

    return selected

# -------- Counter Example --------
activities = [
    Activity(1, 1, 4),
    Activity(2, 3, 5),
    Activity(3, 0, 6),
    Activity(4, 5, 7),
    Activity(5, 8, 9),
    Activity(6, 5, 9)
]

# Make copies so sorting doesn't affect both
import copy
finish_result = select_by_finish(copy.deepcopy(activities))
duration_result = select_by_duration(copy.deepcopy(activities))

print("Correct Strategy (Finish Time):")
for act in finish_result:
    print("Activity", act.id)
print("Total Selected:", len(finish_result))


print("\nWrong Strategy (Shortest Duration):")
for act in duration_result:
    print("Activity", act.id)
print("Total Selected:", len(duration_result))
