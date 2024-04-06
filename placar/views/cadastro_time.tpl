% rebase("layout.tpl", title="Cadastrar Time")

<br />
<br />
<form method="post" action="/cadastrar/time">
    <label>Nome do time:</label>
    <br />
    <input type="text" name="nome" placeholder="Nome do time" required autofocus/>
    <br />
    <br />
    <label>Técnico:</label>
    <br />
    <input type="text" name="tecnico" placeholder="Nome do técnico" required/>
    <br />
    <br />
    <label>Capitão:</label>
    <br />
    <input type="text" name="capitao" placeholder="Nome do capitão" required/>
    <br />
    <br />
    <button type="submit"> Cadastrar </button>
</form>
<br />
<br />
