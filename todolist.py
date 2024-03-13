# uma lista de tarefas vazias onde vai ficar armazenada todas as tarefas adicionadas
tarefas = []

# função para adicionar uma tarefa
def add_tarefa(descricao, prioridade, categoria):
    tarefa = {'descricao': descricao, 'prioridade': prioridade, 'categoria': categoria, 'completa': False}
    tarefas.append(tarefa)
    print('\nSua tarefa foi adicionada com sucesso :)')

# função para ver todas as tarefas
def listar_tarefa():
    if not tarefas:
        print('\nNão existem tarefas adicionadas')
    else:
        for index, tarefa in enumerate(tarefas, 1):
            print(f"\n{index}. Tarefa: {tarefa['descricao']} - Prioridade: {tarefa['prioridade']} - Categoria: {tarefa['categoria']} - Status: {'Concluída' if tarefa['completa'] else 'Pendente'}")

# função para marcar tarefas que foram concluídas
def tarefa_concluida(index):
    if 1 <= index <= len(tarefas):
        tarefas[index - 1]['completa'] = True
        print('\nTarefa marcada como concluída')
    else:
        print('\nÍndice inválido')

# função para exibir tarefas por prioridade
def tarefa_prioritaria(prioridade):
    #o lower pra caso o usuario digitar com letra maiuscula ou minuscula, ele sempre reconhecer
    prioridade_lower = prioridade.lower()
    prioridade_tarefa = [tarefa for tarefa in tarefas if tarefa['prioridade'].lower() == prioridade_lower]
    if prioridade_tarefa:
        for index, tarefa in enumerate(prioridade_tarefa, 1):
            print(f"\n{index}. Tarefa: {tarefa['descricao']} - Categoria: {tarefa['categoria']} - {'Concluída' if tarefa['completa'] else 'Pendente'}")
    else:
        print('\nNão existem tarefas com essa prioridade')

# função para exibir tarefas por categorias
def categorias_tarefas(categoria):
    #o lower pra caso o usuario digitar com letra maiuscula ou minuscula, ele sempre reconhecer
    categoria_lower = categoria.lower()
    categoria_tarefa = [tarefa for tarefa in tarefas if tarefa['categoria'].lower() == categoria_lower]
    if categoria_tarefa:
        for index, tarefa in enumerate(categoria_tarefa, 1):
            print(f"\n{index}. Tarefa: {tarefa['descricao']} - Prioridade: {tarefa['prioridade']} - {'Concluída' if tarefa['completa'] else 'Pendente'} ")
    else:
        print('\nNão existem tarefas com essa categoria')

# função para atualizar uma tarefa já existente
def att_tarefa(index, nova_descricao, nova_prioridade, nova_categoria):
    if 0 <= index < len(tarefas):
        tarefas[index]['descricao'] = nova_descricao
        tarefas[index]['prioridade'] = nova_prioridade
        tarefas[index]['categoria'] = nova_categoria
        #reseta o status da tarefa
        tarefas[index]['completa'] = False
        print('\nTarefa atualizada com sucesso')
    else:
        print('\nÍndice inválido')

# função para excluir uma tarefa
def excluir_tarefa(index):
    if 0 <= index < len(tarefas):
        del tarefas[index]
        print('\nTarefa excluída com sucesso')
    else:
        print('\nÍndice inválido')

# função para o usuário editar as tarefas
def usuario(): 
    while True:
        print('\nMinha Lista de Tarefas\n')
        print('1. Adicionar Tarefa')
        print('2. Listar Tarefas')
        print('3. Marcar Tarefa como Concluída')
        print('4. Exibir Tarefa por Prioridade')
        print('5. Exibir Tarefa por Categoria')
        print('6. Atualizar Tarefa')
        print('7. Excluir Tarefa')
        print('0. Sair\n')

        escolha_usuario = input('\nEscolha uma opção: ')

        #Sair pro programa

        if escolha_usuario == '0':
            print('\nAté mais, volte sempre!')
            break

        #Adcionar uma nova tarefa
        
        elif escolha_usuario == '1':
            descricao = input('\nDigite a descrição da tarefa: ')
            prioridade = input('Digite a prioridade da tarefa: ')
            categoria = input('Digite a categoria da tarefa: ')
            add_tarefa(descricao, prioridade, categoria)
        
        #Ver as tarefas existentes

        elif escolha_usuario == '2':
            listar_tarefa()

        #Alterar o status da Tarefa de pendente para concluída

        elif escolha_usuario == '3':
            listar_tarefa()
            index = int(input('\nDigite o índice da tarefa a ser marcada como concluída: '))
            tarefa_concluida(index)

        #Mostrar apenas as tarefas com a prioridade escolhida pelo usuário

        elif escolha_usuario == '4':
            prioridade = input('\nDigite a prioridade das tarefas a serem exibidas: ')
            print('As tarefas de que tem essa prioridade são:\n')
            tarefa_prioritaria(prioridade)

        #Mostrar apenas as tarefas com a categoria escolhida pelo usuário

        elif escolha_usuario == '5':
            categoria = input('\nDigite a categoria das tarefas a serem exibidas: ')
            print('As tarefas de que tem essa categoria são:\n')
            categorias_tarefas(categoria)

        #Atualizar uma tarefa já existente

        elif escolha_usuario == '6':
            listar_tarefa()
            index = int(input('\nDigite o índice da tarefa que deseja atualizar: '))
            nova_descricao = input('\nDigite a nova descrição da tarefa: ')
            nova_prioridade = input('Digite a nova prioridade da tarefa: ')
            nova_categoria = input('Digite a nova categoria da tarefa: ')
            att_tarefa(index - 1, nova_descricao, nova_prioridade, nova_categoria)

        #Exclui a Tarefa

        elif escolha_usuario == '7':
            listar_tarefa()
            index = int(input('\nDigite o índice da tarefa que deseja excluir: '))
            excluir_tarefa(index - 1)


        else:
            print('\nOpção inválida. Tente novamente.')

usuario()
