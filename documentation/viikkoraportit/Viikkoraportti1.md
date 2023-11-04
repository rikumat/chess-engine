# Viikko 1

## Viikon edistys
Loin alustavan github-projektin, sekä suunnitelman projektin toteuttamiselle. Suunnittelin etukäteen, Miten tulen toteuttamaan laillisten siirtojen kirjaamisen. Tämä tulee toteutumaan jokaisen siirron yhteydessä. Aloitin myös projektin aiheen opiskelun katsomalla videoita minimax-algoritmin ja alpha-beta karsinnan toiminnasta. Katsoin myös opetusvideon shakkipelin luomisesta pythonilla.

## Epäselvät asiat
Projektin kannalta haastavin ja epäselvin asia on tällä hetkellä laillisten siirtojen päivittäminen. Alustava suunnitelma on alustaa mustan ja valkoisen lailliset siirrot esimerkiksi joukkoon tupleina. Jokaisen siirron yhteydessä tarkistetaan mihin nappuloihin siirto vaikuttaa, ja päivittää lailliset siirrot näiden nappuloiden osalta. En kuitenkaan vielä ole keksinyt, miten poistan tehokkaasti jo olemassa olevia siirtoja, jos esimerkiksi nappula siirretään toisen nappulan eteen.

## Seuraavat vaiheet
Projektin ensimmäinen askel on luoda kyky päivittää lailliset siirrot nappulan siirron yhteydessä. Tämän jälkeen luodaan yksinkertainen heuristiikka, jonka avulla arvioidaan kuinka suotuisa pelitilanne on pelaajalle. Tämän jälkeen luodaan minimax algoritmi alpha-beta karsinnalla, jonka jälkeen keskitytään heuristiikan parantamiseen.

