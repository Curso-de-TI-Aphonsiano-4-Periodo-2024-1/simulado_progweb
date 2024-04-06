#!\bin\python
#-*- encoding=utf-8 -*-

from os import getenv
from bottle import debug, run, get, template, abort
from dotenv import load_dotenv
from json import load

# Carregando o arquivo .env para as variáveis de 
# ambiente da sessão.
load_dotenv()

# Obtendo a variável EMAIL_PORT da variável de
# ambiente que foi carregado no .env 
PORT = getenv("EMAIL_PORT", 8080)

# Obtendo a variável EMAIL_AMBIENTE da variável de
# ambiente que foi carregado no .env 
AMBIENTE = getenv("EMAIL_AMBIENTE", "PROD")

# Verificando se o ambiente é DEV ou PROD
# DEV = desenvolvimento
# PROD = produção
dev_mode = AMBIENTE == "DEV"

# Ativar modo debug
debug(dev_mode)


def carregar_arquivo_email():
    arquivo = open("emails.json")
    obj = load(arquivo)
    return obj


# Metodo GET no caminho /login
# Retornará o template com o form de login 
@get("/")
def mostra_lista():
    emails = carregar_arquivo_email()
    return template("lista", emails=emails, titulo="Emails")


@get("/ler/<index:int>")
def mostra_email(index):
    emails = carregar_arquivo_email()

    if not str(index).isnumeric():
        return abort(400, "Bad Request")

    if (int(index) > len(emails) - 1) or (int(index) < 0):
        return abort(404, "Not Found")
    
    email = emails[int(index)]
    return template("leitor", email=email, titulo=email["titulo"])


# Execução do servidor
# Parâmetros:
# - port: porta de escuta
# - reloader: atualizar o servidor ao editar o arquivo
run(port=PORT, reloader=dev_mode)