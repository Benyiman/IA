
madre(lidia,patricio).
padre(ruben,patricio).
madre(lidia,estrella).
padre(ruben,estrella).
madre(lidia,alejando).
padre(ruben,alejando).
madre(lidia,evelyn).
padre(ruben,evelyn).
madre(lidia,benja).
padre(ruben,benja).
madre(tatiana,alexi).
padre(patricio,alexi).
madre(tatiana,catherine).
padre(patricio,catherine).
madre(estrella,monica).
padre(jano,monica).
madre(estrella,wiliam).
padre(guildo,wiliam).
hermano(X,Y):-madre(Z,X),madre(Z,Y), X\=Y.
primos(P,M):-padre(X,P),madre(Y,M),hermano(X,Y).
