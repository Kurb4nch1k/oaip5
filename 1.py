def groundhog_day(texts):
    for i, (prev, curr) in enumerate(zip(texts, texts[1:]), 1):
        differences = [j for j, (x, y) in enumerate(zip(prev, curr)) if x != y]
        if len(differences) > 2:
            return (i,) + tuple(differences)
    return (0, 0)

a = ["Groundhog Festival in Punxsutawney.",
     "Groundhog Festival in Punksutawney.",
     "Groundhog Festivel in Punxsutowney."]
print(groundhog_day(a))

