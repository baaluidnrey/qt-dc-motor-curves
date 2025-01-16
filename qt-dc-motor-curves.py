#!/usr/bin/env python3

"""
qt-dc-motor-curves
"""
__author__ = "Aline Baudry"
__github__ = "baaluidnrey"

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
# from matplotlib.figure import Figure
# import matplotlib.pyplot as plt


class DC_motor_data(QWidget):
     
    def __init__(self, label, value, min=0, max=10000, step=10, parent=None):
        super(DC_motor_data, self).__init__(parent)
        self.label = QLabel(label)
        self.spinbox = QDoubleSpinBox()
        self.spinbox.setMinimum(min)
        self.spinbox.setMaximum(max)
        self.spinbox.setSingleStep(step)
        self.spinbox.setValue(value)
        
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.spinbox)
        self.setLayout(layout)
        
    def value(self):
        return self.spinbox.value()
    
    def set_value(self, value):
        self.spinbox.setValue(value)



# class Graph(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)

#         # ---------------------------------------------------------------------
#         # ATTRIBUTS
#         # ---------------------------------------------------------------------
#         self.figure = Figure(figsize=(10, 5))
#         # self.canvas = FigureCanvas(self.figure)
#         self.ax = self.figure.gca()

#         # ---------------------------------------------------------------------
#         # AXES, TITRES, ETC.
#         # ---------------------------------------------------------------------
#         self.ax.set_title("Force measurement")
#         self.ax.grid(True)
#         self.ax.set_xlabel("Time [secs]")
#         self.ax.set_ylabel("Force [N]")
#         self.ax.set_xlim(0, 50)
#         self.ax.set_ylim(0, 50)

#         # ---------------------------------------------------------------------
#         # CREATION DES GRAPHES
#         # ---------------------------------------------------------------------
#         self.force_plot, = self.ax.plot([], [], color="red", label="data")
#         self.force_t = []
#         self.force_data = []

#         # ---------------------------------------------------------------------
#         # MISE EN FORME
#         # ---------------------------------------------------------------------
#         layout = QVBoxLayout()
#         layout.addWidget(self.canvas)
#         self.setLayout(layout)

#     # -------------------------------------------------------------------------
#     # MISE A JOUR DE LA FIGURE
#     # -------------------------------------------------------------------------

#     def update_data(self, t, data):
#         self.force_t.append(t)
#         self.force_data.append(data)

#     def clean_data(self):
#         self.force_t = []
#         self.force_data = []
#         self.update_graph()
        
#     def update_graph(self):
#         self.force_plot.set_data(self.force_t, self.force_data)
#         # self.canvas.draw()
        


class DC_motor_curves(QMainWindow):
    
    def __init__(self, parent=None):
        super(DC_motor_curves, self).__init__(parent)

        # technical data motor
        self.power_n = DC_motor_data(label='Nominal power [W]', value=350)
        self.speed_n = DC_motor_data(label='Nominal speed [RPM]', value=4300)
        self.torque_n = DC_motor_data(label='Nominal torque [N.m]', value=0.71)
        self.voltage_n = DC_motor_data(label='Nominal voltage [V]', value=24)
        self.current_n = DC_motor_data(label='Nominal current [A]', value=20)
        
        self.torque_cste = DC_motor_data(label='Torque constant [N.m/A]', value=0.05)
        self.motor_voltage_cste = DC_motor_data(label='Motor voltage constant [V.s/rad]', value=0.048)
        
        self.resistance = DC_motor_data(label='Resistance [Ohm]', value=0.120)
        self.inductance = DC_motor_data(label='Inductance [H]', value=0.0001)
        
        self.dry_friction = DC_motor_data(label='Dry friction [N.m]', value=0.2)
        self.viscous_friction = DC_motor_data(label='Viscous friction coefficient [N.m.s/rad]', value=0.0004)
        self.inertia = DC_motor_data(label='Inertia [kg·m^2]', value=0.000012)
        
        
        self.graph = QWidget()
        
        
        # DC Motor parameters
        # -----------
        params_layout = QVBoxLayout()
        params_layout.addWidget(self.power_n)
        params_layout.addWidget(self.speed_n)
        params_layout.addWidget(self.torque_n)
        params_layout.addWidget(self.voltage_n)
        params_layout.addWidget(self.current_n)
        
        params_layout.addWidget(self.torque_cste)
        params_layout.addWidget(self.motor_voltage_cste)
        
        params_layout.addWidget(self.resistance)
        params_layout.addWidget(self.inductance)
        
        params_layout.addWidget(self.dry_friction)
        params_layout.addWidget(self.viscous_friction)
        params_layout.addWidget(self.inertia) 


        # Figures
        # -----------
        layout_fig = QHBoxLayout()
        layout_fig.addWidget(self.graph)

        # Main Layout
        # -----------
        main_layout = QHBoxLayout()
        main_layout.addLayout(params_layout)
        main_layout.addLayout(layout_fig)

        # Widget Central
        # -----------
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        
        self.setWindowTitle("DC motor curves")
        

 
        
def main():
   app = QApplication(sys.argv)
   dc_motor_curves = DC_motor_curves()
   dc_motor_curves.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main() 