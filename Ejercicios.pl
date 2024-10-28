mujer(clara). 
mujer(luisa). 
mujer(maria). 
mujer(ana). 

ocupacion(disenadora). 
ocupacion(florista). 
ocupacion(jardinera). 
ocupacion(directora_de_orquesta).

no_es(clara, florista).
no_es(clara, jardinera).

no_es(luisa, florista).

no_es(luisa, directora_de_orquesta). 
no_es(maria, directora_de_orquesta).

no_es(ana, jardinera). 
no_es(ana, disenadora).

alergica(clara, plantas).

relacionado(jardinera, plantas). 
relacionado(florista, plantas).

no_es(Mujer, Ocupacion) :- alergica(Mujer, X), relacionado(Ocupacion, X).

solo_escucha(luisa, rock). 
solo_escucha(maria, rock).

incompatibles(directora_de_orquesta, rock). 

no_es(Mujer, Ocupacion) :- solo_escucha(Mujer,X), incompatibles(Ocupacion,X).

no_repetido(A, B, C, D) :- not(A == B), not(A == C), not(A == D), not(B == C), not(B == D), not(C == D).
