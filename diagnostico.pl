sintoma(febre).
sintoma(tosse).
sintoma(dor_cabeca).
sintoma(nausea).
sintoma(vomito).
sintoma(espirro).
sintoma(coriza).
sintoma(dor_garganta).
sintoma(emagrecimento).
sintoma(fraqueza).
sintoma(ma_cicatrizacao).

doenca3(X, Y, Z, gripe) :-
    member(febre, [X, Y, Z]),
    member(tosse, [X, Y, Z]),
    member(dor_cabeca, [X, Y, Z]).

doenca3(X, Y, Z, aids) :-
    member(fadiga, [X, Y, Z]),
    member(ma_cicatrizacao, [X, Y, Z]),
    member(emagrecimento, [X, Y, Z]).

doenca1(X, alzheimer) :-
    X = esquecimento.


doenca3(X, Y, Z, virose) :-
    member(febre, [X, Y, Z]),
    member(vomito, [X, Y, Z]),
    member(nausea, [X, Y, Z]).

doenca3(X, Y, Z, resfriado) :-
    member(espirro, [X, Y, Z]),
    member(coriza, [X, Y, Z]),
    member(dor_garganta, [X, Y, Z]).
