#!\bin\python
# -*- coding: utf-8 -*-

from os import getenv
from bottle import debug, run, get, post, template, request, static_file, redirect
from dotenv import load_dotenv

# Carregando o arquivo .env para as variáveis de 
# ambiente da sessão.
load_dotenv()

# Obtendo a variável LOGIN_PORT da variável de
# ambiente que foi carregado no .env 
PORT = getenv("LOGIN_PORT", 8080)

# Obtendo a variável LOGIN_AMBIENTE da variável de
# ambiente que foi carregado no .env 
AMBIENTE = getenv("LOGIN_AMBIENTE", "PROD")

# Verificando se o ambiente é DEV ou PROD
# DEV = desenvolvimento
# PROD = produção
dev_mode = AMBIENTE == "DEV"

# Ativar modo debug
debug(dev_mode)

# Lista de times
times = [
    {
        "nome":"Flamengo",
        "tecnico":"Tite",
        "capitao":"Arascaeta",
    },
    {
        "nome":"Barcelona",
        "tecnico":"Xavi",
        "capitao":"Sergio Roberto",
    }
]

# Lista de confrontos
confrontos = [
    {
        "time1":"Flamengo",
        "gols1": 2,
        "time2": "Barcelona",
        "gols2": 1,
    },
]

# Metodo GET no caminho /
# Retornará o template index 
@get("/")
def index():
    return template("index")

# Metodo GET para arquivos na pasta public
# retornará arquivos estáticos como: imagens, videos, etc
@get("/public/<filename>")
def obter_arquivo_static(filename):
    return static_file(filename, root="public/")

# Metodo GET no caminho /lista/times
# Retornará o template times com a lista de 
# times cadastrados. 
@get("/lista/times")
def listar_times():
    return template("times", times=times)

# Metodo GET no caminho /lista/confrontos
# Retornará o template confrontos com a lista de 
# confrontos cadastrados. 
@get("/lista/confrontos")
def lista_confrontos():
    return template("confrontos", confrontos=confrontos)

# Metodo GET no caminho /cadastro/time
# Retornará o formulário para cadastrar
# times
@get("/cadastro/time")
def lista_confrontos():
    return template("cadastro_time")

# Metodo GET no caminho /cadastro/confronto
# Retornará o formulário para cadastrar
# confronto
@get("/cadastro/confronto")
def lista_confrontos():
    return template("cadastro_confronto", times=times)

# Metodo POST no caminho /cadastrar/time
# Receberá o form de cadastro de time
@post("/cadastrar/time")
def cadastrar_time():
    time = {
        "nome": request.forms.get("nome"),
        "tecnico": request.forms.get("tecnico"),
        "capitao": request.forms.get("capitao"),
    }
    times.append(time)
    redirect("/lista/times")

# Metodo POST no caminho /cadastrar/time
# Receberá o form de cadastro de time
@post("/cadastrar/confronto")
def cadastrar_time():
    confronto = {
        "time1": request.forms.get("time1"),
        "gols1": request.forms.get("gols1"),
        "time2": request.forms.get("time2"),
        "gols2": request.forms.get("gols2"),
    }
    print(confronto)
    confrontos.append(confronto)
    redirect("/lista/confrontos")

# Execução do servidor
# Parâmetros:
# - port: porta de escuta
# - reloader: atualizar o servidor ao editar o arquivo
run(port=PORT, reloader=dev_mode)
