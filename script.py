import time, random

totalRobo = 0
global cabeca, pescoco, tronco, pernas, pes
cabeca = 3
pescoco = 9
tronco = 9
pernas = 18
pes = 6
listaTempo = []
tempoTotalBuscaPecas = {}
tempoTotalMontagemInferiores = {}
tempoTotalMontagemSuperiores = {}
bdTempo = {}
meu_dict = {}
controlador = True
contador = 1

def exibePecas(pecas):
   print("-----------------------------------------------")
   print("Total de peças disponíveis")
   print(f"Cabeça: {pecas['Cabeça']}")
   print(f"Pescoço: {pecas['Pescoço']}")
   print(f"Tronco: {pecas['Tronco']}")
   print(f"Pernas: {pecas['Pernas']}")
   print(f"Pés: {pecas['Pés']}")
   print("-----------------------------------------------")
   print()

def printRoboInteiro():
   robot = """
      [====]
      [::::]
      [::::]
[::::][::::][::::]
[####][####][####]
[####]      [####]
   """
   print(robot)
   
def printInferiores():
   robot = """
[::::][::::][::::]
[####][####][####]
[####]      [####]
   """
   print(robot)

def buscarPecas(pecas):
   for chave, valor in pecas.items():
      print("Procurando por uma peça...")
      tempo = random.randint(1, 2)
      time.sleep(tempo)
      print("Tempo para encontrar a peça: ", tempo, " segundos.")
      print(f"Peça encontrada: {chave}", "\n")
      listaTempo.append(tempo)
      time.sleep(1)
      
def armazenaTempo():
   i = 1
   chavesDict = {1: "Pés", 2: "Pernas", 3: "Tronco", 4: "Pescoço", 5: "Cabeça"}
   for tempo in listaTempo:
      chave = f"Tempo {chavesDict[i]}"
      meu_dict[chave] = tempo
      i+=1
   bdTempo.update({"Tempo": meu_dict})
      
def imprimeTempos():
   print("Tempos de busca de cada peça do robô:")
   for categoria, tempos in bdTempo.items():
      for chave, valor in tempos.items():
         print(f"{chave}: {valor} segundos.")
         time.sleep(2)
         
def armazenaTempoBusca():
   tempoBusca = 0
   for x in listaTempo:
      tempoBusca += x
   chaveContadorBusca = f"Ciclo {contador}"
   tempoTotalBuscaPecas[chaveContadorBusca] = tempoBusca
   print(f"Tempo total para encontrar todas as peças: {tempoBusca} segundos.")
   tempoBusca = 0

def montarInferiores():
   print()
   print("Movendo peças para a área de montagem dos membros inferiores!")
   time.sleep(2)
   print("Montando peças dos membros inferiores...")
   tempoMontagemInferiores = random.randint(5, 8)
   time.sleep(tempoMontagemInferiores)
   print(f"Tempo para montagem: {tempoMontagemInferiores} segundos")
   printInferiores()
   chaveContadorInferiores = f"Ciclo {contador}"
   tempoTotalMontagemInferiores[chaveContadorInferiores] = tempoMontagemInferiores
   time.sleep(2)
   print()
   
def montarSuperiores():
   print("Movendo peças para a área de montagem dos membros superiores!")
   time.sleep(2)
   print("Montando peças dos membros superiores...")
   tempoMontagemSuperiores = random.randint(5,8)
   time.sleep(tempoMontagemSuperiores)
   print(f"Tempo para montagem: {tempoMontagemSuperiores} segundos")
   printRoboInteiro()
   chaveContadorSuperiores = f"Ciclo {contador}"
   tempoTotalMontagemSuperiores[chaveContadorSuperiores] = tempoMontagemSuperiores
   time.sleep(2)
   print()
   
def contagemRobos():
   print(f"Robôs montados: {totalRobo}")
   print()
   
def imprimeTemposMontagemInferiores():
   for x, y in tempoTotalMontagemInferiores.items():
      print(f"{x}: {y} segundos")
      
def imprimeTemposMontagemSuperiores():
   for x, y in tempoTotalMontagemSuperiores.items():
      print(f"{x}: {y} segundos")

while controlador:
   pecas = {"Pés": pes, "Pernas": pernas, "Tronco": tronco, "Pescoço": pescoco, "Cabeça": cabeca}
   exibePecas(pecas)
   
   for valor in pecas.values():
      if valor == 0:
         print("As peças acabaram!")
         break
   
   time.sleep(3)
   buscarPecas(pecas)
   armazenaTempo()
   imprimeTempos()   
   armazenaTempoBusca()
   
   cabeca -= 1
   pescoco -= 3
   tronco -= 3
   pernas -= 6
   pes -= 2
   totalRobo += 1
   time.sleep(2)
   
   listaTempo.clear()
   montarInferiores()
   imprimeTemposMontagemInferiores()
   montarSuperiores()
   imprimeTemposMontagemSuperiores()
   contagemRobos()
   time.sleep(2)
   
   contador += 1
   if totalRobo == 3:
      controlador = False