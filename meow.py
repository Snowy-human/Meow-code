alphabet_to_meow = {
    "A": "mew mrow mrp ",
    "B": "mrow mew mep mow mrp ",
    "C": "merw mow meow mop mrp ",
    "D": "moew mep mew mrp ",
    "E": "mow mrp ",
    "F": "mep mow mrow mew mrp ",
    "G": "moep mrew mow mrp ",
    "H": "mew mop mow mep mrp ",
    "I": "mep mop mrp ",
    "J": "mow mrow merw meaw mrp ",
    "K": "meop mew meop mrp ",
    "L": "mew mrew mrw mep mrp ",
    "M": "meow merp mrp ",
    "N": "meow mew mrp ",
    "O": "merp mrow mrew mrp ",
    "P": "mep merp meow mep mrp ",
    "Q": "merp merp mop meow mrp ",
    "R": "mew merw mop mrp ",
    "S": "mep mew mep mrp ",
    "T": "morw mrp ",
    "U": "mew mow mrop mrp ",
    "V": "mrw mew mop mrep mrp ",
    "W": "mow mrow mrew mrp ",
    "X": "mrop mrw mow meop mrp ",
    "Y": "mrow mep mrop meow mrp ",
    "Z": "meow meow mrw mrw mrp ",
    "0": "meow meow meow meow meow mrp ",
    "1": "mew meow meow meow meow mrp ",
    "2": "mew mew meow meow meow mrp ",
    "3": "mew mew mew meow meow mrp ",
    "4": "mew mew mew mew meow mrp ",
    "5": "mew mew mew mew mew mrp ",
    "6": "meow mew mew mew mew mrp ",
    "7": "meow meow mew mew mew mrp ",
    "8": "meow meow meow mew mew mrp ",
    "9": "meow meow meow meow mew mrp ",
    "Ä": "mew meow mew meow mrp ",
    "Ü": "mew mew meow meow mrp ",
    "ß": "mew mew mew meow meow mew mew mrp ",
    "À": "mew meow meow mew meow mrp ",
    "È": "mew meow mew mew meow mrp",
    "É": "mew mew meow mew mew mrp ",
    ".": "mew meow mew meow mew meow mrp ",
    ",": "meow meow mew mew meow meow mrp ",
    ":": "meow meow meow mew mew mew mrp ",
    ";": "meow mew meow mew meow mew mrp ",
    "?": "meow mew meow meow mew mew mrp ",
    "-": "meow mew mew mew mew meow mrp ",
    "_": "mew mew meow meow mew meow mrp ",
    "(": "meow mew meow meow mew mrp ",
    ")": "meow mew meow meow mew meow mrp ",
    "'": "mew meow meow meow meow mew mrp ",
    "=": "meow mew mew mew meow mrp ",
    "+": "mew meow mew meow mew mrp ",
    "/": "meow mew mew meow mew mrp ",
    "@": "mew meow meow mew meow mew mrp ",
    "Ñ": "meow meow mew meow meow mrp ",
    " ": " *purr* ",
    "" : ""
}


meow_to_meow = {v: k for k, v in alphabet_to_meow.items()}

def remove_unusable_characters(uncorrected_string):
    return "".join(char for char in uncorrected_string.upper() if char in alphabet_to_meow)

def encode(decoded):
    decoded = remove_unusable_characters(decoded)
    words = decoded.split(" ")

    meow_string = []
    for word in words:
        letters = list(word)
        meow_word = [alphabet_to_meow[letter] for letter in letters]
        meow_string.append(":3 ".join(meow_word))

    return " ".join(meow_string)

def decode(encoded):
    # just here just in case it breaks without it lol :3 mrp
    character_string = []

    words = encoded.split(" ")
    for word in words:
        letters = word.split("/")
        character_word = [meow_to_alphabet.get(letter, "?") for letter in letters]
        character_string.append("".join(character_word))

    return " ".join(character_string)