#!/usr/bin/python3.6
#coding: utf-8
import sys
import time

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
        print("\n\n--------------- INICIO DO FCFS ---------------\n\n")

        t_de_resposta = []
        t_de_resposta_media = 0

        clock = 0
        tempo_total = 0
        tempo_total_chegada = 0
        tempo_geral = 0
        k = 0
        lista_aux_saida = []
        lista_de_saida = []

        for j in range (len(dict_processos)):
            tempo_total += self.dict_processos[j][1]
            # print("TEMPO TOTAL",tempo_total)
            tempo_total_chegada += self.dict_processos[j][0]
            # print("TEMPO CHEGADA",tempo_total_chegada)
            tempo_geral = tempo_total + tempo_total_chegada
            # print("TEMPO GERAL",tempo_geral)
        print( "Tempo GERAL--->", tempo_geral )

        while clock <= tempo_geral:

            for i in self.dict_processos:
                if len(self.dict_processos) and self.dict_processos[i][0] <= clock:
                    #print("NO CLOCK :",clock," TEMOS :", self.dict_processos[i][0])
                    lista_aux_saida.append(i)
                    #print(lista_aux_saida)

            if (len(lista_aux_saida)):
                print("SAIU",self.dict_processos[lista_aux_saida[0]])
                t_de_resposta.append(clock - self.dict_processos[k][0])
                clock += self.dict_processos[k][1]
                lista_de_saida.append(self.dict_processos[lista_aux_saida[0]])
                del self.dict_processos[lista_aux_saida[0]]
                lista_aux_saida.pop()
                k += 1
            else:
                clock += 1
            lista_aux_saida = []

        for i in range(len(t_de_resposta)):
            t_de_resposta_media += t_de_resposta[i]
        print(t_de_resposta_media/4)

        print("\n\n SAIDA FINAL :",lista_de_saida)
        # t_de_resposta = []
        # t_de_espera = []
        # t_de_retorno = []

        # tempo_total_atual = 0
        # i = 0
        # while (len(self.dict_processos ) > 0):
        #     print("Processo P",i," PARA PROCESSADOR")

        #     t_de_resposta.append(tempo_total_atual - self.dict_processos[i][0])
        #     t_de_espera.append(tempo_total_atual - self.dict_processos[i][0])
        #     tempo_total_atual += self.dict_processos[i][1]
        #     t_de_retorno.append(tempo_total_atual - self.dict_processos[i][0])

        #     del(self.dict_processos[i])
        #     i += 1
        # print("FILA ZERADA")
        # print("Tempo de Resposta",t_de_resposta)
        # print("Tempo de Retorno",t_de_retorno)
        # print("Tempo de Espera",t_de_espera)
        # print("Tempo Total", tempo_total_atual)

        # total_t_de_resposta = 0
        # total_t_de_retorno = 0
        # total_t_de_espera = 0

        # for i in range(len(t_de_retorno)):
        #     total_t_de_resposta += t_de_resposta[i]
        #     total_t_de_retorno += t_de_retorno[i]
        #     total_t_de_espera += t_de_espera[i]

        # media_t_de_resposta = total_t_de_resposta/len(t_de_resposta)
        # media_t_de_retorno = total_t_de_retorno/len(t_de_retorno)
        # media_t_de_espera = total_t_de_espera/len(t_de_espera)

        # print(f"FCFS [resp - ret - esp] : {media_t_de_resposta} - {media_t_de_retorno} - {media_t_de_espera}")


    def SJF(self):
        print("\n\n--------------- INICIO DO JSF ---------------\n\n")
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
        print( "Tempo GERAL--->", tempo_geral )

        aux_dict_processos_contagem = self.dict_processos
        while clock <= tempo_geral:
            print("CLOCK --- ",clock)

            for i in self.dict_processos:
                print("self.dict_processos  ",self.dict_processos )
                print("----------------------------FOR--------------------------")
                if(self.dict_processos[i][0] <= clock ):
                    aux_dict_processos[i] = self.dict_processos[i]
                    # aux_dict_processos_contagem[i] = self.dict_processos[i]
                    print(aux_dict_processos)
                    sorted_list_dict_processos = sorted(aux_dict_processos.items(), key=lambda kv: kv[1][1])
                    print(sorted_list_dict_processos)

                print("SORTED --> ",sorted_list_dict_processos)
            print("-------------------------FIM---FOR--------------------------")
            # print("COMPARAÇÃO ::::::::::::::",compara)

            # if(len(aux_dict_processos_contagem)):
            #     print("COND. DE PARADA :: ",sorted_list_dict_processos)
            #     del aux_dict_processos_contagem[sorted_list_dict_processos[0][0]]
            #     saida_list_dict_processos.append(sorted_list_dict_processos[0])
            #     print("ENTREI NO IF -----------", saida_list_dict_processos)
            #     print("PROCESSO --->",saida_list_dict_processos)
            #     clock += saida_list_dict_processos[k][1][1]
            #     self.dict_processos[saida_list_dict_processos[k][0]] = [saida_list_dict_processos[k][1][0],1000]
            #     print("VALOR MODIFICADO",dict_processos)
            #     k += 1
            #     print("----------------------------------- FIM ", self.dict_processos)
            # else:
            #     clock += 1
            # print("FIM  CLOCK")

            if(len(aux_dict_processos)):
                saida_list_dict_processos.append(sorted_list_dict_processos[0])
                print("ENTREI NO IF -----------", saida_list_dict_processos)
                print("PROCESSO --->",saida_list_dict_processos)
                clock += saida_list_dict_processos[k][1][1]
                print(k)
                # self.dict_processos[saida_list_dict_processos[k][0]] = [saida_list_dict_processos[k][1][0],1000]
                del(self.dict_processos[saida_list_dict_processos[k][0]])
                print("VALOR MODIFICADO",self.dict_processos)
                k += 1
                print("----------------------------------- FIM ", self.dict_processos)
            else:
                clock += 1
            print("FIM  CLOCK")

            # compara = sorted_list_dict_processos[0][0]
            aux_dict_processos = {}
        print("CLOCK FINAL",clock)

    def RR(self):
        QUANTUM = 4
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
        atualizados = []

        for j in range (len(dict_processos)):
            tempo_total += self.dict_processos[j][1]
            tempo_total_chegada += self.dict_processos[j][0]
            tempo_geral = tempo_total + tempo_total_chegada
        print( "Tempo GERAL--->", tempo_geral )

        while clock <= tempo_geral:
            print ("___________________________________",clock)


            for i in self.dict_processos:
                if len(self.dict_processos) and self.dict_processos[i][0] <= clock:
                    # print("NO CLOCK :",clock," TEMOS :", self.dict_processos[i][0])
                    lista_aux_saida.append(i)
                    print("AUXILIAR",lista_aux_saida)

            if (len(lista_aux_saida)):
                #t_de_resposta.append(clock - self.dict_processos[k][0])
                if(self.dict_processos[lista_aux_saida[0]][1] > QUANTUM):
                    clock += QUANTUM
                    self.dict_processos[lista_aux_saida[0]][1] = self.dict_processos[lista_aux_saida[0]][1] - QUANTUM

                    lista_nova_aux_saida.append(self.dict_processos[lista_aux_saida[0]].copy())
                    print("LISTA NOVA AUX - ",lista_nova_aux_saida)
                    atualizados.append(self.dict_processos[lista_aux_saida[0]])
                    del self.dict_processos[lista_aux_saida[0]]
                else:
                    clock += self.dict_processos[lista_aux_saida[0]][1]
                    self.dict_processos[lista_aux_saida[0]][1] = 0
                    lista_de_saida.append(self.dict_processos[lista_aux_saida[0]].copy())
                    lista_nova_aux_saida.append(self.dict_processos[lista_aux_saida[0]].copy())
                    print(lista_nova_aux_saida)
                    print("SAIU",self.dict_processos[lista_aux_saida[0]])
                    del self.dict_processos[lista_aux_saida[0]]
                    del backup[lista_aux_saida[0]]

                lista_aux_saida.pop()
                print ("VALOR DE K = ",k)
                k += 1
            else:
                clock += 1

            lista_aux_saida = []
            print("atualizados",atualizados," e processos")
            if(atualizados):
                self.dict_processos = backup.copy()
                k = 0
                for tam in range(len(atualizados)):
                    print (tam)
                    if atualizados[tam][1] > 0:
                        self.dict_processos[tam][0] = atualizados[tam][0]
                        self.dict_processos[tam][1] = atualizados[tam][1]
                    else:
                        del self.dict_processos[tam]
                atualizados = []
        print(lista_nova_aux_saida)
        print(lista_de_saida)

### MAIN ###
dict_processos = {}
processos = escalonamento(dict_processos)
# processos.leArquivo(sys.argv[1])
# print(dict_processos)
# processos.FCFS()

# processos.leArquivo(sys.argv[1])
# processos.SJF()

processos.leArquivo(sys.argv[1])
processos.RR()