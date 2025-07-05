# ParadigmasDaProg
Grupo 7. Desenvolvimento em diferentes paradigmas

Exercícios:
7.1) Filtragem e transformação de listas: Aplicar funções de mapeamento, filtragem e redução para transformar coleções de dados.

; Verifica se um número é par
(define (par? x)
  (= (modulo x 2) 0))

; Retorna o dobro de um número
(define (dobro x)
  (* x 2))

; Soma os elementos de uma lista recursivamente
(define (soma lista)
  (if (null? lista)
      0
      (+ (car lista) (soma (cdr lista)))))

; Processa uma lista: filtra pares, aplica o dobro e soma os resultados
(define (pipeline lista)
  (let* ((filtrados (filter par? lista))          ; filtra os pares
         (transformados (map dobro filtrados)))   ; aplica o dobro a cada um
    (soma transformados)))                        ; soma o resultado final

; Exemplo: (pipeline '(1 2 4)) = 12
