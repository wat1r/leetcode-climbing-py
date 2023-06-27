from typing import List


class _1st:
    def minSum(arr, n):
        f = [0] * n
        if n == 1:
            return arr[0]
        if n == 2:
            return min(arr[0], arr[1])
        if n == 3:
            return min(arr[0], arr[1], arr[2])
        if n == 4:
            return min(arr[0], arr[1], arr[2], arr[3])
        f[0] = arr[0]
        f[1] = arr[1]
        f[2] = arr[2]
        f[3] = arr[3]
        for i in range(4, n):
            f[i] = arr[i] + min(f[i - 1], f[i - 2], f[i - 3], f[i - 4])
        return min(f[n - 1], f[n - 2], f[n - 3], f[n - 4])


class _2nd:
    print("")


class _3rd:
    print("")


class _4th:
    print("")

if __name__ == '__main__':
    handler = _1st
    arr = [1, 2, 3, 3, 4, 5, 6, 1]
    n = len(arr)
    print(handler.minSum(arr, n))
