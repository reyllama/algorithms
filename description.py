def goodVsEvil(good, evil):
    import numpy as np
    good_score = np.dot(np.array([1, 2, 3, 3, 4, 10]), np.array([int(i) for i in good.split(' ')]))
    evil_score = np.dot(np.array([1,2,2,2,3,5,10]), np.array([int(i) for i in evil.split(' ')]))
    if good_score > evil_score:
        return "Battle Result: Good triumphs over Evil"
    elif good_score < evil_score:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"
