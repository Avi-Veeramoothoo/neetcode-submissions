class Solution:
    """
    Let m = # of words and n = # of chars in longest word
    Time complexity: O(m*n) 
    Time reason: To iterate over each word and iterate over each of its char
    Space complexity: O(m*n)
    Space reason: To store each word once in the hashmap and output list
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramList = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char)-ord('a')] += 1
            anagramList[tuple(count)].append(word)
        return list(anagramList.values())


"""
1. Why use tuple?
Here, we need to insert keys in the hashmap. Python dictionaries take only hashable and immutable keys. List is mutable, whereas tuple is immutable. So we use tuple.

2. Why use tuples and not set?
Python dictionaries take only hashable and immutable keys. Set is mutable. Moreover, it dedupes the elements, so would violate the condition of anagrams to preserve duplicate letters. Tuple is immutable.

3. Why use ord(char)-ord('a') and not ord('a') - ord(char)?
In ASCII, 'a' maps to 97, i.e. the first char. Later, chars will have greater values. So we need to do greater char value - ord('a') to get non-negative index that we can use to insert in the count array.

"""
        