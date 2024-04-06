% rebase("layout.tpl", title="Cadastrar Confronto")

<br />
<br />
<form method="post" action="/cadastrar/confronto">
    <table width="100%">
        <tr>
            <td align="center">Time A</td>
            <td align="center" width="20%">Gols A</td>
            <td align="center" width="20%">Gols B</td>
            <td align="center">Time B</td>
        </tr>
        <tr>
            <td align="center">
                <select name="time1" required autofocus>
                    <option value=""></option>
                    % for time in times:
                    <option value='{{time["nome"]}}''>{{time["nome"]}}</option>
                    % end
                </select>
            </td>
            <td align="center">
                <input type="number" name="gols1" min="0" max="99" required>
            </td>
            <td align="center">
                <input type="number" name="gols2" min="0" max="99" required>
            </td>
            <td align="center">
                <select name="time2" required autofocus>
                    <option value=""></option>
                    % for time in times:
                    <option value='{{time["nome"]}}''>{{time["nome"]}}</option>
                    % end
                </select>
            </td>
        </tr>
    </table>
    <br />
    <br />
    <center>
        <button type="submit">Cadastrar</button>
    </center>
    <br />
    <br />
</form>