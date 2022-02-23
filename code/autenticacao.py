import psycopg2 as db
import professor
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
        query_0 = """select nome from tbl_coordenador where nome=%s"""
        cursor.execute(query_0,(user,))
        nome_busca = cursor.fetchall()
        query_00 = """select senha from tbl_coordenador where nome=%s"""
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

def autenticacao_professor():
    try:   
        os.system("cls")
        user_professor = input("Informe seu nome e sobrenome: ")
        code_professor = int(input("Informe sua senha: "))
        query_0_professor = """select nome from tbl_professor where nome=%s"""
        cursor.execute(query_0_professor,(user_professor,))
        nome_busca_professor = cursor.fetchall()
        query_00_professor = """select senha from tbl_professor where nome=%s"""
        cursor.execute(query_00_professor,(user_professor,))
        senha_busca_professor = cursor.fetchall()
        query_000_professor = """select id_professor from tbl_professor where nome=%s"""        
        cursor.execute(query_000_professor,(user_professor,))
        id_busca_professor = cursor.fetchall()        
        for rows_professor  in  nome_busca_professor:
            for rows1_professor in senha_busca_professor:
                for rows2_professor in id_busca_professor:
                    x_professor = rows_professor[0]
                    y_professor = rows1_professor[0]
                    id_professor = rows2_professor[0]
                                   

        if x_professor == user_professor and y_professor == code_professor:
            os.system("cls")
            professor.professor_atribuicao(id_professor)
            


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

