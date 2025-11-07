print("--"*20)
print("EXERCÍCIO 66 - Utilizando o break")
print("--"*20)
c=0
soma=0
while True:
    numero=int(input("Digite um número para somar [digite 999 para parar]: "))
    if numero==999:
        break
    c+=1
    soma=soma+numero
print(f"\033[34mVocê digitou {c} números e a soma foi de {soma}.\033[m")