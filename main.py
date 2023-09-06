import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtSql import QSqlTableModel, QSqlRelationalTableModel, QSqlRelation

from ui_main import Ui_MainWindow
from ui_addgoods import Ui_add_goods
from ui_addservice import Ui_add_service 
from ui_addinvoicetype import Ui_add_invoicetype
from ui_addsupervisor import Ui_add_supervisor
from ui_addinvoice import Ui_add_invoice

from connection import Data
from uiviews import MWindow

class Platoon (QMainWindow):
    def __init__(self):
        super(Platoon, self).__init__()
        self.conn = Data()
        self.conn.create_connection()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.view_data()
        self.ui.goodsButton.clicked.connect(self.view_data_goods)
        self.ui.invoicesButton.clicked.connect(self.view_data_invoices)
        self.ui.addGoodsButton.clicked.connect(self.open_new_goods_window)
        self.ui.addServiceButton.clicked.connect(self.open_new_service_window)
        self.ui.addInvoiceTypeButton.clicked.connect(self.open_new_invoice_type_window)
        self.ui.addSupervisorButton.clicked.connect(self.open_new_supervisor_window)
        self.ui.addInvoiceButton.clicked.connect(self.open_new_invoice_window)


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

    def open_new_dialog_window(self, ui_view):
        """universal method for initialise all new windows"""
        self.ui_new_window = QDialog()
        self.new_dialog = ui_view()
        self.new_dialog.setupUi(self.ui_new_window)

        if self.sender().objectName() == 'addServiceButton':
            """model for supervisor combo on new service window"""
            self.model = QSqlTableModel(self)
            self.model.setTable('supervisors')
            self.model.setQuery('SELECT supervisor_id, last_name FROM supervisors')
            self.model.select()
            self.model.removeColumn(0)
            self.new_dialog.cb_supervisor.setModel(self.model)

        elif self.sender().objectName() == 'addInvoiceButton':
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
        if self.sender().objectName() == 'addGoodsButton':
            self.new_dialog.save.clicked.connect(self.add_new_goods)
        elif self.sender().objectName() == 'addServiceButton':
            self.new_dialog.save.clicked.connect(self.add_new_service)
        elif self.sender().objectName() == 'addInvoiceTypeButton':
            self.new_dialog.save.clicked.connect(self.add_new_invoice_type)
        elif self.sender().objectName() == 'addSupervisorButton':
            self.new_dialog.save.clicked.connect(self.add_new_supervisor)
        elif self.sender().objectName() == 'addInvoiceButton':
            self.new_dialog.save.clicked.connect(self.add_new_invoice)



    def open_new_goods_window(self):
        self.open_new_dialog_window(Ui_add_goods)
    
    def open_new_service_window(self):
        self.open_new_dialog_window(Ui_add_service)
    
    def open_new_invoice_type_window(self):
        self.open_new_dialog_window(Ui_add_invoicetype)
    
    def open_new_supervisor_window(self):
        self.open_new_dialog_window(Ui_add_supervisor)
    
    def open_new_invoice_window(self):
        self.open_new_dialog_window(Ui_add_invoice)
        

        
    def add_new_goods (self):
        """ case to get data from form of new good send parameters for query """
        name = self.new_dialog.goodsNameLine.text()
        units = self.new_dialog.goodsUnitsLine.text()
        price = self.new_dialog.goodsPriceLine.text()
        self.conn.add_new_query(
            'goods', 
            ['name', 'units', 'price'], 
            [name, units, price])
        self.view_data()
        self.ui_new_window.close()


    def add_new_service(self):
        """ Fuction to get data from form of new service send parameters for query """
        name = self.new_dialog.le_name.text()
        red_name = self.new_dialog.le_red_name.text()
        supervisor = self.new_dialog.cb_supervisor.currentIndex() #index took from combobox index. May be error here
        self.conn.add_new_query('services',
                                ['name', 'red_name', 'supervisor_id'], 
                                [name, red_name, supervisor] )
        self.view_data()
        self.ui_new_window.close()
        
    def add_new_invoice_type(self):
        """function to get data from form of new invoice type"""
        invoice_type = self.new_dialog.le_type.text()
        self.conn.add_new_query('invoice_type', 
                                ['invoice_type'], 
                                [invoice_type])
        self.ui_new_window.close()

    def add_new_supervisor(self):
        position = self.new_dialog.le_position.text()
        rank = self.new_dialog.le_rank.text()
        name = self.new_dialog.le_name.text()
        sur_name = self.new_dialog.le_surname.text()
        last_name = self.new_dialog.le_lastname.text()
        self.conn.add_new_query(
                'supervisors', 
                ['position', 'rank', 'name', 'sur_name', 'last_name'], 
                [position, rank, name, sur_name, last_name])
        self.ui_new_window.close()

    def add_new_invoice(self):
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
        self.conn.add_new_query(
                'invoices', 
                ['reg_number', 'sh_number', 'doc_number', 'doc_date', 'op_aime', 'op_date',
                 'serv_name', 'sender', 'sender_supervisor', 'reciver', 'rec_supervisor', 
                 'invoice_type'], 
                [reg_number, sh_number, doc_number, doc_date, op_aime, op_date, serv_name,
                 sender, sender_supervisor, reciver, rec_supervisor, invoice_type]) 
        self.ui_new_window.close()                    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Platoon()
    window.show()

    sys.exit(app.exec())
