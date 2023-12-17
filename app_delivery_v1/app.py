import os

restaurants = [
    {'name':'Box Mineiro', 'category':'Caseiro', 'status':False}, 
    {'name':'Pizza Hut', 'category':'Pizzaria', 'status':True},
    {'name':'MC Donalds', 'category':'Lanchonete', 'status':False}
]

## Exibindo o nome do programa
def app_name():
    '''Essa função é responsável por exibir o nome do programa
    
    Outputs:
    - Exibe o nome do programa
    '''
    print('''
𝘿𝙚𝙡𝙞𝙫𝙚𝙧𝙮 𝙀𝙭𝙥𝙧𝙚𝙨𝙨
''')

## Exibindo as opções do programa
def show_options():
    '''Essa função é responssável por exibir as opções do menu principal
    
    Outputs:
    - Exibe as opções do programa
        1. Cadastrar
        2. Listar
        3. Alterar status
        4. Sair
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar status do restaurante')
    print('4. Sair\n')

## Parando o programa
def stop_app():
    '''Essa função é responsável por encerrar o programa
    
    Outputs:
    - Exibe a mensagem de encerramento do programa
    - Encerra o programa
    '''
    menu_caption('Encerrando o App... Bye!')

## Voltando ao menu principal
def back_menu():
    '''Essa função é responsável por voltar ao menu principal
    
    Inputs:
    - Qualquer tecla para retornar ao menu principal
    - Volta ao estado inicial do programa
    '''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

## Exibindo subtitulos
def menu_caption(text):
    '''Essa função é responsável por exibir o subtítulo da categoria selecionada pelo usuário
    
    Outputs:
    - Exibe o subtítulo da função selecionada
    '''
    os.system('clear')
    line = '*' * (len(text))
    print(line)
    print(f'{text}')
    print(line)
    print()

## Opção inválida
def invalid_option():
    '''Essa função é responsável por informar se a entrada foi inválida e retornar ao menu principal
    
    Outputs:
    - Exibe o texto de opção inválida
    - Volta ao menu principal
    '''
    print('Opção inválida!\n')
    back_menu()

## Cadastrar restaurante
def register_restaurant():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante

    Outputs:
    - Adiciona o restaurante ao dicionário de restaurantes
    - Exibe o texto de conclusão do cadastro
    - Inicia a função de voltar ao menu principal
    '''
    menu_caption('Cadastro de novos restaurantes')

    name = input('Digite o nome do restaurante: ')
    category = input(f'Digite a categoria do restaurante {name}: ')
    
    data_restaurant = {
        'name':name,
        'category': category,
        'status':False
    }
    restaurants.append(data_restaurant)
    
    print(f'O restaurante {name}, foi cadastrado com sucesso!\n')
    back_menu()

## Listar restaurantes
def list_restaurants():
    '''Essa função é responsável por listar todos os restaurantes cadastrados

    Outputs:
    - Exibe todos os restaurantes encontrados no dicionário
    - Inicia a função de voltar ao menu principal
    '''
    menu_caption('Listando os restaurantes')
    
    print(f"{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}")
    for eatery in restaurants:
        eatery_name = eatery['name']
        eatery_category = eatery['category']
        eatery_status = 'Ativado' if eatery['status'] else 'Desativado'

        print(f'- {eatery_name.ljust(20)} | {eatery_category.ljust(20)} | {eatery_status}')

    back_menu()

def change_status():
    '''Essa função é responsável por mudar o status de um restaurante selecionado pelo usuário
    
    Inputs:
    - Nome do restaurante

    Outpust:
    - Verifica a existência do restaurante e atualiza o status
    - Exibe o texto de confirmação da ação realizada, ou a mensagem de que não foi possível encontrar nenhum restaurante
    '''
    menu_caption('Alterando o status do restaurante')

    name = input('Digite o nome do restaurante: ')
    check = False
    
    for item in restaurants:
        if name == item['name']:
            check = True
            item['status'] = not item['status']
            message = f'O restaurante {name} foi ativado com sucesso' if item['status'] else f'O restaurante {name} foi desativado com sucesso'
            print(message)

    if not check:
        print(f'O restaurante {name}, não foi encontrado!')

    back_menu()

## Selecionando a opção
def select_option():
    '''Essa função é responsável por capturar a entrada do usuário e direcionar o acesso a função requisitada
    
    Input:
    - 1. Registrar restaurante
    - 2. Listar restaurantes
    - 3. Alterar status do restaurante
    - 4. Sair

    Outputs:
    - 1. Inicia a função de registro de um novo restaurante
    - 2. Inicia a função de listagem de todos os restaurantes do dicionário
    - 3. Inicia a função de altração de status de restaurante
    - 4. Inicia a função de finalização do programa
    '''
    try:
        option = int(input('Escolha uma opção: '))

        if option == 1:
            register_restaurant()
        elif option == 2:
            list_restaurants()
        elif option == 3:
            change_status()
        elif option == 4:
            stop_app() 
        else:
            invalid_option()
    except:
        invalid_option()

## Definindo o main exec
def main():
    '''Essa função é responsável por aplicar os comandos de inicialização do programa
    
    Outputs:
    - Limpa o console
    - Inicia a função que exibe o nome do programa
    - Inicia a função de menu principal
    - Inicia a função de seleção de opções
    '''
    os.system('clear')
    app_name()
    show_options()
    select_option()

if __name__ == '__main__':
    main()