create database obchod;
use obchod;

create table Uzivatel(
ID INT PRIMARY KEY auto_increment,
Jmeno varchar(50) not null,
Prijmeni varchar(50) not null,
Email varchar(50) not null,
Datum_nar date not null
);


create table Produkt(
ID INT PRIMARY KEY auto_increment,
Nazev varchar(50),
Barva varchar(20) not null,
Rozmer enum('S','M','L','XL','XXL') not null,
Cena float not null,
Dostupnost boolean not null
);

create table Pobocka(
ID INT PRIMARY KEY auto_increment,
Adresa varchar(100) not null,
Cislo_popisne int not null,
PSC int not null
);

create table Zamestnanec(
ID INT PRIMARY KEY auto_increment,
Jmeno varchar(20) not null,
Prijmeni varchar(20) not null,
Zacatek_prace date not null
);


create table Objednavka(
ID INT PRIMARY KEY auto_increment,
Datum_obj datetime not null,
Prosla_platba boolean not null,
pob_id int,
  FOREIGN KEY (pob_id) REFERENCES Pobocka(ID),
uz_id int,
  FOREIGN KEY (uz_id) REFERENCES Uzivatel(ID),
prod_id int,
  FOREIGN KEY (prod_id) REFERENCES Produkt(ID)
);

create table prace(
ID INT PRIMARY KEY auto_increment,
pob_id int,
  FOREIGN KEY (pob_id) REFERENCES Pobocka(ID),
zam_id int,
FOREIGN KEY (zam_id) REFERENCES Zamestnanec(ID)
);

create view prehled_objednavky AS
select Objednavka.Datum_obj, Produkt.Nazev, Produkt.Rozmer, Produkt.Barva, Produkt.Cena, Uzivatel.Jmeno, Uzivatel.Prijmeni, Uzivatel.Email, Objednavka.Prosla_platba, Pobocka.Adresa, Pobocka.Cislo_popisne, Pobocka.PSC
from Objednavka, Produkt, Uzivatel, Pobocka
where pob_id= Pobocka.ID and uz_id = Uzivatel.ID and prod_id=Produkt.ID; 

 

create view objednavky_uzivatel AS
SELECT Uzivatel.ID, Jmeno, Prijmeni, Email, COUNT(Objednavka.ID) AS Pocet_objednavek
FROM Uzivatel
JOIN Objednavka ON Uzivatel.ID = Objednavka.uz_id
GROUP BY Uzivatel.ID;

drop table Uzivatel;
drop table Objednavka;
drop table Zamestnanec;
drop table Pobocka;
drop table prace;
drop table Produkt;
