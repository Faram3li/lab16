import collections
import matplotlib.pyplot as plt

file_path = 'textfile.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

ukrainian_alphabet = 'абвгґдежзийіклмнопрстуфхцчшщьюяєії'
text = text.lower()
letters = [char for char in text if char in ukrainian_alphabet]

letter_counts = collections.Counter(letters)

if letter_counts:
    plt.figure(figsize=(10, 6))
    plt.bar(letter_counts.keys(), letter_counts.values(), color='blue')
    plt.xlabel('Літера')
    plt.ylabel('Частота')
    plt.title('Гістограма частот українських літер')
    plt.grid(True)
    plt.show()
else:
    print("Не знайдено українських літер у тексті.")


