from flask import Flask, redirect

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return '<a href="/sobre">sobre</a>' \
           '<br>' \
           '<a href="/experiencia">exp</a>' \
           '<br>' \
           '<a href="/formacao">formacao.</a>' \
           '<br>' \
           '<a href="/contato">contato.</a>' \

@app.route("/sobre", methods=["GET"])
def sobre():
    return 'Mateus Bezerra Ferandes do curso de Sistemas.'

@app.route("/experiencia", methods=["GET"])
def experiencia():
    return 'tecnico em secretaria escolar e tecnologo em segurança do trabalho.'

@app.route("/formacao", methods=["GET"])
def formacao():
    return 'estou fazendo uma segunda faculdade.'

@app.route("/contato", methods=["GET"])
def contato():
    return 'mateus.bezerra.fernandes08@aluno.ifce.edu.br'

if __name__ == '__main__':
    app.run(debug=True)