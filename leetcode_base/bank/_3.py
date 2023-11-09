from collections import Counter
from typing import List


class _1st:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        cnt = Counter()
        left = 0
        for right, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans,right-left+1)
        return ans

class _2nd:
    print("")


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        print("")
