s1 = "state"
s2 = "taste"

for i in range(len(s1)):
    for j in range(len(s2)):
        if (s1[i] == s2[j]):
            print("They are anagram")
            break
