pour lancer le code principal taper :

uv run randomwalkcode 

on a l'existence des differents parsers:
    --N    indique le nombre de particules (1 par défaut)
    --n    indique le nombre d'étapes (100 par défaut)
    -x si on veut la GUI  (non par défaut)
    --fps   indique le nombre d'images par seconde (5 par défaut)
    -o    indique le nom du fichier (finalstate.txt par défaut)

pour lancer le test des fonctions taper : 

uv run python -m pytest test_randomwalkcode.py --cov=randomwalkcode --cov-report=term-missing