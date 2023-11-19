from flask import Flask, render_template
from PyPDF2 import PdfReader

app = Flask(__name__)

@app.route('/')
def index():
    reader = PdfReader('one.pdf')
    page = reader.pages[0]
    text = page.extract_text()

    return render_template('index.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)
