import psycopg2 as db
import os
from datetime import date

conn = db.connect(host='127.0.0.1', database='student_system',
                  user='postgres', password='solteiro12')
cursor = conn.cursor()

def fim_coordenador():
    os.system("cls")
    print("Sessão encerrada!")

def professor_atribuicao(id):
    os.system("cls")
    id_professor = id
    opcao_home_professor=int(input("O que você deseja realizar?\n1 - Inserir notas\n2 - Editar\n3 - Excluir "))
    if opcao_home_professor == 1:
        def inserir_notas_professor(id):
            os.system("cls")
            id_professor = id
            query_1_professor = "insert into tbl_aluno (ID_PROFESSOR, ALUNO, SEXO, TURMA, REGIAO, DATA_REGISTRO, NOTA1, NOTA2, NOTA3, NOTA4) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            aluno = input("Qual é o nome e sobrenome do(a) aluno(a)? ")
            sexo = input("Qual é o sexo do(a) aluno(a)? ")
            turma = input("Qual é a turma do(a) aluno(a)? ")
            regiao = input("Qual é a região da turma? ")
            nota_1 = float(input("Qual é a nota 1 do(a) aluno(a)? "))
            nota_2 = float(input("Qual é a nota 2 do(a) aluno(a)? "))
            nota_3 = float(input("Qual é a nota 3 do(a) aluno(a)? "))
            nota_4 = float(input("Qual é a nota 4 do(a) aluno(a)? "))
            data_atual = date.today()
            data = '{}/{}/{}'.format(data_atual.day,data_atual.month,data_atual.year)
            dados_professor = (id_professor,aluno,sexo,turma,regiao,data,nota_1,nota_2,nota_3,nota_4,)
            cursor.execute(query_1_professor, dados_professor)
            conn.commit()
            print("Notas inseridas com sucesso!")
            def continuar():
                os.system("cls")
                continuacao_1 = int(input("1 - Inserir notas novamente\n2 - Menu principal\n3 - Finalizar sessão\nEscolha uma opção: "))
                if continuacao_1 == 1:
                    inserir_notas_professor(id_professor)
                elif continuacao_1 == 2:
                    professor_atribuicao(id_professor)
                elif continuacao_1 == 3:
                    fim_coordenador()
                else:
                    print("Opção inválida!")
                    continuar()
            continuar()
        inserir_notas_professor(id_professor)

    elif opcao_home_professor == 2:
        def editar_professor(id):
            def continuar_1_professor():
                    continuacao_2 = int(input("1 - Editar alunos/notas\n2 - Menu principal\n3 - Finalizar sessão\nEscolha uma opção: "))
                    if continuacao_2 == 1:
                        editar_professor(id_professor)
                    elif continuacao_2 == 2:
                        professor_atribuicao(id_professor)
                    elif continuacao_2 == 3:
                        fim_coordenador()
                    else: 
                        continuar_1_professor()
            query_2_professor = "select * from tbl_aluno where id_professor = %s"
            id_professor = id
            cursor.execute(query_2_professor,(id_professor,))
            resultado_professor = cursor.fetchall()
            print("As notas e alunos na base de dados são: ")
            for line_x in resultado_professor:
                print("\nAluno(a): ", line_x[2])
                print("Turma: ", line_x[4])
                print("Região: ", line_x[5])
                print("Nota 1: ", line_x[7])
                print("Nota 2: ", line_x[8])
                print("Nota 3: ", line_x[9])
                print("Nota 4: ", line_x[10])
                print("\n")
                print("Última atualização: ", line_x[6])
            nome_editar = input("Escreva o nome do(a) aluno(a) que você deseja editar: ")
            opcao_edicao = int(input("O que você gostaria de editar?\n1 - Aluno e Sexo\n2 - Turma e Região\n3 - Notas "))
            if opcao_edicao == 1:
                os.system("cls")
                editar = input("Você selecionou {}. Escreva o novo nome do(a) aluno(a): ".format(nome_editar))
                editar1 = input("Você selecionou {}. Escreva o novo sexo do(a) aluno(a): ".format(nome_editar))
                data_atual = date.today()
                data = '{}/{}/{}'.format(data_atual.day,data_atual.month,data_atual.year)
                query_3 = "update tbl_aluno set aluno = %s, sexo= %s, data_registro=%s where aluno = %s"
                cursor.execute(query_3, (editar, editar1, data, nome_editar))
                conn.commit()
                os.system("cls")
                print("Aluno(a) e sexo atualizados com sucesso!")
                continuar_1_professor()
            elif opcao_edicao == 2:
                os.system("cls")
                nova_turma = input("Escreva a nova turma do(a) aluno(a) {}: ".format(nome_editar))
                nova_turma1 = input("Escreva a nova região do(a) aluno(a) {}: ".format(nome_editar))
                data_atual = date.today()
                data = '{}/{}/{}'.format(data_atual.day,data_atual.month,data_atual.year)
                query_4 = "update tbl_aluno set turma=%s, regiao=%s, data_registro=%s where aluno = %s"
                cursor.execute(query_4, (nova_turma, nova_turma1, data, nome_editar))
                conn.commit()
                os.system("cls")
                print("Turma e região atualizadas com sucesso!")
                continuar_1_professor()
            elif opcao_edicao == 3:
                os.system("cls")
                nota1 = input("Escreva a nova nota 1 do(a) aluno(a) {}: ".format(nome_editar))
                nota2 = input("Escreva a nova nota 2 do(a) aluno(a) {}: ".format(nome_editar))
                nota3 = input("Escreva a nova nota 3 do(a) aluno(a) {}: ".format(nome_editar))
                nota4 = input("Escreva a nova nota 4 do(a) aluno(a) {}: ".format(nome_editar))
                data_atual = date.today()
                data = '{}/{}/{}'.format(data_atual.day,data_atual.month,data_atual.year)
                query_4 = "update tbl_aluno set nota1 = %s, nota2= %s, nota3= %s, nota4= %s, data_registro=%s where aluno = %s"
                cursor.execute(query_4, (nota1, nota2, nota3, nota4, data, nome_editar))
                conn.commit()
                os.system("cls")
                print("Notas atualizadas com sucesso!")
                continuar_1_professor()
            else:
                print("Não há essa opção!")
                continuar_1_professor()
        editar_professor(id_professor)
    elif opcao_home_professor == 3:
        def excluir_professor(id):
            def continuar_professor2():
                continuacao_3_professor = int(input("1 - Excluir outro(a) aluno(a)\n2 - Menu principal\n3 - Finalizar sessão\nEscolha uma opção: "))
                if continuacao_3_professor == 1:
                    excluir_professor(id_professor)
                elif continuacao_3_professor == 2:
                    professor_atribuicao(id_professor)
                elif continuacao_3_professor == 3:
                    fim_coordenador()
                else: 
                    continuar_professor2()

            query_5_5 = "select * from tbl_aluno where id_professor=%s"
            id_professor = id
            cursor.execute(query_5_5,(id_professor,))
            resultado_1 = cursor.fetchall()
            print("As notas e alunos na base de dados são: ")
            for line_1_1 in resultado_1:
                print(line_1_1[0])
            nome_excluir_professor = input("Escreva o nome do(a) aluno(a) para excluir: ")
            os.system("cls")
            print("Você tem certeza que quer excluir o(a) aluno(a) {} e suas notas? Os dados serão excluídos permanentemente!".format(nome_excluir_professor))
            validar_1 = input("S - Sim / N - Não: ")
            if validar_1 == "S" or validar_1 == 's':
                query_6_6 = "delete from tbl_aluno where aluno = %s"
                cursor.execute(query_6_6, (nome_excluir_professor,))
                conn.commit()
                os.system("cls")
                print("Aluno(a) e registros excluídos com sucesso")
                continuar_professor2()
            elif validar_1 == 'N' or validar_1 == 'n':
                os.system("cls")
                continuar_professor2()
            else:
                print("Não há essa opção")
                continuar_professor2()
        excluir_professor(id_professor)
    else:
        print("Não há essa opção")
        professor_atribuicao()
    




    



