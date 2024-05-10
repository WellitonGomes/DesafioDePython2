def obter_primo():#esta é a função responsavel a pedir ao usuario que digite um numero primo
    while True:#esta linha de codigo inicia um loop infinito que solicitará uma entrada de dados e não irá parar ate que confirme que o usuario digitou algo
        try:#esta linha de codigo inicia um bloco de codigo que pode permitir erros, para que as proximas linhas de codigos definam apos verificacão se esta correto ou nao
            valido = int(input("Digite um numero primo: "))#esta linha solicitara ao usuario que digite um numero, convertera o numero digitado por ele em inteiro e salvara na variavel valido
            return valido#se nenhum erro ocorrer no codigo dentro do bloco de codigos gerado pela linha try esta linha retornara o codigo como valido dando sequencia as operações
        except ValueError:#esta linha de codigo irá ser executada apenas se haver algum erro no codigo, isto ira acontecer se o usuario digitar algo que não possa ser convertido em inteiro
            print("Por favor digite um numero inteiro")#se a linha acima detectar um erro esta mensagem sera mostrada na tela do usuario

def idade():#funcao para verificacao da idade do usuario
    while True:#esta linha de codigo inicia um loop infinito que solicitará uma entrada de dados e não irá parar ate que confirme que o usuario digitou algo
        try:#esta linha de codigo inicia um bloco de codigo que pode permitir erros, para que as proximas linhas de codigos definam apos verificacão se esta correto ou nao
            tempo = int(input("Digite a sua idade: "))#esta linha solicitara ao usuario que digite sua idade, que sera convertida em um valor inteiro, e sera salva na variavel idade
            return tempo#se nenhum erro ocorrer no codigo dentro do bloco de codigos gerado pela linha try esta linha retornara o codigo como valido dando sequencia as operações
        except ValueError:#esta linha de codigo irá ser executada apenas se haver algum erro no codigo, isto ira acontecer se o usuario digitar algo que não possa ser convertido em inteiro
            print("Por favor digite sua idade")#se a linha acima detectar um erro esta mensagem sera mostrada na tela do usuario


def verificar_idade():#função para verificar a idade do usuario
    idade2 = idade()#define que o que foi inserido na função que pede ao usuario a sua idade é atribuida a idade2, ou seja o que for salvo na função idade() tambem sera salvo na variavel idade2
    if idade2 >= 18:#este if diz que se o valor digitado pelo usuario for maior ou igual a 18 o usuario será maior de idade
        print("Você é maior de idade")#esta mensagem confirma ao usuario que o programa reconhece ele como maior de idade
    else:#se a idade digitada pelo usuario não for maior ou igual a 18 a seguinte mensagem sera mostrada
        print("Você é menor de idade")#este é o print que confirma ao usuario que ele não é maior de idade



def fator():#esta linha define uma função chamada fator
    while True:#Isso inicia um loop infinito. O código dentro deste loop será executado repetidamente até que uma condição de parada seja encontrada ou até que o loop seja interrompido de outra forma.
        try:#esta linha de codigo inicia um bloco de codigo que pode permitir erros, para que as proximas linhas de codigos definam apos verificacão se esta correto ou nao
            resultado = int(input("Digite um numero para a verificação do fatorial: "))#esta linha solicitara ao usuario que digite um numero para a verificacão do fatorial do mesmo, o valor sera convertido em inteiro
            return resultado#se nenhum erro ocorrer no codigo dentro do bloco de codigos gerado pela linha try esta linha retornara o codigo como valido dando sequencia as operações
        except ValueError:#esta linha de codigo irá ser executada apenas se haver algum erro no codigo, isto ira acontecer se o usuario digitar algo que não possa ser convertido em inteiro
            print("Por favor digite um numero")

def obter_raiz():
    while True:
        try:
            raiz_quadrada = int(input("Digite um número para verificação da raiz quadrada: "))
            return raiz_quadrada
        except ValueError:
            print("Por favor, digite um número inteiro.")

def palindromo(palavra):
    tamanho = len(palavra)
    for i in range(tamanho // 2):
        if palavra[i] != palavra[tamanho - i - 1]:
            return False
    return True

def palin():
    while True:
        palavra = input("Digite uma palavra para verificar se é um palíndromo: ")
        if palavra.isalpha():
            if palindromo(palavra):
                print("A palavra é um palíndromo!")
            else:
                print("A palavra não é um palíndromo.")
            break
        else:
            print("Por favor, digite apenas letras.")

def is_prime(numero):#criamos uma funcao que ira verificar se um numero inserido pelo usuario e primo
    if numero == 1:#aqui estamos definindo que se a variavel numero receber o numero um o mesmo sera considerado como numero primo
        print("O numero 1 é considerado por algumas convenções matematicas como numero primo")#estramos mostrando na tela do usuario que o numero 1 é considerado por algumas convencoes matematicas como primo
    elif numero < 2:#aqui estamos comparando se o numero que foi inserido pelo usuario é menor que 2
        return False#esta funcao retorna falsa pois por definicao os numeros menores que 2 nao soa primos
    for i in range(2, int(numero ** 0.5) + 1):#nesta linhas iniciamos um loop que vai do numero 2 ate a raiz quadrada do valor inserido pelo usuario e fazendo uma soma de mais 1
        if numero % i == 0:#esta linha de codigo verifica se o numero inserido pelo usuario e divisivel por i que representa todos os numeros de 2 ate a raiz quadrada do numero inserido pelo usuario
            return False#este false indica que o numero nao e primo
    return True#se o numero inserido pelo usuario nao for divisivel por nenhum numero do entre 2 e sua raiz quadrada a funcao retorna verdadeira dizemdo que este e um numero primo

def verifica_primo():#criamos uma funcao para pedir ao usuario um valor para vermos se ele é realmente primo
    numero = obter_primo()#aqui pedimos diretamente ao usuario para que ele digite um valor para coferirmos se ele é primo
    if is_prime(numero):#aqui chamamos a funcao acima desta que e a qual realizara a comparacao para sabermos se o numero e realmente primo
        print("Este numero é primo")#se apos a revisao o numero for realmente primo esta mensagem sera printada mostrando ao usuario que o numero e realmente primo
    else:#se o numero nao passar nos testes de verificacao
        print("Este numero não é primo")#mostramos na tela do usuario que este numero nao é primo
def verifica_primo():
    numero = obter_primo()
    if is_prime(numero):
        print("Este numero é primo")
    else:
        print("Este numero não é primo")

def calcular_fatorial(numero):
    # resultado = 1
    # for i in range(1, numero + 1):
    #     resultado *= i
    #     return resultado
    if numero == 0:
        return 1
    else:
        return numero * calcular_fatorial(numero -1)
        numero = fator()
        resultado = calcular_fatorial(numero)
        print("O fatorial de", numero, "é:", resultado)

def raiz():
    import math
    valor = obter_raiz()
    raiz_quadrada = math.sqrt(valor)
    print("A raiz quadrada de", valor, "é:", raiz_quadrada)


def geral():
    verifica_primo()
    numero = fator()
    print("Fatorial de", numero, "é:", calcular_fatorial(numero))
    palin()
    raiz()
    verificar_idade()

geral()
