#!/usr/bin/python3.6
#coding: utf-8
import sys
import time
import copy
import os


class escalonamento():
    def __init__(self, dict_processos):
        self.dict_processos = dict_processos

    def leArquivo(self,nome):
        i = 0
        arq = open(nome, 'r')
        for line in arq:
            lista_tempos = []
            a,b = line.strip().split()
            lista_tempos.append(int(a))
            lista_tempos.append(int(b))
            self.dict_processos[i] = lista_tempos
            i += 1
        print(self.dict_processos)
        arq.close()

    def FCFS(self):

        t_de_resposta = []
        t_de_resposta_media = 0
        t_de_espera = []
        t_de_espera_media = 0
        t_de_retorno = []
        t_de_retorno_media = 0

        clock = 0
        tempo_total = 0
        tempo_total_chegada = 0
        tempo_geral = 0
        k = 0
        lista_aux_saida = []
        lista_de_saida = []

        for j in range (len(dict_processos)):
            tempo_total += self.dict_processos[j][1]
            tempo_total_chegada += self.dict_processos[j][0]
            tempo_geral = tempo_total + tempo_total_chegada

        while clock <= tempo_geral:

            for i in self.dict_processos:
                if len(self.dict_processos) and self.dict_processos[i][0] <= clock:
                    lista_aux_saida.append(i)

            if (len(lista_aux_saida)):
                t_de_resposta.append(clock - self.dict_processos[k][0])
                t_de_espera.append(clock - self.dict_processos[k][0])
                clock += self.dict_processos[k][1]
                t_de_retorno.append(clock - self.dict_processos[k][0])
                lista_de_saida.append(self.dict_processos[lista_aux_saida[0]])
                del self.dict_processos[lista_aux_saida[0]]
                lista_aux_saida.pop()
                k += 1
            else:
                clock += 1
            lista_aux_saida = []

        for i in range(len(t_de_resposta)):
            t_de_resposta_media += t_de_resposta[i]
            t_de_espera_media += t_de_espera[i]
            t_de_retorno_media += t_de_retorno[i]
        print(f"FCFS - {t_de_retorno_media/4} - {t_de_resposta_media/4} - {t_de_espera_media/4}")
        arquivo.write(f"FCFS\t - \t{round(t_de_retorno_media/4,1)}\t - \t{round(t_de_resposta_media/4,1)}\t - \t{round(t_de_espera_media/4,1)} \n")

    def SJF(self):

        t_de_resposta = []
        t_de_resposta_media = 0
        t_de_espera = []
        t_de_espera_media = 0
        t_de_retorno = []
        t_de_retorno_media = 0

        clock = 0
        tempo_total = 0
        tempo_total_chegada = 0
        aux_dict_processos = {}
        sorted_list_dict_processos = []
        saida_list_dict_processos = []
        compara = self.dict_processos[0][0]
        aux_dict_processos_contagem = {}
        k = 0
        j = 0

        for j in range (len(dict_processos)):
            tempo_total += self.dict_processos[j][1]
            tempo_total_chegada += self.dict_processos[j][0]
            tempo_geral = tempo_total + tempo_total_chegada

        aux_dict_processos_contagem = self.dict_processos
        while clock <= tempo_geral:

            for i in self.dict_processos:
                if(self.dict_processos[i][0] <= clock ):
                    aux_dict_processos[i] = self.dict_processos[i]
                    sorted_list_dict_processos = sorted(aux_dict_processos.items(), key=lambda kv: kv[1][1])

            if(len(aux_dict_processos)):
                saida_list_dict_processos.append(sorted_list_dict_processos[0])
                t_de_resposta.append(clock - self.dict_processos[saida_list_dict_processos[k][0]][0])
                t_de_espera.append(clock - self.dict_processos[saida_list_dict_processos[k][0]][0])
                clock += saida_list_dict_processos[k][1][1]
                t_de_retorno.append(clock - self.dict_processos[saida_list_dict_processos[k][0]][0])
                del(self.dict_processos[saida_list_dict_processos[k][0]])
                k += 1
            else:
                clock += 1

            aux_dict_processos = {}

        for i in range(len(t_de_resposta)):
            t_de_resposta_media += t_de_resposta[i]
            t_de_espera_media += t_de_espera[i]
            t_de_retorno_media += t_de_retorno[i]

        print(f"SJF - {t_de_retorno_media/4} - {t_de_resposta_media/4} - {t_de_espera_media/4}")
        arquivo.write(f"SJF\t - \t{round(t_de_retorno_media/4,1)}\t - \t{round(t_de_resposta_media/4,1)}\t - \t{round(t_de_espera_media/4,1)} \n")

    def RR(self):

        #VARIAVEIS
        QUANTUM = 2                 #TEMPO MAXIMO DE PERMANENCIA DO PROCESSO
        tempo_de_pico = 0           #TEMPO TOTAL DE PICO DOS PROCESSOS
        tempo_de_chegada = 0        #TEMPO TOTAL CHEGADA É A SOMA DOS TEMPOS DE CHEGADA
        tempo_maximo = 0            #TEMPO MAXIMO É A SOMA DOS TEMPOS DE CHEGADA NO SISTEMA
        clock = 0                   #CONTAGEM DO CLOCK ATE ATINGIR O TOPO DO MAXIMO SISTEMA (tempo_maximo)
        flag_troca = False          #FLAG QUE DEFINE SE DEVE FAZER A TROCA OU NÃO
        flag_delete = False         #FLAG QUE DEFINE QUAL ELEMENTO SERÁ DELETADO
        flag_ultimo = True          #DEFINE SE O PROCESSO É O ULTIMO DISPONÍVEL
        contabilizado = False
        tempo_de_retorno = 0
        tempo_de_resposta = 0
        tempo_de_espera = 0

        #LISTAS
        modificar = []              #LISTA QUE ARMAZENA OS VALORES A MODIFICA E FUNCIONA COMO FLAG
        lista_aux_entrada = []      #LISTA AUXILIAR QUE ARBITRA QUEM ENTRARÁ NO SISTEMA
        gantt = []                  #LISTA CONTENDO A ORDEM DE ACESSOS AO PROOCESSADOR
        t_de_saida = []             #LISTA QUE CONTEM O TEMPO DE SAIDA DE UM PROCESSO
        t_de_chegada = []           #LISTA QUE DEFINE OS TEMPOS DE CHEGADA NO PROCESSADOR
        t_de_ultima = []
        t_de_disponibilidade = []


        #DICIONÁRIOS
        backup = copy.deepcopy(self.dict_processos)     #MANTEM OS VALORES ORIGINAIS ARMAZENADOS PARA MANIPULAÇÃO
        contagem = copy.deepcopy(self.dict_processos)   #USADO PARA CONTAR VALORES DE ENTRADA
        reais = copy.deepcopy(self.dict_processos)      #CONTEM TODOS OS VALORES REAIS

        #CALCULO DO TEMPO MAXIMO DO SISTEMA
        for j in range (len(self.dict_processos)):
            tempo_de_pico += self.dict_processos[j][1]
            print( tempo_de_pico)
            tempo_de_chegada += self.dict_processos[j][0]
            tempo_maximo = tempo_de_pico + tempo_de_chegada

        #ENQUANTO O CLOCK FOR MENOR QUE TEMPO GERAL, FAZ-SE O INCREMENTO DO TEMPO
        while clock <= tempo_maximo:
            print("----------------------------------------CLOCK ",clock)

            #FOR QUE DEFINE A LISTA DE ENTRADA DE ONDE SAIRÁ O PROCESSO CORRETO A SER
            #PROCESSADO, SEGUINDO A LOGICA, A PRIORIDADE É DADA POR POSIÇÃO NESSA LISTA
            #SENDO O ELEMENTO DE INDICE ZERO O ELEMENTO COM MAIS PRIORIDADE SOBRE
            for i in self.dict_processos:
                print ("VALORES DE DICT",self.dict_processos[i][0])
                if self.dict_processos and self.dict_processos[i][0] <= clock:
                    lista_aux_entrada.append(i)
                    modificar.append(i)
                    print("modificado")

            #TROCA A POSIÇÃO DO PRIMEIRO PROCESSO COLOCANDO-O NO ULTIMO LUGAR
            if flag_troca:
                lista_aux_entrada.append(lista_aux_entrada[0])
                lista_aux_entrada.pop(0)
                print("APOS MODIFICAR",lista_aux_entrada)
            else:
                print("MODIFICADO POR RETIRADA DE PROCESSOS")
            #RETIRA DO DICIONARIO DE PROCESSOS AQUELES QUE JÁ ENTRARAM NA LISTA
            #DE ENTRADA PARA O PROCESSADOR
            if modificar:
                for j in range(len(modificar)):
                    del self.dict_processos[modificar[j]]
                modificar = []

            #VERIFICA SE TEM PROCESSO LISTA AUXILIAR DE ENTRADA
            if (lista_aux_entrada):

                #PROCURA O ELEMENTO QUE É IGUAL AO ELEMENTO NO PROCESSADOR
                #E ARMAZENA SEU VALOR DE CHEGADA
                for k in contagem:
                    if k == lista_aux_entrada[0]:
                        t_de_chegada.append([lista_aux_entrada[0],clock])
                        flag_delete = True
                #DELETA PARA NÃO PERMITIR NOVO REGISTRO
                if flag_delete:
                    del contagem[lista_aux_entrada[0]]
                    flag_delete = False
                print("SOBREVIVENTES",contagem)

                #VERIFICA SE HÁ PROCESSOS PARA ENTRAR, COLOCA-OS DENTRO OU NÃO
                #E EM MOMENTO OPORTUNO RETIRA-OS ATÉ QUE NÃO RESTE MAIS PROCESSOS
                print("BACKUP __________________",contagem)
                if(backup[lista_aux_entrada[0]][1] > QUANTUM):
                    print("VALORES AQUI", self.dict_processos)
                    #FAZ A CONTAGEM DO ULTIMO MOMENTO DE CHEGADA NO PROCESSADOR DE UM PROCESSO
                    if len(lista_aux_entrada) == 1 and not contabilizado:
                        t_de_ultima.append([lista_aux_entrada[0],clock])
                        flag_ultimo = False
                        contabilizado = True

                    clock += QUANTUM
                    backup[lista_aux_entrada[0]][1] = backup[lista_aux_entrada[0]][1] - QUANTUM
                    print (backup)
                    gantt.append(lista_aux_entrada[0])
                    flag_troca = True
                #ENTRA NESSA SEÇÃO SE FOR MENOR QUE O TEMPO DE QUANTUM, ASSIM FAZENDO A SAÍDA DO SISTEMA
                else:

                    if(flag_ultimo):
                        t_de_ultima.append([lista_aux_entrada[0],clock])

                    clock += backup[lista_aux_entrada[0]][1]
                    backup[lista_aux_entrada[0]][1] = 0
                    gantt.append(lista_aux_entrada[0])
                    t_de_saida.append([lista_aux_entrada[0],clock])
                    print("t de saída ----> ", t_de_saida)
                    lista_aux_entrada.pop(0)
                    flag_troca = False
            else:
                clock += 1

            print(lista_aux_entrada)

            print("GANTT ", gantt)
            print("TEMPO DE CHEGADA", t_de_chegada)
            print("PROCESSO - TEMPO DE SAIDA",t_de_saida)
            print("PRINT DAS ULTIMAS OCORRENCIA", t_de_ultima)
            print("ULTIMA",t_de_ultima)

        #TRANSFORMANDO UMA COLUNA DO DICIONARIO EM UMA LISTA
        # for lll in reais:
        #     t_de_duracai.append(reais[lll][0])
        # print(t_de_duracao)

        for i in range(len(t_de_chegada)):
            #TIRA O TEMPO DE CHEGADA AO SISTEMA DO TEMPO DE SAÍDA
            print("T DE SAIDA ::::::: ", t_de_saida)
            print("T DE CHEGADA ::::: ",t_de_chegada)
            print("BACKUP ::::::::::: ",backup)
            print("T DE ULTIMA :::::: ",t_de_ultima)
            print("REAIS ::::::::: ", reais)
            # tempo_de_retorno += (t_de_saida[i][1] - t_de_chegada[i][1])
            tempo_de_retorno += (t_de_saida[i][1] - backup[i][0])
            tempo_de_resposta += (t_de_chegada[i][1])
            print(t_de_saida)
            print(backup)
            print(reais)
            tempo_de_espera += t_de_saida[i][1] - backup[i][0] - reais[i][1]

        for j in backup:
            #SOMA AO TEMPO DE CHEGADA O VALOR DOS TEMPOS DE CHEGADA AO SISTEMA
            tempo_de_resposta -= backup[j][0]
            print(reais[j][1], " E ", backup[j][0])

        print(f"RR - {tempo_de_retorno/4} - {tempo_de_resposta/4} - {tempo_de_espera/4}")
        arquivo.write(f"RR\t - \t{round(tempo_de_retorno/4,1)}\t - \t{round(tempo_de_resposta/4,1)}\t - \t{round(tempo_de_espera/4,1)} \n")

### MAIN ###
arquivo = open("SO_saida.txt", "w")
dict_processos = {}
processos = escalonamento(dict_processos)

processos.leArquivo(sys.argv[1])
print(dict_processos)
processos.FCFS()

processos.leArquivo(sys.argv[1])
processos.SJF()

processos.leArquivo(sys.argv[1])
processos.RR()

arquivo.close()
print("--------------------------------- END LOG ---------------------------------\n")
os.system("cat SO_saida.txt")