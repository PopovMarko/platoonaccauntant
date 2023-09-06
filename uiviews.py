from PySide6.QtWidgets import QMainWindow
from PySide6 import QtWidgets
from PySide6.QtSql import QSqlTableModel, QSqlRelation, QSqlRelationalTableModel
from ui_main import Ui_MainWindow
from ui_addgoods import Ui_add_goods
from ui_addservice import Ui_add_service 
from ui_addinvoicetype import Ui_add_invoicetype
from ui_addsupervisor import Ui_add_supervisor
from ui_addinvoice import Ui_add_invoice

class MWindow (QMainWindow):
    def __init__(self):
        super(MWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.goodsButton.clicked.connect(self.view_data_goods)
        # self.ui.invoicesButton.clicked.connect(self.view_data_invoices)
        # self.ui.addGoodsButton.clicked.connect(self.handler.btn_clicked)
        # self.ui.addServiceButton.clicked.connect(lambda Ui_add_service : self.open_new_dialog_window(Ui_add_service))
        # self.ui.addInvoiceTypeButton.clicked.connect(lambda Ui_add_invoicetype : self.open_new_dialog_window(Ui_add_invoicetype))
        # self.ui.addSupervisorButton.clicked.connect(lambda Ui_add_supervisor : self.open_new_dialog_window(Ui_add_supervisor))
        # self.ui.addInvoiceButton.clicked.connect(lambda Ui_add_invoice : self.open_new_dialog_window(Ui_add_invoice))

    def open_new_dialog_window(self, ui_view):
        """universal method for initialise all new windows"""
        self.ui_new_window = QtWidgets.QDialog()
        self.new_dialog = ui_view()
        self.new_dialog.setupUi(self.ui_new_window)

        if self.sender.objectName() == 'addServiceButton':
            """model for supervisor combo on new service window"""
            self.model = QSqlTableModel(self)
            self.model.setTable('supervisors')
            self.model.setQuery('SELECT supervisor_id, last_name FROM supervisors')
            self.model.select()
            self.model.removeColumn(0)
            self.new_dialog.cb_supervisor.setModel(self.model)

        elif self.sender.objectName() == 'addInvoiceButton':
            """models for combo and table on new invoice window"""
            self.tablemodel = QSqlRelationalTableModel(self)
            self.tablemodel.setTable('invoice_goods')
            self.tablemodel.setRelation(1, QSqlRelation('goods', 'goods_id', 'name')) 
            self.tablemodel.setRelation(2, QSqlRelation('invoices', 'invoice_id', 'invoice_number'))
            self.tablemodel.select()
            self.new_dialog.tableView.setModel(self.tablemodel)

            """model for Invoice_type combo"""
            self.cb_type_model = QSqlTableModel(self)
            self.cb_type_model.setTable('invoice_type')
            self.cb_type_model.select()
            self.new_dialog.cb_invoice_type.setModel(self.cb_type_model)

            """molel for service name combo"""
            self.cb_serv_name_model = QSqlTableModel(self)
            self.cb_serv_name_model.setTable('services')
            self.cb_serv_name_model.select()
            self.new_dialog.cb_serv_name.setModel(self.cb_serv_name_model)
            
            """model for sender supervisor combo"""
            self.cb_sender_supervisor_model = QSqlTableModel(self)
            self.cb_sender_supervisor_model.setTable('supervisors')
            self.cb_sender_supervisor_model.select()
            self.new_dialog.cb_sender_supervisor.setModel(self.cb_sender_supervisor_model)

            """model for reciver supervisor combo"""
            self.cb_rec_supervisor_model = QSqlTableModel(self)
            self.cb_rec_supervisor_model.setTable('supervisors')
            self.cb_rec_supervisor_model.select()
            self.new_dialog.cb_rec_supervisor.setModel(self.cb_rec_supervisor_model)
             
        self.ui_new_window.show()

        self.new_dialog.cancel.clicked.connect(self.ui_new_window.close)
        if sender.objectName() == 'addGoodsButton':
            self.new_dialog.save.clicked.connect(self.add_new_goods)
            self.new_dialog.save.clicked.connect(self.btn_clicked)
        elif sender.objectName() == 'addServiceButton':
            self.new_dialog.save.clicked.connect(self.add_new_service)
        elif sender.objectName() == 'addInvoiceTypeButton':
            self.new_dialog.save.clicked.connect(self.add_new_invoice_type)
        elif sender.objectName() == 'addSupervisorButton':
            self.new_dialog.save.clicked.connect(self.add_new_supervisor)
        elif sender.objectName() == 'addInvoiceButton':
            self.new_dialog.save.clicked.connect(self.add_new_invoice)
