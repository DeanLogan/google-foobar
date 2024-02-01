
def solution(n):
    stair_cases = [0] * (n + 1)
    stair_cases[0] = 1 

    for total_bricks in range(1, n):
        for last_step_height in range(n, total_bricks - 1, -1):
            # Update the number of staircases that can be built with 'last_step_height' bricks
            # by adding the number of staircases that can be built with 'last_step_height - total_bricks' bricks
            stair_cases[last_step_height] += stair_cases[last_step_height - total_bricks]

    return stair_cases[n]

if __name__ == "__main__":
    print(solution(5))
    print(solution(200))
