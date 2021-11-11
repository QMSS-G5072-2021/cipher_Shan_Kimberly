def cipher(text, shift, encrypt=True):
    """
    One of the simplest and most widely known encryption techniques. 
    Inputs
    ----------
    a single word/ words/ the text contains symbols/ a sentence
    Outputs
    -------
    For each letter in inputs, it is replaced by a letter some fixed number of positions down the alphabet.
    Examples
    --------
    >>> example = 'Apple'
    
    >>> encrypting = cipher(example, 1, )
    >>> print(encrypting)
    Bqqmf
    
    >>> decrypting = cipher(encrypting, 1, False)
    >>> print(decrypting)
    Apple
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text