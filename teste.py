usuarios=[]
usuarios = ([{'clientes': {1: {'cpf': '090987', 'nome': 'jose', 'data_nascimento': 'data_nascimento', 'endereco': 'endereco'}}}], [{'clientes': {1: {'cpf': '090987', 'nome': 'jose', 'data_nascimento': 'data_nascimento', 'endereco': 'endereco'}}}])
cpf = '090987'
print(usuarios)
if usuarios[0]['clientes'][1]['cpf'] == cpf:
    print('CPF já em uso!')

else:
    print('cpf adicionado com sucesso!')





# if usuarios['clientes'][1]['cpf'] == cpf:
#     print('CPF já em uso!')

# else:
#     print('cpf adicionado com sucesso!')