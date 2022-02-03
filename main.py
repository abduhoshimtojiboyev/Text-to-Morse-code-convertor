import ctypes

alps = "a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 ".split()
morses = '.-     -...     -.-.     -..     .     ..-.     --.     ....     ..     .---     -.-     .-..     --     -.     ---     .--.     --.-     .-.     ...     -     ..-     ...-     .--     -..-     -.--     --..     .----     ..---     ...--     ....-     .....     -....     --...     ---..     ----.     -----'.split()
morse_dict = {alp: morse for alp, morse in zip(alps, morses)}
morse_dict[" "] = "......."
alp_dict = {morse: alp for morse, alp in zip(morses, alps)}
alp_dict["......."] = " "


while True:
    morse_or_text = input('Do you want to convert text to morse code(1) or morse code to text(0) (1/0/quit): ')

    if morse_or_text == "quit":
        break

    text = input('Please enter your text: ').lower()
    text_arr = text.split()  # it splits array by space. space length doesn't matter
    text_arr
    space = " "
    morse_code = ''
    for word in text_arr:
        word_letter = list(word)
        for letter in word_letter:
            if morse_or_text == "1":
                try:
                    morse_code = morse_code + morse_dict[letter] + " "
                except KeyError:
                    ctypes.windll.user32.MessageBoxW(0, f"Please use only alphabets and numbers in your text: {letter}", "Invalid letter")
            elif morse_or_text == "0":
                try:
                    morse_code = morse_code + alp_dict[letter] + " "
                except KeyError:
                    ctypes.windll.user32.MessageBoxW(0, f"Please use only valid symbols. this symbols doesn't exist{letter}", "Invalid symbols")
            else:
                print("Please enter valid commands")

    print(morse_code)