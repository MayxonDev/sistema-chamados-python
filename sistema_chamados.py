# ============================================================
#   SISTEMA DE CHAMADOS DE SUPORTE
#   Projeto didático para aprendizado de Python
# ============================================================

# -----------------------------------------------------------
# LISTA GLOBAL DE CHAMADOS
# Funciona como nosso "banco de dados" temporário.
# Cada chamado será um dicionário (dict) dentro desta lista.
# -----------------------------------------------------------
chamados = []

# -----------------------------------------------------------
# CONTADOR DE IDs
# Variável que garante que cada chamado tenha um número único.
# -----------------------------------------------------------
proximo_id = 1


# ===========================================================
# FUNÇÃO: gerar_id()
# Responsabilidade: retorna um ID único e incrementa o contador
# para o próximo chamado.
# ===========================================================
def gerar_id():
    global proximo_id          # Avisa ao Python que vamos modificar a variável global
    id_atual = proximo_id      # Salva o ID atual para retornar
    proximo_id += 1            # Incrementa o contador (+1) para o próximo chamado
    return id_atual


# ===========================================================
# FUNÇÃO: abrir_chamado()
# Responsabilidade: coleta os dados do usuário via input()
# e adiciona um novo chamado à lista global.
# ===========================================================
def abrir_chamado():
    print("\n" + "=" * 40)
    print("        ABRIR NOVO CHAMADO")
    print("=" * 40)

    # --- Coleta o nome do usuário ---
    nome = input("Nome do usuário: ").strip()  # .strip() remove espaços acidentais nas bordas

    # --- Coleta o tipo de problema com validação ---
    print("\nTipos de problema disponíveis:")
    print("  1 - Hardware")
    print("  2 - Software")
    print("  3 - Rede")

    tipos = {"1": "Hardware", "2": "Software", "3": "Rede"}  # Dicionário de opções válidas

    while True:  # Loop que repete até o usuário digitar uma opção válida
        opcao_tipo = input("Escolha o tipo (1, 2 ou 3): ").strip()
        if opcao_tipo in tipos:
            tipo = tipos[opcao_tipo]  # Converte "1" → "Hardware", por exemplo
            break
        else:
            print("⚠  Opção inválida. Tente novamente.")

    # --- Coleta a descrição do problema ---
    descricao = input("Descreva o problema: ").strip()

    # --- Monta o dicionário do chamado ---
    # Um dicionário (dict) armazena dados em pares chave: valor
    novo_chamado = {
        "id":        gerar_id(),   # ID único gerado automaticamente
        "usuario":   nome,
        "tipo":      tipo,
        "descricao": descricao,
        "status":    "Aberto"      # Todo chamado começa com status "Aberto"
    }

    # --- Adiciona o chamado à lista global ---
    chamados.append(novo_chamado)  # .append() insere um item no final da lista

    print(f"\n✅ Chamado #{novo_chamado['id']} aberto com sucesso!")


# ===========================================================
# FUNÇÃO: listar_chamados()
# Responsabilidade: exibe todos os chamados cadastrados
# de forma organizada. Se não houver chamados, avisa o usuário.
# ===========================================================
def listar_chamados():
    print("\n" + "=" * 40)
    print("        LISTA DE CHAMADOS")
    print("=" * 40)

    # Verifica se a lista está vazia
    if not chamados:  # Em Python, uma lista vazia é considerada "False"
        print("Nenhum chamado cadastrado ainda.")
        return  # Encerra a função antecipadamente

    # Percorre cada chamado na lista usando um laço for
    for chamado in chamados:
        print(f"\n🎫 Chamado #{chamado['id']}")
        print(f"   Usuário  : {chamado['usuario']}")
        print(f"   Tipo     : {chamado['tipo']}")
        print(f"   Descrição: {chamado['descricao']}")
        print(f"   Status   : {chamado['status']}")
        print("   " + "-" * 30)


# ===========================================================
# FUNÇÃO: atualizar_status()
# Responsabilidade: permite alterar o status de um chamado
# existente. Busca o chamado pelo ID informado pelo usuário.
# ===========================================================
def atualizar_status():
    print("\n" + "=" * 40)
    print("      ATUALIZAR STATUS DO CHAMADO")
    print("=" * 40)

    # Verifica se há chamados para atualizar
    if not chamados:
        print("Nenhum chamado cadastrado ainda.")
        return

    # --- Solicita o ID do chamado ---
    try:
        # int() converte texto para número inteiro
        # Se o usuário digitar algo que não é número, cai no "except"
        id_buscado = int(input("Digite o ID do chamado: ").strip())
    except ValueError:
        print("⚠  ID inválido. Digite apenas números.")
        return

    # --- Busca o chamado na lista ---
    chamado_encontrado = None  # Começa como None (nenhum chamado encontrado)

    for chamado in chamados:                # Percorre cada chamado
        if chamado["id"] == id_buscado:     # Compara o ID
            chamado_encontrado = chamado    # Guarda a referência ao chamado
            break                           # Para o loop ao encontrar

    # Se nenhum chamado foi encontrado:
    if chamado_encontrado is None:
        print(f"⚠  Chamado #{id_buscado} não encontrado.")
        return

    # --- Exibe o chamado encontrado ---
    print(f"\nChamado encontrado:")
    print(f"  Usuário: {chamado_encontrado['usuario']}")
    print(f"  Status atual: {chamado_encontrado['status']}")

    # --- Mostra as opções de novo status ---
    print("\nNovos status disponíveis:")
    print("  1 - Aberto")
    print("  2 - Em andamento")
    print("  3 - Resolvido")

    status_opcoes = {"1": "Aberto", "2": "Em andamento", "3": "Resolvido"}

    while True:
        opcao_status = input("Escolha o novo status (1, 2 ou 3): ").strip()
        if opcao_status in status_opcoes:
            novo_status = status_opcoes[opcao_status]
            break
        else:
            print("⚠  Opção inválida. Tente novamente.")

    # --- Atualiza o status diretamente no dicionário ---
    # Como "chamado_encontrado" é uma referência ao item da lista,
    # alterar aqui altera também na lista original (chamados[])
    chamado_encontrado["status"] = novo_status

    print(f"\n✅ Status do chamado #{id_buscado} atualizado para: {novo_status}")


# ===========================================================
# FUNÇÃO: exibir_menu()
# Responsabilidade: exibe as opções do menu principal
# e retorna a escolha do usuário.
# ===========================================================
def exibir_menu():
    print("\n" + "=" * 40)
    print("    SISTEMA DE CHAMADOS DE SUPORTE")
    print("=" * 40)
    print("  1 - Abrir chamado")
    print("  2 - Listar chamados")
    print("  3 - Atualizar status do chamado")
    print("  4 - Sair")
    print("=" * 40)
    return input("Escolha uma opção: ").strip()


# ===========================================================
# FUNÇÃO PRINCIPAL: main()
# Responsabilidade: controla o fluxo do programa.
# É o "maestro" que chama as outras funções conforme
# a opção escolhida pelo usuário no menu.
# ===========================================================
def main():
    print("\nBem-vindo ao Sistema de Chamados de Suporte! 🖥")

    while True:  # Loop principal — o programa fica rodando até o usuário escolher "Sair"
        opcao = exibir_menu()

        if opcao == "1":
            abrir_chamado()

        elif opcao == "2":
            listar_chamados()

        elif opcao == "3":
            atualizar_status()

        elif opcao == "4":
            print("\nEncerrando o sistema. Até logo! 👋\n")
            break  # "break" encerra o loop while, saindo do programa

        else:
            print("\n⚠  Opção inválida. Digite 1, 2, 3 ou 4.")


# ===========================================================
# PONTO DE ENTRADA DO PROGRAMA
# Esta verificação garante que main() só seja chamada quando
# o arquivo for executado diretamente (não quando importado).
# É uma boa prática em Python!
# ===========================================================
if __name__ == "__main__":
    main()
