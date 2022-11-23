def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = set("aeiou")

    str = list(s)
    i = 0
    x = len(s) - 1

    while i < x:
        if str[i].lower() not in vowels:
            i += 1
        elif str[x].lower() not in vowels:
            x -= 1
        else:
            str[i], str[x] = str[x], str[i]
            i += 1
            x -= 1

    return "".join(str)