esta_chuvendo = True
print('Hoje estou com as roupas ' + ('secas.', 'molhadas.')[esta_chuvendo]) # A primeira concatena o valor se a a variável for Falsa e a segunda concatena se a variável for Verdadeira.

print('Hoje estou com as roupas ' + ('molhadas.' if esta_chuvendo else 'secas.'))