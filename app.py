from flask import Flask, render_template, request, flash, redirect
import json
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = "PALAVRA-SECRETA"


@app.route("/")
def home():
    return render_template("html/acesso.html")


@app.route("/login", methods=['POST'])
def login():
    usuario = request.form.get('nome')
    senha = request.form.get('senha')
    with open('usuarios.json') as usuarios:
        lista = json.load(usuarios)
        cont = 0
        for c in lista:
            cont += 1
            if usuario == c['nome'] and senha == c['senha']:
                return render_template("inicio.html", nomeUsuario="Seja bem vindo, " + c['nome'])
            if cont >= len(lista):
                flash('usuário inválido')
                return redirect("/")


@app.route("/cadastrar", methods=['POST'])
def cadastrar():
    user = []
    usuario = request.form.get('nomecad')
    senha = request.form.get('senhacad')
    user = [{
        "nome": usuario,
        "senha": senha
    }]
    flash('usuário cadastrado')
    with open('usuarios.json') as uriarios:
        arquivo = json.load(uriarios)
    arquivo2 = arquivo + user
    with open('usuarios.json', 'w') as arquivo:
        json.dump(arquivo2, arquivo, indent=4)
    return render_template("html/login.html", nomecadastro=usuario + " cadastrado!!")


@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

@app.route("/kids")
def kids():
    return render_template("kids.html")


@app.route("/contato")
def contato():
    return render_template("contato.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/perguntasfrequentes")
def perguntasfrequentes():
    return render_template("perguntasfrequentes.html")


if __name__ in '__main__':
    app.run(debug=True)
