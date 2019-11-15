def hh_verbose(answers):
    while True:
        answers[:] = [i for i in answers if i != 0]
        if not answers:
            return True

        answers.sort(reverse=True)
        N = answers.pop(0)
        if N > len(answers):
            return False

        for i in range(N):
            answers[i] -= 1
