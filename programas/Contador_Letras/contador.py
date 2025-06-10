import os
import re

def read_file():
    try:
        file_name = input('Insira o nome do arquivo: ')
        file = open(file_name, 'rt')
        return file
    except Exception as e:
        msg = 'Erro de leitura.'
        print(msg)
        exit()

def count_letters(file):
    try:
        cont_A = cont_B = cont_C = cont_D = cont_E = 0 
        cont_F = cont_G = cont_H = cont_I = cont_J = 0
        cont_K = cont_L = cont_M = cont_N = cont_O = 0
        cont_P = cont_Q = cont_R = cont_S = cont_T = 0
        cont_U = cont_V = cont_W = cont_X = cont_Y = 0
        cont_Z = 0

        line = file.readline()
        while line != '':
            for ch in line:
                if ch.isalpha():
                    match ch.lower():
                        case 'a':
                            cont_A += 1
                        case 'b':
                            cont_B += 1
                        case 'c':
                            cont_C += 1
                        case 'd':
                            cont_D += 1
                        case 'e':
                            cont_E += 1
                        case 'f':
                            cont_F += 1
                        case 'g':
                            cont_G += 1
                        case 'h':
                            cont_H += 1
                        case 'i':
                            cont_I += 1
                        case 'j':
                            cont_J += 1
                        case 'k':
                            cont_K += 1
                        case 'l':
                            cont_L += 1
                        case 'm':
                            cont_M += 1
                        case 'n':
                            cont_N += 1
                        case 'o':
                            cont_O += 1
                        case 'p':
                            cont_P += 1
                        case 'q':
                            cont_Q += 1
                        case 'r':
                            cont_R += 1
                        case 's':
                            cont_S += 1
                        case 't':
                            cont_T += 1
                        case 'u':
                            cont_U += 1
                        case 'v':
                            cont_V += 1
                        case 'w':
                            cont_W += 1
                        case 'x':
                            cont_X += 1
                        case 'y':
                            cont_Y += 1
                        case 'z':
                            cont_Z += 1
            line = file.readline()
        print("\nNumero de letras:")
        print(f"A -> {cont_A} \nB -> {cont_B} \nC -> {cont_C} \nD -> {cont_D} \nE -> {cont_E} \nF -> {cont_F} \nG -> {cont_G}")
        print(f"H -> {cont_H} \nI -> {cont_I} \nJ -> {cont_J} \nK -> {cont_K} \nL -> {cont_L} \nM -> {cont_M} \nN -> {cont_N}")
        print(f"O -> {cont_O} \nP -> {cont_P} \nQ -> {cont_Q} \nR -> {cont_R} \nS -> {cont_S} \nT -> {cont_T} \nU -> {cont_U}")
        print(f"V -> {cont_V} \nW -> {cont_W} \nX -> {cont_X} \nY -> {cont_Y} \nZ -> {cont_Z}")
    except Exception as e:
        msg = f'Erro em contar letras do arquivo {file}.'
        print(msg)
        exit()

if __name__ == '__main__':
    file = read_file()
    count_letters(file)
