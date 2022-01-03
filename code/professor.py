import psycopg2 as db

def logar_coordenador():
    conn = db.connect(host='127.0.0.1', database='student_system', user='postgres', password='solteiro12')
    cursor = conn.cursor()
    code = """select * from coordenador where nome = %s"""
    var = 'Amaral'
    cursor.execute(code,(var))
    record = cursor.fetchone()
    conn.commit()
    print(record)

