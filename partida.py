def criar_baralho():
  pass

def mover_carta():
  pass

def conta_carta():
  pass


def embaralha_cartas(baralho):
  pass


def coloca_carta(baralho):
  pass

def compra_carta():
  pass

def inicia_jogo():
  baralho= criar_baralho()
  embaralha_cartas(baralho) 
  coloca_carta(baralho)
  while(True):
    jogada=input("Qual jogada vc quer fazer?")
    if jogada== "1":
      compra_carta()
    if jogada== "2":
      mover_carta()
    if conta_carta()== 0:
       print("Você perdeu")
       break
    else:
       print("Insira comando válido")
      
