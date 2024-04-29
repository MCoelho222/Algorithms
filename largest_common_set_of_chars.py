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
    smallest_word = words[0] # Will be replaced by the smallest word
    size = len(smallest_word)

    # Find smallest word
    for word in words:
        n = len(word)
        if n < size:
            size = n
            smallest_word = word

    # Iterate through the smallest word with decreasing-size windows/slices
    count = 1
    while count < size:
        print(count)
        char_set = set([]) # Set of the largest consecutive common characters

        for i in range(count):
            window = smallest_word[i : i + size - count + 1]

            # Check the presence of window chars in every word
            isin_word = []
            for word in words:
                if window in word:
                    isin_word.append(True)
                else:
                    isin_word.append(False)
            
            # If in every word, add to char set
            if all(isin_word):
                char_set.add(window)
        
        # Since it uses a decreasing-size window, once a char set is found,it can be returned
        if char_set:
            return char_set
        
        # if no char set was found, continue
        count += 1
    
    # If no char set was found
    return 'There is no common set of characters among these strings.'

if __name__ == "__main__":

    words = ['baseball', 'ballbase', 'baseball']
    print(largest_common_charset(words))

