puede(animal,respirar).
puede(animal,moverse).
puede(ave,volar).
puede(canario,cantar).
carac(animal,piel).
carac(ave,alas).
carac(ave,plumas).
carac(avestruz,alta).
carac(canario,amarillo).
esun(pez,animal).
esun(ave,animal).
esun(avestruz,ave).
esun(canario,ave).
nopuede(avestruz,volar).

%Reglas
%determina características recursivamente
%ejemplo: un canario tiene piel
determinacarac(X,Y):-carac(X,Y).
determinacarac(X,Y):-esun(X,Z),determinacarac(Z,Y).

