from typing import List


class Solution:
    def findString(self, words: List[str], s: str) -> int:
        left, right = 0, len(words) - 1
        while left <= right:
            mid = left + (right - left) // 2
            print(left, mid, right)

            temp = mid  # 记录一下mid的位置，因为下面要移动mid来寻找非空串，如果查找失败需要用temp来恢复位置
            while words[mid] == '' and mid < right:  # 如果mid对应空串则向右寻找
                mid += 1
            if words[mid] == '':
                # 该情况发生在mid走到了right-1的位置，如果right仍对应空，则说明temp右侧都是空，所以将右边界进行改变
                right = temp - 1
                continue
            if words[mid] == s:  # 该情况发生在mid在右移的过程中发现了非空串，则进行正常的二分查找
                return mid
            elif s < words[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1


if __name__ == '__main__':
    handler = Solution()
    words = ["DirNnILhARNS hOYIFB", "SM ", "YSPBaovrZBS", "evMMBOf", "mCrS", "oRJfjw gwuo", "xOpSEXvfI"]
    s = "mCrS"
    handler.findString(words, s)
