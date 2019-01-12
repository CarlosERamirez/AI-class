%ejem.pl
%consult(ejem).

le_gusta(fulano, agua).
le_gusta(fulano, cerveza).
le_gusta(fulano, refresco).
le_gusta(fulano, leche).
le_gusta(zutano, cerveza).
le_gusta(zutano, refresco).
le_gusta(mengano, agua).
le_gusta(mengano, leche).

%Y<X<Z
pertenece(X,Y,Z):-X>Y, X<Z.

%Sucesor
suc(0,1).
suc(X,Y):-X>0, Y is X+1.

%Definición de los naturales
n(c).
n(s(X)):-n(X).

%Suma
suma(c,Y,Y):- n(Y).
suma(s(X),Y,s(Z)):- suma(X,Y,Z).

