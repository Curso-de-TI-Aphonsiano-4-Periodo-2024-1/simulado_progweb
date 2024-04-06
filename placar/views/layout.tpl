<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title or 'No title'}}</title>
</head>
<body>
    <h1> {{title or 'No title'}} </h1>
    
    <hr />

    <nav>
        <a href="/">
            <button> Início</button>
        </a>
        
        <a href="/lista/times">
            <button> Listar Times </button>
        </a>
        
        <a href="/cadastro/time">
            <button> Cadastrar Time </button>
        </a>

        <a href="/lista/confrontos">
            <button> Listar Confrontos </button>
        </a>

        <a href="/cadastro/confronto">
            <button> Cadastrar Confronto </button>
        </a>
    </nav>

    <hr />

    <div>
        {{!base}}
    </div>
    <footer>
        <hr/>
        <p>
            <center>App Placar &reg; 2024</center>
        </p>
    </footer>
</body>
</html>