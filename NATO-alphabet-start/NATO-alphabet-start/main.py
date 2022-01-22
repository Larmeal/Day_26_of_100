# ทำ phonetic

import code
import pandas
nato = pandas.read_csv("C:/Users/acer/Desktop/Coding/Python Code/100 Days of Code The Complete Python Pro Bootcamp for 2022/Day_26/NATO-alphabet-start/NATO-alphabet-start/nato_phonetic_alphabet.csv")

data = {row.letter:row.code for (index, row) in nato.iterrows()}

word = input("Enter a word: ").upper()

quote_word = [data[letter]for letter in word]
print(quote_word)