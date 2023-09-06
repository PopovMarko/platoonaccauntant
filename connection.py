""" connection to database and all manipulations with it"""

from PySide6 import QtWidgets, QtSql, QtGui


class Data:
    def __init__(self):
        super(Data, self).__init__()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('platoon_db.db')

        if not db.open():
            QtWidgets.QMessageBox.information(
                None, "Cant open Database", "Clik Cancel to exit")
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS goods (\
                        goods_id INTEGER primary key, \
                        name TEXT, \
                        units TEXT, \
                        price REAL)")

        query.exec("CREATE TABLE IF NOT EXISTS invoices (\
                        invoice_id INTEGER primary key, \
                        reg_number TEXT, \
                        sh_number TEXT, \
                        doc_number TEXT, \
                        doc_date TEXT, \
                        op_aime TEXT, \
                        op_date TEXT, \
                        serv_name INTEGER, \
                        sender TEXT, \
                        sender_supervisor INTEGER, \
                        reciver TEXT, \
                        rec_supervisor INTEGER, \
                        invoice_type_id INTEGER,\
                        FOREIGN KEY(serv_name) REFERENCES services(service_id) ON DELETE RESTRICT ON UPDATE CASCADE,\
                        FOREIGN KEY (sender_supervisor) REFERENCES supervisors(supervisor_id) ON DELETE RESTRICT ON UPDATE CASCADE,\
                        FOREIGN KEY (rec_supervisor) REFERENCES supervisors(supervisor_id) ON DELETE RESTRICT ON UPDATE CASCADE,\
                        FOREIGN KEY (invoice_type_id) REFERENCES invoice_type(nvoice_type_id) ON DELETE RESTRICT ON UPDATE CASCADE)")

        query.exec("CREATE TABLE IF NOT EXISTS invoice_goods(\
                        invoice_goods_id INTEGER primary key,\
                        invoice_id INTEGER,\
                        goods_id INTEGER, \
                        goods_code TEXT, \
                        category TEXT, \
                        ordered INTEGER,\
                        delivered INTEGER,\
                        FOREIGN KEY (goods_id) REFERENCES goods(goods_id) ON DELETE RESTRICT ON UPDATE CASCADE,\
                        FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id) ON DELETE RESTRICT ON UPDATE CASCADE)")

        query.exec("CREATE TABLE IF NOT EXISTS services (\
                        service_id INTEGER primary key,\
                        name TEXT,\
                        red_name TEXT,\
                        supervisor_id INTEGER,\
                        FOREIGN KEY (supervisor_id) REFERENCES supervisors(supervisor_id) ON DELETE RESTRICT ON UPDATE CASCADE,\
                        FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE RESTRICT ON UPDATE CASCADE)")

        query.exec("CREATE TABLE IF NOT EXISTS supervisors (\
                        supervisor_id INTEGER primary key,\
                        position TEXT,\
                        rank text,\
                        name TEXT,\
                        sur_name TEXT,\
                        last_name TEXT)")

        query.exec("CREATE TABLE IF NOT EXISTS invoice_type (\
                        invoice_type_id INTEGER primary key,\
                        invoice_type TEXT)")

    def execut_query (self, sql_query, params):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if params:
            for value in params:
                query.addBindValue(value)

        query.exec()
        return query

    def add_new_query (self, table, fields, params):
        sql_query = f"INSERT INTO {table} ({', '.join(fields)}) VALUES ({', '.join(['?' for _ in range(len(fields))])})"
        self.execut_query(sql_query, params)

    

