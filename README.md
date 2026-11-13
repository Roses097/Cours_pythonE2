# 🐍 Cours Python E2 Dijon

## ℹ️ Overview

Ensemble des TP informatique Python réalisés pendant le cours E2 à Dijon (ESEO).

### ✍️ Author

- **Name** : Starosciak Rayane
- **GitHub** : [@Roses097](https://github.com/Roses097)
- **Discord** : [@rei_ayanami01](https://discord.com/users/rei_ayanami01)

---

## 📋 Software / Hardware

### Software
- Python 3
- pip
- Packages Python : `rich`, `requests`
- Git (CLI)

### System
- macOS (Apple Silicon, Tahoe)

---

## 📑 Sommaire

- [TP1 : Les bases](#tp1--les-bases)
- [TP2 : Collections](#tp2--collections)
- [TP3 : Fichiers, exceptions, récursivité](#tp3--fichiers-exceptions-récursivité)
- [TP4 : Introduction à la POO](#tp4--introduction-à-la-poo)
- [TP5 : POO suite (héritage)](#tp5--poo-suite-héritage)
- [Notes de cours](#-notes-de-cours)
- [Commandes utiles](#️-commandes-utiles)

---

## 🚀 TP infos

### TP1 : Les bases

| Exo | Sujet | Notions |
|---|---|---|
| 01 | Calcul de l'IMC | `input`, conversion en `float`, formule |
| 02 | Saisie de N entiers jusqu'à un nombre négatif | boucle `while`, listes, `sorted`, `min`, `max`, moyenne |
| 03 | Années humaines → années canines | conditions `if / elif / else`, message d'erreur |
| 04 | Approximation de π (série) | boucle `for`, `range`, alternance de signe |
| 05 | Décimal → binaire | division entière `//`, modulo `%`, chaînes |
| 06 | Calculatrice (a, s, m, d) | gestion de la division par 0, saisie insensible à la casse, boucle « Un autre calcul ? » |
| 07 | Générateur de plaques d'immatriculation `AA-111-AA` | `random`, exclusion des lettres I, O, U et de la combinaison SS |

**DLC**
- **Menu principal (`main.py`)** : point d'entrée qui importe les fonctions de chaque exo et affiche un menu. Si un paramètre est passé au script, l'exo est lancé directement.
- **FizzBuzz** : multiples de 3 → `Fizz`, de 5 → `Buzz`, des deux → `Fizzbuzz`.
- **Duel de cartes** : 10 manches, le joueur prédit si la prochaine carte est supérieure ou non.

```python
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        choix = sys.argv[1]      # python3 main.py 5
    else:
        choix = input("Choix utilisateur : ")
```

```bash
python3 main.py        # affiche le menu
python3 main.py 5      # lance directement l'exo 5
```

---

### TP2 : Collections

| Exo | Sujet | Notions |
|---|---|---|
| 01 | Référence vs copie | `b = a` copie une **référence** ; `copy.copy`, `copy.deepcopy`, `a[:]` |
| 02 | Dictionnaire imbriqué (élève Mike) | accès, modification et ajout de clés, liste dans un dict, `len` |
| 03 | Tableau d'entiers tous différents ? | `set`, comparaison de `len` |
| 04 | Score de baseball | pile (`list`) : `append`, `pop`, opérations `+`, `D`, `C` |
| 05 | Polynômes | `collections.deque`, liste chaînée |
| 06 | Universités via une API | `requests`, JSON, filtre, tri par État, affichage lisible |

**DLC : Bingo de Kakul** : grille 5×5, cases `VIDE` / `MARQUE` / `BRULANTE`, actions `UNDO`, `RESET`, `EXIT` (historique des états).

```python
import copy
a = ["A"]
b = a                    # même objet : modifier b modifie a
c = copy.copy(a)         # copie superficielle
d = copy.deepcopy(a)     # copie profonde
e = a[:]                 # copie par slicing
```

```python
import collections
poly = collections.deque([10, 5, 3])   # 10x² + 5x + 3
poly.append(1)                         # ajout à la fin
poly.appendleft(2)                     # ajout au début
poly.popleft()                         # retire au début
```

---

### TP3 : Fichiers, exceptions, récursivité

Travail dans une branche dédiée `TP3`.

| Exo | Sujet | Notions |
|---|---|---|
| 1 | Factorielle | fonction **récursive** |
| 2 | Suite de Syracuse | récursivité, arrêt quand la valeur vaut 1 |
| 3 | `HeadTail.py` : afficher le début ou la fin d'un fichier | arguments en ligne de commande, `ValueError`, `IOError` |
| 4 | Jeu du pendu | lecture de `dic.txt`, `random.choice`, **exception personnalisée** dans un autre fichier |
| 5 | Tour de Hanoi | récursivité, écriture des mouvements dans `hanoi.txt` |

```bash
./HeadTail.py head 15 dic.txt
```

```python
# Exception personnalisée (fichier séparé, puis importé)
class LettreDejaProposeeError(Exception):
    pass
```

```python
# Récursivité : toujours un cas d'arrêt
def factorielle(n):
    if n <= 1:
        return 1
    return n * factorielle(n - 1)
```

---

### TP4 : Introduction à la POO

Fusion de la branche `TP3` dans `main` via une **Pull Request** avant de commencer.

| Exo | Sujet | Notions |
|---|---|---|
| 01 | Classe `Product` | `__init__`, méthode `get_price_it`, **attribut de classe** (taxe = 0.2) |
| 02 | Classe `Fraction` | **surcharge d'opérateurs** : `__str__`, `+ - * /`, `> < <= >= == !=` |
| 03 | Jeu de cartes : `CardValue`, `CardColor`, `Card`, `Deck` | `__str__`, `__repr__`, `is_equal_value`, `shuffle`, `draw`, `discard` |
| 03 (étape 3) | Duel de cartes recodé en POO | composition d'objets |

```python
class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __add__(self, other):
        return Fraction(self.num * other.den + other.num * self.den,
                        self.den * other.den)

    def __str__(self):
        return f"{self.num}/{self.den}"
```

---

### TP5 : POO suite (héritage)

| Exo | Sujet | Notions |
|---|---|---|
| 1 | `Rectangle` et `Carre` | **héritage**, surcharge d'un attribut |
| 2 | `Airplane` → `CivilAircraft`, `CargoAircraft`, `MilitaryAircraft` + `Airport` | classe mère / classes filles, `super().__init__`, `__str__`, composition avec des listes |

```python
class Airplane:
    def __init__(self, name):
        self.name = name
        self.fly = False

class CivilAircraft(Airplane):
    def __init__(self, name):
        super().__init__(name)
        self.nb_passenger = 0
```

---

## 📚 Notes de cours

### Boucles
- `while` : nombre de répétitions inconnu, on connaît la condition d'arrêt. Penser à incrémenter pour éviter la boucle infinie (`CTRL + C` pour l'arrêter).
- `for ... in range(n)`, `range(p, n)`, `range(p, n, k)` : nombre de répétitions connu.
- `break` interrompt une boucle (à utiliser avec modération).
- Boucles imbriquées : un compteur différent par boucle.

### Exceptions
```python
try:
    resultat = a / b
except ZeroDivisionError:
    print("Division par zéro")
except (TypeError, NameError) as e:
    print("Erreur :", e)
else:
    print("Résultat :", resultat)   # si aucune erreur
finally:
    print("Toujours exécuté")       # nettoyage

raise ValueError("valeur invalide")  # déclencher une exception
```
Toujours préciser le type d'exception après `except`.

| Exception | Cause |
|---|---|
| `ValueError` | valeur incohérente (`int("é")`) |
| `TypeError` | opération incompatible (`'2' + 2`) |
| `NameError` | nom inexistant |
| `IndexError` / `KeyError` | indice / clé inexistant(e) |
| `ZeroDivisionError` | division par 0 |
| `IOError` / `OSError` | erreur fichier / système |

### Récursivité
- Une fonction qui s'appelle elle-même (appel direct ou indirect).
- **Tail** : le dernier appel est l'appel récursif. **Non-tail** : du code s'exécute après l'appel.
- Toujours prévoir une condition d'arrêt, sinon boucle infinie / consommation excessive de ressources.
- Plus lisible qu'une boucle pour certains problèmes, mais plus gourmand en mémoire.

### Listes chaînées
- Collection de nœuds (valeur + lien vers le suivant). Simple ou doublement chaînée.
- Avantages : insertions/suppressions rapides, pas de décalage d'index. Inconvénients : pas d'accès aléatoire, plus de mémoire.
- En Python : `collections.deque` (double liste chaînée, file / queue).

---

## ⌨️ Commandes utiles

### Python / pip

| Commande | Description |
|---|---|
| `python3 main.py` | Lancer un script |
| `python3 main.py 5` | Lancer un script avec un paramètre |
| `python3 -m pip install <package>` | Installer un package (`rich`, `requests`...) |
| `python3 -m pip uninstall <package>` | Désinstaller un package |
| `python3 -m pip list` | Lister les packages installés |
| `python3 -m pip freeze > requirements.txt` | Sauvegarder les dépendances |
| `python3 -m pip install -r requirements.txt` | Installer les dépendances d'un projet |

### Environnement virtuel

| Commande | Description |
|---|---|
| `python3 -m venv venv` | Créer l'environnement |
| `source venv/bin/activate` | Activer l'environnement (macOS / Linux) |
| `deactivate` | Désactiver l'environnement |

### Git

| Commande | Description |
|---|---|
| `git clone <url>` | Cloner un dépôt |
| `git status` | Voir l'état des fichiers |
| `git add .` | Ajouter tous les changements |
| `git commit -m "message"` | Valider les changements |
| `git push` | Envoyer sur GitHub |
| `git pull` | Récupérer les changements distants |
| `git checkout -b TP3` | Créer et se placer sur une nouvelle branche |
| `git push -u origin TP3` | Publier la branche sur GitHub |
| `git checkout main` | Revenir sur la branche `main` |

Fusion d'une branche : onglet **Pull Requests** sur GitHub → créer la PR `TP3 → main` → valider.

### .gitignore conseillé

```text
venv/
__pycache__/
```
