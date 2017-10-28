CREATE TABLE IF NOT EXISTS moradores (
	id_morador 	INTEGER PRIMARY KEY,
	nome 		TEXT	NOT NULL,
	endereco	TEXT	NOT NULL,
	cpf			TEXT	NOT NULL,
	telefone	TEXT	NOT NULL
) ;

CREATE TABLE IF NOT EXISTS usuarios (
	id_usuario	INTEGER PRIMARY KEY,
	login		TEXT	NOT NULL,
	senha		TEXT	NOT NULL,
	permissao	INTEGER	NOT NULL
) ;

CREATE TABLE IF NOT EXISTS morador_usuario (
	id_morador	INTEGER	NOT NULL,
	id_usuario	INTEGER NOT NULL,
	FOREIGN KEY (id_morador) REFERENCES moradores (id_morador) 
	ON DELETE CASCADE ON UPDATE NO ACTION,
	FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario) 
	ON DELETE CASCADE ON UPDATE NO ACTION
) ;


CREATE TABLE IF NOT EXISTS eventos (
	id_evento		INTEGER	PRIMARY KEY,
	id_usuario		INTEGER	NOT NULL,
	horario_inicio	TEXT	NOT NULL,
	horario_final	TEXT	NOT NULL,
	horario_entrada	TEXT	NOT NULL,

	FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario)
	ON DELETE NO ACTION ON UPDATE NO ACTION
) ;


CREATE TABLE IF NOT EXISTS convidados (
	id_convidado	INTEGER PRIMARY KEY,
	nome			TEXT NOT NULL,
	cpf				TEXT,
	endereco		TEXT
) ;

CREATE TABLE IF NOT EXISTS veiculos (
	placa			TEXT PRIMARY KEY,
	id_convidado	INTEGER NOT NULL,
	modelo			TEXT,
	marca			TEXT,
	cor_principal	TEXT,
	cor_secundaria	TEXT
) ;


CREATE TABLE IF NOT EXISTS veiculo_evento (
	placa			TEXT NOT NULL,
	id_evento		INTEGER NOT NULL,
	PRIMARY KEY (placa, id_evento)
);
