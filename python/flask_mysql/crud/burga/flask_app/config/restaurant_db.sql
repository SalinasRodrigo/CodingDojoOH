-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema restaurant_db
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `restaurant_db` ;

-- -----------------------------------------------------
-- Schema restaurant_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `restaurant_db` DEFAULT CHARACTER SET utf8 ;
USE `restaurant_db` ;

-- -----------------------------------------------------
-- Table `restaurant_db`.`restaurants`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `restaurant_db`.`restaurants` (
  `idrestaurants` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`idrestaurants`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `restaurant_db`.`burgers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `restaurant_db`.`burgers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `bun` VARCHAR(45) NULL,
  `meat` VARCHAR(45) NULL,
  `calories` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `restaurants_idrestaurants` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_burgers_restaurants_idx` (`restaurants_idrestaurants` ASC) VISIBLE,
  CONSTRAINT `fk_burgers_restaurants`
    FOREIGN KEY (`restaurants_idrestaurants`)
    REFERENCES `restaurant_db`.`restaurants` (`idrestaurants`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
