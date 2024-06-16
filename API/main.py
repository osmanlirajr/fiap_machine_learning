from fastapi import FastAPI #0.111.0
import requests #2.32.3

app = FastAPI()

@app.get('/api/producao')
def get_producao():
    return {'Produto':'Vinho de Mesa','Quantidade':'20','Tipo':'Timto'}

@app.get('/api/processamento')
def get_processamento():
    return {}

@app.get('/api/comercializacao')
def get_comercializacao():
    return {}

@app.get('/api/importacao')
def get_importacao():
    return {}

@app.get('/api/exportacao')
def get_exportacao():
    return {}
