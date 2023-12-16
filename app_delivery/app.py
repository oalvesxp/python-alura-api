import os

restaurants = [
    {'name':'Box Mineiro', 'category':'Caseiro', 'status':False}, 
    {'name':'Pizza Hut', 'category':'Pizzaria', 'status':True},
    {'name':'MC Donalds', 'category':'Lanchonete', 'status':False}
]

## Exibindo o nome do programa
def app_name():
    print('''
𝘿𝙚𝙡𝙞𝙫𝙚𝙧𝙮 𝙀𝙭𝙥𝙧𝙚𝙨𝙨
''')

## Exibindo as opções do programa
def show_options():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

## Parando o programa
def stop_app():
    menu_caption('Encerrando o App... Bye!')

## Voltando ao menu principal
def back_menu():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

## Exibindo subtitulos
def menu_caption(text):
    os.system('clear')
    print(f'{text}\n')

## Opção inválida
def invalid_option():
    print('Opção inválida!\n')
    back_menu()

## Cadastrar restaurante
def register_restaurant():
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
    menu_caption('Listando os restaurantes')
    
    for eatery in restaurants:
        eatery_name = eatery['name']
        eatery_category = eatery['category']
        eatery_status = eatery['status']

        print(f'- {eatery_name} | {eatery_category} | {eatery_status}')

    back_menu()

def change_status():
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
    os.system('clear')
    app_name()
    show_options()
    select_option()

if __name__ == '__main__':
    main()