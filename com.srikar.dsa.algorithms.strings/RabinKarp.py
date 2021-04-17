def stringMatching(str, subStr):
    if str is None or subStr is None or len(str) < len(subStr):
        return -1

    if len(str) == len(subStr) and str == subStr:
        return 0

    kBase = 26
    kMod = 997
    strHash = 0
    subStrHash = 0
    powerS = 0

    for index in range(len(subStr)):
        if index > 0:
            powerS = powerS * kBase % kMod
        else:
            powerS = 1
        strHash = (strHash * kBase + ord(str[index])) % kMod
        subStrHash = (subStrHash * kBase + ord(subStr[index])) % kMod

    for index in range(len(subStr), len(str)):
        if strHash == subStrHash and str[index - len(subStr): index] == subStr:
            return index - len(subStr)

        strHash -= (ord(str[index - len(subStr)]) * powerS) % kMod
        if strHash < 0:
            strHash += kMod

        strHash = (strHash * kBase + ord(str[index])) % kMod

    if strHash == subStrHash and str[len(str) - len(subStr): len(str)] == subStr:
        return len(str) - len(subStr)

    return -1


print(stringMatching("CBD", "ABCBDA")) #-1
print(stringMatching("ABCBDA", "CBD")) #2
print(stringMatching("ABCBDA", "ABCBDA")) #0
print(stringMatching("ABCBDA", "ABB")) #0
print(stringMatching("ABCBDA", "BDA")) #3
print(stringMatching("ABCBDA", "B")) #3
print(stringMatching("ABCBDA", "DA")) #3
print(stringMatching("BAAAKA", "AA")) #3
