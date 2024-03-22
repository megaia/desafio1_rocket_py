# Desafio 1 - Introdução ao Python
# Desafio: desenvolver uma agenda para salvar, editar, deletar e marcar um contato como favorito. 
# - A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
# - Deve ser possível adicionar um contato: OK
#     - O contato pode ter os dados:
#     - Nome
#     - Telefone
#     - Email
#     - Favorito (está opção é para poder marcar um contato como favorito)
# - Deve ser possível visualizar a lista de contatos cadastrados: OK
# - Deve ser possível editar um contato: OK
# - Deve ser possível marcar/desmarcar um contato como favorito: OK
# - Deve ser possível ver uma lista de contatos favoritos
# - Deve ser possível apagar um contato: OK

# adicionar um contato
def adicionar_contato(contatos, nome_contato="", telefone_contato="", email_contato=""):
    contato = {"contato": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome_contato} foi adicionado à sua agenda com sucesso!")
    return

# ver lista de contatos
def ver_contatos(contatos):
    print("\nLista de Contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "★ " if contato["favorito"] else " "
        nome_contato = contato["contato"]
        print(f"{indice}. [{status}] {nome_contato} - {telefone_contato} - {email_contato}")
        return

# editar um contato
def editar_contato(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["contato"] = novo_nome_contato
        contatos[indice_contato_ajustado]["telefone"] = novo_telefone_contato
        contatos[indice_contato_ajustado]["email"] = novo_email_contato
        print(f"Contato {indice_contato} atualizado para {novo_nome_contato}")
    else:
        print("Indice de Contato Inválido!")
    return

# marcar um contato como favorito
def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado]["favorito"] = True
    print(f"Contato {indice_contato} marcado como favorito!")
    return

# desmarcar um contato como favorito
def desfavoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado]["favorito"] = False
    print(f"Contato {indice_contato} desmarcado como favorito!")
    return

# ver lista só com os favoritos
def ver_contatos_fav(contatos):
    favoritos = [contato for contato in contatos if contato["favorito"]]
    if favoritos:
        print("\nLista de Contatos Favoritos:")
        for indice, contato in enumerate(contatos, start=1):
            print(f"{indice}. {nome_contato} - {telefone_contato} - {email_contato}")
    else:
        print("Nenhum Contato favorito encontrado, adicione um e tente novamente")
        return

# apagar contato
def deletar_contato(contatos, indice_contato):
    try:
        indice_contato = int(indice_contato)
        if 1 <= indice_contato <= len(contatos):
            contato_deletado = contatos.pop(indice_contato - 1)
            print(f"Contato {contato_deletado} deletado!")
        else:
            print("Indice de Contato inválido!")
    except ValueError:
        print("Por favor, digite um número válido")


contatos = []

while True:
    print("\nMenu da Agenda de Contatos:")
    print("1. Adicionar Contato")
    print("2. Ver Contatos Adicionados")
    print("3. Editar Contato")
    print("4. Marcar como Contato Favorito")
    print("5. Ver Contatos Favoritos")
    print("6. Desmarcar como Contato Favorito")
    print("7. Deletar um Contato Adicionado")
    print("8. Sair")


    escolha = input("Digite sua escolha:")
    
    if escolha == "1":
        nome_contato = input("Digite o NOME do Contato que deseja adcionar:")
        telefone_contato = input("Digite o TELEFONE do Contato que deseja adcionar:")
        email_contato = input("Digite o EMAIL do Contato que deseja adcionar:")
        adicionar_contato(contatos, nome_contato)
    
    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do Contato que deseja editar:")
        novo_nome_contato = input("Digite o novo NOME do Contato:")
        novo_telefone_contato = input("Digite o novo TELEFONE do Contato:")
        novo_email_contato = input("Digite o novo EMAIL do Contato:")
        editar_contato(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato)     
    
    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do Contato que você deseja favoritar:")
        favoritar_contato(contatos, indice_contato) 

    elif escolha == "5":
        ver_contatos_fav(contatos)    
    
    elif escolha == "6":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do Contato que você deseja desfavoritar:")
        desfavoritar_contato(contatos, indice_contato)

    elif escolha == "7":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do Contato que você deseja deletar:")
        deletar_contato(contatos, indice_contato)

    elif escolha == "8":
        break