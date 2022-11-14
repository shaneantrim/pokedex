import sys
# from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QDialog, QGroupBox, QLabel
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QWidget, QLabel
from PySide2.QtGui import QPalette, QColor, QImage, QPixmap
import requests

# class Color(QWidget):

#     def __init__(self, color):
#         super(Color, self).__init__()
#         self.setAutoFillBackground(True)

#         palette = self.palette()
#         palette.setColor(QPalette.Window, QColor(color))
#         self.setPalette(palette)

def fetchPokemonImage(name):
  # grabs data from the pokemon API
  URL = "https://pokeapi.co/api/v2/pokemon/"
  # make a request to get data from the pokemon server
  link = URL + name
  response = requests.get(url = link)
  
  # .json() takes a response from a website
  # and turns into a dictionary so that
  # programmers can use the data
  data = response.json()
  return data["sprites"]["front_default"]
  
class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Pokemon Image Finder")
        self.setMinimumWidth(200)
        self.setContentsMargins(20,20,20,20)

        self.create_widgets()
        self.create_layouts()

    def create_widgets(self):
        self.label = QLabel("Enter a Pokemon Name")
        self.lineEdit = QtWidgets.QLineEdit()
        self.button = QtWidgets.QPushButton("Search")
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.setMinimumHeight(100)
        self.imageLabel = QLabel()
        # self.button(Color('blue'))

    def create_layouts(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.lineEdit)
        main_layout.addWidget(self.imageLabel)
        main_layout.addWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("Loading Image...")
        self.button.setEnabled(False)
        pokemonName = self.lineEdit.text()
        imageURL = fetchPokemonImage(pokemonName)

        image = QImage()
        image.loadFromData(requests.get(imageURL).content)
      
        self.imageLabel.setPixmap(QPixmap(image))
        self.imageLabel.show()

        
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()

