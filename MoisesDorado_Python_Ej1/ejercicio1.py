MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
    'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': ' '
}

REVERSE_MORSE_CODE = {value: key for key, value in MORSE_CODE.items()}

def morse_converter(input_text):
    if all(c in ".- " for c in input_text):
        words = input_text.split("  ")
        return ''.join(''.join(REVERSE_MORSE_CODE[char] for char in word.split()) + ' ' for word in words).strip()
    else:
        return '  '.join(' '.join(MORSE_CODE[char.upper()] for char in word) for word in input_text.split())


print(morse_converter("Hola Mundo"))
print(morse_converter(".... --- .-.. .-  -- ..- -. -.. ---"))