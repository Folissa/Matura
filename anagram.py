# anagram to wyraz lub zdanie powstałe po przestawieniu liter innego wyrazu (zdania)

def anagram(wyraz_pierwszy, wyraz_drugi):
    litery = {}
    if len(wyraz_pierwszy) != len(wyraz_drugi):
        return False
    else:
        for i in wyraz_pierwszy:
            if i not in litery:
                litery[i] = 1
            else:
                litery[i] += 1
        for i in wyraz_drugi:
            if i in litery:
                litery[i] -= 1
        for i in litery:
            if litery[i] != 0:
                return False
        return True


print(anagram("anna", "naan"))
