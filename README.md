# Sudoku-Magic
Sudoku programma voor mensen die uitdagende puzzels wil oplossen. Het bevat een mooie vormgeving en een algoritme die u kan helpen als u niet uit de puzzel komen kan.

# Probleembeschrijving

Stel je voor je bent een groot fan van Sudoku en andere puzzels en je gaat dus door boeken heen alsof het niks is. Dit is het geval voor mijn oma ze is super snel met het oplossen en heeft dus erg veel afgeronden puzzelboeken thuis liggen die niet meer gebruikt worden. Dit kan natuurlijk best een kostenpost worden en over het algemeen zijn de sudoku’s in de boeken niet de allermoeilijkste. 

Hierom heb ik een applicatie gemaakt die op 4 verschillende niveau’s sudoku’s genereert die bijna nooit hetzelfde zijn van elkaar. Het minimale aantal cijfers nodig voor een unieke oplossing van een sudoku board is 17 cijfers. Dit is dus ook de grootste uitdaging en deze uitdaging is ook speelbaar in de applicatie.

# Het algoritme
Het algoritme wat ik geschreven heb gaat op zoek naar een lege cell. Vervolgens vult die met een loop cijfers van 1 tot 9 in. Per cijfer worden er checks uitgevoerd of het valid is in die cell. Als dat het geval is word het algoritme zelf aangeroepen, dit is de recursie. Het moment dat er geen valid cijfers zijn. Word de huidige cell waar net cijfers in geprobeerd zijn terug veranderd naar 0 en word de voorgaande cel een cijfer groter gekozen, dit is het backtracking gedeelte. Vervolgens word dit gedaan zolang als er geen lege plekken meer zijn in het Sudoku board.

# Requirements

Er zijn een aantel libraries nodig om het programma goed te laten werken. 
```
pip install -r requirements.txt
```

&&

Tkinter moet geïnstalleerd en werken zijn.