import psycopg2 as db
import coordenador
import os

conn = db.connect(host='127.0.0.1', database='student_system',
                  user='postgres', password='solteiro12')
cursor = conn.cursor()

def autenticacao_coordenador():
    try:   
        os.system("cls")
        user = input("Informe seu nome e sobrenome: ")
        code = int(input("Informe sua senha: "))
        query_0 = """select nome from coordenador where nome=%s"""
        cursor.execute(query_0,(user,))
        nome_busca = cursor.fetchall()
        query_00 = """select senha from coordenador where nome=%s"""
        cursor.execute(query_00,(user,))
        senha_busca = cursor.fetchall()
            
        for rows  in  nome_busca:
            for rows1 in senha_busca:
                x = rows[0]
                y = rows1[0]

        if x == user and y == code:
            os.system("cls")
            opcao_home = int(input("Qual opção você gostaria de atribuir \n 1 - Coordenador \n 2 - Professor "))
            if opcao_home == 1:
                coordenador.coordenador_atribuicao()
            elif opcao_home == 2:
                coordenador.professor_atribuicao()
                #print("")
                
        else:
            print("Usuário e senha incorretos! Tente novamente!")
        

        #query_00 = "select senha from coordenador where nome=%s"
        #cursor.execute(query_00, (user,))
        #resultado2 = cursor.fetchall()
        '''for rows in y:
            print("ID: ", rows[0])
            print("Nome e sobrenomme: ", rows[1])
            print("Senha: ", rows[2]) '''
        #print(resultado1)
        #print(resultado1[1])
        #print(resultado2)
        #if resultado1[0]==user:
         #   print("Gooo")
        #else:
         #   print("Não!")
    except:
        print("Usuário inexistente!")
