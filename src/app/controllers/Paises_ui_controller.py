from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator
from PySide6.QtWidgets import (
    QAbstractItemView, QInputDialog, QMainWindow, QMessageBox, QTableWidgetItem
)

from src.app.ui.Paises_ui import Ui_Paises
from src.app.services import Pais_service as service
from src.app.services.Pais_service import PaisError, PATRON_NOMBRE, ID_MAX, NOMBRE_MAX


class VentanaPaises(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Paises()
        self.ui.setupUi(self)

        # VALIDACIÓN 3: longitud máxima
        self.ui.EIdPais.setMaxLength(9)
        self.ui.ENombre.setMaxLength(NOMBRE_MAX)

        # VALIDACIÓN 2: tipo de dato
        # ID: solo números enteros positivos
        self.ui.EIdPais.setValidator(QIntValidator(1, ID_MAX, self))
        # Nombre: solo letras y espacios
        self.ui.ENombre.setValidator(
            QRegularExpressionValidator(QRegularExpression(PATRON_NOMBRE + "|"), self)
        )

        # Tabla: solo lectura, se selecciona toda la fila
        self.ui.TPaises.setColumnCount(2)
        self.ui.TPaises.setHorizontalHeaderLabels(["ID", "Nombre"])
        self.ui.TPaises.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.TPaises.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.TPaises.horizontalHeader().setStretchLastSection(True)

        # Botones
        self.ui.BGuardar.clicked.connect(self.guardar)
        self.ui.BModificar.clicked.connect(self.modificar)
        self.ui.BEliminar.clicked.connect(self.eliminar)
        self.ui.BSalir.clicked.connect(self.close)

        # VALIDACIÓN 8: clic en un registro de la tabla -> llena las cajas
        self.ui.TPaises.cellClicked.connect(self.seleccionar_fila)

        # VALIDACIÓN 5: al terminar de escribir el ID, busca y llena el nombre
        self.ui.EIdPais.editingFinished.connect(self.buscar_por_id)

        # VALIDACIÓN 10: orden del cursor con Tab
        self.setTabOrder(self.ui.EIdPais, self.ui.ENombre)
        self.setTabOrder(self.ui.ENombre, self.ui.BGuardar)
        self.setTabOrder(self.ui.BGuardar, self.ui.BModificar)
        self.setTabOrder(self.ui.BModificar, self.ui.BEliminar)
        self.ui.EIdPais.setFocus()   # el cursor empieza en el ID

        # La tabla se llena sola al abrir
        self.cargar_tabla()

    # ---------- utilidades ----------
    def cargar_tabla(self):
        """VALIDACIÓN 7: refresca la tabla con el SELECT."""
        try:
            paises = service.listar()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar la tabla: {e}")
            return

        self.ui.TPaises.setRowCount(len(paises))
        for fila, p in enumerate(paises):
            self.ui.TPaises.setItem(fila, 0, QTableWidgetItem(str(p["idpais"])))
            self.ui.TPaises.setItem(fila, 1, QTableWidgetItem(p["nombre"]))

    def limpiar(self):
        self.ui.EIdPais.clear()
        self.ui.ENombre.clear()
        self.ui.TPaises.clearSelection()
        self.ui.EIdPais.setFocus()

    def pedir_id(self, titulo, pregunta):
        """Abre una ventanita que pregunta el ID. Regresa el ID o None si cancela."""
        texto = self.ui.EIdPais.text().strip()
        inicial = int(texto) if texto else 1
        id_pais, ok = QInputDialog.getInt(
            self, titulo, pregunta, inicial, 1, ID_MAX
        )
        return id_pais if ok else None

    # ---------- eventos ----------
    def seleccionar_fila(self, fila, columna):
        self.ui.EIdPais.setText(self.ui.TPaises.item(fila, 0).text()) #type: ignore
        self.ui.ENombre.setText(self.ui.TPaises.item(fila, 1).text()) #type: ignore

    def buscar_por_id(self):
        texto = self.ui.EIdPais.text().strip()
        if not texto:
            return
        try:
            pais = service.buscar(texto)
        except PaisError as e:
            QMessageBox.warning(self, e.titulo, e.mensaje)
            return
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al buscar: {e}")
            return
        if pais:
            self.ui.ENombre.setText(pais["nombre"])

    # ---------- botones ----------
    def guardar(self):
        """INSERT de un país nuevo."""
        # VALIDACIONES 1, 2, 3 y 6 (vacíos, tipo, longitud, ID repetido) -> en el service
        try:
            service.crear(self.ui.EIdPais.text(), self.ui.ENombre.text())
        except PaisError as e:
            QMessageBox.warning(self, e.titulo, e.mensaje)
            return
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar: {e}")
            return

        QMessageBox.information(self, "Listo", "País guardado correctamente")
        self.limpiar()
        self.cargar_tabla()

    def modificar(self):
        """UPDATE: pregunta cuál ID quieres modificar."""
        id_pais = self.pedir_id("Modificar", "¿Qué ID de país quieres modificar?")
        if id_pais is None:
            return

        try:
            pais = service.obtener(id_pais)
        except PaisError as e:
            QMessageBox.warning(self, e.titulo, e.mensaje)
            return
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al buscar: {e}")
            return

        # muestra el registro en las cajas
        self.ui.EIdPais.setText(str(id_pais))
        self.ui.ENombre.setText(pais["nombre"])

        nuevo, ok = QInputDialog.getText(
            self, "Modificar", "Escribe el nuevo nombre:", text=pais["nombre"]
        )
        if not ok:
            return

        # VALIDACIONES 1, 2 y 3 -> en el service
        try:
            service.modificar(id_pais, nuevo)
        except PaisError as e:
            QMessageBox.warning(self, e.titulo, e.mensaje)
            return
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo modificar: {e}")
            return

        QMessageBox.information(self, "Listo", "País modificado correctamente")
        self.limpiar()
        self.cargar_tabla()

    def eliminar(self):
        """DELETE: pregunta cuál ID quieres eliminar."""
        id_pais = self.pedir_id("Eliminar", "¿Qué ID de país quieres eliminar?")
        if id_pais is None:
            return

        try:
            # VALIDACIÓN 4: no eliminar si tiene hijos (ciudades) -> en el service
            pais = service.validar_eliminacion(id_pais)

            resp = QMessageBox.question(
                self, "Confirmar", f"¿Seguro que quieres eliminar {pais['nombre']}?"
            )
            if resp != QMessageBox.StandardButton.Yes:
                return

            service.eliminar(id_pais)
        except PaisError as e:
            QMessageBox.warning(self, e.titulo, e.mensaje)
            return
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo eliminar: {e}")
            return

        QMessageBox.information(self, "Listo", "País eliminado correctamente")
        self.limpiar()
        self.cargar_tabla()
