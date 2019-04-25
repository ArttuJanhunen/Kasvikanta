* Huolimattomana ja hajamielisenä henkilönä haluan, että voin tarkistaa kasvieni nimet ja viimeisimmän
kastelupäivän

* Kasviharrastajana haluan listata mahdollisimman paljon kasveja ja taata niille hoito-ohjeita muitakin
varten (SELECT * FROM Plant;)

* Uteliaana haluan nähdä, mihin eri pääheimoihin kasvit voidaan yleisesti jakaa (SELECT * FROM Family)

* Sivulla vierailevana henkilönä voin tarkastella erilaisten kasvien tietoja (SELECT FROM Plant WHERE Plant.id=halutunKasvinId)

* Käyttäjänä voin lisätä kasveja listaan, liittää niihin hoito-ohjeita ja valokuvan (UPDATE Plant SET care_instructions='halutut ohjeet' WHERE id=haluttuId)(UPDATE Plant SET plant_image='haluttuUrl' WHERE id=haluttuId)

* Voin halutessani rekisteröityä sivulle (INSERT INTO Account(name, username, password, is_admin) VALUES('haluttuNimi', 'haluttuKäyttäjätunnus', 'haluttuSalasana', false))

* Admin-oikeuksien avulla pääkäyttäjänä voin tehdä samoja asioita kuin tavallinenkin käyttäjä,
mutta minulla on myös valtuudet poistaa kasveja ja hallinnoida muiden käyttäjätilejä (DELETE FROM Plant WHERE id=haluttuId)(DELETE FROM Account WHERE id=haluttuId)
