from collections import Counter
import re
import os
from os import system
class Text_analizer():
    def from_clipboard(text):
        text = text.lower()
        text = re.sub(r'[^\w\s\n]', '', text)
        words_list = text.split()
        words_number = len(words_list)
        frequency = Counter(words_list)
        print(f"The number of words in the paragraph is {words_number} and the 3 most repeated words are:\n {frequency.most_common(3)}")
        pass
    def from_archive(text):
        text = text.lower()
        text = re.sub(r'[^\w\s\n]', '', text)
        words_list = text.split()
        words_number = len(words_list)
        frequency = Counter(words_list)
        print(f"The number of words in the text is {words_number} and the 3 most repeated words are:\n {frequency.most_common(3)}")
        pass

while True:
    print("##Welcome to the text analyzer##\nPress 1 for analize a paragraph:\nPress 2 for analize a text archive\nPress 0 for exit")
    option = int(input("Your Option:"))
    if option == 0:
        def clear():
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
        clear()
        break
    if option == 1:
        text = str(input("Paste your text:"))
        Text_analizer.from_clipboard(text)
    if option == 2:
        path = input("enter the file path (only a txt format supported): ") 
        f = open(path,'r') 
        w = f.read()
        f.close()
        Text_analizer.from_archive(w)
