import matplotlib.pyplot as plt
from collections import Counter
import re

with open('Aufgabe1.txt', 'r', encoding='utf-8') as file:
    text = file.read()

filtered_text = re.findall(r'[a-ü]', text.lower())

letter_counts = Counter(filtered_text).most_common()

letters, counts = zip(*sorted(letter_counts))

plt.bar(letters, counts)

plt.show()