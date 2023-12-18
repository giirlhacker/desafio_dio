
nivel_vida = int(input("Digite seu nivel de vida de 1 ate 10: "))
level = int(input("Digite seu level de 1.000 ate 10.000: "))
nome_jogador = input("Digite seu nome: ")

print("Ola, ", nome_jogador, ". Seja muito-bem vindo(a)!")


print("-"*30)
print("Analisando seu nivel de vida")
print("-"*30)

if 1 <= nivel_vida <= 3:
    print("Nivel de vida muito baixo, se recupere!!!")
elif 4 <= nivel_vida <= 7:
    print("Seja cauteloso!")
elif 8 <= nivel_vida <=10:
    print("Sua vida esta otima")
else:
    print("Por favor, tente novamente. Coloque um valor entre 1 e 10")

print("-"*30)
print("Analisando sua experiencia")
print("-"*30)

while level < 1000:
    print("Ferro")
    break
while 1001 <= level <= 2000:
    print("Bronze")
    break
while 2001 <= level <= 5000:
    print("Prata")
    break
while 5001 <= level <= 6000:
    print("Ouro")
    break
while 6001 <= level <= 7000:
    print("Platina")
    break
while 7001 <= level <= 8000:
    print("Ascendente")
    break
while 8001 <= level <= 9000:
    print("Imortal")
    break
while 9001 <= level <= 10000:
    print("Radiante")
    break

print("Chegamos ao fim, ", nome_jogador, ". Aqui está seu XP: ", level, "e sua vida: ", nivel_vida)

