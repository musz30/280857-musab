import strops

def main():
    s = input("Enter a string: ")
    ss = input("Enter a substring: ")

    print(f"Span of '{ss}' in '{s}':", strops.getspan(s, ss))
    print(f"Reversed words: {strops.reverseWords(s)}")
    print(f"Without punctuation: {strops.removePunctuation(s)}")
    print(f"Word count: {strops.countWords(s)}")
    print(f"Character frequency: {strops.characterMap(s)}")
    print(f"Title case: {strops.makeTitle(s)}")
    print(f"Normalized spaces: {strops.normalizeSpaces(s)}")
    print(f"Transformed string: {strops.transform(s)}")
    print(f"Permutations: {strops.getPermutations(s)}")

if __name__ == "__main__":
    main()
