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
        t_de_espera = []
        t_de_retorno = []
        tempo_total_atual = 0
        i = 0
        while (len(self.dict_processos ) > 0):
            print("Processo P",i," PARA PROCESSADOR")

            t_de_resposta.append(tempo_total_atual - self.dict_processos[i][0])
            t_de_espera.append(tempo_total_atual - self.dict_processos[i][0])
            tempo_total_atual += self.dict_processos[i][1]
            t_de_retorno.append(tempo_total_atual - self.dict_processos[i][0])

            del(self.dict_processos[i])
            i += 1
        print("FILA ZERADA")
        print("Tempo de Resposta",t_de_resposta)
        print("Tempo de Retorno",t_de_retorno)
        print("Tempo de Espera",t_de_espera)
        print("Tempo Total", tempo_total_atual)

        total_t_de_resposta = 0
        total_t_de_retorno = 0
        total_t_de_espera = 0
        for i in range(len(t_de_retorno)):
            total_t_de_resposta += t_de_resposta[i]
            total_t_de_retorno += t_de_retorno[i]
            total_t_de_espera += t_de_espera[i]

        media_t_de_resposta = total_t_de_resposta/len(t_de_resposta)
        media_t_de_retorno = total_t_de_retorno/len(t_de_retorno)
        media_t_de_espera = total_t_de_espera/len(t_de_espera)

        print(f"FCFS [resp - ret - esp] : {media_t_de_resposta} - {media_t_de_retorno} - {media_t_de_espera}")


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

### MAIN ###
dict_processos = {}
processos = escalonamento(dict_processos)
processos.leArquivo(sys.argv[1])
print(dict_processos)
processos.FCFS()

processos.leArquivo(sys.argv[1])
processos.SJF()