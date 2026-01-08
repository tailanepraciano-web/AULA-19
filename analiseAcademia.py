import json

#carregar dados json

with open("baseAcademia.json","r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
    
lista_alunos =dados["alunos"]

for aluno in lista_alunos:
    print(f"Nome: {aluno["nome"]} | Mensalidade: R${aluno["mensalidade"]} | Tipo plano:{aluno["plano"]} | Frequência mensal:{aluno["frequencia_mensal"]}")