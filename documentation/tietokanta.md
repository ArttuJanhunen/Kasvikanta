![Kaavio](https://github.com/ArttuJanhunen/Kasvikanta/blob/master/documentation/Tietokantakaavio.png)

## CREATE TABLE-lauseet:

Family:
```sql
CREATE TABLE family (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(150) NOT NULL, 
	latin_name VARCHAR(150) NOT NULL, 
	PRIMARY KEY (id)
);
```
User:
```sql
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(150) NOT NULL, 
	username VARCHAR(150) NOT NULL, 
	password VARCHAR(150) NOT NULL, 
	is_admin BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (is_admin IN (0, 1))
);
```
Plant:
```sql
CREATE TABLE plant (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(150) NOT NULL, 
	latin_name VARCHAR(150) NOT NULL, 
	care_instructions VARCHAR(300) NOT NULL, 
	plant_image VARCHAR(300) NOT NULL, 
	family_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(family_id) REFERENCES family (id) ON DELETE CASCADE
);
```
Liitostaulu PlantUser:
```sql
CREATE TABLE plant_user (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	user_id INTEGER NOT NULL, 
	plant_id INTEGER NOT NULL, 
	date_watered VARCHAR(50), 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES "account" (id) ON DELETE CASCADE, 
	FOREIGN KEY(plant_id) REFERENCES plant (id) ON DELETE CASCADE
);
```
