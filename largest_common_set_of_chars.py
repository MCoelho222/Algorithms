def largest_common_charset(words: list[str]) -> str:
    """
    Find largest common set of consecutive characters.

    Parameters
    ----------
        words
            A list of strings.

    Return
    ------
        A set of the largest common consecutive characters. For example, 
        if words = ['ball', 'basketball', 'baseball'] it will return {'ball'}.
        if words = ['baseball', 'ballbase', 'baseball'] it will return {'ball', 'base'}.
    """
    smallest_word = words[0] # Start with first word. It will be replaced by the smallest word.
    size = len(smallest_word)

    # Find smallest word.
    for word in words:
        n = len(word)
        if n < size:
            size = n
            smallest_word = word

    # Iterate the smallest word with decreasing-size windows/slices.
    count = 1
    while count < size:
        print(count)
        char_set = set([]) # Sets of the largest consecutive common characters.
        for i in range(count): # count increases the range for i.
            window = smallest_word[i : i + size - count + 1] # count decreases the range of the slice.

            # Check if the window characters are in every word.
            isin_word = []
            for word in words:
                if window in word:
                    isin_word.append(True)
                else:
                    isin_word.append(False)
            
            # Add to the char set if it is in every word.
            if all(isin_word):
                char_set.add(window)
        
        # Since the window size is decreasing, once char_set is not empty,
        # the largest common consecutive set of characters have been found
        # and can be returned.
        if char_set:
            return char_set
        
        # if no char set was found, continue
        count += 1
    
    # If no char set was found, return message
    return 'There is no common set of characters among these strings.'

if __name__ == "__main__":

    words = ['baseball', 'ballbase', 'baseball']
    print(largest_common_charset(words))

