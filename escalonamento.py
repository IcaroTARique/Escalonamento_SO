#!/usr/bin/python3.6
#coding: utf-8
import sys
import time
import copy

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

    def RR(self):

        t_de_resposta = []
        t_de_resposta_media = 0
        t_de_espera = []
        t_de_espera_media = 0
        t_de_retorno = []
        t_de_retorno_media = 0

        QUANTUM = 2
        clock = 0
        tempo_total = 0
        tempo_total_chegada = 0
        tempo_geral = 0
        k = 0
        lista_aux_saida = []
        lista_de_saida = []
        lista_nova_aux_saida = []
        registro_de_CPU = []
        backup = self.dict_processos.copy()
        referencial = copy.deepcopy(self.dict_processos)
        atualizados = []
        atualizados_key = []

        #TESTE
        conferencias = []
        check = []
        confere = copy.deepcopy(self.dict_processos)
        non_repeatable = []
        primeiros = []
        aux_de_retorno = []
        aux_de_resposta = []
        chave = 0
        getback = []

        for j in range (len(dict_processos)):
            tempo_total += self.dict_processos[j][1]
            tempo_total_chegada += self.dict_processos[j][0]
            tempo_geral = tempo_total + tempo_total_chegada

        while clock <= tempo_geral:
            print("----------------------------------------CLOCK ",clock)
            if len(self.dict_processos) == 1:
                non_repeatable = []

            for r in self.dict_processos :
                for q in range(len(non_repeatable)):
                    if (r == non_repeatable[q]):
                        check.append(r)

            for i in self.dict_processos:
                if len(self.dict_processos) and self.dict_processos[i][0] <= clock:
                    lista_aux_saida.append(i)
                    print("CRIAÇÃO :::: ",lista_aux_saida)

            if (conferencias):
                for e in range(len(conferencias)):
                    for u in range (len(lista_aux_saida)):
                        if (lista_aux_saida[u] == conferencias[e]):
                            del (lista_aux_saida[u])
                conferencias = []

            if (len(lista_aux_saida)):
                #INCREMENTA O TEMPO DE ESPERA DOS PROCESSOS
                for i in range(len(lista_aux_saida)):
                    print("LIAUX", lista_aux_saida[0])

                #PEGA AS PRIMEIRAS OCORRÊNCIAS DOS PROCESSOS
                print("LISTA AUX DE SAIDA",lista_aux_saida)
                for iii in confere:
                    print(iii, " = ", lista_aux_saida[0])
                    if iii == lista_aux_saida[0]:
                        print("entrei")
                        primeiros.append(iii)
                    print(primeiros)
                if primeiros:
                    print("DELETADO", confere[primeiros[0]])
                    aux_de_resposta.append([primeiros[0],clock])
                    aux_de_retorno.append([primeiros[0],clock - confere[primeiros[0]][0]])
                    print("AUXILIAR DE RETORNO", aux_de_retorno)
                    print("AUXILIAR DE RESPOSTA", aux_de_resposta)
                    del confere[primeiros[0]]
                    primeiros = []

                    print("ESTES SÃO OS PRIMEIROS",primeiros)
                if(self.dict_processos[lista_aux_saida[0]][1] > QUANTUM):
                    clock += QUANTUM
                    self.dict_processos[lista_aux_saida[0]][1] = self.dict_processos[lista_aux_saida[0]][1] - QUANTUM
                    lista_nova_aux_saida.append(self.dict_processos[lista_aux_saida[0]].copy())
                    non_repeatable.append(lista_aux_saida[0])
                    chave += 1
                    atualizados.append(self.dict_processos[lista_aux_saida[0]])
                    atualizados_key.append(lista_aux_saida[0])
                    del self.dict_processos[lista_aux_saida[0]]
                else:
                    #CALCULA UM POR UM OS TEMPOS DE RESPOSTA
                    for jjj in range(len(aux_de_resposta)):
                        if aux_de_resposta[jjj][0] == lista_aux_saida[0]:
                            print("PARA RESPOSTA ", aux_de_resposta[jjj][1]," - ", referencial[lista_aux_saida[0]][0])
                            t_de_resposta.append( aux_de_resposta[jjj][1] - referencial[lista_aux_saida[0]][0])
                            print("T DE RESPOSTA == ",t_de_resposta)

                    t_de_espera.append(clock - referencial[lista_aux_saida[0]][0])
                    clock += self.dict_processos[lista_aux_saida[0]][1]
                    print("ASDFAFAFSFASF",referencial[lista_aux_saida[0]][0])
                    print("referencial ---->", lista_aux_saida[0])
                    #CALCULA UM POR UM OS TEMPOS DE RETORNO
                    for jjj in range(len(aux_de_retorno)):
                        if aux_de_retorno[jjj][0] == lista_aux_saida[0]:
                            print(clock ," - ", aux_de_retorno[jjj][1])
                            t_de_retorno.append(clock - aux_de_retorno[jjj][1])
                            print("TO DENTRO ", t_de_retorno)

                    self.dict_processos[lista_aux_saida[0]][1] = 0
                    lista_de_saida.append(self.dict_processos[lista_aux_saida[0]].copy())
                    lista_nova_aux_saida.append(self.dict_processos[lista_aux_saida[0]].copy())
                    chave += 1
                    del self.dict_processos[lista_aux_saida[0]]
                    del backup[lista_aux_saida[0]]

                k += 1
            else:
                clock += 1
#----------------------------------------------------------------------------------------
            if( not lista_aux_saida and atualizados ):
                clock -=1
                self.dict_processos = backup.copy()
                k = 0

                for tam in range(len(atualizados_key)):
                    if atualizados[tam][1] > 0 :

                        self.dict_processos[atualizados_key[tam]][0] = atualizados[tam][0]
                        self.dict_processos[atualizados_key[tam]][1] = atualizados[tam][1]

                    else:
                        del self.dict_processos[tam]
                atualizados = []
                atualizados_key = []
            if lista_aux_saida:
                getback.append(lista_aux_saida[0])
                print("GET BACK",getback)
            lista_aux_saida = []

        print("PRIMEIRAS OCORRENCIAS :: ",t_de_resposta)
        print(lista_nova_aux_saida)
        print(lista_de_saida)
        print("T DE RETORNO", t_de_retorno)
        for i in range(len(t_de_retorno)):
            t_de_resposta_media += t_de_resposta[i]
            t_de_espera_media += t_de_espera[i]
            t_de_retorno_media += t_de_retorno[i]
        print(f"RR - {t_de_retorno_media/4} - {t_de_resposta_media/4} - {t_de_espera_media/4}")
### MAIN ###
dict_processos = {}
processos = escalonamento(dict_processos)
processos.leArquivo(sys.argv[1])
print(dict_processos)
processos.FCFS()

processos.leArquivo(sys.argv[1])
processos.SJF()

processos.leArquivo(sys.argv[1])
processos.RR()