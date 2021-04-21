def solution(genres, plays):
    answer = []
    rank = {}
    for genre, play, i in zip(genres, plays, [x for x in range(len(genres))]):
        try:
            rank[genre]
            rank[genre].append((play, i))
            rank[genre].sort(reverse=True, key=lambda x: (x[0], -x[1]))
        except KeyError:
            rank[genre] = [(play, i)]
    sorted_key = sorted(rank, key=lambda x: x[0], reverse=True)
    sum_of_rank = []
    for key in sorted_key:
        sum_of_rank.append([key, sum(plays for plays, index in rank[key])])

    sum_of_rank.sort(key=lambda total : total[1], reverse=True)
    # print(sum_of_rank)
    for key, total in sum_of_rank:
        for song, i in rank[key][:2 if len(rank[key]) >= 2 else 1]:
            answer.append(i)

    return answer


print(solution(["classic", "k_pop", "k_pop", "classic", "classic", "pop"], [500, 600, 700, 150, 800, 2500]))
