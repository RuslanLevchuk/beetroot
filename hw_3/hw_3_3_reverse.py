morse_dict = {
    "А": "·–", "Б": "–···", "В": "·––", "Г": "––·", "Д": "–··", "Е": "·", "Є": "·", "Ж": "···–", "З": "––··", "И": "··",
    "І": "··", "Й": "·–––", "К": "–·–", "Л": "·–··", "М": "––", "Н": "–·", "О": "–––", "П": "·––·", "Р": "·–·", "С": "···",
    "Т": "–", "У": "··–", "Ф": "··–·", "Х": "····", "Ц": "–·–·", "Ч": "–––·", "Ш": "––––", "Щ": "––·–", "Ы": "–·––",
    "Ь": "–··–", "Ъ": "–··–", "Э": "··–··", "Ю": "··––", "Я": "·–·–",
}

message = []
reverse_morse_dict = {}
#converting reversed dict
for letter, code in morse_dict.items():
    reverse_morse_dict[code] = letter

while True:

    input_message = input("Введіть фразу для переведення з коду морзе: ").split()
    for code in input_message:
        message.append(reverse_morse_dict[code])

    print(''.join(message))
    message = []