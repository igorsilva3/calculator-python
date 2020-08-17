from app.interface import Application
import sys

Calculadora = Application(sys.argv)

def main(app):
    folder = "UI"
    filename = "calculadora.ui"

    file = app.get_ui_file(folder, filename)

    MainWindow = app.loadUiWidget(file)
    MainWindow.show()
    sys.exit(app.init_app.exec_())


if __name__ == "__main__":
    main(Calculadora)
