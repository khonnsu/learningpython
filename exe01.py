#calcula e imprime ano em que usuário terá 100 anos de idade
import datetime 					#usa módulo para conseguir ano atual
name = input("escreva seu nome: ")			#lê string após imprimir a frase descrita
age = int(input("escreva sua idade: "))			#faz o mesmo da anterior porém transforma em int
year = datetime.datetime.now().year + (100 - age)	#calcula ano atual + anos que faltam para completar 100
print(name+" tera 100 anos em "+str(year))		#imprime concatenando strings, para o ano é feito cast
