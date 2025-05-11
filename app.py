from flask import Flask, redirect

app = Flask(__name__)

@app.route('/stream/<file_id>')
def stream(file_id):
    return redirect(f'https://drive.google.com/uc?export=download&id= {file_id}')

if __name__ == '__main__':
    app.run()