# DESAFIO 024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cid = str(input("Em que cidade você nasceu: "))
print(cid[:5].upper() == 'SANTO')