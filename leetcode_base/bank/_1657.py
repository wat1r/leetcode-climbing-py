from collections import Counter


class _1st:
    def closeStrings(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return set(s) == set(t) and \
               Counter(Counter(s).values()) == Counter(Counter(t).values())


class _2nd:
    def closeStrings(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cs, ct = Counter(s), Counter(t)
        return cs.keys() == ct.keys() and Counter(cs.values()) == Counter(ct.values())


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        word1 = "abc"
        word2 = "bca"
        handler.closeStrings(word1, word2)
