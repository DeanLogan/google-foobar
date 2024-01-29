def solution(s):
    passes = 0
    rights = 0  # counts the number of '>' characters

    for i in range(0, len(s)):
        if s[i] == '>':
            rights += 1
        elif s[i] == '<':
            passes += rights

    return passes * 2  # each pass results in 2 salutes


if __name__ == '__main__':
    print(solution("<<<><<"))
    print(solution("<<>><"))
    print(solution(">--<<--<<"))