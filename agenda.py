import sqlite3

import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('agenda.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table named 'contacts' with fields for name, phone, and email
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# Insert 10 sample records into the table
records = [
    ("Alice Santos", "1234567890", "alice@example.com"),
    ("Bruno Ferreira", "0987654321", "bruno@example.com"),
    ("Carla Souza", "1122334455", "carla@example.com"),
    ("Diego Lima", "5566778899", "diego@example.com"),
    ("Eva Costa", "6677889900", "eva@example.com"),
    ("Felipe Alves", "9988776655", "felipe@example.com"),
    ("Giovana Rocha", "5544332211", "giovana@example.com"),
    ("Hugo Martins", "4433221100", "hugo@example.com"),
    ("Isabela Silva", "3344556677", "isabela@example.com"),
    ("Jorge Mendes", "2233445566", "jorge@example.com")
]

# Insert the records into the contacts table
cursor.executemany('''
INSERT INTO contacts (name, phone, email) 
VALUES (?, ?, ?)
''', records)

# Commit the changes and close the connection
conn.commit()
conn.close()

"Table 'contacts' created and 10 records inserted successfully."




# Função para criar um novo contato (Create)
def create_contact(name, phone, email):
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)', (name, phone, email))
    conn.commit()
    conn.close()
    return f"Contato {name} criado com sucesso."

# Função para ler todos os contatos (Read)
def read_contacts():
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()  # Retorna todos os registros
    conn.close()
    return contacts

# Função para atualizar um contato existente (Update)
def update_contact(contact_id, name=None, phone=None, email=None):
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()

    # Atualiza apenas os campos fornecidos (não nulos)
    if name:
        cursor.execute('UPDATE contacts SET name = ? WHERE id = ?', (name, contact_id))
    if phone:
        cursor.execute('UPDATE contacts SET phone = ? WHERE id = ?', (phone, contact_id))
    if email:
        cursor.execute('UPDATE contacts SET email = ? WHERE id = ?', (email, contact_id))

    conn.commit()
    conn.close()
    return f"Contato com ID {contact_id} atualizado com sucesso."

# Função para excluir um contato (Delete)
def delete_contact(contact_id):
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
    conn.commit()
    conn.close()
    return f"Contato com ID {contact_id} excluído com sucesso."

# Função para buscar um contato por nome
def search_contact_by_name(name):
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts WHERE name LIKE ?', ('%' + name + '%',))
    contacts = cursor.fetchall()
    conn.close()
    return contacts

# Inserindo registros de exemplo e mostrando a funcionalidade

# Criar um novo contato
print(create_contact("Laura Oliveira", "9876543210", "laura@example.com"))

# Ler todos os contatos
print("Todos os contatos:")
for contact in read_contacts():
    print(contact)

# Atualizar um contato
print(update_contact(1, phone="1122334455"))

# Excluir um contato
print(delete_contact(2))

# Buscar um contato pelo nome
print("Buscar contato pelo nome 'Laura':")
for contact in search_contact_by_name("Laura"):
    print(contact)
