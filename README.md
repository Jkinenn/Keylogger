# Keylogger
Yksinkertainen Pythonilla ja pynput-kirjastolla toteutettu keylogger kuolutus- ja opiskelutarkoituksiin

# Simple Python Keylogger ⌨️

Yksinkertainen näppäilyntallennin (keylogger), joka on kirjoitettu Pythonilla käyttäen `pynput`-kirjastoa. Skripti kuuntelee näppäimistön tapahtumia ja tallentaa painallukset aikaleimojen kanssa paikalliseen tekstitiedostoon.

## ⚠️ Vastuuvapauslauseke (Disclaimer)
**Tämä projekti on luotu ainoastaan koulutus- ja tutkimustarkoituksiin.** Tätä ohjelmistoa saa käyttää vain järjestelmissä ja laitteissa, joihin sinulla on nimenomainen ja laillinen lupa (esimerkiksi oma tietokoneesi). Tekijä ei ota mitään vastuuta tämän työkalun väärinkäytöstä, laittomasta käytöstä tai sen aiheuttamista vahingoista. Käyttämällä tätä ohjelmistoa hyväksyt nämä ehdot.

## Ominaisuudet
* Tallentaa tavalliset kirjaimet ja numerot.
* Tunnistaa ja kirjaa ylös erikoisnäppäimet (kuten Välilyönti, Enter, Shift ja Ctrl).
* Tallentaa datan lokaaliin `keylogs.txt` -tiedostoon helppolukuisessa muodossa.
* Turvallinen lopetus `Esc`-näppäintä painamalla.

## Vaatimukset
Tarvitset Python 3:n ja `pynput`-kirjaston toimiakseen.

Asenna vaaditut riippuvuudet komennolla:
```bash
pip install pynput
