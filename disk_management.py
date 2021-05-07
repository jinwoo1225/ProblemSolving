def solution(jobs):
    answer = 0
    time = 0
    n = len(jobs)
    jobs = sorted(jobs, key=lambda x: (x[0], x[1]), reverse=True)
    queue = []
    finished = 0
    while finished != n:
        while jobs:
            request, duration = jobs.pop()
            if request <= time:
                queue.append([request, duration])
            else:
                jobs.append([request, duration])
                break
        # print(queue)
        if not queue:
            time += 1

        queue.sort(key=lambda x: x[1], reverse=True)
        print(queue)
        if queue:
            request, duration = queue.pop()
            time += duration
            answer += time - request
            finished += 1

    # print(time)
    return int(answer / n)


# print(solution([[0, 3], [1, 9], [2, 6]]))
# print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))
# print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))
print(solution([[0, 10], [4, 10], [15, 2], [5, 11]]))
# print(solution([[1, 3], [1, 9],[1, 7],[1, 8],[1, 2], [2, 6], [2, 4]]))
