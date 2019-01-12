fact(0,s(0)).
fact(s(X),Y*s(X)):-fact(X,Y).

fact2(0,1).
fact2(X,Y):-X>0, X1 is X-1, fact2(X1,Y1), Y is X*Y1.

fib(0,s(0)).
fib(s(0),s(0)).
fib(s(s(X)),Y+Z):-fib(X,Y),fib(s(X),Z).

conc(A,B,C):- A=[], C=B.
conc(A,B,C):- A=[X|Y], conc(Y,B,Z), C=[X|Z].
% los argumentos a la derecha de :- pueden ponerse dentro de paréntesis
% del mismo lado izquierdo, ejemplo:
%buscarlos en el pdf Tema 2 Prolog
