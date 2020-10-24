#criacao-database

create table genero (
        id serial primary key not null,
        descricao varchar(60) not null);

create table classificacao (
        id serial primary key not null,
        descricao varchar(45) not null);
        
create table tipo_audio (
        id serial primary key not null,
        descricao varchar(45) not null);
        
create table estado_filme (
        id serial primary key not null,
        descricao varchar(45) not null);
        
create table filme (
        id serial primary key not null,
        nome varchar(200) not null,
        duracao int not null,
        ref_genero int not null references genero(id),
        ref_tipo_audio int not null references tipo_audio(id),
        ref_classificacao int not null references classificacao(id),
        ref_estado_filme int not null references estado_filme(id),
		poster_url varchar(200));
        
create table sala (
        id serial primary key not null,
        total_cadeiras int not null);

create table cadeira(
        id serial primary key not null,
        estado_cadeira boolean not null,
        ref_sala int not null references sala(id),
		nome varchar(2) not null);
        
create table sessao(
        id serial primary key not null,
        horario_inicio time not null,
        ref_filme int not null references filme(id),
        ref_sala int not null references sala(id),
		horario_fim time not null);

create table ingresso(
        id serial primary key not null,
        valor float not null,
        ref_sessao int not null references sessao(id),
        ref_cadeira int not null references cadeira(id));

create table tipo_usuario(
        id serial primary key not null,
        descricao varchar(45) not null);

create table usuario(
        id serial primary key not null,
        usuario varchar(20) not null,
        senha varchar(60) not null,
        nome varchar(200) not null,
        cpf varchar(45),
        email varchar(60) not null,
        telefone varchar(45),
        ref_tipo_usuario int not null references tipo_usuario(id),
		fl_ativo boolean default TRUE);
        
create table venda(
        id serial primary key not null,
        valor_total float not null,
        desconto float,
        data timestamp not null,
        ref_usuario int not null references usuario(id));
        
create table ingresso_venda(
        id serial primary key not null,
        ref_ingresso int not null references ingresso(id),
        ref_venda int not null references venda(id));
