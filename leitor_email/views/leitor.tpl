% rebase("layout.tpl", titulo=titulo)

<a href="/"> Voltar </a>

<hr />

<dl>
    <dt>Remetente:</dt>
    <dd>{{email["remetente"]}}</dd>
    <dt>Destinatário:</dt>
    <dd>{{email["destinatario"]}}</dd>
    <dt>Email:</dt>
    <dd>{{email["conteudo"]}}</dd>
</dl>