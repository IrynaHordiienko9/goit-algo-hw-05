import timeit
import matplotlib.pyplot as plt


def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return 0
    skip = {c: m for c in set(text)}
    for i in range(m - 1):
        skip[pattern[i]] = m - i - 1
    i = m - 1
    while i < n:
        k = 0
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1
        if k == m:
            return i - m + 1
        i += skip.get(text[i], m)
    return -1


def kmp(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return 0

    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
  
    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                return i - m
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def rabin_karp(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return 0
    base = 256
    mod = 101
    pat_hash = txt_hash = 0
    for i in range(m):
        pat_hash = (base * pat_hash + ord(pattern[i])) % mod
        txt_hash = (base * txt_hash + ord(text[i])) % mod
    h = pow(base, m - 1, mod)
    for i in range(n - m + 1):
        if pat_hash == txt_hash:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            txt_hash = (base * (txt_hash - ord(text[i]) * h) + ord(text[i + m])) % mod
            txt_hash = (txt_hash + mod) % mod
    return -1


algorithms = {
    "Boyer-Moore": boyer_moore,
    "KMP": kmp,
    "Rabin-Karp": rabin_karp
}


with open('article 1 for task 3.txt', encoding='utf-8') as f:
    text1 = f.read()
with open('article 2 for task 3.txt', encoding='utf-8') as f:
    text2 = f.read()


patterns = {
    "real text 1": "код - це всього лише інструмент досягнення мети",  
    "real text 2": "три основні сутності",
    "fictional": "з Днем Святого Миколая" 
}


for i, text in enumerate([text1, text2], 1):
    print(f"\nArticle {i}:")
    for kind, pattern in patterns.items():
        print(f"  '{kind}' substring:")
        for name, algo in algorithms.items():
            t = timeit.timeit(lambda: algo(text, pattern), number=100)
            print(f"    {name:<15}: {t:.5f} s")


algorithms = ["Boyer-Moore", "KMP", "Rabin-Karp"]
labels = []
bm_times, kmp_times, rk_times = [], [], []

for i, text in enumerate([text1, text2], 1):
    for kind, pattern in patterns.items():
        labels.append(f"Article {i}\n{kind}")
        bm_times.append(timeit.timeit(lambda: boyer_moore(text, pattern), number=100))
        kmp_times.append(timeit.timeit(lambda: kmp(text, pattern), number=100))
        rk_times.append(timeit.timeit(lambda: rabin_karp(text, pattern), number=100))

# Побудова простого графіка
x = range(len(labels))
plt.figure(figsize=(10, 5))
plt.bar(x, bm_times, width=0.25, label="Boyer-Moore")
plt.bar([i + 0.25 for i in x], kmp_times, width=0.25, label="KMP")
plt.bar([i + 0.5 for i in x], rk_times, width=0.25, label="Rabin-Karp")
plt.xticks([i + 0.25 for i in x], labels, rotation=30, ha='right')
plt.ylabel('Час (секунди, 100 запусків)')
plt.title('Порівняння швидкості алгоритмів пошуку підрядка')
plt.legend()
plt.tight_layout()
plt.show()
