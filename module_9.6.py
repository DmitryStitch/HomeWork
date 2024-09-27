def all_variants(text):

    for i in range(len(text)):
        for j in range(i, len(text)):
            yield text[i:j + 1]

a = all_variants("abc")
sorted_variants = sorted(a, key=len)
for i in sorted_variants:
    print(i)

