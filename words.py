# def print_upper_words (words):
#     """Accepts a list of words and prints them uppercased"""
#     for word in words:
#         print(f"{word.upper()}")

# print_upper_words(["hello", "tutu", "Hulabaloo"])

# def print_e_words (words):
#     """Accepts a list of words and prints words that start with the letter e, uppercased"""
#     for word in words:
#         if (word.upper().startswith('E')):
#             print(f"{word.upper()}")
        
# print_e_words(["everyone", "tutu", "excite"])

def print_upper_words (words, must_start_with):
    """Accepts a list of words and a set of letters,
     prints words that start with any of the letters in the set, uppercased"""
    for word in words:
        for letter in must_start_with:
            if (word.upper().startswith(f"{letter.upper()}")):
                print(f"{word.upper()}")
        
print_upper_words(["everyone", "tutu", "excite", "baby", "bazooka"], must_start_with={"t", "b"})