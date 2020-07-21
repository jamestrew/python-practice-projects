scores = {(0, 0): None, (0, 1): 2, (0, 2): 2, (0, 3): None, (0, 4): 7, (0, 5): 7, (0, 6): 7, (0, 7): 7, (1, 0): None, (1, 1): 2, (1, 2): 2, (1, 3): 7, (1, 4): 7, (1, 5): None, (1, 6): 7, (1, 7): None, (2, 0): 3, (2, 1): 2, (2, 2): 2, (2, 3): None, (2, 4): None, (2, 5): None, (2, 6): None, (2, 7): None, (3, 0): 3, (3, 1): 2, (3, 2): 2, (3, 3): None, (3, 4): 3, (3, 5): 2, (3, 6): 9, (3, 7): 9, (4, 0): 3, (4, 1): None, (4, 2): 3, (4, 3): 3, (4, 4): 3, (4, 5): 2, (4, 6): 9, (4, 7): None, (5, 0): 4, (5, 1): 3, (5, 2): 3, (5, 3): 3, (5, 4): None, (5, 5): 9, (5, 6): 9, (5, 7): None, (6, 0): 4, (6, 1): 4, (6, 2): 3, (6, 3): 3, (6, 4): None, (6, 5): 9, (6, 6): 9, (6, 7): None, (7, 0): 4, (7, 1): 2, (7, 2): 2, (7, 3): None, (7, 4): None, (7, 5): 9, (7, 6): 9, (7, 7): None}

scores = [coord: score for coord, score in scores.items() if score is not None}
print(scores)
highscore = max(scores.values())
coord_list = list(scores.keys())
scores_list = list(scores.values())
print(coord_list[scores_list.index(9)])
