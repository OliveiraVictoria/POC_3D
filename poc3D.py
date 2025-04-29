import pyvista as pv
import numpy as np  # Para manipulação numérica
import os  # Para lidar com caminhos de arquivos

print('VISUALIZAÇÃO POC')

# Subpasta onde estão os arquivos .stl
pasta_modelos = "stl"  # Subpasta 'stl' dentro da pasta atual

# Caminhos relativos para os arquivos .stl
caminho_modelo_1 = os.path.join(pasta_modelos, "casing.STL")
caminho_modelo_2 = os.path.join(pasta_modelos, "tubing.STL")
caminho_modelo_3 = os.path.join(pasta_modelos, "poc.STL")

# Carregar os modelos .stl
modelo_1 = pv.read(caminho_modelo_1)  # Casing
modelo_2 = pv.read(caminho_modelo_2)  # Tubing
modelo_3 = pv.read(caminho_modelo_3)  # POC

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