import os

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

## Selecionando a opção
def select_option():
    option = int(input('Escolha uma opção: '))

    if option == 1:
        print('Cadastrar restaurante')
    elif option == 2:
        print('Listar restaurante')
    elif option == 3:
        print('Ativar restaurante')
    else:
        stop_app()

## Definindo o main exec
def main():
    app_name()
    show_options()
    select_option()

if __name__ == '__main__':
    main()