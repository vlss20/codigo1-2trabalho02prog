def registrar_aula(disciplina, boletim_aluno):
    """""
    Simula o registro de uma nova aula.
    Tenta alterar o nome da disciplina (string, imutável) e atualiza
    o boletim do aluno (dicionário, mutável) com novas notas e mais faltas.
    """
    # Tentativa de mudar a string (imutável)
    # A variável original 'materia' permanecerá a mesma, pois é imutável.
    disciplina = disciplina + " - Semestre 2025/2"
    print(f"    -> Dentro da função, a variável 'disciplina' é: '{disciplina}'")

    # Modificando o dicionário (mutável)
    # As alterações são feitas no objeto original pois a função recebeu uma referência a ele.
    nova_nota = 9.0
    boletim_aluno['notas'].append(nova_nota) # Adiciona um item na lista de notas
    boletim_aluno['faltas'] += 1             # Aumento o número de faltas em 1
    print(f"    -> Dentro da função, o boletim foi atualizado para: {boletim_aluno}") # Mostra o boletim atualizado

# --- Programa Principal (Secretaria da Escola) ---
# Dados iniciais antes do registro da nova aula
materia = "Programação de Sistemas"
boletim = {
    'aluno_id': 123,
    'notas': [7.5, 6.1],
    'faltas': 3
}

print("DADOS ANTES DA CHAMADA DA FUNÇÃO")
print(f"Nome da matéria: '{materia}\n'")
print(f"Boletim do Aluno: {boletim}\n")

# Chamando a função registrar_aula para fazer a mudança no boletim
registrar_aula(materia, boletim)

print("DADOS APÓS A CHAMADA DA FUNÇÃO")
print(f"O nome da matéria não foi alterado: '{materia}'")
print(f"O boletim do aluno foi alterado: {boletim}")