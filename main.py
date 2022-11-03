import sys
import win32com.client
import pandas as pd
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Requisição de compra")

        # # #
        # Botões de Comando
        self.btn_abrir.clicked.connect(self.open_file)
        self.btn_gerar.clicked.connect(self.registrar_compras)
        # # #

    def open_file(self):
        self.file = QFileDialog.getOpenFileName(self, "Selecione a Planilha")
        self.txt_path.setText(str(self.file[0]))



    def connect_sap(self):
        
        SapGuiAuto = win32com.client.GetObject("SAPGUI")
        application = SapGuiAuto.GetScriptingEngine
        connection = application.Children(0)
        session    = connection.Children(0)

    def registrar_compras(self):

        self.connect_sap()
        self.file = self.txt_path.text
        data = pd.read_excel(self.file)
        data = data.values.tolist()

        self.session.findById("wnd[0]/tbar[0]/okcd").text = "ME51N"
        self.session.findById("wnd[0]").sendVKey(0)
        
        id = 0
        mygrid = self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:3212/cntlGRIDCONTROL/shellcont/shell").modifyCell
       
        for i, j in enumerate(data):
            if id == 0:
                mygrid.modifyCell(i, "MATNR", j[0])
                mygrid.modifyCell(i, "MENGE", j[1])
                mygrid.modifyCell(i, "NAME1", j[2])
                mygrid.pressEnter
            else:
                mygrid2 = self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0015/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:3212/cntlGRIDCONTROL/shellcont/shell").modifyCell

            mygrid2.modifyCell(i, "MATNR", j[0])
            mygrid2.modifyCell(i, "MENGE", j[1])
            mygrid2.modifyCell(i, "NAME1", j[2])
            mygrid2.pressEnter()

            id+=1

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Registros efetuados com sucesso!")
        msg.exec_()
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

