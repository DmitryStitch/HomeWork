class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    line = line.replace(',', '').replace('.', '').replace('=', '').replace('!', '').replace('?',
                                                                                                            '').replace(
                        ';', '').replace(':', '').replace(' - ', ' ')
                    words.extend(line.split())
                all_words[file_name] = words

        for name, words in all_words.items():
            print(f"Файл: {name}")
            print(f"Слова: {words}")
            print("-" * 20)

        return all_words

    def find(self, word):
        word_positions = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                word_positions[file_name] = words.index(word)
        return word_positions

    def count(self, word):
        word_counts = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            word_counts[file_name] = words.count(word)
        return word_counts



file1 = WordsFinder('file1.txt', 'file2.txt',
                    'file3.txt')
print(file1.get_all_words())
finder = WordsFinder('file1.txt', 'file2.txt',
                    'file3.txt')
print(finder.get_all_words())
print(finder.find('TEXT')) # 3 слово по счёту
print(finder.count('teXT'))