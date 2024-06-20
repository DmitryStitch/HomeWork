def single_root_words(root_word, *other_words):
    some_words = []
    root_word = root_word.lower()
    for i in other_words:
        i = i.lower()
        if root_word in i or i in root_word:
            some_words.append(i)
    return some_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
