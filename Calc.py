
#Definindo a Função
def calculate():
    Operação = input("Selecione o operador desejado sendo: + para adcição | - para subteação | * para multiplicação | / para divisão: ")
        

    PrimeiroNum = int(input("Selecione o primeiro numerero: "))
    SegundoNum = int(input("Selecione o segundo numerero: "))
    

#Add os operadores 

#Soma 
    if Operação == "+":
        print("{} + {} = ".format(PrimeiroNum, SegundoNum))
        print(PrimeiroNum + SegundoNum)

#Subtração 
    elif Operação == "-":
        print("{} - {} = ".format(PrimeiroNum, SegundoNum))
        print(PrimeiroNum - SegundoNum)

#multiplicação 
    elif Operação == "*":
        print("{} * {} = ".format(PrimeiroNum, SegundoNum))
        print(PrimeiroNum * SegundoNum)

#Divisão 
    elif Operação == "/":
        print("{} / {} = ".format(PrimeiroNum, SegundoNum)) 
        print(PrimeiroNum / SegundoNum)

    else:
        print("Operador Inválido, tente novamente :D")
        calculate()

#-------------------------------------------------------------------------------------------------#

# essa função permite que você use a calculadora novamente 
def RodNovamente():
    
    Calc_Novamente = input("Deseja calcular novamente? Digite Y para sim e N de deseja sair da calculadora: ")
    
    #aceitar caracter min
    if Calc_Novamente.upper() == "Y":
        calculate()
    elif Calc_Novamente.upper() == "N":
        print("Obrigado por usar nossa calculadora, te vejo em uma proxima :D")
    
    #Se o user selecionar Y 
    if Calc_Novamente == "Y":
        calculate()
        
    #Se o user selecionar N
    elif Calc_Novamente == "N":
        print("Obrigado por usar nossa calculadora, te vejo em uma proxima :D")
    
    #Se o user selecionar outro simb
    else:
        RodNovamente()
    
    # chama a função calculate fora da função
calculate()