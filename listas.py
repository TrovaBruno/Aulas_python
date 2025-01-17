nomes = ['Luiz', 'Maria', 'Joao', 'Helena']
# novos_nomes = [nome.lower() for nome in nomes] ////minusculas
# novos_nomes = [nome.upper() for nome in nomes] ////maiuscula
# novos_nomes = [nome.title() for nome in nomes] ////Primeiro maiuscula
novos_nomes = [
    f'{nome[:-1].lower()}{nome[-1].upper()}'
    for nome in nomes] 

print(novos_nomes)