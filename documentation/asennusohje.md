### Paikallinen asennus:
* Mene sovelluksen juurikansioon
* kirjoita terminaaliin 'python3 -m venv venv'
* kirjoita terminaaliin 'source venv/bin/activate'
* kirjoita terminaaliin 'pip install -r requirements.txt'
* sovellus käynnistyy terminaaliin kirjoitella käskyllä 'python3 runPlants.py'
* käynnistä selain ja kirjoita sivuksi 'http://localhost:5000/'
* Voila!

### Sovellus pilvipalvelussa:
* Paikallisen asennuksen jälkeen sovelluksella on jo riippuvuudet asennettuna
* Poista mukana tullut .git-kansio ja luo uusi käskyllä git init
* Tämän jälkeen commitoi sovellus paikalliseen versionhallintaan
* Paikallisen asennuksen jälkeen kirjoita terminaaliin 'heroku create'
* Tämän jälkeen sovellusta varten on luotu sivu herokun palvelimelle
* Kerrotaan paikalliselle versionhallinnalle herokusta käskyllä 'git remote add heroku SOVELLUKSENURL'
* Kirjoita terminaaliin käsky 'git push heroku master'
* Tämän jälkeen sovelluksen tulisi olla käynnissä sivulla, jonka aiemmin loit käskyllä 'heroku create'
