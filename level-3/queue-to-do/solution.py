# calculates the xor value for a given range of numbers
# abuses the fact that XOR results repeat every 4 values lowering the need to loop over every number and perform the XOR operation
def calculate_xor(start, end):
    start -= 1
    xor_start = [start, 1, start + 1, 0][start % 4]
    xor_end = [end, 1, end + 1, 0][end % 4]
    return xor_start ^ xor_end

def solution(start, length):
    checksum = 0
    for i in range(length):    
        # The range starts from the current worker ID and ends at the worker ID that is i positions before the end of the line
        checksum ^= calculate_xor(start, start + length - i - 1)
        start += length
    return checksum


if __name__ == "__main__":
    print(solution(0, 3))
    print(solution(17, 4))
    print(solution(0, 1))
    print(solution(10, 5))
    print(solution(2000000000, 1))