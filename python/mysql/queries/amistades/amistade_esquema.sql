-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema amistades_esquema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `amistades_esquema` ;

-- -----------------------------------------------------
-- Schema amistades_esquema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `amistades_esquema` DEFAULT CHARACTER SET utf8 ;
USE `amistades_esquema` ;

-- -----------------------------------------------------
-- Table `amistades_esquema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `amistades_esquema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `frist_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `amistades_esquema`.`friendships`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `amistades_esquema`.`friendships` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `friend_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  INDEX `fk_users_has_users_users1_idx` (`friend_id` ASC) VISIBLE,
  INDEX `fk_users_has_users_users_idx` (`user_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_users_has_users_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `amistades_esquema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_users_users1`
    FOREIGN KEY (`friend_id`)
    REFERENCES `amistades_esquema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
