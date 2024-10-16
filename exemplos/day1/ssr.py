#BASE DO SERVER SIDE RENDER

# Carregar os Dados= Ler os dados

dados = [{"nome": "Bruno", "Cidade": "Viana"},
         {"nome": "Matheus", "Cidade": "Carazinho"}
]

# Processar: Tratar, validar, aplicar uma condicional em cima destes dados - Definir templates e processar

template = """\
<html>
<body>
    <ul>
        <li> Nome: {dados[nome]} </li>
        <li> Cidade: {dados[Cidade]} </li>
    </ul>
</body>
</html>
"""

# Renderizar

for item in dados:
    print(template.format(dados=item))