# Shakkipeli

## Yleistä
- Projektin kieli on Python
- Pythonin lisäksi hallitsen erinomaisesti JavaScript-kielen.
- Projektissa parhaan siirron laskemiseksi käytetään minimax algoritmiä ja alpha-beta karsintaa.
- [Viikkoraportit](./viikkoraportit)

## Projektin laajuus
projekti toteutetaan komentorivikäyttöliittymällä, jolle käyttäjä voi syöttää siirtonsa, ja johon ohjelma vastaa omalla siirrollaan. Alustavasti suunnitelmissa ei ole toteuttaa suoraa toiminnallisuutta, joka mahdollistaisi tietokoneen pelaamisen itseään vastaan.

## Algoritmit

Ongelma, jonka projekti haluaa ratkaista, on hyvän siirron keksiminen shakkipelin jokaisessa vaiheessa. Valitsin minimax-algoritmin, koska se on suhteellisen yksinkertainen totetutaa, ja soveltuu shakkitekoälyn kehittämiseen kohtalaisen hyvin etenkin, jos neuroverkkoja ei voi käyttää. Alpha-beta karsinta soveltuu tämän algoritmin tehostamiseen, ja on välttämätön jos liikkeitä haluaa laskea jokseenkin järkevässä ajassa kolmea siirtoa pidemmälle. 

Sallitut siirrot lasketaan laskentatehon säästämiseksi ahneella algoritmillä, päivittämällä mahdolliset siirrot jokaisen siirron jälkeen. Alkuperäisessä suunnitelmassa pelaaja syöttää siirtonsa komentorivillä, johon ohjelma vastaa omalla siirrollaan. 

Siirron laskemiseksi aikavaativuus on O(n^3) ja tilavaativuus O(n), Missä n on laillisten siirtojen lukumäärä. Tässä tapauksessa ennakoitavien siirtojen lukumäärä on 3. Tavoite laillisten siirtojen päivittämisen aikavaativuudelle on O(n) ja tilavaativuudelle O(1).

## Lisätietoja
- opinto-ohjelma tietojenkäsittelytieteen kandidaatti (TKT)
- Dokumentaation kieli: kaikki kurssiin liittyvä suomeksi (määrittelydokumentti, viikkoraportit) ja kaikki projektiin liittyvä tieto englanniksi (tuntikirjanpito, readme, docstring...)




