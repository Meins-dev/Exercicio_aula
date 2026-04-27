#OBJETIVO : Atualizar produtos (PEGAR SOMENTE O PRECO PARA A SOMATORIA)

## 0# git branch feature/pe-548 (feature/pe-548 = o nome da branch. É preciso criar uma branch antes de qualquer coisa)
## 1# pwd (Verifica onde esta localizado a pasta)
## 2# git config --global user.name "nome_do_git_aqui_dentro"  (Coloque o nome do git certinho)
## 3# git config --global user.email "prometheusamvs1@gmail.com" (mesmo email do git)
## 4# clear (limpa o terminal)
## 5# git init (inicializa o repositorio)
## 6# ls (mostra o arquivo dentro da pasta)
## 7# ls -la (mostra quantos arquivos ha dentro da pasta)
## 8# git branch -m main (Por boas praticas devemos trocar a branch master para o main )
## 9# git push origin main --delete master (Vai deletar a master e deixar apenas a main)
## 10# git status (Mostra o status dos arquivo)
## 11# git add . (Faz isso apos fazer uma modificacao ou adicionar um arquivo novo, somente depois use commit)
## 12# git commit -m "mensagem" (Preparando o arquivo antes de enviar)
## 13# Vá no site git hub e cria um novo repositorio (É preciso fazer isso antes de qualquer outra coisa de push)
## 14# Vai em code e copia o HTTPS e coloca o comando no terminal > git remote add origin link
## 15# git branch (Vai mostrar o arquivo main)
## 16# git branch -r (Vai mostrar a branch localmente, caso apareça vermelho quer dizer que está certo)
## 17# git push -u origin main (Vai publicar no site)
## 18# git checkout feature/pe-548 (git checkout vai mudar de branch exemplo: git checkout feature/pe-548 ; caso vc esteja na main vai para a feature/pe-548)
## 19# git push --set-upstream origin NOMEDABRANCH (vai deixar a branch local)

#git fetch para ve se tem path e git pull para atualizar


#lista1 = [10,20,30,40,50,60,70]
#lista2 = ["Daniel","Miguel","Joao"]

#print("",lista1,"\n",lista2)
#Criando listas
#_____________________________________
#lista3 = ["Oi",2.0,5,[10,20]]

#print(lista3) #Caso use o Len vai contar todos os dentro da lista e inclusive a sub lista e ela vai ser considerada apenas 1 caractere print(len(lista3)
#_____________________________________
#numero = [17,123,87,34,66,8398,44]

#print(numero[2])
#print(numero[9-8])
#print(numero[-2])
#print(numero[-1])

#uma_lista = [3,67,"gato",[56,57,"cachorro"],[],3.14,False]
#print(uma_lista[2][0]) #[2] = vai pegar o "gato". [0] = vai pegar o (g).
#_____________________________________
#frutas = ["maca", "laranja","banana", "cereja"]

#print("maca" in frutas)
#print("pera" in frutas)
#Vai dizer se é True caso esteja na lista e False caso nao esteja

#print([1,2] + [3,4])
#print(frutas + [6,7,8,9])

#print(["test"] * 4)
#print([1,2,["olá","adeus"]]*2)
#______________________________________
#a = [1,2,3,4,5,6,7,8,9]

#print(a)
#print(max(a))
#print(min(a))
#print(sum(a))
#______________________________________
#uma_lista = ["a","b","c","d","e","f"]
#print(uma_lista[1:3])
#print(uma_lista[:4])
#print(uma_lista[3:])
#print(uma_lista[:])
#print(uma_lista[0:6])
#______________________________________
#frutas = ["banana","maca"]
#frutas[0] = "pera"
#frutas[-1] = "abacate"

#print(frutas)
#______________________________________
#uma_lista = ["a","b","c","d","e","f"]
#uma_lista[1:3] = ["x","y"]
#print(uma_lista)
#Vai trocar certos dados

#______________________________________
#uma_lista = ["a","d","f"]
#uma_lista[1:1] = ["b","c"]
#print(uma_lista)
#uma_lista[4:4] = ["e"]
#print(uma_lista)
#Vai espremer o conteudo da direita para a esquerda, acrescentando ele.
#______________________________________
#a = ["um","dois","tres"]
#del a [1] #Vai deletar apenas o "dois"
#print(a)

#lista = ["a","b","c","d","e","f"]
#del lista[1:5] # O ultimo ou seja 5 n vai contar vai parar no 4  entao vai ser impresso no console : a , f
#print(lista)
#______________________________________
#a = [81,82,83]
#a.append(5)
#print(a)
#Vai colocar ou seja acrescentar na lista
#______________________________________
#a = [88,81,82,83]
#b = ["Daniel","Santana","Ana"]
#b.sort()
#a.sort()
#print(a)
#print(b)
#Vai ordenar
#______________________________________
#a = [1,2,3,4,5,6,7,8,9]
#print(a.index(9)) # pode ser string tambem para ser encontrado exemplo : (a.index("Daniel"))
#Vai mostrar onde que se encontra a posicao declarada 
#______________________________________
#a = [88,81,82,83]
#a.insert(1,100) # O primeiro numero vai escolher em qual posicao vai colocar e o segundo é o valor que vai ser colocado poderia ser string tambem no segundo valor 
#print(a)
#Vai inserir dados na lista
#______________________________________
#a = [88,2121,312134,34,56,786,32,82,88,88,88,88]
#print(a)
#print(a.count(88)) # Vai mostrar quantas vezes repetiu o numero ou string declarada no caso do exemplo ai vai mostrar quantos 88 existe na lista
#Vai contar quantos dados repetidos existe
#______________________________________
#a = [88,81,82,83,88,85,88,86]
#a.pop()
#print(a)
#Ele vai excluir o ultimo elemento da lista caso vc n declare nada dentro dos parenteses
#a.pop(0)#selecionando posicao
#print(a)
#Nesse caso ele vai excluir a posicao selecionada e dessa forma ele vai ser usado igual o del
#______________________________________
#lista = [1,2,3]
#lista.extend([4,5])
#print(lista)
#Diferente do append o extend pode colocar uma lista de uma vez ou varias informações na lista existente
#______________________________________
#t = [[1,2], [3], [4,5,6]] # Lista com subs listas

#print(sum(t[0]+t[1]+t[2]))  # Soma todas as sub listas

#print(t[0][0]+t[0][1]) # Vai somar 1 + 2 da primeira sub lista

#Somando dentro da lista. SUM(Vai somar os dados)
#______________________________________
#y = [1,2,3]

#resultado={
#     sum(y[0:1]),
#     sum(y[0:2]),
#     sum(y[0:3])
#}

#print(resultado)
#Para fazer isso precisa criar uma variavel e dentro dela usar o sum para imprimir o resultado depois
#______________________________________
#lista = ["Alemanha","Itália","Japao"]

#lista.append("Brasil")
#print(lista)
#Para colocar algum item dentro da lista usa o append
#______________________________________
#lista = [0,1,2,3,4,5,6,7,8,9,10]
#print(lista[1:10]) #Intervalo de 1 a 9
#print(lista[8:]) #Intervalo de 8 a 1
#print(sum(lista[0:])) # SOMA DA LISTA
#print(lista[-1],lista[-2],lista[-3],lista[-4],lista[-5],lista[-6],lista[-7],lista[-8],lista[-9],lista[-10]) #Lista Reversa
#print(lista[0],lista[1],lista[3],lista[5],lista[7],lista[9],"Impars") #Impares
#print(lista[2],lista[4],lista[6],lista[8],lista[10], "Pares")  #Pares
#______________________________________
#lista = [0,1,43,4,54,845,3245,323,543,7564,213421,5646,6767,8787,234]
#lista.sort()
#print()
#print(lista)





#uma_lista = ["a","b","c","d","e","f"]
#uma_lista[1:3] = ["x","y"]
#print(uma_lista)
#Vai trocar certos dados



if atualizar_produto == True:
    
    nome_do_produto = str(input("\nQual o nome do produto que deseja colocar?"))
    print(lista_produto)
    selecionar_produto = int(input("\nDigite qual o produto deseja substituir? (Lembrando que o primeiro item da lista é 0)"))

    print("\nQual produto você deseja selecionar para atualizar?")
    print(lista_produto)
    lista_produto[1:3] = [nome_do_produto]
