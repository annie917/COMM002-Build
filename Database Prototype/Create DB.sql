-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema wisley
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema wisley
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `wisley` DEFAULT CHARACTER SET UTF8MB3 ;
USE `wisley` ;

-- -----------------------------------------------------
-- Table `wisley`.`node`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `wisley`.`node` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `coordinates` POINT NULL DEFAULT NULL,
  `proj_coord` POINT NOT NULL,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = UTF8MB3;


-- -----------------------------------------------------
-- Table `wisley`.`edge`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `wisley`.`edge` (
  `node1` INT(11) NOT NULL,
  `node2` INT(11) NOT NULL,
  `proj1` POINT NULL DEFAULT NULL,
  `proj2` POINT NULL DEFAULT NULL,
  `weight` DOUBLE NULL DEFAULT NULL,
  `direction_1_to_2` VARCHAR(256) NULL DEFAULT NULL,
  `direction_2_to_1` VARCHAR(256) NULL DEFAULT NULL,
  PRIMARY KEY (`node1`, `node2`),
  INDEX `edge_node2_fkey_idx` (`node2` ASC),
  CONSTRAINT `edge_node1_fkey`
    FOREIGN KEY (`node1`)
    REFERENCES `wisley`.`node` (`id`),
  CONSTRAINT `edge_node2_fkey`
    FOREIGN KEY (`node2`)
    REFERENCES `wisley`.`node` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = UTF8MB3;


-- -----------------------------------------------------
-- Table `wisley`.`flower_bed`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `wisley`.`flower_bed` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `polygon` POLYGON NULL DEFAULT NULL,
  `nearest_node` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `flower_bed_nearest_node_fkey_idx` (`nearest_node` ASC),
  CONSTRAINT `flower_bed_nearest_node_fkey`
    FOREIGN KEY (`nearest_node`)
    REFERENCES `wisley`.`node` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = UTF8MB3;


-- -----------------------------------------------------
-- Table `wisley`.`place`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `wisley`.`place` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `coordinates` POINT NULL DEFAULT NULL,
  `proj_coord` POINT NULL DEFAULT NULL,
  `description` VARCHAR(500) NULL DEFAULT NULL,
  `nearest_node` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `place_nearest_node_fkey_idx` (`nearest_node` ASC),
  CONSTRAINT `place_nearest_node_fkey`
    FOREIGN KEY (`nearest_node`)
    REFERENCES `wisley`.`node` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = UTF8MB3;


-- -----------------------------------------------------
-- Table `wisley`.`plant_bed`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `wisley`.`plant_bed` (
  `plant_id` INT(11) NOT NULL,
  `bed_id` INT(11) NOT NULL,
  PRIMARY KEY (`plant_id`, `bed_id`),
  INDEX `plant_bed_bed_id_fkey_idx` (`bed_id` ASC),
  CONSTRAINT `plant_bed_bed_id_fkey`
    FOREIGN KEY (`bed_id`)
    REFERENCES `wisley`.`flower_bed` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = UTF8MB3;


-- -----------------------------------------------------
-- Table `wisley`.`plant_month`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `wisley`.`plant_month` (
  `plant_id` INT(11) NOT NULL,
  `month_id` INT(11) NOT NULL,
  PRIMARY KEY (`plant_id`, `month_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = UTF8MB3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;