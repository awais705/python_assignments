create database lms;

CREATE TABLE `lms`.`user` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NULL,
  `email` VARCHAR(100) NOT NULL,
  `password` VARCHAR(100) NOT NULL,
  `created_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE);


CREATE TABLE `lms`.`role` (
  `id` INT(11) UNSIGNED NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  `created_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE);

CREATE TABLE `lms`.`user_role` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `role_id` INT(11) NOT NULL,
  `role_key` VARCHAR(45) NOT NULL COMMENT 'This will be the combination of user_id and role_id',
  `created_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `role_key_UNIQUE` (`role_key` ASC) VISIBLE);


ALTER TABLE `lms`.`user_role` 
CHANGE COLUMN `id` `id` INT(11) UNSIGNED NOT NULL ;


ALTER TABLE `lms`.`user_role` 
ADD INDEX `fk_user_id_idx` (`user_id` ASC) VISIBLE;
;
ALTER TABLE `lms`.`user_role` 
ADD CONSTRAINT `fk_user_id`
  FOREIGN KEY (`user_id`)
  REFERENCES `lms`.`user` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


ALTER TABLE `lms`.`user_role` 
ADD INDEX `fk_role_id_idx` (`role_id` ASC) VISIBLE;
;
ALTER TABLE `lms`.`user_role` 
ADD CONSTRAINT `fk_role_id`
  FOREIGN KEY (`role_id`)
  REFERENCES `lms`.`roles` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


CREATE TABLE `lms`.`books` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` VARCHAR(255) NULL,
  `category` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  PRIMARY KEY (`id`));


CREATE TABLE `lms`.`book_borrow` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `book_id` INT UNSIGNED NOT NULL,
  `user_id` INT UNSIGNED NOT NULL,
  `from_date` DATE NOT NULL,
  `to_date` DATE NOT NULL,
  `status` ENUM('PENDING', 'BORROWED', 'RETURN ON TIME', 'RETURNED LATE') NOT NULL DEFAULT 'PENDING',
  `return _date` DATE NULL,
  `created_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_book_id_idx` (`book_id` ASC) VISIBLE,
  INDEX `fk_user_id_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_book_id`
    FOREIGN KEY (`book_id`)
    REFERENCES `lms`.`books` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_idx_userid`
    FOREIGN KEY (`user_id`)
    REFERENCES `lms`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
