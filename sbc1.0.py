import networkx as nx
import matplotlib.pyplot as plt

# instancia o grafo
Brasil = nx.Graph()

# adicionando os nos
Brasil.add_node('RR')
Brasil.add_node('AP')
Brasil.add_node('AM')
Brasil.add_node('AC')
Brasil.add_node('RO')
Brasil.add_node('PA')
Brasil.add_node('AP')
Brasil.add_node('MA')
Brasil.add_node('PI')
Brasil.add_node('CE')
Brasil.add_node('RN')
Brasil.add_node('PB')
Brasil.add_node('PE')
Brasil.add_node('AL')
Brasil.add_node('SE')
Brasil.add_node('BA')
Brasil.add_node('TO')
Brasil.add_node('MT')
Brasil.add_node('GO')
Brasil.add_node('MS')
Brasil.add_node('MG')
Brasil.add_node('ES')
Brasil.add_node('RJ')
Brasil.add_node('SP')
Brasil.add_node('PR')
Brasil.add_node('SC')
Brasil.add_node('RS')

#brasil = {}


# adicionando as arestas
Brasil.add_edge('RR', 'AM')
Brasil.add_edge('RR', 'PA')
#brasil[retorna_cod_estado('RR')] = [retorna_cod_estado('AM'), retorna_cod_estado('PA')]
Brasil.add_edge('AP', 'PA')
#brasil[retorna_cod_estado('AP')] = [retorna_cod_estado('PA')]
Brasil.add_edge('AM', 'RR')
Brasil.add_edge('AM', 'PA')
Brasil.add_edge('AM', 'MT')
Brasil.add_edge('AM', 'RO')
Brasil.add_edge('AM', 'AC')
#brasil[retorna_cod_estado('AM')] = [retorna_cod_estado('RR'), retorna_cod_estado('PA'), retorna_cod_estado('MT'), retorna_cod_estado('RO'), retorna_cod_estado('AC')]
Brasil.add_edge('RR', 'AM')
Brasil.add_edge('RR', 'PA')
#brasil[retorna_cod_estado('RR')] = [retorna_cod_estado('AM'), retorna_cod_estado('PA')]
Brasil.add_edge('PA', 'RR')
Brasil.add_edge('PA', 'AP')
Brasil.add_edge('PA', 'MA')
Brasil.add_edge('PA', 'TO')
Brasil.add_edge('PA', 'AM')
Brasil.add_edge('PA', 'MT')
#brasil[retorna_cod_estado('PA')] = [retorna_cod_estado('RR'), retorna_cod_estado('AP'), retorna_cod_estado('MA'), retorna_cod_estado('TO'), retorna_cod_estado('AM'), retorna_cod_estado('MT')]
Brasil.add_edge('MA', 'PA')
Brasil.add_edge('MA', 'TO')
Brasil.add_edge('MA', 'PI')
#brasil[retorna_cod_estado('AP')] = [retorna_cod_estado('PA'), retorna_cod_estado('TO'), retorna_cod_estado('PI')]
Brasil.add_edge('PI', 'MA')
Brasil.add_edge('PI', 'TO')
Brasil.add_edge('PI', 'BA')
Brasil.add_edge('PI', 'PE')
Brasil.add_edge('PI', 'CE')
#brasil[retorna_cod_estado('PI')] = [retorna_cod_estado('MA'), retorna_cod_estado('TO'), retorna_cod_estado('BA'), retorna_cod_estado('PE'), retorna_cod_estado('CE')]
Brasil.add_edge('CE', 'PI')
Brasil.add_edge('CE', 'RN')
Brasil.add_edge('CE', 'PB')
Brasil.add_edge('CE', 'PE')
#brasil[retorna_cod_estado('CE')] = [retorna_cod_estado('PI'), retorna_cod_estado('RN'), retorna_cod_estado('PB'), retorna_cod_estado('PE')]
Brasil.add_edge('RN', 'CE')
Brasil.add_edge('RN', 'PB')
#brasil[retorna_cod_estado('RN')] = [retorna_cod_estado('CE'), retorna_cod_estado('PB')]
Brasil.add_edge('PB', 'CE')
Brasil.add_edge('PB', 'RN')
Brasil.add_edge('PB', 'PE')
#brasil[retorna_cod_estado('PB')] = [retorna_cod_estado('CE'), retorna_cod_estado('RN'), retorna_cod_estado('PE')]
Brasil.add_edge('PE', 'PB')
Brasil.add_edge('PE', 'CE')
Brasil.add_edge('PE', 'PI')
Brasil.add_edge('PE', 'AL')
Brasil.add_edge('PE', 'BA')
#brasil[retorna_cod_estado('PE')] = [retorna_cod_estado('PB'), retorna_cod_estado('CE'), retorna_cod_estado('PI'), retorna_cod_estado('AL'), retorna_cod_estado('BA')]
Brasil.add_edge('AL', 'PE')
Brasil.add_edge('AL', 'SE')
Brasil.add_edge('AL', 'BA')
#brasil[retorna_cod_estado('AL')] = [retorna_cod_estado('PE'), retorna_cod_estado('SE'), retorna_cod_estado('BA')]
Brasil.add_edge('SE', 'AL')
Brasil.add_edge('SE', 'BA')
#brasil[retorna_cod_estado('SE')] = [retorna_cod_estado('AL'), retorna_cod_estado('BA')]
Brasil.add_edge('BA', 'SE')
Brasil.add_edge('BA', 'AL')
Brasil.add_edge('BA', 'PE')
Brasil.add_edge('BA', 'PI')
Brasil.add_edge('BA', 'TO')
Brasil.add_edge('BA', 'GO')
Brasil.add_edge('BA', 'MG')
Brasil.add_edge('BA', 'ES')
#brasil[retorna_cod_estado('BA')] = [retorna_cod_estado('SE'), retorna_cod_estado('AL'), retorna_cod_estado('PE'), retorna_cod_estado('PI'), retorna_cod_estado('TO'), retorna_cod_estado('GO'), retorna_cod_estado('MG'), retorna_cod_estado('ES')]
Brasil.add_edge('TO', 'PA')
Brasil.add_edge('TO', 'MA')
Brasil.add_edge('TO', 'PI')
Brasil.add_edge('TO', 'BA')
Brasil.add_edge('TO', 'GO')
Brasil.add_edge('TO', 'MT')
#brasil[retorna_cod_estado('TO')] = [retorna_cod_estado('PA'), retorna_cod_estado('MA'), retorna_cod_estado('PI'), retorna_cod_estado('BA'), retorna_cod_estado('GO'), retorna_cod_estado('MT')]
Brasil.add_edge('MT', 'RO')
Brasil.add_edge('MT', 'AM')
Brasil.add_edge('MT', 'PA')
Brasil.add_edge('MT', 'TO')
Brasil.add_edge('MT', 'GO')
Brasil.add_edge('MT', 'MS')
#brasil[retorna_cod_estado('MT')] = [retorna_cod_estado('RO'), retorna_cod_estado('AM'), retorna_cod_estado('PA'), retorna_cod_estado('TO'), retorna_cod_estado('GO'), retorna_cod_estado('MS')]
Brasil.add_edge('RO', 'MT')
Brasil.add_edge('RO', 'AM')
Brasil.add_edge('RO', 'AC')
#brasil[retorna_cod_estado('RO')] = [retorna_cod_estado('MT'), retorna_cod_estado('AM'), retorna_cod_estado('AC')]
Brasil.add_edge('AC', 'AM')
Brasil.add_edge('AC', 'RO')
#brasil[retorna_cod_estado('AC')] = [retorna_cod_estado('AM'), retorna_cod_estado('RO')]
Brasil.add_edge('GO', 'MT')
Brasil.add_edge('GO', 'TO')
Brasil.add_edge('GO', 'BA')
Brasil.add_edge('GO', 'MG')
Brasil.add_edge('GO', 'MS')
#brasil[retorna_cod_estado('GO')] = [retorna_cod_estado('MT'), retorna_cod_estado('TO'), retorna_cod_estado('BA'), retorna_cod_estado('MG'), retorna_cod_estado('MS')]
Brasil.add_edge('MG', 'BA')
Brasil.add_edge('MG', 'ES')
Brasil.add_edge('MG', 'GO')
Brasil.add_edge('MG', 'RJ')
Brasil.add_edge('MG', 'SP')
Brasil.add_edge('MG', 'MS')
#brasil[retorna_cod_estado('MG')] = [retorna_cod_estado('BA'), retorna_cod_estado('ES'), retorna_cod_estado('GO'), retorna_cod_estado('RJ'), retorna_cod_estado('SP'), retorna_cod_estado('MS')]
Brasil.add_edge('ES', 'BA')
Brasil.add_edge('ES', 'MG')
Brasil.add_edge('ES', 'RJ')
#brasil[retorna_cod_estado('ES')] = [retorna_cod_estado('BA'), retorna_cod_estado('MG'), retorna_cod_estado('RJ')]
Brasil.add_edge('RJ', 'ES')
Brasil.add_edge('RJ', 'MG')
Brasil.add_edge('RJ', 'SP')
#brasil[retorna_cod_estado('RJ')] = [retorna_cod_estado('ES'), retorna_cod_estado('MG'), retorna_cod_estado('SP')]
Brasil.add_edge('MS', 'MT')
Brasil.add_edge('MS', 'GO')
Brasil.add_edge('MS', 'MG')
Brasil.add_edge('MS', 'SP')
Brasil.add_edge('MS', 'PR')
#brasil[retorna_cod_estado('MS')] = [retorna_cod_estado('MT'), retorna_cod_estado('GO'), retorna_cod_estado('MG'), retorna_cod_estado('SP'), retorna_cod_estado('PR')]
Brasil.add_edge('SP', 'RJ')
Brasil.add_edge('SP', 'MG')
Brasil.add_edge('SP', 'MS')
Brasil.add_edge('SP', 'PR')
#brasil[retorna_cod_estado('SP')] = [retorna_cod_estado('RJ'), retorna_cod_estado('MG'), retorna_cod_estado('MS'), retorna_cod_estado('PR')]
Brasil.add_edge('PR', 'MS')
Brasil.add_edge('PR', 'SP')
Brasil.add_edge('PR', 'SC')
#brasil[retorna_cod_estado('PR')] = [retorna_cod_estado('MS'), retorna_cod_estado('SP'), retorna_cod_estado('SC')]
Brasil.add_edge('SC', 'PR')
Brasil.add_edge('SC', 'RS')
#brasil[retorna_cod_estado('SC')] = [retorna_cod_estado('PR'), retorna_cod_estado('RS')]
Brasil.add_edge('RS', 'SC')
#brasil[retorna_cod_estado('RS')] = [retorna_cod_estado('SC')]

# print(brasil)
#print('Código do RJ: ', retorna_cod_estado('RJ'))
# print(brasil[retorna_cod_estado('RJ')])
# print(len(brasil[retorna_cod_estado('RJ')]))

# funções utilizadas

estados = list(Brasil.nodes)
estados.sort()
traduz = []
for i in range(len(estados)):
    traduz.append({'estado': str(estados[i]), 'cod': i})

malha_rodoviaria = {}


def retorna_cod_estado(estado):
    for i in range(len(estados)):
        if traduz[i]['estado'] == estado:
            cod = traduz[i]['cod']
    return cod


def retorna_nome_estado(cod):
    estado = str('-')
    for i in range(len(traduz)):
        if traduz[i]['cod'] == int(cod):
            estado = traduz[i]['estado']
    return estado


def bfs(grafo, inicio, fim):
    print('inicio = ', inicio)
    print('fim = ', fim)
    explorado = []
    fila = [[inicio]]
    if inicio == fim:
        return inicio
    while fila:
        print('fila = ', fila)
        caminho = fila.pop(0)
        no = caminho[-1]
        if no not in explorado:
            vizinhos = grafo[no]
            print('vizinhos = ', vizinhos)
            for vizinho in vizinhos:
                novo_caminho = caminho.copy()
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)
                if vizinho == fim:
                    return novo_caminho
            explorado.append(no)


def reativa_estrada(estado1, estado2):
    Brasil.add_edge(estado1, estado2)
    return


def estados_ligados(estado):
    lista_estados_ligados = Brasil.neighbors(estado)
    return lista_estados_ligados


def imprime_mapa():
    nx.draw_spring(Brasil, with_labels=1)
    plt.show()
    return


lista_estradas_inativas = []


def inativa_estrada(estado1, estado2):
    Brasil.remove_edge(estado1, estado2)
    lista_estradas_inativas.append({'estado1': estado1, 'estado2': estado2})
    return


def mostra_estradas_inativas():
    if len(lista_estradas_inativas) == 0:
        print('\nNão há estradas inativas.\n')
    else:
        print('\nEstradas inativas:')
        for i in range(len(lista_estradas_inativas)):
            print(str(i) + '. ' + str(lista_estradas_inativas[i]['estado1']) + ' - ' + str(
                lista_estradas_inativas[i]['estado2']))
        print()


def melhor_caminho(estado_1, estado_2):

    estradas = list(Brasil.edges)
    #print('estradas = ', estradas)
    #print('tam = ', len(estradas))

    for i in range(len(estradas)):

        estado1 = estradas[i][0]
        estado2 = estradas[i][1]
        cod_estado1 = retorna_cod_estado(estado1)
        #print('cod_estado1 = ', cod_estado1)
        #print('nome_estado1 = ', retorna_nome_estado(cod_estado1))
        cod_estado2 = retorna_cod_estado(estado2)
        #print('cod_estado2 = ', cod_estado2)
        #print('nome_estado2 = ', retorna_nome_estado(cod_estado2))
        # print()

        # len(malha_rodoviaria[cod_estado1]) == 0:
        if cod_estado1 not in malha_rodoviaria:
            malha_rodoviaria[cod_estado1] = []

        malha_rodoviaria[cod_estado1].append(cod_estado2)

    print('malha_rodoviaria = ', malha_rodoviaria)

    caminho = bfs(malha_rodoviaria, retorna_cod_estado(
        estado_1), retorna_cod_estado(estado_2))

    print('caminho = ', caminho)

    # caminho = nx.shortest_path(Brasil, source=estado1, target=estado2)

    for i in range(len(caminho)):
        if i == (len(caminho) - 1):
            print(retorna_nome_estado(caminho[i]))
        else:
            print(retorna_nome_estado(caminho[i]), end=' -> ')

    return


def pergunta_caminho():
    print('\nOlá, caminhoneiro!\n')

    print('No Brasil nós temos os seguintes estados:')
    lista_estados = list(Brasil.nodes)
    lista_estados.sort()
    for i in range(len(lista_estados)):
        if i == (len(lista_estados) - 1):
            print(str(lista_estados[i]) + '.')
        else:
            print(str(lista_estados[i]), end=', ')

    estado_atual = input('\nDigite a sigla do estado onde você está: ')
    estado_destino = input('Digite a sigla do estado onde você quer ir: ')

    print('\nAtualmente o melhor caminho para você utilizar é:')
    melhor_caminho(estado_atual, estado_destino)

    print('\nBoa viagem!')
    return


def mostra_estradas():
    print('\nEstradas ativas:')
    lista_estradas = list(Brasil.edges)
    for i in range(len(lista_estradas)):
        print(str(i) + '. ' +
              str(lista_estradas[i][0]) + ' - ' + str(lista_estradas[i][1]))
    print()
    return


def pergunta_inativar():
    print('\nHá algum problema com as estradas?\nAqui você pode desativar uma delas.\n')

    print('Atualmente temos as seguintes estradas funcionando:\n')
    mostra_estradas()

    lista_estradas = list(Brasil.edges)
    cod_estrada = int(
        input('\nDigite o número da estrada que você deseja desativar: '))
    estado_origem = lista_estradas[cod_estrada][0]
    estado_final = lista_estradas[cod_estrada][1]
    inativa_estrada(estado_origem, estado_final)

    print('\nA estrada que liga ' + estado_origem +
          ' a ' + estado_final + ' foi desativada.\n')
    return


def ativa_estrada(estado1, estado2):
    Brasil.add_edge(estado1, estado2)
    return


def pergunta_ativar():
    print('\nHá alguma estrada restaurada?\nAqui você pode reativar uma delas.\n')

    print('Atualmente temos as seguintes estradas desativadas:\n')
    mostra_estradas_inativas()

    cod_estrada = int(
        input('Digite o número da estrada que você deseja reativar: '))
    estado_origem = lista_estradas_inativas[cod_estrada]['estado1']
    estado_final = lista_estradas_inativas[cod_estrada]['estado2']
    ativa_estrada(estado_origem, estado_final)
    lista_estradas_inativas.pop(cod_estrada)

    print('\nA estrada que liga ' + estado_origem +
          ' a ' + estado_final + ' foi reativada.\n')
    return


print('RJ = ', retorna_cod_estado('RJ'))
print('RS = ', retorna_cod_estado('RS'))
print(melhor_caminho('RJ', 'RS'))

#print('traduz = ', traduz)
# print(traduz[2]['estado'])


# print(malha_rodoviaria)
# print(len(malha_rodoviaria))

#print(bfs(malha_rodoviaria, retorna_cod_estado('GO'), retorna_cod_estado('SP')))

# print(estradas[0][1])
# print(traduz)
# parte interativa do programa
"""
while(1):
    print('\nOlá! Seja bem-vindo ao Siga Bem Caminhoneiro!\nPrimeiramente faça o seu login.\n')
    print('Você deseja acessar como:\n1. Caminhoneiro\n2. Fiscal do DER')
    login = int(input())
    #menu = 0

    if login == 1:

        print('\nSeja bem-vindo, caminhoneiro!')
        while(1):

            print('\nQual serviço você deseja?\n1. Encontrar a melhor rota para o meu destino.\n2. Saber quais estradas estão ativas.\n3. Saber quais estradas estão inativas.\n4. Ter um mapa das estradas atuais.\n0. Fechar programa.\n')
            opcao = int(input())

            if opcao == 1:
                pergunta_caminho()
            elif opcao == 2:
                mostra_estradas()
            elif opcao == 3:
                mostra_estradas_inativas()
            elif opcao == 4:
                nx.draw_spring(Brasil, with_labels=1)
                plt.show()
                print()
            elif opcao == 0:
                print('\nObrigado por utilizar o Siga Bem Caminhoneiro!\n')
                exit()

            print('Deseja realizar outra ação?\n')
            print('1. Sim.\n2. Não.\n0. Fechar programa.\n')
            opcao2 = int(input())

            if opcao2 == 1:
                continue
            elif opcao2 == 0:
                print('\nObrigado por utilizar o Siga Bem Caminhoneiro!\n')
                exit()
            else:
                #menu = 1
                break

    elif login == 2:

        print('\nSeja bem-vindo, servidor do DER!')
        while(1):

            print('\nQual serviço você deseja?\n1. Inativar uma estrada.\n2. Reativar uma estrada.\n3. Saber quais estradas estão ativas.\n4. Saber quais estradas estão inativas.\n5. Ter um mapa das estradas atuais.\n0. Fechar programa.\n')
            opcao = int(input())

            if opcao == 1:
                pergunta_inativar()
            elif opcao == 2:
                pergunta_ativar()
            elif opcao == 3:
                mostra_estradas()
            elif opcao == 4:
                mostra_estradas_inativas()
            elif opcao == 5:
                nx.draw_spring(Brasil, with_labels=1)
                plt.show()
                print()
            elif opcao == 0:
                print('\nObrigado por utilizar o Siga Bem Caminhoneiro!\n')
                exit()

            print('Deseja realizar outra ação?\n')
            print('1. Sim.\n2. Não.\n0. Fechar programa.\n')
            opcao2 = int(input())

            if opcao2 == 1:
                continue
            elif opcao2 == 0:
                print('\nObrigado por utilizar o Siga Bem Caminhoneiro!\n')
                exit()
            else:
                #menu = 1
                break

    # elif menu == 1:
    #    continue

    print('\nObrigado por utilizar o Siga Bem Caminhoneiro!\n')
    break
"""
