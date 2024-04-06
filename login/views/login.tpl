<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <!-- Elemento fieldset para organizar o formulário em uma caixa com título -->
    <fieldset>
        <!-- Elemento legend é o título do fieldset -->
        <legend>Login</legend>
        <!-- Formulário com methodo post com action (local de envio) /login -->
        <form method="post" action="/login">
            <label>Usuário:</label><br/>
            <input type="email" name="usuario" placeholder="Informe o email" autofocus required /><br/>
            <br/>
            <label>Senha:</label><br/>
            <input type="password" name="senha" placeholder="Informe a senha" required /><br/>
            <br/>
            <button type="submit">Entrar</button>
        </form>
    </fieldset>
</body>
</html>