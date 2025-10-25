----------------------------------
BMA Geometriaműhely
----------------------------------


----------------------------------
Biró Máté András — monogram: BMA
----------------------------------


Indítás: main.py
----------------------------------

Feladat leírása
Interaktív, teknőc-grafikás alakzatlabor: billentyűkkel szabályos sokszög rajzolása, mozgatása, forgatása; az oldalszám és sugár állítása; színváltoztatás; élőben számolt terület és kerület megjelenítése. 

----------------------------------------------------------------------------------------------------------------------------------------

Vezérlés
Billentyűk:

n – új véletlenszerű sokszög

f – forgatás balra 15°

g – forgatás jobbra 15°

↑ ↓ ← → – mozgatás

c – színváltoztatás

s – oldalszám növelése

a – oldalszám csökkentése

x – sugár növelése

z – sugár csökkentése

i – információ (terület, kerület) ki/be

Esc – kilépés 


--------------------------------------------------------------------

Modulok és a modulokban használt függvények

math
Geometriai számításokhoz (csúcsok, terület, kerület):

sin(θ), cos(θ) – koordináták számítása

hypot(x, y) – távolság/oldalhossz

radians(°) – fok → radián átváltás

pi – kör/ívhossz számításokhoz 

random
Véletlenszerű kezdőszínek/paraméterek előállításához. 


turtle
Grafikus megjelenítés és eseménykezelés:

  onkey(f, key) – billentyűesemények

  listen(), mainloop() – eseményfigyelés és futtatás 



bma_geom (saját modul)
BMA_ előtaggal — alakzatokhoz kapcsolódó segédfüggvények/kezelők. 

BMA_regular_polygon_vertices(n, R, center, heading)

BMA_regular_polygon_side_length(n, R)

BMA_regular_polygon_perimeter(n, R)

BMA_regular_polygon_area(n, R)

BMA_distance(p1, p2)

BMA_rotate_point(p, angle, origin)
--------------------------------------------------------------------------------------------------------------------------------

Osztályok

BMAFigure, BMAPolygon — a bma_shapes.py fájlban definiálva. 


--------------------------------------------------------------------