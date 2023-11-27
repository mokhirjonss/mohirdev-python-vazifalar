#26 "SO'Z TOPISH" O'YINI

# Kompyuter so'z o'ylaydi, biz topamiz.

# 1-QISM: TANISHUV

# 2-QISM: KOD

import random
from uzwords import words

def get_word():
    word = random.choice(words)
    while "-" in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def display(user_letters, word):
    display_letter = ""
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += "_"
    return display_letter

def play():
    word = get_word()
    # So'zdagi harflar
    word_letters = set(word)
    # Foydalanuvchi kiritgan harflar
    user_letters = ''
    print(f"Мен {len(word)} хонали суз уйладим. Топа оласизми?")
    # print(word)
    while len(word_letters) > 0:
        print(display(user_letters, word))
        if len(user_letters) > 0:
            print(f"Шу вақтгача киритган ҳарфларингиз: {user_letters}")

        letter = input("Харф киритинг: ").upper()
        if letter in user_letters:
            print("Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг.")
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} харфи тугри.")
        else:
            print("Бундай харф йук.")
        user_letters += letter
    print(f"Табриклайман! {word} сўзини {len(user_letters)} та уринишда топдингиз.")