import tools_karkkainen_sanders as tks
import unittest


def longest(s):
    '''
    longest repeating substring
    '''
    sa = tks.simple_kark_sort(s)
    lcp = tks.LCP(s, sa)
    maxI, maxV = -1, -1
    for i, v in enumerate(lcp):
        if v > maxV:
            maxI, maxV = i, v
    return s[sa[maxI]:sa[maxI] + maxV]


def search(P, sStr):
    '''
    find the substring P
    '''
    sa = tks.simple_kark_sort(sStr)
    m = len(P)
    n = len(sStr)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) >> 1
        comp = cmp(P, sStr[sa[mid]:sa[mid] + m])
        if comp == -1:
            right = mid - 1
        elif comp == 1:
            left = mid
        else:
            left = right = mid
            break
    if left > right:
        return -1, -1
    while P == sStr[sa[left - 1]:sa[left - 1] + m]:
        left -= 1
    while P == sStr[sa[right + 1]:sa[right + 1] + m]:
        right += 1

    result = [sa[i] for i in range(left, right + 1)]
    result.sort()
    return result


class testUtility(unittest.TestCase):

    def test_longest(self):
        s = 'aaaabcaa'
        self.assertEquals(longest(s), 'aaa')

    def test_(self):
        s = 'aaaabcaa'
        occurance = search('aa', s)
        self.assertEquals(occurance, [0, 1, 2, 6])


if __name__ == '__main__':
    unittest.main()
