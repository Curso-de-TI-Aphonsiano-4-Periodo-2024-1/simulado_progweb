% rebase("layout.tpl", title="Times")

<table border="1" width="100%">
    <thead>
        <tr>
            <th> # </th>
            <th> Time </th>
            <th> Técnico </th>
            <th> Capitão </th>
        </tr>
    </thead>
    <tbody>
        % if len(times) == 0:
        <tr>
            <td colspan="4" align="center"> Nenhum time cadastrado! </td>
        </tr>
        % else:
            % for i, time in enumerate(times):
            <tr>
                <td>{{i + 1}}</td>
                <td>{{time["nome"]}}</td>
                <td>{{time["tecnico"]}}</td>
                <td>{{time["capitao"]}}</td>
            </tr>
            % end
        % end
    </tbody>
</table>