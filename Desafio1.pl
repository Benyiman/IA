madre(Lidia,benjamin).
padre(Ruben,benjamin).
madre(Lidia,evelyn).
padre(Ruben,evelyn).
madre(Lidia,alejando).
padre(Ruben,alejando).


hijo(X,Y):-madre(M,X),madre(M,Y),padre(P,X),padre(P,Y), X\=Y.
