from loguru import logger

from PySide6.QtWidgets import QMainWindow, QDialog
from PySide6.QtSql import QSqlTableModel

from ui_main import Ui_MainWindow
from ui_addgoods import Ui_add_goods
from ui_addservice import Ui_add_service 
from ui_addinvoicetype import Ui_add_invoicetype
from ui_addsupervisor import Ui_add_supervisor
from ui_addinvoice import Ui_add_invoice

from models import MTableModel, WidgetModel
from connection import SqlQueryExec

class MainWindow (QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.opengoods = GoodWindow()
        self.openinvoice = InvoiceWindow()
        self.openservice = ServiceWindow()
        self.opensupervisor = SupervisorWindow() 
        self.openinvoicetype = InvoiceTypeWindow()
        self.ui.goodsButton.clicked.connect(self.view_data_goods)
        self.ui.invoicesButton.clicked.connect(self.view_data_invoices)
        self.ui.addGoodsButton.clicked.connect(self.opengoods.window_show)
        self.ui.addServiceButton.clicked.connect(self.openservice.window_show)
        self.ui.addInvoiceTypeButton.clicked.connect(self.openinvoicetype.window_show)
        self.ui.addSupervisorButton.clicked.connect(self.opensupervisor.window_show)
        self.ui.addInvoiceButton.clicked.connect(self.openinvoice.window_show)

    def view_data(self, table_to_show='goods'):
        """ Show data from model into tableview"""
        self.model = QSqlTableModel()
        self.model.setTable(table_to_show)
        self.model.select()
        self.ui.tableView.setModel(self.model)

    def view_data_goods(self):
        """Send goods table name to view_data """
        self.view_data('goods')

    def view_data_invoices(self):
        """Send invoices table name to view_data """
        self.view_data('invoices')

class GoodWindow (QDialog):

    def window_show(self):
        self.ui_new_window = QDialog()
        self.new_dialog = Ui_add_goods()
        self.new_dialog.setupUi(self.ui_new_window)
        self.new_dialog.cancel.clicked.connect(self.ui_new_window.close)
        self.new_dialog.save.clicked.connect(self.add_new_goods)
        self.ui_new_window.show()

    def add_new_goods (self):
        query = SqlQueryExec()
        name = self.new_dialog.goodsNameLine.text()
        units = self.new_dialog.goodsUnitsLine.text()
        price = self.new_dialog.goodsPriceLine.text()
        query.add_new_query(
            'goods', 
            ['name', 'units', 'price'], 
            [name, units, price])
        # self.view_data()
        self.ui_new_window.close()

class InvoiceWindow (QDialog):

    def window_show(self):
        self.ui_new_window = QDialog()
        self.new_dialog = Ui_add_invoice()
        self.new_dialog.setupUi(self.ui_new_window)
        self.new_dialog.cancel.clicked.connect(self.ui_new_window.close)
        self.new_dialog.save.clicked.connect(self.add_new_invoice)
        
        self.tablemodel = MTableModel('invoices')
        self.tablemodel.insertRow(0)
        self.new_dialog.tableView.setModel(self.tablemodel)


        self.model = WidgetModel('invoice_type')
        self.new_dialog.cb_invoice_type.setModel(self.model)

        """molel for service name combo"""
        self.cb_serv_name_model = QSqlTableModel(self)
        self.cb_serv_name_model.setTable('services')
        self.cb_serv_name_model.select()
        self.cb_serv_name_model.removeColumn(0)
        self.new_dialog.cb_serv_name.setModel(self.cb_serv_name_model)
        
        """model for sender supervisor combo"""
        self.cb_sender_supervisor_model = QSqlTableModel(self)
        self.cb_sender_supervisor_model.setTable('supervisors')
        self.cb_sender_supervisor_model.select()
        self.cb_sender_supervisor_model.removeColumn(0)
        self.new_dialog.cb_sender_supervisor.setModel(self.cb_sender_supervisor_model)

        """model for reciver supervisor combo"""
        self.cb_rec_supervisor_model = QSqlTableModel(self)
        self.cb_rec_supervisor_model.setTable('supervisors')
        self.cb_rec_supervisor_model.select()
        self.cb_rec_supervisor_model.removeColumn(0)
        self.new_dialog.cb_rec_supervisor.setModel(self.cb_rec_supervisor_model)

        self.ui_new_window.show()
    

    def add_new_invoice(self):
        query = SqlQueryExec()
        reg_number = self.new_dialog.le_reg_number.text()
        sh_number = self.new_dialog.le_sh_number.text()
        doc_number = self.new_dialog.le_doc_number.text()
        doc_date = self.new_dialog.de_doc_date.text()
        op_aime = self.new_dialog.le_op_aime.text()
        op_date = self.new_dialog.de_op_date.text()
        serv_name = self.new_dialog.cb_serv_name.currentIndex()
        sender = self.new_dialog.le_sender.text()
        sender_supervisor = self.new_dialog.cb_sender_supervisor.currentIndex()
        reciver = self.new_dialog.le_reciver.text()
        rec_supervisor = self.new_dialog.cb_rec_supervisor.currentIndex()
        invoice_type = self.new_dialog.cb_invoice_type.currentIndex()
        # next string may include mistakes 
        query.add_new_query(
                'invoices', 
                ['reg_number', 'sh_number', 'doc_number', 'doc_date', 'op_aime', 'op_date',
                 'serv_name', 'sender', 'sender_supervisor', 'reciver', 'rec_supervisor', 
                 'invoice_type_id'], 
                [reg_number, sh_number, doc_number, doc_date, op_aime, op_date, serv_name,
                 sender, sender_supervisor, reciver, rec_supervisor, invoice_type]) 
        self.model.submitAll()
        self.ui_new_window.close()                    

class ServiceWindow(QDialog):

    def window_show (self):
        self.ui_new_window = QDialog()
        self.new_dialog = Ui_add_service()
        self.new_dialog.setupUi(self.ui_new_window)
        self.new_dialog.cancel.clicked.connect(self.ui_new_window.close)
        self.new_dialog.save.clicked.connect(self.add_new_service)

        """model for supervisor combo on new service window"""
        self.model = QSqlTableModel(self)
        self.model.setTable('supervisors')
        self.model.setQuery('SELECT supervisor_id, last_name FROM supervisors')
        self.model.select()
        self.model.removeColumn(0)
        self.new_dialog.cb_supervisor.setModel(self.model)

        self.ui_new_window.show()

    def add_new_service(self):
        """ Fuction to get data from form of new service send parameters for query """
        query = SqlQueryExec()
        name = self.new_dialog.le_name.text()
        red_name = self.new_dialog.le_red_name.text()
        supervisor = self.new_dialog.cb_supervisor.currentIndex() #index took from combobox index. May be error here
        query.add_new_query('services',
                                ['name', 'red_name', 'supervisor_id'], 
                                [name, red_name, supervisor] )
        # self.view_data()
        self.ui_new_window.close()

class SupervisorWindow(QDialog):

    def window_show (self):
        self.ui_new_window = QDialog()
        self.new_dialog = Ui_add_supervisor()
        self.new_dialog.setupUi(self.ui_new_window)
        self.new_dialog.cancel.clicked.connect(self.ui_new_window.close)
        self.new_dialog.save.clicked.connect(self.add_new_supervisor)

        self.ui_new_window.show()


    def add_new_supervisor(self):
        query = SqlQueryExec()
        position = self.new_dialog.le_position.text()
        rank = self.new_dialog.le_rank.text()
        name = self.new_dialog.le_name.text()
        sur_name = self.new_dialog.le_surname.text()
        last_name = self.new_dialog.le_lastname.text()
        query.add_new_query(
                'supervisors', 
                ['position', 'rank', 'name', 'sur_name', 'last_name'], 
                [position, rank, name, sur_name, last_name])
        self.ui_new_window.close()

class InvoiceTypeWindow(QDialog):

    def window_show (self):
        self.ui_new_window = QDialog()
        self.new_dialog = Ui_add_invoicetype()
        self.new_dialog.setupUi(self.ui_new_window)
        self.new_dialog.cancel.clicked.connect(self.ui_new_window.close)
        self.new_dialog.save.clicked.connect(self.add_new_invoice_type)

        self.ui_new_window.show()

    def add_new_invoice_type(self):
        """function to get data from form of new invoice type"""
        query = SqlQueryExec()
        invoice_type = self.new_dialog.le_type.text()
        query.add_new_query('invoice_type', 
                                ['invoice_type'], 
                                [invoice_type])
        self.ui_new_window.close()
