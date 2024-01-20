# import Math
import os

def geral():
    def nome_programa():
        print('IR 2000')
        print()
    def clear():
        return os.system('cls')
    clear()
    nome_programa()
    opcoes()
    escolha_modo()

def opcoes():
    print('1. Fazer o cálculo do meu imposto de renda\n2. Opções com arquivo\n3. Finalizar app')

def mensagem_de_erro(index):
    mensagens_de_erros = ['Opção inválida', 'Digite apenas números']
    print(f'Erro! {mensagens_de_erros[index]}.')
    voltar_ao_menu()

    
def exibi_subtitulo(txt):
    os.system('cls')
    print(f'IR 2000 - {txt}')

def voltar_ao_menu():
    input('Digite algo para voltar ao menu: ')
    main()

def calculo_ir_simplificado():
    exibi_subtitulo('Cálculo do IR - DEDUÇÃO SIMPLICADA')
    print('Teste')
    # Primeiro montando o sistema. Posteriormente irei adicionar o cálculo
    try:
        rendimento = float(input('Digite o seu rendimento: '))
        print(rendimento)
        voltar_ao_menu()
    except ValueError:
        mensagem_de_erro(1)
        voltar_ao_menu()




def escolha_modo():
    try:
        escolha = int(input('Digite a opção desejada: '))
        match escolha:
            case 1:
                calculo_ir_simplificado()
            case 2:
                voltar_ao_menu()
            case 3:
                os.system('cls')
                print('cabo')
    except ValueError:
        mensagem_de_erro(0)
        

def main():
    geral()

if __name__ == "__main__":
    main()