# ListGen

Petit outil Python avec interface Tkinter pour générer une liste d'entiers aléatoires et explorer ses statistiques.

## Fonctionnalités

- Choix des bornes minimum et maximum et de la taille de la liste.
- Affichage de la liste générée et de sa version triée.
- Calcul du minimum, du maximum, de la moyenne et de la médiane.
- Interface en français avec fond animé.

## Lancer l'application

Prérequis : **Python 3** avec **Tkinter** et un environnement graphique.

```bash
git clone https://github.com/GameNotCreator/listgen.git
cd listgen
python main.py
```

Le programme utilise uniquement la bibliothèque standard de Python. Certaines distributions Linux proposent Tkinter dans un paquet séparé.

## Utilisation

Saisir des bornes entières non négatives, avec **minimum ≤ maximum**, et une taille **strictement positive**, puis cliquer sur « Générer la liste ».

## Structure et limites

Toute l'application se trouve dans `main.py`. Il s'agit d'un exercice pédagogique : le tri utilise deux boucles imbriquées et convient à de petites listes.

La validation actuelle ne rejette pas une taille nulle ni des bornes inversées avant le calcul. La médiane affichée est arrondie à l'entier. Ces limites sont à prendre en compte lors de l'utilisation.
