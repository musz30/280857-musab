import string
import itertools

def getspan(s, ss):
    """Returns the start and end index (span) of substring ss in string s."""
    start = s.find(ss)
    if start == -1:
        return None
    return start, start + len(ss)

def reverseWords(s):
    """Reverses the order of words in s."""
    return ' '.join(s.split()[::-1])

def removePunctuation(s):
    """Removes all punctuation from s."""
    return s.translate(str.maketrans('', '', string.punctuation))

def countWords(s):
    """Counts the number of words in s."""
    return len(s.split())

def characterMap(s):
    """Returns a dictionary with characters of s as keys and their frequencies as values."""
    return {char: s.count(char) for char in set(s)}

def makeTitle(s):
    """Converts s to title case."""
    return s.title()

def normalizeSpaces(s):
    """Removes extra spaces, leaving only single spaces between words."""
    return ' '.join(s.split())

def transform(s):
    """Reverses the string and swaps case."""
    return s[::-1].swapcase()

def getPermutations(s):
    """Returns all permutations of the string s."""
    return [''.join(p) for p in itertools.permutations(s)]
