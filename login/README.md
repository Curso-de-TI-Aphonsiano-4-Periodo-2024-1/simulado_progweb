# App Login 

## Tela de login

Um site de notícias decidir criar uma área para assinantes para publicar notícias que somente assinantes podem ler. Para isso necessitam de uma página de login que receba o email e senha do assinante e retorne se existe este usuário na lista de assinantes. 

### Requisitos
* A tela de login deve ter na url o caminho /login
* Os campo de email deve ter o tipo email e deve ser obrigatório


## Configurações

* Configurando ambiente virtual

```
python -m venv .
```

* Ativando o ambiente virtual

```
Scripts\activate
```

* Instalando dependências

```
pip install [nome da biblioteca]
```

* Listar as dependências

```
pip list
```

* Salvando dependências instaladas

```
pip freeze > requirements.txt
```

* Instalando dependências a partir do requirements.txt

```
pip install -r requirements.txt
```

## Projeto

* Framework Bottle
* Utilizanção de variáveis de ambiente
* Rotas
    - GET /login
    - POST /login
* Modo debug
    - No modo debug (linha 24 do arquivo login.py) ativa o modo debug para mostrar mais informações no console
* Atualização automática
    - Na linha de execução (run(port=PORT, reloader=dev_mode)) é passado o parametro reloader que atualiza a aplicação sem a necessidade de para o servidor e executá-lo novamente.
