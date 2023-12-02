

CREATE TABLE `cms`.`users` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `password` VARCHAR(50) NOT NULL,
  `staff_number` VARCHAR(45) NULL,
  `user_type` ENUM('SUPER_ADMIN', 'ADMIN', 'STAFF') NULL,
  `last_login` DATETIME NULL,
  `created_at` DATETIME NULL,
  `is_deleted` TINYINT NULL,
  PRIMARY KEY (`id`),
  INDEX `ind_name` (`name` ASC) VISIBLE);



CREATE TABLE `cms`.`complaint_category` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NULL,
  `description` TEXT(1000) NULL,
  `created_at` DATETIME NULL,
  `created_by` INT NULL,
  PRIMARY KEY (`id`));


ALTER TABLE `cms`.`complaint_category` 
CHANGE COLUMN `name` `name` VARCHAR(100) NOT NULL ,
CHANGE COLUMN `created_at` `created_at` DATETIME NOT NULL ,
CHANGE COLUMN `created_by` `created_by` INT UNSIGNED NOT NULL ,
ADD INDEX `fk_created_by_idx` (`created_by` ASC) VISIBLE;
;
ALTER TABLE `cms`.`complaint_category` 
ADD CONSTRAINT `fk_created_by`
  FOREIGN KEY (`created_by`)
  REFERENCES `cms`.`users` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


CREATE TABLE `cms`.`complaint` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `description` TEXT(100) NULL,
  `status` ENUM('ASSIGNED', 'RESOLVED') NOT NULL,
  `created_at` DATETIME NOT NULL,
  `created_by` DATETIME NOT NULL,
  `category_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `ind_title` (`title` ASC) VISIBLE);



ALTER TABLE `cms`.`complaint` 
CHANGE COLUMN `created_by` `created_by` INT UNSIGNED NOT NULL ,
ADD INDEX `fk_cms_created_idx` (`created_by` ASC) VISIBLE,
ADD INDEX `fk_cms_category_idx` (`category_id` ASC) VISIBLE;
;
ALTER TABLE `cms`.`complaint` 
ADD CONSTRAINT `fk_cms_created`
  FOREIGN KEY (`created_by`)
  REFERENCES `cms`.`users` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_cms_category`
  FOREIGN KEY (`category_id`)
  REFERENCES `cms`.`complaint_category` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


CREATE TABLE `cms`.`complaint_assign` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `complaint_id` INT UNSIGNED NOT NULL,
  `staff_number` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `created_by` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `FK_COMPLAINT_ID_idx` (`complaint_id` ASC) VISIBLE,
  INDEX `FK_COM_CREATED_idx` (`created_by` ASC) VISIBLE,
  CONSTRAINT `FK_COMPLAINT_ID`
    FOREIGN KEY (`complaint_id`)
    REFERENCES `cms`.`complaint` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_COM_CREATED`
    FOREIGN KEY (`created_by`)
    REFERENCES `cms`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


ALTER TABLE `cms`.`complaint_assign` 
DROP FOREIGN KEY `FK_COM_CREATED`;
ALTER TABLE `cms`.`complaint_assign` 
DROP COLUMN `created_by`,
CHANGE COLUMN `staff_number` `staff_number` INT UNSIGNED NOT NULL ,
ADD INDEX `FK_STAFF_NUM_idx` (`staff_number` ASC) VISIBLE,
DROP INDEX `FK_COM_CREATED_idx` ;
;
ALTER TABLE `cms`.`complaint_assign` 
ADD CONSTRAINT `FK_STAFF_NUM`
  FOREIGN KEY (`staff_number`)
  REFERENCES `cms`.`users` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


ALTER TABLE `cms`.`complaint_assign` 
ADD COLUMN `assigned_by` INT UNSIGNED NOT NULL AFTER `created_at`;

ALTER TABLE `cms`.`complaint_assign` 
ADD INDEX `FK_CREATED_idx` (`assigned_by` ASC) VISIBLE;
;
ALTER TABLE `cms`.`complaint_assign` 
ADD CONSTRAINT `FK_CREATED`
  FOREIGN KEY (`assigned_by`)
  REFERENCES `cms`.`users` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `cms`.`users` 
CHANGE COLUMN `is_deleted` `is_deleted` TINYINT NULL DEFAULT 0 ;




ALTER TABLE `cms`.`users` 
CHANGE COLUMN `user_type` `user_type` ENUM('SUPER_ADMIN', 'ADMIN', 'STAFF') NOT NULL ,
CHANGE COLUMN `created_at` `created_at` DATETIME NOT NULL ,
CHANGE COLUMN `is_deleted` `is_deleted` TINYINT NOT NULL DEFAULT '0' ;

ALTER TABLE `cms`.`users` 
ADD COLUMN `created_by` INT UNSIGNED NOT NULL AFTER `is_deleted`;


ALTER TABLE `cms`.`users` 
ADD COLUMN `updated_at` DATETIME NULL AFTER `created_by`;

ALTER TABLE `cms`.`complaint` 
CHANGE COLUMN `status` `status` ENUM('NOT ASSIGNED', 'ASSIGNED', 'RESOLVED') NOT NULL ;


ALTER TABLE `cms`.`complaint_assign` 
DROP FOREIGN KEY `FK_STAFF_NUM`;
ALTER TABLE `cms`.`complaint_assign` 
CHANGE COLUMN `staff_number` `staff_id` INT UNSIGNED NOT NULL ,
DROP INDEX `FK_STAFF_NUM_idx` ;
;

ALTER TABLE `cms`.`complaint_assign` 
ADD INDEX `FK_STAFF_ID_idx` (`staff_id` ASC) VISIBLE;
;
ALTER TABLE `cms`.`complaint_assign` 
ADD CONSTRAINT `FK_STAFF_ID`
  FOREIGN KEY (`staff_id`)
  REFERENCES `cms`.`users` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


ALTER TABLE `cms`.`complaint` 
ADD COLUMN `resolved_date` DATETIME NULL AFTER `category_id`;

ALTER TABLE `cms`.`complaint` 
ADD COLUMN `assigned_to` INT UNSIGNED NULL AFTER `resolved_date`;

ALTER TABLE `cms`.`complaint` 
ADD COLUMN `upload_doc` VARCHAR(255) NULL AFTER `assigned_to`;




