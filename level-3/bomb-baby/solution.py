def solution(x, y):
    M = int(x)
    F = int(y)
    cycles = 0

    while True:
        if M == 1:
            return str(cycles + F - 1)
        elif F == 1:
            return str(cycles + M - 1)
        elif M <= 0 or F <= 0 or M == F:
            return "impossible"
        elif M > F:
            cycles += M // F
            M %= F
        else:
            cycles += F // M
            F %= M

if __name__ == "__main__":
    print(solution('4','7'))
    print(solution('2','1'))