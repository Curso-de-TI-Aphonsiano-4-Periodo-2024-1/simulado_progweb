% rebase("layout.tpl", titulo=titulo)


<table border="1" width="100%" bgcolor="#ECECEC">
    <thead bgcolor="#D0D0D0">
        <tr>
            <th>Servidor</th>
            <th>Remetente</th>
            <th>Destinatário</th>
            <th>Título</th> 
            <th>Opção</th>
        </tr>
    </thead>
    <tbody>
        % for i,email in enumerate(emails):
        <tr>
            <td>{{email["servidor"]}}</td>
            <td>{{email["remetente"]}}</td>
            <td>{{email["destinatario"]}}</td>
            <td>{{email["titulo"]}}</td>
            <td> <a href="/ler/{{i}}">LER</a> </td>
        </tr>
        % end
    </tbody>
</table>