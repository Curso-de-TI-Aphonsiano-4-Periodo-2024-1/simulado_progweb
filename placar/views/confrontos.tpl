% rebase("layout.tpl", title="Confrontos")

<table border="1" width="100%">
    <thead>
        <tr>
            <th> Time A </th>
            <th> Gols A </th>
            <th> Gols B </th>
            <th> Time B </th>
        </tr>
    </thead>
    <tbody>
        % if len(confrontos) == 0:
        <tr>
            <td colspan="4" align="center"> Nenhum confronto realizado! </td>
        </tr>
        % else:
            % for confronto in confrontos:
            <tr>
                <td align="center" width="40%">{{ confronto["time1"] }}</td>
                <td align="center">{{ confronto["gols1"] }}</td>
                <td align="center">{{ confronto["gols2"] }}</td>
                <td align="center" width="40%">{{ confronto["time2"] }}</td>
            </tr>
            % end
        % end
    </tbody>
</table>