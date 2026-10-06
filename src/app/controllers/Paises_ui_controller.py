from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Qt
from app.services import PaisService
from app.ui import Ui_VentanaPaises
from app.presenters.pais_table_model import PaisTableModel


class VentanaPais(QWidget):
    def __init__(self, pais_service):
        super().__init__()
        self.ui = Ui_VentanaPaises()
        self.ui.setupUi(self)

        self.service: PaisService = pais_service

        self.table_model = PaisTableModel(self)
        self.ui.vistaPaises.setModel(self.table_model)

        self.ui.vistaPaises.setSelectionBehavior(
            self.ui.vistaPaises.SelectionBehavior.SelectRows
        )
        self.ui.vistaPaises.setSelectionMode(
            self.ui.vistaPaises.SelectionMode.SingleSelection
        )
        self.ui.vistaPaises.setEditTriggers(
            self.ui.vistaPaises.EditTrigger.NoEditTriggers
        )
        self.ui.vistaPaises.horizontalHeader().setStretchLastSection(True)

        self.ui.ppaisNuevo.clicked.connect(self.on_nuevo)
        self.ui.ppaisActualizar.clicked.connect(self.on_actualizar)
        self.ui.ppaisEliminar.clicked.connect(self.on_eliminar)
        self.ui.ppaisBuscar.clicked.connect(self.on_buscar)

        self.ui.vistaPaises.doubleClicked.connect(self.on_fila_seleccionada)

        self.refrescar_tabla()

    def refrescar_tabla(self):

        try:
            paises = self.service.listar() # type: ignore[call-arg]
            self.table_model.set_data(paises)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar la lista:\n{e}")

    def limpiar_formulario(self):
        self.ui.lineIDPais.clear()
        self.ui.lineNombrePais.clear()

    def _id_actual(self):
        txt = self.ui.lineIDPais.text().strip()
        return int(txt) if txt.isdigit() else None


    def on_nuevo(self):
        idpais = self.ui.lineIDPais.text()
        nombre = self.ui.lineNombrePais.text()
        try:
            self.service.crear(idpais, nombre) # type: ignore[call-arg]
        except ValueError as e:
            QMessageBox.warning(self, "Validación", str(e))
            return
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            return

        self.limpiar_formulario()
        self.refrescar_tabla()          # <- aquí se actualiza la tabla

    def on_actualizar(self):
        idpais = self._id_actual()
        if idpais is None:
            QMessageBox.warning(self, "Validación", "Seleccione un país válido.")
            return
        try:
            self.service.actualizar(idpais, self.ui.lineNombrePais.text()) # type: ignore[call-arg]
        except ValueError as e:
            QMessageBox.warning(self, "Validación", str(e))
            return
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            return

        self.limpiar_formulario()
        self.refrescar_tabla()

    def on_eliminar(self):
        idpais = self._id_actual()
        if idpais is None:
            QMessageBox.warning(self, "Validación", "Seleccione un país válido.")
            return
        if QMessageBox.question(self, "Confirmar",
                                f"¿Eliminar país id={idpais}?") != QMessageBox.StandardButton.Yes:
            return
        try:
            self.service.eliminar(idpais) # type: ignore[call-arg]
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            return

        self.limpiar_formulario()
        self.refrescar_tabla()

    def on_buscar(self):
        idpais = self._id_actual()
        if idpais is None:
            QMessageBox.warning(self, "Validación", "Ingrese un ID numérico.")
            return
        pais = self.service.buscar_por_id(idpais) # type: ignore[call-arg]
        if pais is None:
            QMessageBox.information(self, "Buscar", "No se encontró el país.")
            return
        self.ui.lineNombrePais.setText(pais.nombre)

    def on_fila_seleccionada(self, index):
        pais = self.table_model.get_pais_at(index.row())
        if pais:
            self.ui.lineIDPais.setText(str(pais.idpais))
            self.ui.lineNombrePais.setText(pais.nombre)     