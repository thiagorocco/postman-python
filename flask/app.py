from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor' : 'JRR Tolkien'
    }
    {
        'id': 2,
        'título': 'Harry Poter e a pedra filosofal',
        'autor' : 'JK Howling'
    }
    {
        'id': 3,
        'título': 'James Clear',
        'autor' : 'Hábitos Atômicos'
    }
]