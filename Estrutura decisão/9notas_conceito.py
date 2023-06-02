# Duas notas parciais obtidas por um aluno

nota1 = float(input('Digite a nota1:'))
nota2 = float(input('Digite a nota2:'))

# Calcular a média

media = (nota1 + nota2)/ 2

conceito = None
mensagem = None

if 9.0 <= media <= 10.0:
    conceito = "A"
elif 7.5 <= media < 9.0:
    conceito = "B"
elif 6.0 <= media < 7.5:
    conceito = "C"
elif 4.0 <= media < 6.0:
    conceito = "D"
else:
    conceito = "E"

if conceito in ["A", "B", "C"]:
    mensagem = "APROVADO"
else:
    mensagem = "REPROVADO"

print("Notas: {} e {}".format(nota1, nota2))
print("Média: {:.2f}".format(media))
print("Conceito: {}".format(conceito))
print("Resultado: {}".format(mensagem))