# Military Unit Material Assets Accounting System

## Project Description

Automated warehouse accounting system for military units. Provides a complete cycle of material and technical assets (MTA) and weapons accounting with automatic balance calculation and cost control.

## Key Features

### Document Management
- **Receipt invoices** - accounting for incoming material assets
- **Write-off acts** - registration of MTA disposal
- **Transfer acts** - movement of assets between units
- Automatic document numbering
- Assignment to specific materially responsible persons

### Material Assets Accounting
- Registry of all MTA and weapons
- Automatic warehouse balance calculation
- Cost accounting for each item
- Complete transaction history for MTA
- Material assets movement control

### Search and Filtering
- Search by item name
- Search by invoice or act number
- Document filtering by date
- Quick access to transaction history
- Selection by document type

### Reporting
- Current warehouse balances
- Turnover balance sheets
- Period-based reports
- Cost accounting of MTA movement
- Transaction history for each item

## Technology Stack

**Backend:**
- Python 3.x
- SQLite - relational database
- SQLAlchemy ORM - for database operations

**Frontend:**
- Python UI framework (PyQt/Tkinter)
- Graphical interface with input forms

## Project Structure

```
platoonaccauntant/
├── main.py                    # Main application file
├── models.py                  # Database models (ORM)
├── connection.py              # Database connection configuration
├── views.py                   # Business logic
├── uiviews.py                 # UI controllers
├── ui_main.py                 # Main application window
├── ui_addgoods.py             # Add goods form
├── ui_addinvoice.py           # Create invoice form
├── ui_addinvoicetype.py       # Document types form
├── ui_addservice.py           # Units form
├── ui_addsupervisor.py        # Materially responsible persons form
├── platoon.sqlite3            # SQLite database
├── platoon_db.db              # Backup database
└── ui_source/                 # Interface design files
```

## Data Models

The project includes the following main models:

- **Goods** - inventory of goods and weapons
- **Invoice** - receipt and expenditure documents
- **InvoiceType** - document types (invoice, write-off act, transfer act)
- **Service** - organizational units
- **Supervisor** - materially responsible persons
- **InvoiceItems** - document line items
- **Balance** - automatically calculated balances

## Installation and Setup

### Requirements
- Python 3.8 or higher
- pip (Python package manager)
- virtualenv (recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/PopovMarko/platoonaccauntant.git
cd platoonaccauntant
```

### Step 2: Create Virtual Environment

**For Linux/MacOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**For Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python main.py
```

### Deactivate Virtual Environment

After finishing work:
```bash
deactivate
```

## Functional Capabilities

### 1. Inventory Management
- Add new MTA and weapons items
- Edit item information
- Set costs
- Categorize by types

### 2. Document Processing
- Create receipt invoices
- Process write-off acts
- Prepare transfer acts
- Automatic numbering and dating
- Assignment to materially responsible persons

### 3. Transaction Accounting
- Automatic balance calculation after each transaction
- Support for multiple items in one document
- Cost control for each transaction
- Chronological history of all movements

### 4. Search and Analysis
- Quick search by name
- Filter by document number
- Selection by date range
- View history for each MTA item

### 5. Balance Control
- Current balances as of today
- Negative balance warnings
- Availability check before write-off
- Cost accounting of balances

## Business Logic

### Balance Calculation Algorithm

1. **Receipt (+)** - receipt invoice increases quantity and cost
2. **Write-off (-)** - write-off act decreases quantity
3. **Transfer (-)** - transfer act decreases quantity in sender unit
4. **Receipt (+)** - transfer act increases quantity in receiver unit

Balances are calculated automatically with each transaction, taking into account document chronology.

## Security and Reliability

- Local data storage in SQLite
- Automatic database backup
- Data validation before saving
- Transaction integrity control
- Duplicate document prevention

## Technical Features

- **MVC Architecture** - separation of models, views, and controllers
- **SQLAlchemy ORM** - database abstraction
- **Transactions** - atomicity of complex operations
- **Database Indexes** - fast search and filtering
- **Automatic Calculations** - balances and costs

## Future Improvements

- [ ] Export reports to Excel and PDF
- [ ] MTA barcode system
- [ ] Warehouse inventory functionality
- [ ] Multi-level unit structure
- [ ] Web application version
- [ ] Accounting system integration
- [ ] Mobile app for inventory
- [ ] Critical balance notification system
- [ ] Graphical analytics of MTA movement

## Typical Use Cases

### Receiving Goods to Warehouse
1. Open "New Invoice" form
2. Select "Receipt Invoice" type
3. Specify materially responsible person
4. Add MTA items with quantity and cost
5. Save document
6. Balances update automatically

### MTA Write-off
1. Create "Write-off Act"
2. Select items for write-off
3. Specify write-off reason
4. System checks balance availability
5. If sufficient quantity - document is saved
6. Balances decrease automatically

### Transfer Between Units
1. Prepare "Transfer Act"
2. Specify sender and receiver units
3. Select items for transfer
4. System generates document with both parties
5. Balances for both units are updated

## Author

Popov Marko Vyacheslavovych

## License

Private project for official use

---

**Note:** The system is designed for military warehouse accounting and contains confidential information. Usage is restricted to official needs.
