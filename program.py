print("Olá Mundo!!")

# variavel = 12
variavel = 5.19
variavel = "Gugas"
variavel = (["Maça","Uva"])
variavel = True

nome = input("Nome: ")
idade = int(input("Idade: "))
altura = float(input("Altura: "))

print("Seu nome: " + nome + "Possui: " + idade + "tem: " + altura +"m") 


fh = float(input("Valor: "))
celcius = (fh - 32) * 5/9
print(celcius)

nota1 = int(input("Nota 1 : "))
nota2 = int(input("Nota 2 : "))
media = (nota1 + nota2) / 2
if(media >= 5.0):
  print("Aprovado")
elif(media >= 3.0 and media < 5.0):
  print("Exame")
else: 
  print("Reprovado")