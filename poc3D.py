import pyvista as pv
import numpy as np  # Para manipulação numérica

print('VISUALIZAÇÃO POC')

# Carregar os modelos .stl
modelo_1 = pv.read("casing.STL")  # Substitua pelo nome do primeiro arquivo
modelo_2 = pv.read("tubing.STL")  # Substitua pelo nome do segundo arquivo
modelo_3 = pv.read("poc.STL")  # Substitua pelo nome do terceiro arquivo

# Criar o plotter para visualização
plotter = pv.Plotter()

# Calcular os centros geométricos e convertê-los em arrays NumPy
centro_modelo_1 = np.array(modelo_1.center)
centro_modelo_2 = np.array(modelo_2.center)
centro_modelo_3 = np.array(modelo_3.center)

# Reposicionar todos os modelos para a origem
modelo_1.translate(-centro_modelo_1)  # Centraliza o casing na origem
modelo_2.translate(-centro_modelo_2)  # Centraliza o tubing na origem
modelo_3.translate(-centro_modelo_3)  # Centraliza a POC na origem

# Adicionar os modelos ao plotter com cores e opacidades iniciais
actor_1 = plotter.add_mesh(modelo_1, color="grey", opacity=0.1)  # Casing com opacidade reduzida
actor_2 = plotter.add_mesh(modelo_2, color="dark grey", opacity=0.3)  # Tubing com opacidade ajustada
actor_3 = plotter.add_mesh(modelo_3, color="violet", opacity=1)  # POC com opacidade máxima

# Mostrar os eixos para ajudar no alinhamento
plotter.show_axes()
plotter.camera_position = 'iso'

# Exibir o ambiente interativo
plotter.show()