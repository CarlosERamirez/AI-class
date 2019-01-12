%ag.pl
%Hechos(conocimiento)
hombre(pedro).
hombre(paco).
mujer(luz).
mujer(maria).
progenitor(pedro,paco).
progenitor(pedro,maria).
progenitor(luz,paco).
progenitor(luz,maria).
progenitor(luis,pedro).
progenitor(andrea,pedro).
progenitor(roberto,luz).
progenitor(diana,luz).
%Reglas
madre(X,Y):-mujer(X),progenitor(X,Y).
padre(X,Y):-hombre(X),progenitor(X,Y).
hija(X,Y):-mujer(X),progenitor(Y,X).
hijo(X,Y):-hombre(X),progenitor(Y,X).
abuelo(X,Y):-hombre(X),progenitor(X,Z),progenitor(Z,Y).
abuela(X,Y):-mujer(X),progenitor(X,Z),progenitor(Z,Y).


tiene_sintoma(manuel,fiebre).
tiene_sintoma(alicia,cansancio).
sintoma_de(fiebre,gripe).
sintoma_de(tos,gripe).
sintoma_de(cansancio,anemia).
elimina(vitaminas,cansancio).
elimina(aspirinas,fiebre).
elimina(jarabe,tos).

%Reglas
recetar_a(X,Y):-enfermo_de(Y,A),alivia(X,A).
alivia(X,Y):-elimina(X,A),sintoma_de(A,Y).
enfermo_de(X,Y):-tiene_sintoma(X,Z),sintoma_de(Z,Y).

