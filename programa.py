def obter_informacoes_aluno():
    """Solicita informações do aluno e retorna um dicionário com os dados."""
    aluno = {}
    
    # Solicita o nome do aluno
    aluno['nome'] = input('Digite o nome do aluno: ').strip()
    
    # Solicita a média do aluno e garante que seja um número válido
    while True:
        try:
            aluno['media'] = float(input(f'Digite a média de {aluno["nome"]}: '))
            if 0 <= aluno['media'] <= 10:  # Verifica se a média está entre 0 e 10
                break
            else:
                print("A média deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    # Avalia a situação do aluno com base na média
    aluno['situacao'] = 'Aprovado' if aluno['media'] >= 7 else 'Reprovado'
    
    return aluno

def exibir_informacoes_aluno(aluno):
    """Exibe as informações do aluno de forma formatada."""
    print("\nInformações do Aluno:")
    for chave, valor in aluno.items():
        print(f'{chave.capitalize()} é igual a {valor}')

def main():
    """Função principal que executa o programa."""
    aluno = obter_informacoes_aluno()
    exibir_informacoes_aluno(aluno)

if __name__ == "__main__":
    main()
