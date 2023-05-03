def textt(user_text):
    x = list(user_text)
    new_text = ""
    for symbol in x:
        if symbol == " ":
            new_text += " "
        else:
            new_text += "*"
    return new_text

def letters(text_input, letters_user):
    start = 0
    char_index = []
    for burti in range(text_input.count(letters_user)):
        index = text_input[start:].find(letters_user)
        if index != -1:
            char_index.append(start + index)
            start += index +1
    return char_index

def return_burti(new_text, letter_user, char_index):
    list_text = list(new_text)
    for index in char_index:
        list_text[index] = letter_user
    normal_text = "".join(list_text)
    return normal_text

text = input("Ievadi tekstu: ")

star = textt(user_text=text)

while "*" in star:
    burts_user = input("Atmini burtiņu :) ")
    index_burti = letters(text, burts_user)
    star = return_burti(star, burts_user, index_burti)
    print(star)
    print("Result " + star)
    print("Uraaaa! Tu uzvarēji!")