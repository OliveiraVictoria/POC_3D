import sys
import os
import numpy as np
import pyvista as pv
from pyvistaqt import QtInteractor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton,
    QVBoxLayout, QHBoxLayout, QSpinBox, QMessageBox
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("POC 3D Viewer")
        self.resize(800, 450)
        self.centralizar_janela()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout_principal = QVBoxLayout(self.central_widget)

        self.btn_run = QPushButton("Run POC")
        self.btn_run.clicked.connect(self.inicializar_visualizacao)
        self.layout_principal.addWidget(self.btn_run)

        self.plotter_widget = None

    def centralizar_janela(self):
        tela = QApplication.primaryScreen().availableGeometry()
        x = (tela.width() - self.width()) // 2
        y = (tela.height() - self.height()) // 2
        self.move(x, y)

    def inicializar_visualizacao(self):
        QMessageBox.information(self, "Inicialização", "Aguarde alguns instantes... A visualização da POC será exibida.")
        self.btn_run.hide()

        self.plotter = QtInteractor(self)
        self.plotter.setMinimumSize(1000, 500)
        self.layout_principal.addWidget(self.plotter)

        pasta_modelos = "stl"
        caminho_modelo_1 = os.path.join(pasta_modelos, "casing.STL")
        caminho_modelo_2 = os.path.join(pasta_modelos, "tubing.STL")
        caminho_modelo_3 = os.path.join(pasta_modelos, "poc.STL")

        self.modelo_1 = pv.read(caminho_modelo_1)
        self.modelo_2 = pv.read(caminho_modelo_2)
        self.modelo_3 = pv.read(caminho_modelo_3)

        self.actor_1 = self.plotter.add_mesh(self.modelo_1, color="grey", opacity=0.1)
        self.actor_2 = self.plotter.add_mesh(self.modelo_2, color="darkgrey", opacity=0.3)
        self.actor_3 = self.plotter.add_mesh(self.modelo_3, color="violet", opacity=1)

        self.plotter.camera.focal_point = (264, 918, 865)
        self.plotter.camera.view_up = (0, 1, 0)
        self.plotter.camera.position = (-30, 1000, 980)
        self.plotter.camera.view_angle = 30.0
        self.plotter.camera.SetParallelProjection(True)
        self.plotter.renderer.ResetCamera()
        self.plotter.render()

        # Opacidade Casing
        self.spin_opacidade_casing = QSpinBox()
        self.spin_opacidade_casing.setRange(1, 100)
        self.spin_opacidade_casing.setValue(10)
        self.btn_opacidade_casing = QPushButton("Opacidade Casing")
        self.btn_opacidade_casing.clicked.connect(self.alterar_opacidade_casing)

        opacidade_casing_layout = QHBoxLayout()
        opacidade_casing_layout.addWidget(self.spin_opacidade_casing)
        opacidade_casing_layout.addWidget(self.btn_opacidade_casing)
        self.layout_principal.addLayout(opacidade_casing_layout)

        # Opacidade Tubing
        self.spin_opacidade = QSpinBox()
        self.spin_opacidade.setRange(1, 100)
        self.spin_opacidade.setValue(30)
        self.btn_opacidade = QPushButton("Opacidade Tubing")
        self.btn_opacidade.clicked.connect(self.alterar_opacidade_tubing)

        opacidade_layout = QHBoxLayout()
        opacidade_layout.addWidget(self.spin_opacidade)
        opacidade_layout.addWidget(self.btn_opacidade)
        self.layout_principal.addLayout(opacidade_layout)

        # Movimento Tubing
        self.spin_posicao_tubing = QSpinBox()
        self.spin_posicao_tubing.setRange(-50, 50)
        self.spin_posicao_tubing.setValue(0)
        self.btn_posicao_tubing = QPushButton("Mover Tubing")
        self.btn_posicao_tubing.clicked.connect(self.mover_tubing)

        posicao_tubing_layout = QHBoxLayout()
        posicao_tubing_layout.addWidget(self.spin_posicao_tubing)
        posicao_tubing_layout.addWidget(self.btn_posicao_tubing)
        self.layout_principal.addLayout(posicao_tubing_layout)

        # Movimento Casing
        self.spin_posicao_casing = QSpinBox()
        self.spin_posicao_casing.setRange(-50, 50)
        self.spin_posicao_casing.setValue(0)
        self.btn_posicao_casing = QPushButton("Mover Casing")
        self.btn_posicao_casing.clicked.connect(self.mover_casing)

        posicao_casing_layout = QHBoxLayout()
        posicao_casing_layout.addWidget(self.spin_posicao_casing)
        posicao_casing_layout.addWidget(self.btn_posicao_casing)
        self.layout_principal.addLayout(posicao_casing_layout)

    def alterar_opacidade_tubing(self):
        opacidade = self.spin_opacidade.value() / 100.0
        self.actor_2.GetProperty().SetOpacity(opacidade)
        self.plotter.render()

    def alterar_opacidade_casing(self):
        opacidade = self.spin_opacidade_casing.value() / 100.0
        self.actor_1.GetProperty().SetOpacity(opacidade)
        self.plotter.render()

    def mover_tubing(self):
        valor = self.spin_posicao_tubing.value()
        self.modelo_2.translate([valor * 10, 0, 0], inplace=True)
        self.plotter.render()

    def mover_casing(self):
        valor = self.spin_posicao_casing.value()
        self.modelo_1.translate([valor * 10, 0, 0], inplace=True)
        self.plotter.render()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())