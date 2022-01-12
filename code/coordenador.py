import psycopg2 as db
import os

conn = db.connect(host='127.0.0.1', database='student_system',
                  user='postgres', password='solteiro12')
cursor = conn.cursor()

def fim_coordenador():
    os.system("cls")
    print("Sessão encerrada!")

def coordenador_atribuicao():
    os.system("cls")
    opcao_home_coordenador=int(input("O que você deseja realizar?\n1 - Criar\n2 - Editar\n3 - Excluir "))
    if opcao_home_coordenador == 1:
        def criar_coordenador():
            os.system("cls")
            query_1 = "insert into tbl_coordenador (NOME, SENHA, SEXO) values (%s,%s,%s)"
            nome_sobrenome = input("Qual é o nome e sobrenome do(a) coordenador(a)? ")
            senha = int(input("Qual é a senha do(a) coordenador(a)? "))
            sexo = input("Qual é o sexo do(a) coordenador(a)? ")
            dados = (nome_sobrenome, senha, sexo)
            cursor.execute(query_1, dados)
            conn.commit()
            print("Coordenador(a) cadastrado(a) com sucesso!")
            def continuar():
                os.system("cls")
                continuacao_1 = int(input("1 - Criar outro(a) coordenador(a)\n2 - Menu principal\n3 - Finalizar sessão\nEscolha uma opção: "))
                if continuacao_1 == 1:
                    criar_coordenador()
                elif continuacao_1 == 2:
                    coordenador_atribuicao()
                elif continuacao_1 == 3:
                    fim_coordenador()
                else:
                    print("Opção inválida!")
                    continuar()
            continuar()
        criar_coordenador()

    elif opcao_home_coordenador == 2:
        def editar_coordenador():
            def continuar_1():
                    continuacao_2 = int(input("1 - Editar outro(a) coordenador(a)\n2 - Menu principal\n3 - Finalizar sessão\nEscolha uma opção: "))
                    if continuacao_2 == 1:
                        editar_coordenador()
                    elif continuacao_2 == 2:
                        coordenador_atribuicao()
                    elif continuacao_2 == 3:
                        fim_coordenador()
                    else: 
                        continuar_1()
            query_2 = "select all nome from tbl_coordenador"
            cursor.execute(query_2)
            resultado = cursor.fetchall()
            print("Os coordenadores na base de dados são: ")
            for line in resultado:
                print(line[0])
            nome_editar = input("Escreva o nome do(a) coordenador(a) que você deseja editar: ")
            opcao_edicao = int(input("O que você gostaria de editar? \n 1 - Nome \n 2 - Senha \n 3 - Sexo "))
            if opcao_edicao == 1:
                os.system("cls")
                editar = input("Você selecionou {}. Escreva o novo nome do(a) coordenador(a): ".format(nome_editar))
                query_3 = "update tbl_coordenador set nome = %s where nome = %s"
                cursor.execute(query_3, (editar, nome_editar))
                conn.commit()
                os.system("cls")
                print("Nome e sobrenome atualizados com sucesso!")
                continuar_1()
            elif opcao_edicao == 2:
                os.system("cls")
                nova_senha = input("Escreva a nova senha do(a) coordenador(a) {}: ".format(nome_editar))
                query_4 = "update tbl_coordenador set senha = %s where nome = %s"
                cursor.execute(query_4, (nova_senha, nome_editar))
                conn.commit()
                os.system("cls")
                print("Senha atualizada com sucesso!")
                continuar_1()
            elif opcao_edicao == 3:
                os.system("cls")
                nova_senha = input("Escreva o novo sexo do(a) coordenador(a) {}: ".format(nome_editar))
                query_4 = "update tbl_coordenador set sexo = %s where nome = %s"
                cursor.execute(query_4, (nova_senha, nome_editar))
                conn.commit()
                os.system("cls")
                print("Sexo atualizado com sucesso!")
                continuar_1()
            else:
                print("Não há essa opção!")
                continuar_1()
        editar_coordenador()
    elif opcao_home_coordenador == 3:
        def excluir_coordenador():
            def continuar_2():
                continuacao_3 = int(input("1 - Excluir outro(a) coordenador(a)\n2 - Menu principal\n3 - Finalizar sessão\nEscolha uma opção: "))
                if continuacao_3 == 1:
                    excluir_coordenador()
                elif continuacao_3 == 2:
                    coordenador_atribuicao()
                elif continuacao_3 == 3:
                    fim_coordenador()
                else: 
                    continuar_2()

            query_5 = "select all nome from tbl_coordenador"
            cursor.execute(query_5)
            resultado = cursor.fetchall()
            print("Os coordenadores na base de dados são: ")
            for line_1 in resultado:
                print(line_1[0])
            nome_excluir = input("Escreva o nome do(a) coordenador(a) para excluir: ")
            os.system("cls")
            print("Você tem certeza que quer excluir o(a) coordenador(a) {}? Os dados serão excluídos permanentemente!".format(nome_excluir))
            validar = input("S - Sim / N - Não: ")
            if validar == "S" or validar == 's':
                query_6 = "delete from tbl_coordenador where nome = %s"
                cursor.execute(query_6, (nome_excluir,))
                conn.commit()
                os.system("cls")
                print("Coordenador(a) excluído(a) com sucesso")
                continuar_2()
            elif validar == 'N' or validar == 'n':
                os.system("cls")
                continuar_2()
            else:
                print("Não há essa opção")
                continuar_2()
        excluir_coordenador()
    else:
        print("Não há essa opção")
        coordenador_atribuicao()
    
def professor_atribuicao():
    os.system("cls")
    opcao_home_professor=int(input("O que você deseja realizar?\n1 - Criar\n2 - Editar\n3 - Excluir "))
    if opcao_home_professor == 1:
        def criar_professor():
            os.system("cls")
            query_1_1 = "insert into tbl_professor (NOME, SENHA, SEXO) values (%s,%s,%s)"
            prof_nome_sobrenome = input("Qual é o nome e sobrenome do(a) professor(a)? ")
            prof_senha = int(input("Qual é a senha do(a) professor(a)? "))
            sexo = input("Qual é o sexo do(a) professor(a)? ")
            dados_1 = (prof_nome_sobrenome, prof_senha,sexo)
            cursor.execute(query_1_1, dados_1)
            conn.commit()
            print("Professor(a) cadastrado(a) com sucesso!")
            def continuar_professor():
                os.system("cls")
                continuacao_1_professor = int(input("1 - Criar outro(a) professor(a)\n2 - Menu principal\n3 - Finalizar sessão\nEscolha uma opção: "))
                if continuacao_1_professor == 1:
                    criar_professor()
                elif continuacao_1_professor == 2:
                    professor_atribuicao()
                elif continuacao_1_professor == 3:
                    fim_coordenador()
                else:
                    print("Opção inválida!")
                    continuar_professor()
            continuar_professor()
        criar_professor()
    elif opcao_home_professor == 2:
        def editar_professor():
            def continuar_professor1():
                    continuacao_2_professor = int(input("1 - Editar outro(a) professor(a)\n2 - Menu principal\n3 - Finalizar sessão\nEscolha uma opção: "))
                    if continuacao_2_professor == 1:
                        editar_professor()
                    elif continuacao_2_professor == 2:
                        professor_atribuicao()
                    elif continuacao_2_professor == 3:
                        fim_coordenador()
                    else: 
                        continuar_professor1()
            query_2_2 = "select all nome from tbl_professor"
            cursor.execute(query_2_2)
            resultado_professor = cursor.fetchall()
            print("Os coordenadores na base de dados são: ")
            for line_professor in resultado_professor:
                print(line_professor[0])
            nome_editar_professor = input("Escreva o nome do(a) professor(a) que você deseja editar: ")
            opcao_edicao_professor = int(input("O que você gostaria de editar?\n1 - Nome\n2 - Senha\n3 - Sexo "))
            if opcao_edicao_professor == 1:
                os.system("cls")
                editar = input("Você selecionou {}. Escreva o novo nome do(a) professor(a): ".format(nome_editar_professor))
                query_3_3 = "update tbl_professor set nome = %s where nome = %s"
                cursor.execute(query_3_3, (editar, nome_editar_professor))
                conn.commit()
                os.system("cls")
                print("Nome e sobrenome atualizados com sucesso!")
                continuar_professor1()
            elif opcao_edicao_professor == 2:
                os.system("cls")
                nova_senha_professor = input("Escreva a nova senha do(a) professor(a) {}: ".format(nome_editar_professor))
                query_4_4 = "update tbl_professor set senha = %s where nome = %s"
                cursor.execute(query_4_4, (nova_senha_professor, nome_editar_professor))
                conn.commit()
                os.system("cls")
                print("Senha atualizada com sucesso!")
                continuar_professor1()
            elif opcao_edicao_professor == 3:
                os.system("cls")
                novo_sexo_professor = input("Escreva o novo sexo do(a) professor(a) {}: ".format(nome_editar_professor))
                query_5_5 = "update tbl_professor set sexo = %s where nome = %s"
                cursor.execute(query_5_5, (novo_sexo_professor, nome_editar_professor))
                conn.commit()
                os.system("cls")
                print("Sexo atualizado com sucesso!")
                continuar_professor1()
            else:
                print("Não há essa opção!")
                continuar_professor1()
        editar_professor()
    elif opcao_home_professor == 3:
        def excluir_professor():
            def continuar_professor2():
                continuacao_3_professor = int(input("1 - Excluir outro(a) coordenador(a)\n2 - Menu principal\n3 - Finalizar sessão\nEscolha uma opção: "))
                if continuacao_3_professor == 1:
                    excluir_professor()
                elif continuacao_3_professor == 2:
                    professor_atribuicao()
                elif continuacao_3_professor == 3:
                    fim_coordenador()
                else: 
                    continuar_professor2()

            query_5_5 = "select all nome from tbl_professor"
            cursor.execute(query_5_5)
            resultado_1 = cursor.fetchall()
            print("Os professores na base de dados são: ")
            for line_1_1 in resultado_1:
                print(line_1_1[0])
            nome_excluir_professor = input("Escreva o nome do(a) professor(a) para excluir: ")
            os.system("cls")
            print("Você tem certeza que quer excluir o(a) professor(a) {}? Os dados serão excluídos permanentemente!".format(nome_excluir_professor))
            validar_1 = input("S - Sim / N - Não: ")
            if validar_1 == "S" or validar_1 == 's':
                query_6_6 = "delete from tbl_professor where nome = %s"
                cursor.execute(query_6_6, (nome_excluir_professor,))
                conn.commit()
                os.system("cls")
                print("Professor(a) excluído(a) com sucesso")
                continuar_professor2()
            elif validar_1 == 'N' or validar_1 == 'n':
                os.system("cls")
                continuar_professor2()
            else:
                print("Não há essa opção")
                continuar_professor2()
        excluir_professor()
    else:
        print("Não há essa opção")
        professor_atribuicao()
    
            


    



        
