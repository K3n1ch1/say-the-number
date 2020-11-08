import random as r

def loop():
    n = r.randint(10,100)

    # Variables
    s = ['S', 's', 'Sim', 'sim', 'SIM', 'Y', 'y', 'Yes', 'yes', 'YES']
    n = ['N', 'n', 'Não', 'Nao', 'NÃO', 'NAO', 'No', 'NO']

    while True:
        try:
            answer = int(input("Digite um número de 10 a 100: "))
        except ValueError and TypeError or TypeError or ValueError:
            print('Por favor digite um número inteiro')
        else:
            if answer == n:
                print("Acertou o número")
                cont = str(input("Gostaria de repetir o programa?"))
                
                if cont in s:
                    return loop()
                elif cont in n:
                    print('Adeus')
                    break
                else: 
                    print("Erro no sistema")
            elif answer < n:
                print("Maior")
            elif answer > n:
                print("Menor")

loop()