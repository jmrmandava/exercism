def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    #x = sorted(scores, reverse=True)

    return sorted(scores, reverse=True)[0:3]
