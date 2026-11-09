
class Category:
    def __init__(self, id:int, nome:str, descricao:str):
        self._id = id
        self._nome = nome
        self._descricao = descricao

        if not self._nome.strip():
            raise TypeError('O nome da categoria nao pode estar vazio! Porfavo insira um nome para ela')


    @property
    def nome(self):
        return self._nome

    @property
    def id(self):
        return self._id

    @property
    def descricao(self):
        return self._descricao
    

    def __str__(self):
        return (f'{self._nome}. Descrição da categoria: {self._descricao}')


class Product:
    def __init__(self, id:int, nome:str, preco:float, categoria:Category):
        self._id = id
        self._nome = nome
        self._preco = preco
        self._categoria = categoria

        if self._preco <= 0:
            raise ValueError('Preço nao pode ser abaixo ou igual a 0. Porfavor insira um valor positivo!')
    

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco: float):
        if preco <= 0:
            raise ValueError('Preço nao pode ser abaixo ou igual a 0. Porfavor insira um valor positivo!')
        self._preco = preco

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria: Category):
        self._categoria = categoria


    def __str__(self):
        return (f'O produto {self._nome} pertence a categoria {self._categoria}')


class Customer:
    def __init__(self, id:int, nome:str, telefone:str):
        self._id = id
        self._nome = nome
        self._telefone = telefone

        if not self._nome.strip():
            raise TypeError('O nome do cliente nao pode estar vazio! Porfavo insira um nome para ele')

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone

class Restaurant:
    def __init__(self, nome: str):
        self._nome = nome
        self._produtos = []
        self._categorias = []

    def cadastrar_categoria(self, categoria: Category):
        for i in self._categorias:
            if categoria.id == i.id:
                raise ValueError('Não é possivel cadastrar duas categorias com o mesmo id')
        self._categorias.append(categoria)

    def buscar_categoria_por_id(self, categoria_id: int):
        for i in self._categorias:
            if categoria_id == i.id:
                return i
        return None


    def cadastrar_produto(self, produto: Product):
        for i in self._produtos:
            if produto.id == i.id:
                raise ValueError('Não é possivel cadastrar dois produtos com o mesmo id')
        self._produtos.append(produto)
    

    def buscar_produto_por_id(self, produto_id: int):
        for i in self._produtos:
            if produto_id == i.id:
                return i
        return None


    def editar_produto(self, produto_id: int):
        produto = self.buscar_produto_por_id(produto_id)
        
        if produto is None:
            return ('Esse produto nao foi encontrado')

        perguta = int(input(f"""Qual valor do produto {produto.nome} voçê gostaria de alterar?
                        [1] nome | [2] preço | [3] categoria"""))
        
        while 3 > perguta < 1:
            perguta = int(input(f"""Qual valor do produto {produto.nome} voçê gostaria de alterar?
                [1] nome | [2] preço | [3] categoria"""))

        match perguta:
            case 1:
                valor = input(f'Insira um novo nome para o produto {produto.nome}:  ')
                produto.nome = valor 
            case 2:
                valor = float(input(f'Insira um novo preço para o produto {produto.nome} que ira substituir o valor atual de R${produto.preco}:  '))
                produto.preco = valor
            case 3:
                print("Lista de categorias existentes:")
                for i in self._categorias:
                    print(f'Categoria: {i.nome} | ID: {i.id}')
                
                try:
                    valor = int(input('Insira o id da categoria: '))
                except ValueError:
                    return 'Insira apenas valores numericos'

                valor = self.buscar_categoria_por_id(valor)
                if valor is None:
                    return 'Não é possivel alterar  '
                produto.categoria = valor


        



    def remover_produto(self, id: int):
        # encontrar e remover o produto
        pass


categoria = Category(1, 'Bebidas', 'Bebidas quentes e frias')
produto = Product(1, 'Café', 5.50, categoria)

# print(produto)
# print(categoria)