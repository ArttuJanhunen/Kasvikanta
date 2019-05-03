* Huolimattomana ja hajamielisenä henkilönä haluan, että voin tarkistaa kasvieni nimet ja viimeisimmän
kastelupäivän

* Uteliaana haluan nähdä, mihin eri pääheimoihin kasvit voidaan yleisesti jakaa 
```sql
SELECT Family.id, Family.name FROM Family
LEFT JOIN Plant ON Plant.family_id = Family.id
GROUP BY Family.id
HAVING COUNT(Plant.id)>0
ORDER BY Family.name
```

* Sivulla vierailevana henkilönä voin tarkastella erilaisten kasvien tietoja 
```sql
SELECT FROM Plant WHERE Plant.id=halutunKasvinId;
```

* Käyttäjänä voin lisätä kasveja listaan, liittää niihin hoito-ohjeita ja valokuvan 
```sql
INSERT INTO Plant(name, latin_name, family_id) VALUES(kasvinNimi, kasvinLatinankielinenNimi, valitunHeimonId);
```
```sql
UPDATE Plant SET care_instructions='halutut ohjeet' WHERE id=haluttuId;
```
```sql
UPDATE Plant SET plant_image='haluttuUrl' WHERE id=haluttuId;
```

* Voin halutessani rekisteröityä sivulle 
```sql
INSERT INTO account(name, username, password, is_admin) VALUES('haluttuNimi', 'haluttuKäyttäjätunnus', 'haluttuSalasana', false);
```

* Admin-oikeuksien avulla pääkäyttäjänä voin tehdä samoja asioita kuin tavallinenkin käyttäjä,
mutta minulla on myös valtuudet poistaa kasveja ja hallinnoida muiden käyttäjätilejä 
```sql
DELETE FROM Plant WHERE id=haluttuId;
```
```sql
DELETE FROM account WHERE id=haluttuId;
```
