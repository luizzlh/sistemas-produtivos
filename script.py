import time, random, statistics, math

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
meuDict = {}
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
      tempo = random.randint(1, 4)
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
      meuDict[chave] = tempo
      i+=1
   bdTempo.update({"Tempo": meuDict})

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

def montarInferiores():
   print()
   print("Movendo peças para a área de montagem dos membros inferiores!")
   time.sleep(2)
   print("Montando peças dos membros inferiores...")
   tempoMontagemInferiores = random.randint(6, 9)
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
   tempoMontagemSuperiores = random.randint(6,9)
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

def desvioPadrao(valoresTempos):
   totalItens = sum(valoresTempos)
   qtdItens = len(valoresTempos)
   media = totalItens / qtdItens
   valorBaseDP = 0
   for x in valoresTempos:
      valorBaseDP += (x - media) * (x - media)
   valorBaseDP = valorBaseDP / qtdItens
   valorBaseDP = math.sqrt(valorBaseDP)
   return valorBaseDP

def coeficienteVariacao(valoresTempos):
   totalItens = sum(valoresTempos)
   qtdItens = len(valoresTempos)
   media = totalItens / qtdItens
   coeficiente_variacao = (desvioPadrao(valoresTempos) / media) * 100
   return coeficiente_variacao

def calculaEstatisticas(valoresTempos):
   if not valoresTempos:
      print("Lista de tempos está vazia. Não é possível calcular estatísticas.")
      return

   tempoTotal = sum(valoresTempos)
   media = tempoTotal / len(valoresTempos)
   dp = desvioPadrao(valoresTempos)
   coefVariacao = coeficienteVariacao(valoresTempos)
   moda = statistics.mode(valoresTempos) if len(set(valoresTempos)) < len(valoresTempos) else "Sem moda"
   mediana = statistics.median(valoresTempos)
   
   print("=== Estatísticas de Tempos ===")
   time.sleep(2)
   print(f"Tempo Total: {tempoTotal:.2f} segundos")
   time.sleep(2)
   print(f"Média dos Tempos: {media:.2f} segundos")
   time.sleep(2)
   print(f"Desvio Padrão: {dp:.2f} segundos")
   time.sleep(2)
   print(f"Coeficiente de Variação: {coefVariacao:.2f}%")
   time.sleep(2)
   print(f"Moda: {moda}")
   time.sleep(2)
   print(f"Mediana: {mediana:.2f} segundos")
   time.sleep(2)

   tempoComTolerancia = media * 1.15
   print(f"Tempo Médio com 15% de Tolerância: {tempoComTolerancia:.2f} segundos")

   return tempoTotal, media, tempoComTolerancia

def calculaProducao(mediaTempo):
   if mediaTempo == 0:
      print("Média dos tempos é zero. Não é possível calcular a produção.")
      return

   tempoDisponivelDiario = 8 * 60 * 60  # 8 horas em segundos
   producaoDiaria100 = tempoDisponivelDiario / mediaTempo

   print("=== Cálculo de Produção ===")
   for eficiencia in [100, 90, 75]:
      producao = producaoDiaria100 * (eficiencia / 100)
      producao5Dias = producao * 5
      producao24Dias = producao * 24

      print(f"\nEficiência: {eficiencia}%")
      time.sleep(2)
      print(f"Produção Diária: {producao:.0f} robôs")
      time.sleep(2)
      print(f"Produção em 5 Dias: {producao5Dias:.0f} robôs")
      time.sleep(2)
      print(f"Produção em 24 Dias: {producao24Dias:.0f} robôs")
      time.sleep(2)

def calculaEstatisticasTempoTotal(dicionarioTempos, descricao):
   if not dicionarioTempos:
      print(f"Não há dados disponíveis para {descricao}.")
      return

   listaDeTempos = list(dicionarioTempos.values())
   print(f"\n=== Estatísticas para {descricao} ===")
   calculaEstatisticas(listaDeTempos)

listaTempoTotal = []

while controlador:
   pecas = {"Pés": pes, "Pernas": pernas, "Tronco": tronco, "Pescoço": pescoco, "Cabeça": cabeca}
   exibePecas(pecas)

   for valor in pecas.values():
      if valor == 0:
         print("As peças acabaram!")
         break

   buscarPecas(pecas)
   armazenaTempo()
   armazenaTempoBusca()

   tempoTotalCiclo = sum(listaTempo)

   cabeca -= 1
   pescoco -= 3
   tronco -= 3
   pernas -= 6
   pes -= 2
   totalRobo += 1

   listaTempo.clear()
   montarInferiores()
   montarSuperiores()

   contador += 1
   if totalRobo == 3:
      controlador = False

for x in tempoTotalBuscaPecas.values():
   listaTempoTotal.append(x)
for x in tempoTotalMontagemInferiores.values():
   listaTempoTotal.append(x)
for x in tempoTotalMontagemSuperiores.values():
   listaTempoTotal.append(x)

if tempoTotalBuscaPecas:
   calculaEstatisticasTempoTotal(tempoTotalBuscaPecas, "Tempo Total de Busca de Peças")

if tempoTotalMontagemInferiores:
   calculaEstatisticasTempoTotal(tempoTotalMontagemInferiores, "Tempo Total de Montagem dos Inferiores")

if tempoTotalMontagemSuperiores:
   calculaEstatisticasTempoTotal(tempoTotalMontagemSuperiores, "Tempo Total de Montagem dos Superiores")

if listaTempoTotal:
   print("\n=== Estatísticas Globais ===")
   tempoTotal, mediaTempo, tempoComTolerancia = calculaEstatisticas(listaTempoTotal)
   calculaProducao(mediaTempo)
else:
   print("Não há tempos registrados para calcular a produção.")