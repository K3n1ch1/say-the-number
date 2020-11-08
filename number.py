import random as r

def Loop():
    num = r.randint(10,100)

    # Variables
    s = ['S', 's', 'Sim', 'sim', 'SIM', 'Y', 'y', 'Yes', 'yes', 'YES']
    n = ['N', 'n', 'Não', 'Nao', 'NÃO', 'NAO', 'No', 'NO']

    while True:
        try:
            answer = int(input("Type a number between 10 and 100: "))
        except ValueError and TypeError or TypeError or ValueError:
            print('Por favor digite um número inteiro')
        else:
            if answer == num:
                print("Correct Answer! Nice work")
                cont = str(input("Would you like to retry? "))
                
                if cont in s:
                    return Loop()
                elif cont in n:
                    print('See you next time')
                    break
                else: 
                    print("System ERROR")
            elif answer < num:
                print("Too Low")
            elif answer > num:
                print("Too High")

Loop()