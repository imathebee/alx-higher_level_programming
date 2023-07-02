#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    result = ""
    prev_char = ""

    for char in text:
        if char in punctuation:
            result += char + "\n\n"
        else:
            result += char
        prev_char = char

    print(result.strip())
