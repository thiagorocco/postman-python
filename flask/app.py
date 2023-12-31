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
@app.route('/livros',methods=['GET'])
def obterLivros():
    return jsonify(livros)

# Consultar (id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id (id):
    livro_alterado = request.get_json()
    for indice, livro, in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

# Excluir

app.run(port=5000, host='localhost',debug=True)