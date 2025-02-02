# input 
nomeDoHeroi = input("Qual seu nome ?")
xpDoHeroi = int(input("quanto de xp o heroi possue?"))

#process
xp = xpDoHeroi
if xp <= 1000:
    nivelDoHeroi = "ferro"
elif xp > 1000 and xp < 2001:
    nivelDoHeroi = "bronze"
elif xp > 2000 and xp < 5001:
    nivelDoHeroi = "prata"
elif xp > 5000 and xp < 7001: 
    nivelDoHeroi = "ouro"
elif xp > 7000 and xp < 8001:
    nivelDoHeroi = "platina"
elif xp > 6000 and xp < 7001: 
    nivelDoHeroi = "ascendente"
elif xp > 6000 and xp < 7001:        
    nivelDoHeroi = "imortal"
elif xp > 8000:        
    nivelDoHeroi = "radiante"
else:
    nivelDoHeroi = "indisponivel"       

#output
print("O heroi de nome " + nomeDoHeroi + " está no nivel de " + nivelDoHeroi)
