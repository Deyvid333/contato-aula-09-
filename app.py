import sqlite3

# def criar_tabela():

def conexao_banco():
    conexao = sqlite3.connect("contatos.db")
    cursor = conexao.cursor()
    sql = '''
    create table if not exists contatos (
        id integer primary key autoincrement,
        nome text not null,
        telefone text not null,
        email text not null
    )
    '''
    cursor.execute(sql)
    conexao.commit()
    return conexao

def adicionar_contato(nome, telefone, email):
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = '''
        insert into contatos (nome, telefone, email)
        values (?, ?, ?);'''
    cursor.execute(sql, (nome, telefone, email))
    conexao.commit()
    conexao.close()


def listar_contatos():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = "select * from contatos"
    cursor.execute(sql)
    contatos = cursor.fetchall()
    if len(contatos) == 0:
        print("Nenhum contato encontrado.")
    else:
        print("### LISTA DE CONTATOS ###")
        print("{:<5} {:<20} {:<15} {:<30}".format("ID", "NOME", "TELEFONE", "EMAIL"))
        print("-" * 70)
        for contato in contatos:
            print("{:<5} {:<20} {:<15} {:<30}".format(contato[0], contato[1], contato[2], contato[3]))

def buscar_contato():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    nome = input("Digite o nome do contato que deseja buscar: ")
    sql = "select * from contatos where nome like ?"
    cursor.execute(sql, ('%' + nome + '%',))
    contatos = cursor.fetchall()
    if len(contatos) == 0:
        print("Nenhum contato encontrado com esse nome.")
    else:
        print("### RESULTADO DA BUSCA ###")
        print("{:<5} {:<20} {:<15} {:<30}".format("ID", "NOME", "TELEFONE", "EMAIL"))
        print("-" * 70)
        for contato in contatos:
            print("{:<5} {:<20} {:<15} {:<30}".format(contato[0], contato[1], contato[2], contato[3]))

def atualizar_contato():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    id_contato = input("Digite o ID do contato que deseja atualizar: ")
    sql = "select * from contatos where id = ?"
    cursor.execute(sql, (id_contato,))
    contato = cursor.fetchone()
    if contato is None:
        print("Contato não encontrado.")
    else:
        print("### DADOS ATUAIS DO CONTATO ###")
        print("{:<5} {:<20} {:<15} {:<30}".format("ID", "NOME", "TELEFONE", "EMAIL"))
        print("-" * 70)
        print("{:<5} {:<20} {:<15} {:<30}".format(contato[0], contato[1], contato[2], contato[3]))
        print("Digite os novos dados do contato (deixe em branco para manter o valor atual):")
        novo_nome = input("Novo nome: ")
        novo_telefone = input("Novo telefone: ")
        novo_email = input("Novo email: ")
        if novo_nome == "":
            novo_nome = contato[1]
        if novo_telefone == "":
            novo_telefone = contato[2]
        if novo_email == "":
            novo_email = contato[3]
        sql = "update contatos set nome = ?, telefone = ?, email = ? where id = ?"
        cursor.execute(sql, (novo_nome, novo_telefone, novo_email, id_contato))
        conexao.commit()
        print("Contato atualizado com sucesso!")

def deletar_contato():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    id_contato = input("Digite o ID do contato que deseja deletar: ")
    sql = "select * from contatos where id = ?"
    cursor.execute(sql, (id_contato,))
    contato = cursor.fetchone()
    if contato is None:
        print("Contato não encontrado.")
    else:
        print("### DADOS DO CONTATO ###")
        print("{:<5} {:<20} {:<15} {:<30}".format("ID", "NOME", "TELEFONE", "EMAIL"))
        print("-" * 70)
        print("{:<5} {:<20} {:<15} {:<30}".format(contato[0], contato[1], contato[2], contato[3]))
        confirmacao = input("Tem certeza que deseja deletar este contato? (s/n): ")
        if confirmacao.lower() == "s":
            sql = "delete from contatos where id = ?"
            cursor.execute(sql, (id_contato,))
            conexao.commit()
            print("Contato deletado com sucesso!")
        else:
            print("Operação cancelada.")

def menu():
    while True:
        print("### CONTATOS ###")
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Buscar contato por nome")
        print("4 - Atualizar contato")
        print("5 - Deletar contato")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")
            adicionar_contato(nome, telefone, email)
            print("Contato adicionado com sucesso!")

        elif escolha == "2":
            listar_contatos()


        elif escolha == "3":
            buscar_contato()


        elif escolha == "4":
            atualizar_contato()


        elif escolha == "5":
            deletar_contato()


        elif escolha == "0":
            print("Saindo do programa...")
            break

menu()