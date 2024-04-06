# App Placar 

Para organizar os campeonatos de bairro, um gestor de comunidade solicitou o desenvolvimento de um aplicativo que receba o cadastro das equipes e registre os confrontos.

## Requisitos

* Deve haver uma página para cadastro de equipe com o nome, técnico e capitão do time
* Deve haver uma página para listar as equipes cadastradas
* Deve haver uma página para registrar os confrontos, onde deve ser selecionado duas equipes e informar o placar
* Deve haver uma página para mostrar os resultados dos confrontos.


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
