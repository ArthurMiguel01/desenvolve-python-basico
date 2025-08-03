idade = int(input("Digite sua idade: "))
jogos_jogados = int(input("Quantos jogos de tabuleiro você já jogou? "))
vitorias = int(input("Quantos jogos já venceu? "))

apto = 16 <= idade <= 18 and jogos_jogados >= 3 and vitorias >= 1

print("Apto para ingressar no clube de jogos de tabuleiro:", apto)
