from tpessoa import Pessoa

p1 = Pessoa ()
p1.nome = "Ricardo Sousa Pereira"
p1.cpf = "613.456.977-16"
p1.data_nasc = "19/06/1995"

p2 = Pessoa ()

p2.nome = "Chico França Azevedo"
p2.cpf = "467.876.232-87"
p2.data_nasc = "22/03/1997"

print("Dados da P1")
print('Nome:', p1.nome)
print('CPF:', p1.cpf)
print('Data de Nascimento:', p1.data_nasc)

print("-----------------------------------")

print("Dados da P2")
print('Nome:', p2.nome)
print('CPF:', p2.cpf)
print('Data de Nascimento:', p2.data_nasc)
