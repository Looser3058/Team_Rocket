# Team_Rocket
Grupo de 10 personas ISPC


BASE DE DATOS

-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema proyecto_integral_
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema proyecto_integral_
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `proyecto_integral_` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `proyecto_integral_` ;

-- -----------------------------------------------------
-- Table `proyecto_integral_`.`categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_integral_`.`categoria` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 9
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `proyecto_integral_`.`jurisdiccion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_integral_`.`jurisdiccion` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `proyecto_integral_`.`tipo_normativa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_integral_`.`tipo_normativa` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `proyecto_integral_`.`ley`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_integral_`.`ley` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre_normativa` VARCHAR(50) NOT NULL,
  `numero_normativa` INT NOT NULL,
  `fecha_sancion` DATE NULL DEFAULT NULL,
  `descripcion` TEXT NULL DEFAULT NULL,
  `organo_legislativo` VARCHAR(50) NULL DEFAULT NULL,
  `categoria_id` INT NULL DEFAULT NULL,
  `tipo_normativa_id` INT NULL DEFAULT NULL,
  `jurisdiccion_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `categoria_id` (`categoria_id` ASC) VISIBLE,
  INDEX `tipo_normativa_id` (`tipo_normativa_id` ASC) VISIBLE,
  INDEX `jurisdiccion_id` (`jurisdiccion_id` ASC) VISIBLE,
  CONSTRAINT `ley_ibfk_1`
    FOREIGN KEY (`categoria_id`)
    REFERENCES `proyecto_integral_`.`categoria` (`id`),
  CONSTRAINT `ley_ibfk_2`
    FOREIGN KEY (`tipo_normativa_id`)
    REFERENCES `proyecto_integral_`.`tipo_normativa` (`id`),
  CONSTRAINT `ley_ibfk_3`
    FOREIGN KEY (`jurisdiccion_id`)
    REFERENCES `proyecto_integral_`.`jurisdiccion` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `proyecto_integral_`.`palabra_clave`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_integral_`.`palabra_clave` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `palabra` VARCHAR(50) NOT NULL,
  `ley_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `ley_id` (`ley_id` ASC) VISIBLE,
  CONSTRAINT `palabra_clave_ibfk_1`
    FOREIGN KEY (`ley_id`)
    REFERENCES `proyecto_integral_`.`ley` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 18
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
