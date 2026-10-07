import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem, QHeaderView

# Se importa desde Bancos_ui en lugar de Bancos
from src.app.ui.Bancos_ui import Ui_VentanaBancos

# Importación de la conexión a PostgreSQL
from database.connection import get_db_connection


class VentanaBancos(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Inicializar la interfaz visual
        self.ui = Ui_VentanaBancos()
        self.ui.setupUi(self)

        # Mostrar la página de Insertar/Agregar por defecto
        if hasattr(self.ui, "stackedCRUDBanco"):
            self.ui.stackedCRUDBanco.setCurrentIndex(1)
        elif hasattr(self.ui, "staAckedWidget"):
            self.ui.stackedCRUDBanco.setCurrentIndex(1)

        # Conectar botones y eventos de la tabla
        self._conectar_eventos()

        # Cargar los registros iniciales
        self.cargar_bancos()

    def _conectar_eventos(self):
        if hasattr(self.ui, "pInsertarBanco"):
            self.ui.pInsertarBanco.clicked.connect(self.insertar_banco)
            self.ui.pActualizarBanco.clicked.connect(self.actualizar_banco)
            self.ui.pEliminarBanco.clicked.connect(self.eliminar_banco)
            self.ui.pBuscarBanco.clicked.connect(self.buscar_banco)
        elif hasattr(self.ui, "pushButton_2"):
            self.ui.pBuscarBanco.clicked.connect(self.insertar_banco)
            self.ui.pActualizarBanco.clicked.connect(self.actualizar_banco)
            self.ui.pEliminarBanco.clicked.connect(self.eliminar_banco)
            self.ui.pBuscarBanco.clicked.connect(self.buscar_banco)

        if hasattr(self.ui, "VistaBancos"):
            self.ui.VistaBancos.itemClicked.connect(self.seleccionar_fila)
        elif hasattr(self.ui, "tableWidget"):
            self.ui.VistaBancos.itemClicked.connect(self.seleccionar_fila)

    def cargar_bancos(self, queryl= "SELECT idbanco, nombre FROM banco ORDER BY idbanco ASC;"):
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(queryl) #type: ignore
                registros = cursor.fetchall()

                tabla = getattr(self.ui, "VistaBancos", getattr(self.ui, "tableWidget", None))
                if tabla:
                    tabla.setRowCount(0)
                    tabla.setColumnCount(2)
                    tabla.setHorizontalHeaderLabels(["ID Banco", "Nombre"])
                    tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

                    for row_idx, row_data in enumerate(registros):
                        tabla.insertRow(row_idx)
                        for col_idx, value in enumerate(row_data):
                            tabla.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

                cursor.close()
        except Exception as e:
            QMessageBox.critical(self, "Error de Base de Datos", f"No se pudieron cargar los registros: {e}")

    def insertar_banco(self):
        id_banco = getattr(self.ui, "lineIDBanco", getattr(self.ui, "lineEdit", None)).text().strip() #type: ignore
        nombre = getattr(self.ui, "lineNombreBanco", getattr(self.ui, "lineEdit_2", None)).text().strip() #type: ignore

        if not id_banco or not nombre:
            QMessageBox.warning(self, "Campos Incompletos", "Completa el ID y el Nombre del Banco.")
            return

        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO banco (idbanco, nombre) VALUES (%s, %s);", (id_banco, nombre))
                conn.commit()
                cursor.close()

            QMessageBox.information(self, "Éxito", "Banco registrado correctamente.")
            self.limpiar_campos()
            self.cargar_bancos()
        except Exception as e:
            QMessageBox.critical(self, "Error de Inserción", f"No se pudo guardar el registro: {e}")

    def actualizar_banco(self):
        id_banco = getattr(self.ui, "lineIDBanco", getattr(self.ui, "lineEdit", None)).text().strip() #type: ignore
        nombre = getattr(self.ui, "lineNombreBanco", getattr(self.ui, "lineEdit_2", None)).text().strip() #type: ignore

        if not id_banco or not nombre:
            QMessageBox.warning(self, "Campos Incompletos", "Selecciona una fila o ingresa el nuevo nombre.")
            return

        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE banco SET nombre = %s WHERE idbanco = %s;", (nombre, id_banco))
                conn.commit()
                cursor.close()

            QMessageBox.information(self, "Éxito", "Banco actualizado correctamente.")
            self.limpiar_campos()
            self.cargar_bancos()
        except Exception as e:
            QMessageBox.critical(self, "Error de Actualización", f"No se pudo actualizar el registro: {e}")

    def eliminar_banco(self):
        id_banco = getattr(self.ui, "lineIDBanco", getattr(self.ui, "lineEdit", None)).text().strip() #type: ignore

        if not id_banco:
            QMessageBox.warning(self, "Atención", "Ingresa o selecciona un ID para eliminar.")
            return

        confirmar = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Deseas eliminar permanentemente el banco con ID {id_banco}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if confirmar == QMessageBox.StandardButton.Yes:
            try:
                with get_db_connection() as conn:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM banco WHERE idbanco = %s;", (id_banco,))
                    conn.commit()
                    cursor.close()

                QMessageBox.information(self, "Éxito", "Banco eliminado correctamente.")
                self.limpiar_campos()
                self.cargar_bancos()
            except Exception as e:
                QMessageBox.critical(self, "Error de Eliminación", f"No se pudo eliminar el registro: {e}")

    def buscar_banco(self):
        id_banco = getattr(self.ui, "lineIDBanco", getattr(self.ui, "lineEdit", None)).text().strip() #type: ignore
        nombre = getattr(self.ui, "lineNombreBanco", getattr(self.ui, "lineEdit_2", None)).text().strip() #type: ignore

        if id_banco:
            query = f"SELECT idbanco, nombre FROM banco WHERE idbanco = '{id_banco}';"
        elif nombre:
            query = f"SELECT idbanco, nombre FROM banco WHERE nombre ILIKE '%{nombre}%';"
        else:
            query = "SELECT idbanco, nombre FROM banco ORDER BY idbanco ASC;"

        self.cargar_bancos(query)

    def seleccionar_fila(self, item):
        tabla = getattr(self.ui, "VistaBancos", getattr(self.ui, "tableWidget", None))
        if tabla:
            row = item.row()
            id_banco = tabla.item(row, 0).text()
            nombre = tabla.item(row, 1).text()

            line_id = getattr(self.ui, "lineIDBanco", getattr(self.ui, "lineEdit", None))
            line_nombre = getattr(self.ui, "lineNombreBanco", getattr(self.ui, "lineEdit_2", None))

            if line_id:
                line_id.setText(id_banco)
            if line_nombre:
                line_nombre.setText(nombre)

    def limpiar_campos(self):
        line_id = getattr(self.ui, "lineIDBanco", getattr(self.ui, "lineEdit", None))
        line_nombre = getattr(self.ui, "lineNombreBanco", getattr(self.ui, "lineEdit_2", None))

        if line_id:
            line_id.clear()
        if line_nombre:
            line_nombre.clear()

    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaBancos()
    ventana.show()
    sys.exit(app.exec())