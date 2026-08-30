# Python program for above approach
def search(pat, txt):
    M = len(pat)
    N = len(txt)
    for i in range(N-M):
        for j in range(M):
            k = j+1
            if(txt[i+j] != pat[j]):
                break
        if(k == M):
            print("Pattern found at index ", i)

txt = "AABAACAADAABAAABAA"
pat = "AABA"
search(pat, txt)
