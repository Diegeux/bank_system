CREATE TABLE tbl_aluno(
 id_aluno SERIAL PRIMARY KEY,
 id_professor int NOT NULL,
 aluno varchar(40) NOT NULL,
 sexo varchar(1) NOT NULL,
 turma varchar(1) NOT NULL,
 regiao varchar NOT NULL,
 data_registro date NOT NULL,
 nota1 double precision NOT NULL,
 nota2 double precision NOT NULL,
 nota3 double precision NOT NULL,
 nota4 double precision NOT NULL,
 FOREIGN KEY (id_professor) REFERENCES tbl_professor(id_professor)
);