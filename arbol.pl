%arbol.pl
%Hechos(conocimiento)
hombre(carl).
hombre(adam).
hombre(dave).
hombre(fred).
hombre(gustav).
mujer(bettina).
mujer(eva).
progenitor(carl,adam).
progenitor(carl,dave).
progenitor(carl,eva).
progenitor(bettina,adam).
progenitor(bettina,dave).
progenitor(bettina,eva).
progenitor(eva,gustav).
progenitor(fred,gustav).
ojos(carl,green).
ojos(bettina,green).
ojos(adam,yellow).
ojos(dave,black).
ojos(eva,blue).
ojos(fred,pink).
ojos(gustav,brown).
fecha(carl,1926).
fecha(bettina,1926).
fecha(adam,1950).
fecha(dave,1955).
fecha(eva,1965).
fecha(fred,1966).
fecha(gustav,1988).

%Reglas
%determina si el nodo actual o un ancestro tienen ojo azul
ancestroojoazul(X):-ojos(X,blue).
ancestroojoazul(X):-progenitor(Y,X),ancestroojoazul(Y).

%determina si un ancestro tiene ojo azul, no el nodo actual
vancestroojoazul(X):-progenitor(Y,X),ancestroojoazul(Y).
