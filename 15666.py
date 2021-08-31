from itertools import combinations_with_replacement

N, M = map(int, input().split())

list(
    map(
        print,
        sorted(
            map(
                " ".join,
                set(combinations_with_replacement(
                    sorted(
                        input().split(),
                        key=int
                    )
                    , M
                ))
            )
            , key=lambda x: list(map(int, x.split()))
        )
    )
)
