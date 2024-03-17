def remove_exclamation_marks(s):
    r = ""
    for c in s:
        if c is not "!":
            r += c
    return r
