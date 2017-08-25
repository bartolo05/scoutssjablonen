# scoutssjablonen

## Getting Started

Deze instructies leggen uit hoe je een pdfsjabloon maakt met deze code,
getest met ubuntu 16.04lts, met texlive, xelatex en python2.

### Prerequisites
Om te genereren moeten python2.x of python3.x en Xelatex geinstalleerd zijn

### Genereren
genereer mastworpsjabloon in map sjablonen voor tak <tak>:
```$ python gensjabloon.py -t <tak>```

### genereren met titel
genereer sjabloon voor andere doeleinden voor tak <tak> met onderwerp <onderwerp> :
```$ python gensjabloon.py -t <tak> -o <onderwerp>```
om een ander logo dan het mastworplogo te gebruiken, plaats het logo in de map logos met de naam logo_<onderwerp>.png
logo moet ongeveer grootteverhouding 13/8 hebben
als het logo niet gevonden wordt, wordt het mastworplogo gebruikt

### genereren voor elke tak
genereer voor elke tak:
```$ python gensjabloon.py -a```
of
```$ python gensjabloon.py -a -o <onderwerp>```

### .tex file genereren
genereer de .tex broncode in de tex map met
```$ python gensjabloon.py -t <tak> -s```
```$ python gensjabloon.py -t <tak> -o <onderwerp> -s```

### opmerking over jinlogo
opmerking, jin logo wordt enkel in jin sjabloon gegenereerd
om een niet jin sjabloon te genereren met het jin logo:
```$ python gensjabloon.py -t <tak> -j```
```$ python gensjabloon.py -t <tak> -o <onderwerp> -j```

### lijst van geaccepteerde taknamen:	
 
 * kapoenen, kapoenen1, kapoenen2:			logos/logo_01kapoenen.png,
 * welpen,	kabouters, kawelpen: 			logos/logo_02kawelpen.png,
 * jonggidsen, jongverkenners, jonggivers: 	logos/logo_03jonggivers.png,
 * givers:						logos/logo_04givers.png,
 * jin: 						logos/logo_05jin.png,
 * leiding: 					logos/logo_06leiding.png,
 * groeps, groepsleiding: 				logos/logo_07groepsleiding.png
 
vragen/opmerkingen/suggesties, mail naar vdbroeckb@gmail.com


