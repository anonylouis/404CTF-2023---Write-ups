#!/bin/python3.11

# /!\ Ce challenge est conçu pour PYTHON 3.11 !
# Il ne FONCTIONNERA PAS SUR UNE VERSION ANTERIEURE !
# Il a été testé, et est fonctionnel sur python 3.11.0 et python 3.11.3, je ne garanti RIEN, sur les autres versions
# Modifiez le fichier à vos risques et périls.... Je ne suis pas responsable.

h = __import__('dis')
dico = {'adaptive': True}

a = ["a" for i in range(48)]

a[0], a[1], a[2] = chr(72), chr(33), chr(68)
a[3], a[4], a[5] = chr(100), chr(38), chr(78)
a[6], a[7], a[8] = chr(45), chr(118), chr(52)
a[9], a[10], a[11] = chr(114), chr(36), chr(95)
a[12], a[13], a[14] = chr(102), chr(48), chr(114)
a[15], a[16], a[17] = chr(95), chr(53), chr(112)
a[18], a[19], a[20] = chr(51), chr(99), chr(105)
a[21], a[22], a[23] = chr(97), chr(76), chr(105)
a[24], a[25], a[26] = chr(122), chr(51), chr(100)
a[27], a[28], a[29] = chr(95), chr(48), chr(112)
a[30], a[31], a[32] = chr(67), chr(111), chr(68)
a[33], a[34], a[35] = chr(51), chr(83), chr(33)
a[36], a[37], a[38] = chr(124), chr(49), chr(50)
a[39], a[40], a[41] = chr(84), chr(53), chr(89)
a[42], a[43], a[44] = chr(50), chr(50), chr(69)
a[45], a[46], a[47] = chr(77), chr(76), chr(56)

print("".join(a))

a = [ord(c) for c in a]

def check(dumas, zola):
    cody = h.Bytecode(check, **dico).dis().count('I')
    carmen = 0

    if dumas[36] + cody * dumas[37] + dumas[38] == 25556: # B 1
        carmen += 1
    if dumas[3] + cody * dumas[4] + dumas[5] == 19862: # C 1
        carmen += 1
    if dumas[21] + cody * dumas[22] + dumas[23] == 39570:
        carmen += 1
    if dumas[0] + dumas[1] + cody * dumas[2] == 35329:
        carmen += 1
    if dumas[6] + dumas[7] + cody * dumas[8] == 67347:  #FAUX
        carmen += 1
    if dumas[3] + dumas[4] + cody * dumas[5] == 100914: #FAUX
        carmen += 1
    if dumas[3] + cody * dumas[4] + dumas[5] == 49274: # C 2
        carmen += 1    
    if dumas[6] + cody * dumas[7] + dumas[8] == 61221:
        carmen += 1
    if dumas[36] + dumas[37] + cody * dumas[38] == 64773: # D 1
        carmen += 1
    if dumas[9] + dumas[10] + cody * dumas[11] == 49360:
        carmen += 1
    if dumas[9] + cody * dumas[10] + dumas[11] == 18857: # E 1
        carmen += 1
    if dumas[9] + cody * dumas[10] + dumas[11] == 46721: # E 2
        carmen += 1    
    if dumas[15] + dumas[16] + cody * dumas[17] == 58164:
        carmen += 1
    if dumas[15] + dumas[16] + cody * dumas[17] == 144852: #FAUX
        carmen += 1
    if dumas[12] + dumas[13] + cody * dumas[14] == 147438: #FAUX
        carmen += 1
    if dumas[12] + dumas[13] + cody * dumas[14] == 59202:
        carmen += 1
    if dumas[45] + cody * dumas[46] + dumas[47] == 39501:
        carmen += 1
    if dumas[12] + cody * dumas[13] + dumas[14] == 25080: # F 1
        carmen += 1
    if dumas[15] + cody * dumas[16] + dumas[17] == 27661:
        carmen += 1
    if dumas[18] + dumas[19] + cody * dumas[20] == 135810:  #FAUX
        carmen += 1
    if dumas[18] + cody * dumas[19] + dumas[20] == 128064:  #FAUX
        carmen += 1    
    if dumas[15] + cody * dumas[16] + dumas[17] == 68683:  #FAUX
        carmen += 1    
    if dumas[12] + cody * dumas[13] + dumas[14] == 62232: # F 2
        carmen += 1    
    if dumas[24] + cody * dumas[25] + dumas[26] == 66114:  #FAUX
        carmen += 1    
    if dumas[27] + cody * dumas[28] + dumas[29] == 25071: # G 1
        carmen += 1
    if dumas[6] + cody * dumas[7] + dumas[8] == 152553:  #FAUX
        carmen += 1    
    if dumas[6] + dumas[7] + cody * dumas[8] == 27099:
        carmen += 1
    if dumas[21] + dumas[22] + cody * dumas[23] == 54563:
        carmen += 1
    if dumas[45] + cody * dumas[46] + dumas[47] == 98325:  #FAUX
        carmen += 1 
    if dumas[39] + dumas[40] + cody * dumas[41] == 115125:  #FAUX
        carmen += 1
    if dumas[24] + cody * dumas[25] + dumas[26] == 26640:
        carmen += 1
    if dumas[21] + dumas[22] + cody * dumas[23] == 135833:  #FAUX
        carmen += 1
    if dumas[9] + dumas[10] + cody * dumas[11] == 122890:  #FAUX
        carmen += 1
    if dumas[39] + dumas[40] + cody * dumas[41] == 46239:
        carmen += 1
    if dumas[0] + dumas[1] + cody * dumas[2] == 87961:  #FAUX
        carmen += 1
    if dumas[27] + dumas[28] + cody * dumas[29] == 144847:  #FAUX
        carmen += 1
    if dumas[30] + dumas[31] + cody * dumas[32] == 35402:
        carmen += 1
    if dumas[27] + dumas[28] + cody * dumas[29] == 58159:
        carmen += 1
    if dumas[3] + dumas[4] + cody * dumas[5] == 40542:
        carmen += 1
    if dumas[0] + cody * dumas[1] + dumas[2] == 42776: # A 1
        carmen += 1    
    if dumas[30] + cody * dumas[31] + dumas[32] == 57633:
        carmen += 1
    if dumas[42] + cody * dumas[43] + dumas[44] == 26019: # H 1
        carmen += 1
    if dumas[18] + dumas[19] + cody * dumas[20] == 54540:
        carmen += 1
    if dumas[18] + cody * dumas[19] + dumas[20] == 51438:
        carmen += 1
    if dumas[21] + cody * dumas[22] + dumas[23] == 98394:  #FAUX
        carmen += 1    
    if dumas[24] + dumas[25] + cody * dumas[26] == 51973:
        carmen += 1
    if dumas[24] + dumas[25] + cody * dumas[26] == 129373:  #FAUX
        carmen += 1
    if dumas[30] + dumas[31] + cody * dumas[32] == 88034:  #FAUX
        carmen += 1
    if dumas[0] + cody * dumas[1] + dumas[2] == 17234: # A 2
        carmen += 1
    if dumas[30] + cody * dumas[31] + dumas[32] == 143547:  #FAUX
        carmen += 1    
    if dumas[33] + cody * dumas[34] + dumas[35] == 43078:
        carmen += 1
    if dumas[33] + dumas[34] + cody * dumas[35] == 42770: # I 1
        carmen += 1
    if dumas[33] + cody * dumas[34] + dumas[35] == 107320:  #FAUX
        carmen += 1    
    if dumas[36] + dumas[37] + cody * dumas[38] == 26073: # D 2
        carmen += 1
    if dumas[33] + dumas[34] + cody * dumas[35] == 17228: # I 2
        carmen += 1
    if dumas[39] + cody * dumas[40] + dumas[41] == 27627:
        carmen += 1
    if dumas[39] + cody * dumas[40] + dumas[41] == 68649:  #FAUX
        carmen += 1    
    if dumas[27] + cody * dumas[28] + dumas[29] == 62223: # G 2
        carmen += 1    
    if dumas[42] + cody * dumas[43] + dumas[44] == 64719: # H 2
        carmen += 1    
    if dumas[45] + dumas[46] + cody * dumas[47] == 29161:
        carmen += 1
    if dumas[42] + dumas[43] + cody * dumas[44] == 35842:
        carmen += 1
    if dumas[36] + cody * dumas[37] + dumas[38] == 63482: # B 2
        carmen += 1    
    if dumas[42] + dumas[43] + cody * dumas[44] == 89248:  #FAUX
        carmen += 1
    if dumas[45] + dumas[46] + cody * dumas[47] == 72505:  #FAUX
        carmen += 1

    zola+zola
    return carmen == 32


if len(a) != 48:
    print('mauvaise longueur')
    print('Non, c\'est pas ça...')
    exit(0)

for i in range(10): #Checker 10 fois c'est mieux que 1 seule fois ! Comme ça je suis sûr de moi...
    if not (check(a, 1) or check(a, 1)): 
        print('Non, c\'est pas ça...')
        exit(0)

print('Bravo ! Le flag est 404CTF{le mot de passe que vous avez rentré pour valider}!')
