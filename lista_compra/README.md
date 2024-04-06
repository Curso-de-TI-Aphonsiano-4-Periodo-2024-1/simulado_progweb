# Lista de Compras 

## História

Para melhor organizar a lista de compra de uma família, surgiu a necessidade de ter uma aplicativo web que permita os integrantes da família adicionar itens, para quando forem realizar as compras semanal ou mensal terem todos os itens faltantes à mão.

## Requisitos

* No cadastro do item deve ser informado a descrição, a quantidade e o solicitante do item (pai, mãe, filhos) 
* A lista e o cadastro deve estar no início do aplicativo
* Deve ter a opção de limpar a lista
* A lista deve estar em formato de tabela


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
