#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
        Time: Best case: O(1); worst case: O(n)
        Space: Best Case: O(1) when pattern not found, O(n) when the whole string matches
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    return find_all_indexes(text, pattern, False) != None

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    Time: Best case: O(1); worst case: O(n)
    Space: Best Case: O(1) when pattern not found, O(n) when the whole string matches
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    return find_all_indexes(text, pattern, False)
    


def find_all_indexes(text, pattern, flag=True):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    Time: Best case: O(1); worst case: O(n)
    Space: Best Case: O(1) when pattern not found, O(n) when the whole string matches
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # return [i for i in range(len(text) - len(pattern) + 1) if not any(i for j in range(len(pattern)) if text[i + j] != pattern[j])]

    if flag:
        if pattern == '':
            return [i for i in range(len(text))]
        else:
            arr = []
    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                break
        else:
            if flag:
                arr.append(i)
            else:
                return i
    if flag:
        return arr
    else:
        return None
    
    
    


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
