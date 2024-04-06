# App Email

Para facilitar a leitura de emails de um departamento de RH, foi sugerido que os emails fossem enviados para um único local. Sendo assim, criaram uma aplicação que une os emails de diferentes servidores SMTP e disponibiliza uma lista de dicionários contendo informações como: remetente, destinatário, servidor (hotmail, gmail, bol, etc), título e conteúdo. Crie uma tela que mostre uma tabela com servidor, remetente, destinatário, título e um link para outra tela para leitura do conteúdo.

## Requisitos:

* A aplicação deve ter duas telas, uma para listar os emails e outra para leitura
* Na tela de listagem deve ter uma tabela com as colunas:
    - servidor
    - remetente
    - destinatário
    - título 
    - opção (que terá o link LER, que mudará para a página com o conteúdo) 
* Na tela de leitura deve ter o título, o conteúdo e a opção de voltar para a lista
* A primeira versão utilizará listas em memória.


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
* Modo debug
    - No modo debug (linha 24 do arquivo login.py) ativa o modo debug para mostrar mais informações no console
* Atualização automática
    - Na linha de execução (run(port=PORT, reloader=dev_mode)) é passado o parametro reloader que atualiza a aplicação sem a necessidade de para o servidor e executá-lo novamente.
