import sys, os
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QMainWindow
from principal_ui import Ui_Buscardor
from resultado_ui import Ui_Resultado


class Resultado(QMainWindow):
    def __init__(self):
        super(Resultado, self).__init__()
        self.ui = Ui_Resultado()
        self.ui.setupUi(self)

    @Slot()
    def cerrar(self):
        self.close()


class Principal(QMainWindow):
    def __init__(self):
        super(Principal, self).__init__()
        self.ui = Ui_Buscardor()
        self.ui.setupUi(self)
        self.opened_file = None

    @Slot()
    def buscar(self):
        self.nombre = self.ui.lblNombre.text() #Lee la caja de texto
        self.user = os.popen("whoami").read() #Obtiene el usuario
        self.user = self.user.rsplit() #Elimina el salto de carro
        self.deruta = "/home/"+self.user[0] #Arma la ruta
        os.chdir(self.deruta) #Configura donde se ejecuta el comando
        self.resultado = os.popen("find -not -path '*/\.*' | grep '" + self.nombre + "'").read() #Busca los archivos que coinciden
        print(self.resultado)
        self.ventanita = Resultado() #Se crea un objeto que es la ventana nueva
        self.ventanita.ui.txtResultado.setText(self.resultado) #Le pasa el resultado a la caja de texto
        self.ventanita.show() #Configura donde se va a efectuar el comando

    @Slot()
    def borrar(self):
        self.ui.lblNombre.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Principal()
    window.show()
    sys.exit(app.exec_())