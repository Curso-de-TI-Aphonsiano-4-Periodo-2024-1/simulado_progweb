#!\bin\python
from os import getenv
from bottle import debug, run, get, post, template, request
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

# Lista de usuários existente
lista_de_assinantes = [
    {
        "email": "admin@admin.com",
        "senha": "admin123",
    }
]

# Metodo GET no caminho /login
# Retornará o template com o form de login 
@get("/login")
def mostra_login():
    return template("login")

# Metodo POST no caminho /login
# Receberá o form de login para validação
@post("/login")
def login():
    email = request.forms.get("usuario")
    senha = request.forms.get("senha")
    
    for usuario in lista_de_assinantes:
        if (usuario["email"] == email and usuario["senha"] == senha):
            return "Encontrado"
    
    return "Inexistente"

# Execução do servidor
# Parâmetros:
# - port: porta de escuta
# - reloader: atualizar o servidor ao editar o arquivo
run(port=PORT, reloader=dev_mode)