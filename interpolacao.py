mail_tmpl = """
olá, %(nome)s
 
teria interesse em comprar %(produto)s?
 
o produto pode te ajudar com %(texto)s
 
clique agora em %(link)s
 
apenas %(quantidade)d disponíveis!

preço promocional: %(preco).2f
"""

clientes = ['maria', 'joao', 'bruno']

for cliente in clientes:
    print(mail_tmpl % {'nome': cliente, 'produto': 'caneta', 'texto': 'a escrita de textos', 'link': 'https://canetaboa.com.br', 'quantidade': 1, 'preco': 50.5})
