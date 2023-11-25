-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema lms
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema lms
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `lms` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `lms` ;

-- -----------------------------------------------------
-- Table `lms`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lms`.`books` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT NULL DEFAULT NULL,
  `category` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `added_by` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_bookname` (`name` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 53
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `lms`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lms`.`user` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `password` VARCHAR(100) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 70
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `lms`.`book_borrow`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lms`.`book_borrow` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `book_id` INT UNSIGNED NOT NULL,
  `user_id` INT UNSIGNED NOT NULL,
  `from_date` DATE NOT NULL,
  `to_date` DATE NOT NULL,
  `status` ENUM('PENDING', 'BORROWED', 'RETURNED') NOT NULL DEFAULT 'PENDING',
  `return_date` DATE NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_book_id_idx` (`book_id` ASC) VISIBLE,
  INDEX `fk_user_id_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_book_id`
    FOREIGN KEY (`book_id`)
    REFERENCES `lms`.`books` (`id`),
  CONSTRAINT `fk_idx_userid`
    FOREIGN KEY (`user_id`)
    REFERENCES `lms`.`user` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `lms`.`roles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lms`.`roles` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `lms`.`user_role`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lms`.`user_role` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` INT UNSIGNED NOT NULL,
  `role_id` INT UNSIGNED NOT NULL,
  `role_key` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `role_key_UNIQUE` (`role_key` ASC) VISIBLE,
  INDEX `fk_user_id_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_role_id_idx` (`role_id` ASC) VISIBLE,
  CONSTRAINT `fk_role_id`
    FOREIGN KEY (`role_id`)
    REFERENCES `lms`.`roles` (`id`),
  CONSTRAINT `fk_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `lms`.`user` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 66
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
