import sys

# Morse code mapping
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
    ' ': '/'
}

def encode_morse(text):
    """Convert text to Morse code."""
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <text to encode>")
        return
    
    input_text = " ".join(sys.argv[1:])
    morse_code = encode_morse(input_text)
    print(morse_code)

if __name__ == "__main__":
    main()
