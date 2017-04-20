import string

def czy_pangram(fraza):
    """Sprawdza czy fraza jest pangramem"""
    #funkcja zawiera litery od a do z male
    for litera in string.ascii_lowercase:
        if litera not in str(fraza).lower():
            return False
    return True

print(czy_pangram("abcDE"))
