def shortcut( s ):
    return "".join([char for char in s if char not in "aeiou"])


//using translate

def shortcut( s ):
    return s.translate(None,'aeiou')

