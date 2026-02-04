
from PySide6.QtSql import QSqlQueryModel, QSqlTableModel, QSqlRelationalTableModel, QSqlRelation

class MTableModel(QSqlRelationalTableModel):
    def __init__(self, table_name):
        super().__init__()
        self.setTable(table_name)
        self.setRelation(2, QSqlRelation('goods', 'goods_id', 'name')) 
        self.setRelation(1, QSqlRelation('invoices', 'invoice_id', 'reg_number'))
        self.select()

class WidgetModel(QSqlTableModel):
    def __init__(self, table_name):
        super().__init__()
        self.setTable(table_name)
        self.select()
        self.removeColumn(0)

class CbModel(QSqlQueryModel):
    pass
