# Activity Selection using Finish Time (Correct Greedy Strategy)
print("NIVASRI  | 24BAD081")
class Activity:
    def __init__(self, act_id, start, finish):
        self.id = act_id
        self.start = start
        self.finish = finish


def activity_selection(activities):
    # Sort by Finish Time
    activities.sort(key=lambda x: x.finish)

    selected = []
    last_finish = -1

    for act in activities:
        if act.start >= last_finish:
            selected.append(act)
            last_finish = act.finish

    return selected


# -------- User Input Test (5 activities, 3 overlapping) --------
activities = [
    Activity(1, 1, 4),
    Activity(2, 2, 5),
    Activity(3, 3, 6),
    Activity(4, 5, 7),
    Activity(5, 8, 9)
]

result = activity_selection(activities)

print("Selected Activity IDs:")
for act in result:
    print(act.id)

print("Total Maximum Activities:", len(result))
