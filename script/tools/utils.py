from sys import stdin


def get_answer(criteria):
    answer = ""
    if type(criteria) is int:
        while len(answer) < criteria:
            answer = stdin.readline().strip()
    elif type(criteria) is list or type(criteria) is tuple or type(criteria) is dict:
        while answer not in criteria:
            answer = stdin.readline().strip()
    return answer
