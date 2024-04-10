from flask import Flask, request
import utils
import sys

CHARS_TO_MORSE_CODE_MAPPING = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

app = Flask(__name__)

@app.route('/')
def get_my_ip():
    ip_address = request.remote_addr
    morse_code = to_morse_code(ip_address)
    return morse_code

# function to encode plain English text to morse code
def to_morse_code(text):
    morse_code = ''
    for char in text:
        if char == ' ':
            morse_code += ' '
        else:
            morse_code += CHARS_TO_MORSE_CODE_MAPPING[char.upper()] + ' '
    return morse_code

if __name__ == '__main__':
    args = utils.parse_args()
    if not args.port:
        print("ERROR: Please enter app port with --port flag")
        sys.exit(1)
    else:
        app.run(host='0.0.0.0', debug=True, port=args.port)