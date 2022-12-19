"""
POO - Métodos Mágicos

Métodos Mágicos, são todos os métodos que utilizam dunder

dunder init -> __init__()

Dunder -> Double Underscore
"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        """dunder repr -> Representação do objeto"""
        return f'{self.titulo} {self.autor} {self.paginas}'

    def __str__(self):
        """ele não tem diferenca entre o dunder repr porem se os dois estiverem
           na sua classe ele da preferencia para o __str__"""
        return f'{self.titulo} {self.autor} {self.paginas}'

    def __len__(self):
        return self.paginas

    def __del__(self):
        print(f'Um objeto do tipo Livro {self} foi deletado da memória')

    def __add__(self, other):
        return f'{self} - {other}'

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += ' ' + str(self)
            return msg
        return 'Nao posso multiplicar'


livro1 = Livro('Python', 'Geek', 400)
livro2 = Livro('I.A', 'Geek', 800)

print(livro1)
print(livro2)
print(len(livro2))
print(livro1 + livro2)
print(livro1 * 3)
