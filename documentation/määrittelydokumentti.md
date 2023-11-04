# Shakkipeli

## Yleistä
- Projektin kieli on Python
- Pythonin lisäksi hallitsen erinomaisesti JavaScript-kielen.
- Projektissa parhaan siirron laskemiseksi käytetään minimax algoritmiä ja alpha-beta karsintaa.
- [Viikkoraportit](./viikkoraportit)

## Projektin laajuus
projekti toteutetaan komentorivikäyttöliittymällä, jolle käyttäjä voi syöttää siirtonsa, ja johon ohjelma vastaa omalla siirrollaan. Ohjelma pitää tietoa myös shakkilaudan tilanteesta, jolloin käyttäjä voi halutessaan tulostaa pelitilanteen kokonaisuudessaan. Alustavasti suunnitelmissa ei ole toteuttaa suoraa toiminnallisuutta, joka mahdollistaisi tietokoneen pelaamisen itseään vastaan. Ohjelma osaa pelata shakkipelin alusta loppuun, mutta ei osaa antaa siirtoa satunnaisesti annettuun pelitilanteeseen.

## Algoritmit

Ongelma, jonka projekti haluaa ratkaista, on hyvän siirron keksiminen shakkipelin jokaisessa vaiheessa. Valitsin minimax-algoritmin, koska se on suhteellisen yksinkertainen totetutaa, ja soveltuu shakkitekoälyn kehittämiseen kohtalaisen hyvin etenkin, jos neuroverkkoja ei voi käyttää. Alpha-beta karsinta soveltuu tämän algoritmin tehostamiseen, ja on välttämätön jos liikkeitä haluaa laskea jokseenkin järkevässä ajassa kolmea siirtoa pidemmälle. 

Sallitut siirrot lasketaan laskentatehon säästämiseksi ahneella algoritmillä, päivittämällä mahdolliset siirrot jokaisen siirron jälkeen. Alkuperäisessä suunnitelmassa pelaaja syöttää siirtonsa komentorivillä, johon ohjelma vastaa omalla siirrollaan. 

Siirron laskemiseksi aikavaativuus on O(n^3) ja tilavaativuus O(n), Missä n on laillisten siirtojen lukumäärä. Tässä tapauksessa ennakoitavien siirtojen lukumäärä on 3. Tavoite laillisten siirtojen päivittämisen aikavaativuudelle on O(n) ja tilavaativuudelle O(1), Missä n on uusien laillisten siirtojen lukumäärä jokaisen siirron jälkeen.

## Lisätietoja
- opinto-ohjelma tietojenkäsittelytieteen kandidaatti (TKT)
- Dokumentaation kieli: määrittelydokumentti suomeksi, kaikki muu englanniksi.




