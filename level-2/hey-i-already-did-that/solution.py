def solution(n, b):
    k = len(n)
    # seen is used to record the IDs that have been generated and when 
    # the IDs were first seen, this means that it is possible to 
    # detect when a value has been seen and calc the cycle count
    seen = {}
    while n not in seen:
        seen[n] = len(seen)
        x = ''.join(sorted(n))
        y = x[::-1]
        z =  int(y, b) - int(x, b)
        n = str(to_base(z,b))
        while len(n) < k:
            n = '0' + n
    return len(seen) - seen[n] # return the length of the ending cycle

# convert a number m to the given base b
def to_base(n, b):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, b)
        nums.append(str(r))
    return ''.join(reversed(nums))

if __name__ == '__main__':
    print(solution('1211', 10))
    print(solution('210022', 3))