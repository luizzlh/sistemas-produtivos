import time, random

totalRobo = 0
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

while controlador:
   pecas = {"Pés": pes, "Pernas": pernas, "Tronco": tronco, "Pescoço": pescoco, "Cabeça": cabeca}
   
   print("-----------------------------------------------")
   print("Total de peças disponíveis")
   print(f"Cabeça: {pecas['Cabeça']}")
   print(f"Pescoço: {pecas['Pescoço']}")
   print(f"Tronco: {pecas['Tronco']}")
   print(f"Pernas: {pecas['Pernas']}")
   print(f"Pés: {pecas['Pés']}")
   print("-----------------------------------------------")
   print()
   
   for valor in pecas.values():
      if valor == 0:
         print("As peças acabaram!")
         break
   
   time.sleep(3)

   for chave, valor in pecas.items():
      print("Procurando por uma peça...")
      tempo = random.randint(1, 2)
      time.sleep(tempo)
      print("Tempo para encontrar a peça: ", tempo, " segundos.")
      print(f"Peça encontrada: {chave}", "\n")
      listaTempo.append(tempo)
      time.sleep(1)

   i = 1
   chavesDict = {1: "Pés", 2: "Pernas", 3: "Tronco", 4: "Pescoço", 5: "Cabeça"}
   for tempo in listaTempo:
      chave = f"Tempo {chavesDict[i]}"
      meu_dict[chave] = tempo
      i+=1
      
   bdTempo.update({"Tempo": meu_dict})
   
   print("Tempos de busca de cada peça do robô:")
   for categoria, tempos in bdTempo.items():
      for chave, valor in tempos.items():
         print(f"{chave}: {valor} segundos.")
         time.sleep(2)
         
   tempoBusca = 0
   for x in listaTempo:
      tempoBusca += x
   
   chaveContadorBusca = f"Ciclo {contador}"
   tempoTotalBuscaPecas[chaveContadorBusca] = tempoBusca
   print(f"Tempo total para encontrar todas as peças: {tempoBusca} segundos.")
   tempoBusca = 0
   time.sleep(2)
   
   cabeca -= 1
   pescoco -= 3
   tronco -= 3
   pernas -= 6
   pes -= 2
   totalRobo += 1
   
   listaTempo.clear()
   
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

   print(f"Robôs montados: {totalRobo}")
   print()
   time.sleep(2)
   
   contador += 1
   
   if totalRobo == 3:
      controlador = False