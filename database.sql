CREATE DATABASE IF NOT EXISTS `KOKUA`;

USE `KOKUA`;

DROP TABLE IF EXISTS `Usuarios`;

CREATE TABLE `Usuarios` (
  `IDUsuario` INT PRIMARY KEY AUTO_INCREMENT,
  `Username` VARCHAR(100),
  `Password` VARCHAR(100),
  `TipoAcceso` ENUM('Almacen','Proveedor','Ejecutivo','Compras', 'Medico', 'Paciente', 'Administrador')
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Doctores`;

CREATE TABLE `Doctores` (
  `IDDoctor` INT PRIMARY KEY AUTO_INCREMENT,
  `IDUsuario` INT,
  `CedulaProfesional` INT NOT NULL,
  `Nombre` VARCHAR(255),
  `Apellido` VARCHAR(255),
  `FechaNacimiento` DATE,
  `CostoCita` DOUBLE,
  `Especialidad` VARCHAR(255)
  FOREIGN KEY (`IDUsuario`) REFERENCES `Usuarios`(`IDUsuario`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `Pacientes`;

CREATE TABLE `Pacientes` (
  `IDPaciente` INT PRIMARY KEY AUTO_INCREMENT,
  `IDUsuario` INT,
  `Nombre` VARCHAR(255),
  `Apellido` VARCHAR(255),
  `Padecimento` VARCHAR(255),
  `EstatusPaciente` ENUM('Muerto','Critico', 'Atencion_Constante', 'Estable','Servicio_Expirado'),
  `SaldoActual` DOUBLE
  FOREIGN KEY (`IDUsuario`) REFERENCES `Usuarios`(`IDUsuario`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Aseguradoras`;

CREATE TABLE `Aseguradoras` (
  `IDAseguradora` INT PRIMARY KEY,	
  `NombreAseguradora` VARCHAR(100),
  `Direccion` VARCHAR(100),
  `NumContacto` VARCHAR(255)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `EmpresasTerceras`;

CREATE TABLE `EmpresasTerceras` (
  `idEmpresaTercera` INT PRIMARY KEY AUTO_INCREMENT,
  `Nombre` VARCHAR(255),
  `Descripcion` VARCHAR(255)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `PersonasApoyo`;

CREATE TABLE `PersonasApoyo` (
  `IDPersonaApoyo` INT PRIMARY KEY AUTO_INCREMENT,
  `Nombre` VARCHAR(255),
  `Apellido` VARCHAR(255),
  `TipoDeServicio` VARCHAR(255)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Medicinas`;

CREATE TABLE `Medicinas` (
  `IDMedicina` INT PRIMARY KEY AUTO_INCREMENT,
  `NombreMedicina` VARCHAR(255) NOT NULL,
  `Descripción` TEXT,
  `Precio_Unitario` DOUBLE,
  `Criticidad`  ENUM('Alto', 'Medio', 'Bajo'),
  `NivelDeInventario` INT
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Proveedor`;

CREATE TABLE `Proveedores` (
  `IDProveedor` INT PRIMARY KEY AUTO_INCREMENT,
  `IDUsuario` INT,
  `Nombre` VARCHAR(255) NOT NULL,
  `Ubicación` VARCHAR(255),
  `NumContacto` VARCHAR(255)
  FOREIGN KEY (`IDUsuario`) REFERENCES `Usuarios`(`IDUsuario`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Polizas`;

CREATE TABLE `Polizas` (
  `IDPoliza` INT PRIMARY KEY AUTO_INCREMENT,
  `IDAseguradora` INT,
  `Vigencia_de_Poliza` DATE,
  `TipoDePoliza` ENUM('Premium', 'Estandar', 'Basica'),
  `SumaAsegurada` DOUBLE,	
  `FechaInicio` DATE,
  `Prima` Double,
  FOREIGN KEY (`IDAseguradora`) REFERENCES `Aseguradoras`(`IDAseguradora`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Asignaciones`;

CREATE TABLE `Asignaciones` (
  `IDPaciente` INT,
  `FechaAsignacion` Date,
  `IDDoctor` INT,
  `IDPersonaApoyo` INT,
  `IDPoliza` INT,
  PRIMARY KEY (IDPaciente,IDDoctor,IDPersonaApoyo,IDPoliza),
  FOREIGN KEY (`IDPersonaApoyo`) REFERENCES `PersonasApoyo`(`IDPersonaApoyo`),
  FOREIGN KEY (`IDDoctor`) REFERENCES `Doctores`(`IDDoctor`),
  FOREIGN KEY (`IDPaciente`) REFERENCES `Pacientes`(`IDPaciente`),
  FOREIGN KEY (`IDPoliza`) REFERENCES `Polizas`(`IDPoliza`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `Citas`;

CREATE TABLE `Citas` (
  `IDCita` INT PRIMARY KEY AUTO_INCREMENT,
  `IDPaciente` INT,
  `IDDoctor` INT,
  `TipoCita` ENUM('Estandar','DePrueba'),
  `EstatusCita` ENUM('Realizada','Agendada','Cancelada'),
  `Fecha` DATE,
  FOREIGN KEY (`IDDoctor`) REFERENCES `Doctores`(`IDDoctor`),
  FOREIGN KEY (`IDPaciente`) REFERENCES `Pacientes`(`IDPaciente`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Receta`;

CREATE TABLE `Receta` (
  `IDReceta` INT PRIMARY KEY AUTO_INCREMENT,
  `IDCita` INT,
  `IDMedicina` INT,
  `CantidadDiaria` INT,
  `Indicaciones` TEXT,
  FOREIGN KEY (`IDCita`) REFERENCES `Citas`(`IDCita`),
  FOREIGN KEY (`IDMedicina`) REFERENCES `Medicinas`(`IDMedicina`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Lote`;

CREATE TABLE `Lote` (
  `IDLote` INT PRIMARY KEY AUTO_INCREMENT,
  `IDMedicina` INT,
  `FechaManufactura` DATE NOT NULL,
  `FechaExpiración` DATE NOT NULL,
  `IDProveedor` INT,
  `CantidadRecibida` FLOAT NOT NULL,
  `CantidadRestante` FLOAT NOT NULL,
  `UbicacionAlmacen` VARCHAR(100),
  FOREIGN KEY (`IDProveedor`) REFERENCES `Proveedores`(`IDProveedor`),
  FOREIGN KEY (`IDMedicina`) REFERENCES `Medicinas`(`IDMedicina`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `Factura`;

CREATE TABLE `Factura` (
  `idFactura` INT PRIMARY KEY AUTO_INCREMENT,
  `idCita` INT,
  `Costo` DOUBLE,/*No se si quieren dejarlo porque es un campo calculado de los demás costos*/
  FOREIGN KEY (`IDCita`) REFERENCES `Citas`(`IDCita`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `ServiciosExtra`;

CREATE TABLE `ServiciosExtra` (
  `IDServicio` INT PRIMARY KEY AUTO_INCREMENT,
  `IDEmpresaTercera` INT,
  `IDPaciente` INT,
  `Fecha_contratada` DATE,
  `Costo` DOUBLE,
  `Estatus` ENUM('Realizado','Agendado','Cancelado'),
  FOREIGN KEY (`IDEmpresaTercera`) REFERENCES `EmpresasTerceras`(`IDEmpresaTercera`),
  FOREIGN KEY (`IDPaciente`) REFERENCES `Pacientes`(`IDPaciente`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Ordenes`;

CREATE TABLE `Ordenes` (
  `IDOrden` INT PRIMARY KEY AUTO_INCREMENT,
  `IDUsuario` INT,
  `FechaOrden` DATE,
  `IDProveedor` INT,
  `IDMedicina` INT,
  `CantidadOrdenada` INT NOT NULL,
  `EntregaEsperada` DATE,
  `Costo` DOUBLE,
  `Estatus` ENUM('Realizado','Agendado','Cancelado'),
  FOREIGN KEY (`IDProveedor`) REFERENCES `Proveedores`(`IDProveedor`),
  FOREIGN KEY (`IDMedicina`) REFERENCES `Medicinas`(`IDMedicina`),
  FOREIGN KEY (`IDUsuario`) REFERENCES `Usuarios`(`IDUsuario`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `LogInventarios`;

CREATE TABLE `LogInventarios` (
  `IDLog` INT PRIMARY KEY AUTO_INCREMENT,
  `IDUsuario` INT,
  `TimeStamp` DATE,
  `IDMedicina` INT,
  `Cantidad` INT,
  FOREIGN KEY (`IDMedicina`) REFERENCES `Medicinas`(`IDMedicina`),
  FOREIGN KEY (`IDUsuario`) REFERENCES `Usuarios`(`IDUsuario`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;



