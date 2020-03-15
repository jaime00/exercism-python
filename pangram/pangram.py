import re
def is_pangram(sentence):
    letters = r"[a-z]"
    letters = re.findall(letters,sentence.lower())
    length = len(set(letters)) == 26
    return length