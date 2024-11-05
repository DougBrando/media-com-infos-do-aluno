# Cria um dicionário para armazenar informações do aluno
aluno = {}

# Solicita o nome do aluno e armazena no dicionário
aluno['nome'] = input('Digite o nome do aluno: ')

# Solicita a média do aluno e armazena no dicionário, convertendo para float
aluno['media'] = float(input(f'Digite a média de {aluno["nome"]}: '))

# Avalia a situação do aluno com base na média
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'  # Se a média for maior ou igual a 7, o aluno está aprovado
else:
    aluno['situacao'] = 'Reprovado'  # Caso contrário, o aluno está reprovado

# Exibe as informações do aluno
print("\nInformações do Aluno:")
for chave, valor in aluno.items():
    print(f'{chave.capitalize()} é igual a {valor}')  # Capitaliza a primeira letra da chave para melhor apresentação
