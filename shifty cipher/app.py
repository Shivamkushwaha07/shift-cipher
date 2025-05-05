from flask import Flask, render_template, request

app = Flask(__name__)

def shifty_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        elif char.isdigit():
            result += str((int(char) + shift) % 10)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    hashed_output = None
    original_input = None
    if request.method == 'POST':
        original_input = request.form['input_string']
        shift_value = int(request.form['shift_value'])
        hashed = shifty_cipher(original_input, shift_value)
        hashed_output = hashed.replace('-', '')  # Remove hyphens
    return render_template('index.html', hashed_output=hashed_output, original_input=original_input)

if __name__ == '__main__':
    app.run(debug=True)
