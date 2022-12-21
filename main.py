from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/index')
def homepage():
    tabela1 = pd.read_csv('Tabela tutoriais.csv')
    tutorial = tabela1['titulo']
    resposta1 = {tutorial}
    return jsonify(resposta1)

app.run(host = 'localhost')

#tabela2 = pd.read_csv('Tabela passo.csv')
#passo = tabela2['descriçao']
#resposta2 = {'Passo a passo': passo}