Voici le challenge extreme de ce CTF  

Pour ce challenge de Cryptanalyse on nous fournit un code python *challenge.py* et un fichier *data.txt*, output du script precedent.  

Pas de mystere : Il faut se servir de l'output pour remonter au flag.  

## Comprendre challenge.py

Commencons par la fonction qui nous interesse :

```python3
def encrypt_flag(self, flag):
    iv = urandom(16)
    key = sha256(str(self.sk).encode()).digest()[:16]
    aes = AES.new(key, AES.MODE_CBC, iv=iv)
    ciphertext = aes.encrypt(pad(flag, 16))
    return ciphertext.hex(), iv.hex()
```

*data.txt* nous donne le resultat de cette fonction, on peut donc naivement tenter de reverse la fonction donnee :
```python3
def decrypt_flag(cipher, iv, sk):
    key = sha256(sk).digest()[:16]
    aes = AES.new(key , AES.MODE_CBC, iv=iv)
    flag = unpad(aes.decrypt(cipher), 16)
    print(flag)
```
Et ca marche ! ... Enfin localement... en ayant *sk*... Bon Bah plus qu'a obtenir la variable sk !  

Et pour l'avoir il faut regarder les autres datas donnees qui constituent un set de messages / signatures.

* Les messages sont obtenues par :
    ```python3
    messages = [pow(C.d, i, q) for i in range(1, 5)]
    ```
    On peut donc retenir que la valeur de **C.d** peut etre facilement retrouvee avec messages[0] !

* Les signatures sont obtenues par :
    ```python3
    def sign(self, m):
      self.get_next_nonce()
      assert self.q > m > 0
      P = self.k * self.G
      r = P.x
      assert r > 0
      s = (pow(self.k, -1, self.q) * (m + self.sk * r)) % self.q
      assert s > 0
      return r, s
    ```
    Pour retrouver sk on doit donc resoudre :
    $$s \equiv k^{-1} * (m + sk * r) \[q]  $$
    $$sk \equiv (k * s - m ) * r^{-1} \[q] $$
    Les valeurs de r et s sont obtenues dans ***data.txt***, la valeur de q est une    constante donnee par `q = P521.q`, mais k est inconnue !!
 /home/anonylouis/404CTF-2023---Write-ups/Cryptanalyse/La_ou_les_nombres_n_existent_pas/solve.py
Je resume : Pour trouver **flag** il nous faut **key**, pour trouver **key** il nous faut **sk**, pour trouver **sk** il nous **k** !

Les valeurs de k et a changent au debut de chaque generation de signature selon la formule :
```python3
self.a = (self.a + self.d) % self.q
self.k = (self.a * self.k + self.b) % self.q
```

## Les Mathematiques avec un grand M

Au total 4 inconnues : **a**, **b**, **k** et **sk**, et bien heureusement 4 equations avec nos 4 signatures :
> Toutes les prochaines equations seront modulos q  
> Je note ($m_1$, $s_1$, $r_1$) ... ($m_4$, $s_4$, $r_4$), les 4 couples de valeurs messages/signatures

$$ s_1 * k  - sk * r_1 = m_1 $$  

$$ s_2 * (a * k + b)  - sk * r_2 = m_2 $$  

$$ s_3 * ((a + d) * (a * k + b)) + b)  - sk * r_3 = m_3 $$  

$$ s_4 * ((a + 2d) * ((a + d) * (a * k + b)) + b))  - sk * r_4 = m_4 $$  

Ca fait peur ? normal  

Bon maintenant il faut simplifier ces equations pour tenter d'obtenir 4 equations lineaires et obtenir un systeme simple a resoudre !

Avec eq2 et eq3, on a :

$$ s_3 * ((a + d) * (s_2^{-1} * m_2 + sk * r_2) + b)  - sk * r_3 = m_3 $$  

Avec eq3 et eq4, on a :

$$ s_4 * ((a + 2d) * (s_3^{-1} * m_3 + sk * r_3) + b)  - sk * r_4 = m_4 $$  

Je peux egalement exprimer le terme $a * sk$ lineairement en fonction de a, sk et b avec eq1 et eq2 :

$$ a * sk = sk * r_2 * s_2^{-1}  * s_1 * r_1^{-1} + m_2 * s_2^{-1} * s_1 * r_1^{-1} - a * m_1* r_1^{-1} - b  * s_1 * r_1^{-1}$$  

Je peux maintenant developper les equations 3 et 4  et remplacer le terme $a * sk$ par sa valeur afin d'obtenir des equations lineaires !
 
* Equation 3 :

$$ sk * C_1 + b * C_2 + a * C_3 = C_4 $$ 

```python3
# Equation 3
C1 = (r[1] * pow(s[1], -1, q) * s[0] * pow(r[0], -1, q) - r[2] * pow(s[2], -1, q) * pow(r[1], -1, q) * s[1] + decrypt_d) % q
C2 = (pow(r[1], -1, q) * s[1] - s[0] * pow(r[0], -1, q)) % q
C3 = (m[1] * pow(r[1], -1, q) - m[0] * pow(r[0], -1, q)) % q
C4 = (m[2] * pow(s[2], -1, q) * pow(r[1], -1, q) * s[1] - decrypt_d * pow(r[1], -1, q) * m[1] - m[1] * pow(s[1], -1, q) * s[0] * pow(r[0], -1, q)) % q
```

* Equation 4 :

$$ sk * C_5 + b * C_6 + a * C_7 = C_8 $$ 

```python3
C5 = (r[1] * pow(s[1], -1, q) * s[0] * pow(r[0], -1, q) -  s[2] * pow(r[2], -1, q) * pow(s[3], -1, q) * r[3] + 2 * decrypt_d ) % q
C6 = (s[2] * pow(r[2], -1, q) - s[0] * pow(r[0], -1, q) ) % q
C7 = (pow(r[2], -1, q) * m[2] - m[0] * pow(r[0], -1, q) ) % q
C8 = (s[2] * pow(r[2], -1, q) * pow(s[3], -1, q) * m[3] - m[1] * pow(s[1], -1, q) * s[0] * pow(r[0], -1, q) - 2 * decrypt_d * pow(r[2], -1, q) * m[2] ) % q
```

Arriver ici, on peut voir que eq1, eq3 et eq4 sont lineaires et impossible de lineariser eq2, j'ai beau retourner le probleme comme je veux je tourne en boucle j'ai donc continuer sans lineariser eq2 :

Avec eq3 et eq4 je peux exprimer a et b en fonction de sk, et avec eq1 je peux exprimer k en fonction de sk :

$$ b = E_1 - E_2 * sk $$

$$ a = F_1 - F_2 * sk $$

$$ k = G_1 + G_2 * sk $$

> Les valeurs de E1, E2, F1, F2, G1, G2 sont trouvable dans *solve.py*

On insere alors tout dans eq2 afin d'avoir une grosse equation en fonction de sk :

$$ s_2 * (a * k + b)  - sk * r_2 = m_2 $$  

$$ s_2 * ((F_1 - F_2 * sk) * (G_1 + G_2 * sk) + E_1 - E_2 * sk)  - sk * r_2 = m_2 $$  

$$ (F_2 * G_2) * sk^{2} + (F_2 * G_1 - F_1 * G_2 + E_2 + r_2 * s_2^{-1}) * sk + (m_2 * s_2^{-1} - F_1 * G_1 - E_1) = 0 $$  

## Plus qu'a resoudre

Voici la meilleur equation que l'on puisse obtenir, encore faut il la resoudre !!  
> Attention l'equation etant modulo **q** ce n'est pas une simple equation du second degre  

Google nous parle de ***quadratic congruence***  
Et l'on peut trouver un solver python facilement sur [github](https://github.com/panoti/CH_QuadraticCongruenceSolver)

On l'appelle pour trouver **sk** et on affiche **flag**

>404CTF{N_0ub1ie_j4m415_C3lu1_qu1_cr017_5@v0ir_n'4ppr3nd_plu5.}
