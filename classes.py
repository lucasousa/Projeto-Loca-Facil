class Person():
	def __init__(self):
		self.__name        = None
		self.__cpf         = None
		self.__sex		   = None	
		self.__telephone   = None
		self.__email       = None

	@property
	def name(self):
		return self.__name
	@name.setter
	def name(self, name):
		if(len(name)<10 or len(name)>50):
			raise ValueError
		else:
			self.__name = name
	
	@property
	def sex(self):
		return self.__sex
	@sex.setter
	def sex(self, sexo):
		if(len(sexo) <= 9 and len(sexo)>=8):
			self.__sex = sexo.lower()
		else: raise ValueError

	@property
	def cpf(self):
		return self.__cpf
	@cpf.setter
	def cpf(self, cpf):
		if(len(cpf)<11 or len(cpf)>11):
			print("CPF inválido.")
		else:
			self.__cpf = cpf

	@property
	def telephone(self):
		return self.__telephone
	@telephone.setter
	def telephone(self, telephone):
		if(len(telephone)<11 or len(telephone)>11):
			raise ValueError
		else:
			self.__telephone = telephone
	
	@property
	def email(self):
		return self.__email
	@email.setter
	def email(self, email):
		self.__email = email

	def Register(self, name, cpf, telephone, email):
		self.__name = name
		self.__cpf = cpf
		self.__telephone = telephone
		self.__email = email

	def printPerson(self):
		cpf = self.__cpf
		print('Nome: {}'.format(self.__name))
		print('CPF: {}.{}.{}-{}'.format(cpf[0:3],cpf[3:6],cpf[6:9],cpf[9:12]))
		print('Telefone: ({}){}'.format(self.__telephone[0:2],self.__telephone[2:]))
		print('E-mail: {}'.format(self.__email))
		print('')



#classe Aluguel
class Rent(object):
	__id = 0
	def __init__(self):
		self.__desc         = None
		self.__neighborhood = None
		self.__sit          = None #
		self.__street       = None 
		self.__number       = None
		self.__complement   = None
		self.__cep          = None
		self.__price        = None
		self.__id           = Rent.__id #
		Rent.__id += 1

	def registerRent(self, desc, neighborhood, street, number, complement, cep, price):
		self.__desc         = desc
		self.__neighborhood = neighborhood
		self.__sit          = True
		self.__street       = street 
		self.__number       = number
		self.__complement   = complement
		self.__cep          = cep
		self.__price        = price
		self.__quality      = float(0)

	@property
	def description(self):
		return self.desc

	@description.setter
	def description(self, desc):
		self.__desc = desc

	@property
	def situation(self):
		return self.__sit
	@situation.setter
	def situation(self, st):
		self.__sit = st
	

	@property
	def street(self):
		return self.__st
	@street.setter
	def street(self, s):
		self.__street = s

	@property
	def number(self):
		return self.__number
	@number.setter
	def number(self,n):
		if(type(n)!= int):
			raise ValueError
		else:
			self.__number = n
	@property
	def complement(self):
		return self.__complement
	@complement.setter
	def complement(self, comp):
		self.__complement = comp

	@property
	def cep(self):
		return self.__cep
	@cep.setter
	def cep(self,cep):
		self.__cep = cep

	@property
	def price(self):
		return self.__price
	@price.setter
	def price(self, p):
		self.__price = p


	@property
	def quality(self):
		return self.__quality
	@quality.setter
	def quality(self, q):
		if(float(q)<0.0 or float(q)>5.0):
			raise ValueError
		else:
			self.__quality = q
			
	def printRent(self):
		print("Descrição do Local: {}".format(self.__desc))
		print("Situação: ",end='') 
		if self.__sit:
			print("Disponível para Aluguel") 
		else:
			print('Indisponível para aluguel')
		print("Rua: {}".format(self.__street))
		print("Número: {}".format(self.__number))
		print("Complemento: {}".format(self.__complement))
		print("CEP: {}".format(self.__cep))
		print("Preço: {:.2f}".format(self.__price))
		print("Avaliação: {}".format(self.__quality))

	

class Renter(Person):
	__id = 0
	def __init__(self):
		self.__id        = Renter.__id
		self.__rent      = None
		Renter.__id   += 1

	@property
	def rent(self):
		return self.__rent
	@rent.setter
	def rent(self, r):
		if(type(r) != Rent):
			raise Exception("Erro")
		else:
			self.__rent = r


class User(Person):
	__id = 0 
	def __init__(self):
		self.__id      = User.__id 
		User.__id     += 1		
	
	def RegUser(self, Username, passwd):
		self.__username = Username
		self.__passwd  = passwd

	@property
	def username(self):
		return self.__username
	@property
	def passwd(self):
		return self.__passwd