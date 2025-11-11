import sqlite3

# Conecta (ou cria) o banco de dados
conexao = sqlite3.connect("torcida.db")
cursor = conexao.cursor()

# Cria a tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS torcedores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    clube TEXT NOT NULL
)
""")

# Funções principais
def cadastrar_torcedor():
    nome = input("Digite o nome da pessoa: ")
    clube = input("Digite o clube que ela torce: ")
    cursor.execute("INSERT INTO torcedores (nome, clube) VALUES (?, ?)", (nome, clube))
    conexao.commit()
    print(f"✅ {nome} cadastrado como torcedor do {clube}!\n")

def listar_torcedores():
    print("\n=== Lista de Torcedores ===")
    cursor.execute("SELECT id, nome, clube FROM torcedores")
    dados = cursor.fetchall()
    if not dados:
        print("Nenhum torcedor cadastrado ainda.\n")
    else:
        for id_, nome, clube in dados:
            print(f"{id_}. {nome} → {clube}")
        print()

def buscar_por_clube():
    clube = input("Digite o nome do clube: ")
    cursor.execute("SELECT nome FROM torcedores WHERE clube = ?", (clube,))
    torcedores = cursor.fetchall()
    if torcedores:
        print(f"\nTorcedores do {clube}:")
        for t in torcedores:
            print("-", t[0])
    else:
        print(f"Nenhum torcedor do {clube} cadastrado.\n")

# Menu principal
while True:
    print("=== Sistema de Torcida ===")
    print("1 - Cadastrar torcedor")
    print("2 - Listar torcedores")
    print("3 - Buscar por clube")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_torcedor()
    elif opcao == "2":
        listar_torcedores()
    elif opcao == "3":
        buscar_por_clube()
    elif opcao == "4":
        print("Saindo... 👋")
        break
    else:
        print("Opção inválida, tente novamente.\n")

# Fecha a conexão ao sair
conexao.close()
