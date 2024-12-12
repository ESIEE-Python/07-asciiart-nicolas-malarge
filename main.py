"""
Voici mon code pour l'exercie ASCIIART
"""
import sys
sys.setrecursionlimit(1100)
#### Imports et définition des variables globales


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de 
    caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    c = []
    n = []
    p = []
    ind = 0
    c.append(s[ind])
    n.append(1)
    for i in range(1,len(s)):
        if s[i] == c[-1]:
            n[-1] += 1
        else :
            c.append(s[i])
            n.append(1)
            ind += 1
        i+=1

    for i in zip(c,n):
        p.append(i)
    return p


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    if not s:
        return []
    ind = 1
    while ind < len(s) and s[ind] == s[0]:
        ind += 1
    return [(s[0], ind)] + artcode_r(s[ind:])

#### Fonction principale


def main():
    """
    Retourne deux fois de maniere iteratif et recursif
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
