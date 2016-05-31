Kjør GUI_rc.py for å starte spillet. OBS! Har du forstørret tekst/applikasjoner i ditt OS kan det hende at du må redusere forstørrelsen
for å se hele GUIen. 
Bruk knappene i det grafiske brukergrensesnittet for å endre tilstanden i spillet. 

Vilkår: 
Kylling/rev/korn må inn i båten før mannen om man skal krysse elven.

Bug:
Kaller man crossRiver() med mann og rev i båt, for å endre tilstanden til mann og rev i båt på høyre side, og deretter prøver å ta reven
ut av båten vil reven settes tilbake på venstre side. 


OBS! På linje 54 i GUI_rc.py finnes vårt (mislykket) forslag til hvordan vi kan implementere vilkår for game over. 
Fordi vi ikke har fått denne metoden til å fungere korrekt har vi valgt å ikke implementere den, men den kommenterte metoden isItDead()
viser hvordna vi har tenkt. 
