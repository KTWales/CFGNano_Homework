"""
Create required phrase.
----------------------

You are given a string of available characters and
a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate the required
word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique
    characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you
    are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters
    including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""

def generate_phrase(characters, phrase):
    c_length = len(characters)
    p_length = len(phrase)

    sorted_characters_ = sorted(characters)
    sorted_characters = "".join(sorted_characters_)
    sorted_phrase_ = sorted(phrase)
    sorted_phrase = "".join(sorted_phrase_)

    # Check if the length of the string and phrase are the same:
    if c_length < p_length:
        return False
    else:
        for x in range(0,c_length,1):
            if x in range(0, p_length, 1):
                return sorted_characters == sorted_phrase
            else:
                return False

print(generate_phrase("cbacba","aabbcc"))
print(generate_phrase("abgba","bbaagx"))