"""7. Анализ текста
# Проанализируйте текст и выведите статистику:
# - Количество слов
# - самое длинное слово
# - сколько букв a
text = "привет мир это тестовый текст для анализа текста"""

text = "привет мир это тестовый текст для анализа текста"
word_count = 0
longest_word = ""
repeated_word = ""
a_count = 0

word = ""
len_word = 0
for letter in text:
    if letter == "а":
        a_count += 1
    if letter == " ":
        word_count += 1
        if len_word < len(word):
            len_word = len(word)
            longest_word = word
        word = ""
    else:
        word += letter

print("a:", a_count)
print("words:", word_count + 1)
print("longest_word:", longest_word)


