# (function: remove special characters)
def remove_special_characters(text):
    special_characters = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    for character in special_characters:
        text = text.replace(character, "")
    return text