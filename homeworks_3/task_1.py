# Реализуйте функцию count_letter, которая принимает список слов и некоторую букву 
# и возвращает количество слов в списке, в которых эта буква встречается хотя бы один раз.

# Например, для списка ['python', 'c++', 'c', 'scala', 'java'] и буквы c ваша функция должна вернуть число 3.
# Подсказки

#     Используйте конструкцию for word in ... для итерации по списку.
#     Используйте переменную для хранения промежуточного результата подсчета.
#     Используйте конструкцию letter in word для проверки наличия буквы в слове.

texts = ['python', 'c++', 'c+', 'scala', 'java']
letter = 'c'

def count_letter(texts, letter):
    counter = 0
    for word in texts:
        if letter in word:
            counter += 1
            return counter

print(count_letter((texts), letter))
