nomes = ["Ana", "Bruno", "Carlos"]
print(nomes[0])
print(nomes[1])
print(nomes[2])
print('///////////////////////////////////////')
nomes = ["Ana", "Bruno", "Carlos"]
for nome in nomes:
 print(nome)
print('///////////////////////////////////////')
nomes = ["Ana", "Bruno", "Carlos"]
for i in range(len(nomes)):
 print(nomes[i])
print('///////////////////////////////////////')
nomes = ["Ana", "Bruno"]
nomes.append("Carlos")
print(nomes)
print('///////////////////////////////////////')
nomes = ["Ana", "Bruno"]
nomes.insert(1, "Carlos")
print(nomes)
print('///////////////////////////////////////')
nomes = ["Ana", "Bruno", "Carlos", "Ana"]
nomes.remove("Ana")
print(nomes) 
print('///////////////////////////////////////')
nomes = ["Ana", "Bruno", "Carlos"]
nome_removido = nomes.pop(1)
print(nomes)
print('lixeira: ', nome_removido)
print('///////////////////////////////////////')
nomes = ["Ana", "Bruno", "Carlos"]
nomes = nomes .clear()
print('Lixeira limpa')
print('///////////////////////////////////////')
nomes = ["Ana", "Bruno", "Carlos"]
if "Carlos" in nomes: 
    print('Carlos está em casa')
else:
    print('João não está em casa')
