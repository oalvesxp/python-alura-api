import os

restaurants = ['Box Mineiro', 'Pizza Hut']

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
    os.system('clear')
    print('Encerrando o App! Bye!\n')

## Opção inválida
def invalid_option():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal!')
    main()

## Cadastrar restaurante
def register_restaurant():
    os.system('clear')
    print('Cadastro de novos restaurantes:\n')
    name = input('Digite o nome do restaurante: ')
    restaurants.append(name)
    print(f'O restaurante {name}, foi cadastrado com sucesso!\n')
    input('\nDigite uma tecla para voltar ao menu principal!')
    main()

## Listar restaurantes
def list_restaurants():
    os.system('clear')
    print('Listando os restaurantes:\n')
    
    for eatery in restaurants:
        print(f'.{eatery}')

    input('\nDigite uma tecla para voltar ao menu principal!')
    main()

## Selecionando a opção
def select_option():
    try:
        option = int(input('Escolha uma opção: '))

        if option == 1:
            register_restaurant()
        elif option == 2:
            list_restaurants()
        elif option == 3:
            print('Ativar restaurante')
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