create database proyecto_integral_;

use proyecto_integral_;


-- --------------------------------------------------------


create table ley (
  id int not null auto_increment ,
  nombre_normativa varchar(50) not null,
  numero_normativa int not null,
  fecha_sancion date,
  descripcion text,
  organo_legislativo varchar(50),
  primary key(id)
);


insert into ley (id, nombre_normativa, numero_normativa, fecha_sancion, descripcion, organo_legislativo)
values (1, 'Regimen legal del contrato del teletrabajo', 27555, '2020-07-30', 
	    'La presente ley tiene por objeto establecer los presupuestos legales mínimos para la regulación de la modalidad del teletrabajo',
        'Congreso de la nación');
        
insert into ley (id, nombre_normativa, numero_normativa, fecha_sancion, descripcion, organo_legislativo)
values (2, 'Ley de contrato de trabajo', 20744, '1974-11-11', 
	    'Esta ley establece los derechos y obligaciones de empleadores y empleados en el ámbito privado',
        'Congreso de la nación');
        
insert into ley (id, nombre_normativa, numero_normativa, fecha_sancion, descripcion, organo_legislativo)
values (3, 'Ley de ejercicio profesional', 7642, '1987-11-21', 
	    'Determinación de las condiciones para el ejercicio profesional de ciencias informáticas y constitución del consejo profesional',
        'Legislatura de Córdoba');
        
        
 -- --------------------------------------------------------

       
create table categoria (
  id int primary key auto_increment,
  nombre varchar(50) not null
);

INSERT INTO Categoria (id, nombre)
VALUES
  (1, 'Laboral'),
  (2, 'Penal'),
  (3, 'Civil'),
  (4, 'Comercial'),
  (5, 'Familia y sucesiones'),
  (6, 'Agrario y ambiental'),
  (7, 'Minería'),
  (8, 'Derecho informático');
  
  
  -- --------------------------------------------------------
  
  
  create table tipo_normativa (
  id int primary key auto_increment,
  nombre varchar(50) not null
);
  
 insert into tipo_normativa (id, nombre)
 values
  (1, 'Ley'),
  (2, 'Decreto'),
  (3, 'Resolución');
  
  
-- --------------------------------------------------------
    
    
  create table jurisdiccion (
  id int primary key auto_increment,
  nombre varchar(50) not null
);
    
 insert into jurisdiccion (id, nombre)
 values
  (1, 'Nacional'),
  (2, 'Provincial');    
    
    
-- --------------------------------------------------------
  
  
  create table palabra_clave (
  id int primary key auto_increment,
  palabra varchar(50) not null,
  ley_id int not null,
  foreign key (ley_id) references ley(id)
);


-- Insertar palabra clave para la primera ley nacional
insert into palabra_clave (palabra, ley_id)
values ('trabajo', 1), ('empleador', 1), ('empleado', 1), ('ley de contrato de trabajo', 1), ('ministerio de trabajo', 1), ('empleo', 1), ('seguridad de la nación', 1);

-- Insertar palabra clave para la segunda ley nacional
insert into palabra_clave (palabra, ley_id)
values ('ley de contrato de trabajo', 2), ('relacion laboral', 2), ('empleador', 2), ('empleado', 2), ('legislacion laboral', 2);

-- Insertar palabra clave para la ley provincial
insert into palabra_clave (palabra, ley_id)
values ('ley de ejercicio profesional', 3), ('ciencias informáticas', 3), ('ejercicio profesional', 3), ('profesional', 3), ('matrícula', 3);


  -- --------------------------------------------------------
  
         
ALTER TABLE ley
ADD COLUMN categoria_id int,
ADD FOREIGN KEY (categoria_id) REFERENCES categoria(id);

        
ALTER TABLE ley
ADD COLUMN tipo_normativa_id int,
ADD FOREIGN KEY (tipo_normativa_id) REFERENCES tipo_normativa(id);
        
        
ALTER TABLE ley
ADD COLUMN jurisdiccion_id int,
ADD FOREIGN KEY (jurisdiccion_id) REFERENCES jurisdiccion(id);

