from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor' : 'JRR Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry Poter e a pedra filosofal',
        'autor' : 'JK Howling'
    },
    {
        'id': 3,
        'titulo': 'Hábitos Atômicos',
        'autor' : 'James Clear',
    },
]

# Consultar (todos)
@app.route('/livros')
def obterLivros():
    return jsonify(livros)
# Consultar (id)
# Editar
# Excluir

app.run(port=5000, host='localhost',debug=True)