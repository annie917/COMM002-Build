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

-- -----------------------------------------------------
-- Populate node table
-- -----------------------------------------------------
INSERT INTO node (coordinates, proj_coord, name) VALUES (ST_PointFromText('POINT(-0.85302115624881 51.2914391458255)', 4326), ST_PointFromText('POINT(480075.52727804193 155325.20673843563)'), 'Node 1');
INSERT INTO node (coordinates, proj_coord, name) VALUES (ST_PointFromText('POINT(-0.85251421874499 51.2916135892949)', 4326), ST_PointFromText('POINT(480110.57192593836 155345.15844900193)'), 'Node 2');
INSERT INTO node (coordinates, proj_coord, name) VALUES (ST_PointFromText('POINT(-0.8524257058475 51.2918769305846)', 4326), ST_PointFromText('POINT(480116.2860712755 155374.54049788768)'), 'Node 3');
INSERT INTO node (coordinates, proj_coord, name) VALUES (ST_PointFromText('POINT(-0.85234255736804 51.2920077620013)', 4326), ST_PointFromText('POINT(480121.85640956485 155389.18057912646)'), 'Node 4');
INSERT INTO node (coordinates, proj_coord, name) VALUES (ST_PointFromText('POINT(-0.85246593898272 51.2921419476825)', 4326), ST_PointFromText('POINT(480113.02015144937 155403.96862270025)'), 'Node 5');
INSERT INTO node (coordinates, proj_coord, name) VALUES (ST_PointFromText('POINT(-0.85266710465884 51.2921402703639)', 4326), ST_PointFromText('POINT(480098.9963780598 155403.56291188815)'), 'Node 6');
INSERT INTO node (coordinates, proj_coord, name) VALUES (ST_PointFromText('POINT(-0.85208238309359 51.2923650305096)', 4326), ST_PointFromText('POINT(480139.37654836953 155429.19518049734)'), 'Node 7');
INSERT INTO node (coordinates, proj_coord, name) VALUES (ST_PointFromText('POINT(-0.85187317079043 51.2923985767057)', 4326), ST_PointFromText('POINT(480153.9059029 155433.15384258004)'), 'Node 8');
INSERT INTO node (coordinates, proj_coord, name) VALUES (ST_PointFromText('POINT(-0.85161836093402 51.2923063246076)', 4326), ST_PointFromText('POINT(480171.8333823625 155423.17251680512)'), 'Node 9');
INSERT INTO node (coordinates, proj_coord, name) VALUES (ST_PointFromText('POINT(-0.85269929116702 51.2916605547311)', 4326), ST_PointFromText('POINT(480097.58562198514 155350.179731822)'), 'Node 10');
INSERT INTO node (coordinates, proj_coord, name) VALUES (ST_PointFromText('POINT(-0.85259468501544 51.2919020905014)', 4326), ST_PointFromText('POINT(480104.45986591815 155377.15435603145)'), 'Node 11');
INSERT INTO node (coordinates, proj_coord, name) VALUES (ST_PointFromText('POINT(-0.8519026750896 51.2916672640752)', 4326), ST_PointFromText('POINT(480153.12022010185 155351.79401970515)'), 'Node 12');

-- -----------------------------------------------------
-- Populate edge table
-- -----------------------------------------------------
INSERT INTO edge (node1, node2, weight) VALUES ('1', '2', 40.33793082308226);
INSERT INTO edge (node1, node2, weight) VALUES ('1', '10', 33.32971510457651);
INSERT INTO edge (node1, node2, weight) VALUES ('2', '3', 29.941273689650515);
INSERT INTO edge (node1, node2, weight) VALUES ('2', '12', 43.07518790884984);
INSERT INTO edge (node1, node2, weight) VALUES ('3', '4', 15.668568440186627);
INSERT INTO edge (node1, node2, weight) VALUES ('3', '11', 12.115160922032716);
INSERT INTO edge (node1, node2, weight) VALUES ('4', '5', 17.231921670228612);
INSERT INTO edge (node1, node2, weight) VALUES ('5', '6', 14.033740294973267);
INSERT INTO edge (node1, node2, weight) VALUES ('5', '7', 36.49406422651829);
INSERT INTO edge (node1, node2, weight) VALUES ('6', '11', 26.975666498644166);
INSERT INTO edge (node1, node2, weight) VALUES ('7', '8', 15.063387998015651);
INSERT INTO edge (node1, node2, weight) VALUES ('8', '9', 20.52479885263658);
INSERT INTO edge (node1, node2, weight) VALUES ('10', '11', 27.844900425211215);

-- -----------------------------------------------------
-- Update edge table with projected coordinates
-- -----------------------------------------------------

UPDATE edge SET proj1 = ST_PointFromText('POINT(480075.52727804193 155325.20673843563)') WHERE node1 = 1 AND node2 = 2;
UPDATE edge SET proj1 = ST_PointFromText('POINT(480110.57192593836 155345.15844900193)') WHERE node1 = 2 AND node2 = 3;
UPDATE edge SET proj1 = ST_PointFromText('POINT(480116.2860712755 155374.54049788768)') WHERE node1 = 3 AND node2 = 4;
UPDATE edge SET proj1 = ST_PointFromText('POINT(480121.85640956485 155389.18057912646)') WHERE node1 = 4 AND node2 = 5;
UPDATE edge SET proj1 = ST_PointFromText('POINT(480113.02015144937 155403.96862270025)') WHERE node1 = 5 AND node2 = 6;
UPDATE edge SET proj1 = ST_PointFromText('POINT(480113.02015144937 155403.96862270025)') WHERE node1 = 5 AND node2 = 7;
UPDATE edge SET proj1 = ST_PointFromText('POINT(480139.37654836953 155429.19518049734)') WHERE node1 = 7 AND node2 = 8;
UPDATE edge SET proj1 = ST_PointFromText('POINT(480153.9059029 155433.15384258004)') WHERE node1 = 8 AND node2 = 9;
UPDATE edge SET proj1 = ST_PointFromText('POINT(480075.52727804193 155325.20673843563)') WHERE node1 = 1 AND node2 = 10;
UPDATE edge SET proj1 = ST_PointFromText('POINT(480116.2860712755 155374.54049788768)') WHERE node1 = 3 AND node2 = 11;
UPDATE edge SET proj1 = ST_PointFromText('POINT(480098.9963780598 155403.56291188815)') WHERE node1 = 6 AND node2 = 11;
UPDATE edge SET proj1 = ST_PointFromText('POINT(480097.58562198514 155350.179731822)') WHERE node1 = 10 AND node2 = 11;
UPDATE edge SET proj1 = ST_PointFromText('POINT(480110.57192593836 155345.15844900193)') WHERE node1 = 2 AND node2 = 12;
UPDATE edge SET proj2 = ST_PointFromText('POINT(480110.57192593836 155345.15844900193)') WHERE node1 = 1 AND node2 = 2;
UPDATE edge SET proj2 = ST_PointFromText('POINT(480116.2860712755 155374.54049788768)') WHERE node1 = 2 AND node2 = 3;
UPDATE edge SET proj2 = ST_PointFromText('POINT(480121.85640956485 155389.18057912646)') WHERE node1 = 3 AND node2 = 4;
UPDATE edge SET proj2 = ST_PointFromText('POINT(480113.02015144937 155403.96862270025)') WHERE node1 = 4 AND node2 = 5;
UPDATE edge SET proj2 = ST_PointFromText('POINT(480098.9963780598 155403.56291188815)') WHERE node1 = 5 AND node2 = 6;
UPDATE edge SET proj2 = ST_PointFromText('POINT(480139.37654836953 155429.19518049734)') WHERE node1 = 5 AND node2 = 7;
UPDATE edge SET proj2 = ST_PointFromText('POINT(480153.9059029 155433.15384258004)') WHERE node1 = 7 AND node2 = 8;
UPDATE edge SET proj2 = ST_PointFromText('POINT(480171.8333823625 155423.17251680512)') WHERE node1 = 8 AND node2 = 9;
UPDATE edge SET proj2 = ST_PointFromText('POINT(480097.58562198514 155350.179731822)') WHERE node1 = 1 AND node2 = 10;
UPDATE edge SET proj2 = ST_PointFromText('POINT(480104.45986591815 155377.15435603145)') WHERE node1 = 3 AND node2 = 11;
UPDATE edge SET proj2 = ST_PointFromText('POINT(480104.45986591815 155377.15435603145)') WHERE node1 = 6 AND node2 = 11;
UPDATE edge SET proj2 = ST_PointFromText('POINT(480104.45986591815 155377.15435603145)') WHERE node1 = 10 AND node2 = 11;
UPDATE edge SET proj2 = ST_PointFromText('POINT(480153.12022010185 155351.79401970515)') WHERE node1 = 2 AND node2 = 12;

-- -----------------------------------------------------
-- Update edge table with directions
-- -----------------------------------------------------

UPDATE edge SET direction_1_to_2 = 'Directions node 1 to node 2', direction_2_to_1 = 'Directions node 2 to node 1' WHERE node1 = 1 AND node2 = 2;
UPDATE edge SET direction_1_to_2 = 'Directions node 2 to node 3', direction_2_to_1 = 'Directions node 3 to node 2' WHERE node1 = 2 AND node2 = 3;
UPDATE edge SET direction_1_to_2 = 'Directions node 3 to node 4', direction_2_to_1 = 'Directions node 4 to node 3' WHERE node1 = 3 AND node2 = 4;
UPDATE edge SET direction_1_to_2 = 'Directions node 4 to node 5', direction_2_to_1 = 'Directions node 5 to node 4' WHERE node1 = 4 AND node2 = 5;
UPDATE edge SET direction_1_to_2 = 'Directions node 5 to node 6', direction_2_to_1 = 'Directions node 6 to node 5' WHERE node1 = 5 AND node2 = 6;
UPDATE edge SET direction_1_to_2 = 'Directions node 5 to node 7', direction_2_to_1 = 'Directions node 7 to node 5' WHERE node1 = 5 AND node2 = 7;
UPDATE edge SET direction_1_to_2 = 'Directions node 7 to node 8', direction_2_to_1 = 'Directions node 8 to node 7' WHERE node1 = 7 AND node2 = 8;
UPDATE edge SET direction_1_to_2 = 'Directions node 8 to node 9', direction_2_to_1 = 'Directions node 9 to node 8' WHERE node1 = 8 AND node2 = 9;
UPDATE edge SET direction_1_to_2 = 'Directions node 1 to node 10', direction_2_to_1 = 'Directions node 10 to node 1' WHERE node1 = 1 AND node2 = 10;
UPDATE edge SET direction_1_to_2 = 'Directions node 3 to node 11', direction_2_to_1 = 'Directions node 11 to node 3' WHERE node1 = 3 AND node2 = 11;
UPDATE edge SET direction_1_to_2 = 'Directions node 6 to node 11', direction_2_to_1 = 'Directions node 11 to node 6' WHERE node1 = 6 AND node2 = 11;
UPDATE edge SET direction_1_to_2 = 'Directions node 10 to node 11', direction_2_to_1 = 'Directions node 11 to node 10' WHERE node1 = 10 AND node2 = 11;
UPDATE edge SET direction_1_to_2 = 'Directions node 2 to node 12', direction_2_to_1 = 'Directions node 12 to node 2' WHERE node1 = 2 AND node2 = 12;

-- -----------------------------------------------------
-- Populate flower_beds
-- -----------------------------------------------------
INSERT INTO flower_bed (polygon) VALUES (ST_PolyFromText('POLYGON((480091.0084510239 155402.97166917197, 480098.62633110624 155394.3215879643, 480094.68395606265 155353.30622820352, 480084.0303176317 155340.73232448293, 480074.08102478756 155330.96810194952, 480077.52405924647 155344.0823968802, 480088.08154250006 155362.8118507454, 480091.0084510239 155402.97166917197))'));
INSERT INTO flower_bed (polygon) VALUES (ST_PolyFromText('POLYGON((480110.56790857145 155354.39401722339, 480103.2695884135 155354.55984210657, 480101.0949974294 155344.0774733913, 480108.26192790514 155346.33511277428, 480108.5278908757 155347.2721612925, 480110.56790857145 155354.39401722339))'));
INSERT INTO flower_bed (polygon) VALUES (ST_PolyFromText('POLYGON((480097.13054419804 155334.4067251996, 480098.9847651873 155335.461879677, 480106.94377043925 155340.90373531287, 480105.6754023277 155338.27181347102, 480099.76783875044 155333.23516726177, 480097.13054419804 155334.4067251996))'));
INSERT INTO flower_bed (polygon) VALUES (ST_PolyFromText('POLYGON((480156.9324378428 155356.23821514263, 480161.9851860688 155362.10114290385, 480167.0875104554 155364.79302059818, 480170.196742026 155363.34901882344, 480169.8635323964 155360.73171531633, 480157.79446312843 155354.94564565655, 480157.5095517987 155355.22105828047, 480156.9324378428 155356.23821514263))'));
INSERT INTO flower_bed (polygon) VALUES (ST_PolyFromText('POLYGON((480151.85750909336 155435.5472957212, 480152.00661717844 155437.97510614575, 480154.5197383981 155438.76070065395, 480162.10284920584 155438.3195467536, 480167.9675991088 155434.12002425702, 480166.82196647674 155429.62429638917, 480159.64514579944 155433.9898830427, 480151.85750909336 155435.5472957212))'));
INSERT INTO flower_bed (polygon) VALUES (ST_PolyFromText('POLYGON((480119.2060228403 155430.0926440966, 480124.861858247 155427.2891189018, 480135.4858501103 155435.75778876813, 480137.38542505377 155439.8921385896, 480142.2115255997 155442.2997728816, 480147.49661613174 155451.24470833119, 480141.37363687315 155465.98165734223, 480136.0152483492 155449.75919490342, 480119.2060228403 155430.0926440966))'));
INSERT INTO flower_bed (polygon) VALUES (ST_PolyFromText('POLYGON((480114.55848413915 155398.30207811095, 480111.92681535473 155393.13009167084, 480116.2939314505 155389.00035791515, 480119.4747809187 155388.95678025574, 480114.55848413915 155398.30207811095))'));

-- -----------------------------------------------------
-- Update flower_bed with nearest nodes
-- -----------------------------------------------------
UPDATE flower_bed SET nearest_node = 10 WHERE id = 1;
UPDATE flower_bed SET nearest_node = 2 WHERE id = 2;
UPDATE flower_bed SET nearest_node = 2 WHERE id = 3;
UPDATE flower_bed SET nearest_node = 12 WHERE id = 4;
UPDATE flower_bed SET nearest_node = 8 WHERE id = 5;
UPDATE flower_bed SET nearest_node = 7 WHERE id = 6;
UPDATE flower_bed SET nearest_node = 4 WHERE id = 7;

-- -----------------------------------------------------
-- Populate place table
-- -----------------------------------------------------
INSERT INTO place (name, coordinates, proj_coord, description) VALUES ('Picnic Area', ST_PointFromText('POINT(-0.85198112970328 51.2924438640308)', 4326), ST_PointFromText('POINT(480146.2995520728 155438.07245414014)'), 'Picnic Area Description');
INSERT INTO place (name, coordinates, proj_coord, description) VALUES ('Entrance', ST_PointFromText('POINT(-0.85324042683577 51.2912194132039)', 4326), ST_PointFromText('POINT(480060.6195600935 155300.5319708603)'), 'Entrance Description');
INSERT INTO place (name, coordinates, proj_coord, description) VALUES ('Nature Reserve', ST_PointFromText('POINT(-0.8506869638536 51.2924270909523)', 4326), ST_PointFromText('POINT(480236.5665050254 155437.61872661478)'), 'Nature Reserve Description');

-- -----------------------------------------------------
-- Update place table with nearest nodes
-- -----------------------------------------------------
UPDATE place SET nearest_node = 8 WHERE id = 1;
UPDATE place SET nearest_node = 1 WHERE id = 2;
UPDATE place SET nearest_node = 9 WHERE id = 3;

-- -----------------------------------------------------
-- Populate plant_bed
-- -----------------------------------------------------
INSERT INTO plant_bed (plant_id, bed_id) VALUES (97811, 1);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (100980, 1);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (59261, 1);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (311173, 1);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (64031, 1);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (18556, 2);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (76294, 2);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (97224, 2);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (59261, 2);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (288795, 2);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (100980, 3);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (18556, 3);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (59261, 3);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (97811, 3);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (97224, 3);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (100980, 4);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (72209, 4);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (311173, 4);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (97224, 4);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (64031, 4);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (311173, 5);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (97811, 5);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (76294, 5);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (97224, 5);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (18556, 5);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (97811, 6);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (97224, 6);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (288795, 6);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (18556, 6);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (59261, 6);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (288795, 7);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (97811, 7);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (76294, 7);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (72209, 7);
INSERT INTO plant_bed (plant_id, bed_id) VALUES (64031, 7);

-- -----------------------------------------------------
-- Populate plant_month
-- -----------------------------------------------------
INSERT INTO plant_month (plant_id, month_id) VALUES ('18556', 1);
INSERT INTO plant_month (plant_id, month_id) VALUES ('18556', 4);
INSERT INTO plant_month (plant_id, month_id) VALUES ('59261', 5);
INSERT INTO plant_month (plant_id, month_id) VALUES ('59261', 8);
INSERT INTO plant_month (plant_id, month_id) VALUES ('64031', 3);
INSERT INTO plant_month (plant_id, month_id) VALUES ('64031', 9);
INSERT INTO plant_month (plant_id, month_id) VALUES ('72209', 3);
INSERT INTO plant_month (plant_id, month_id) VALUES ('72209', 10);
INSERT INTO plant_month (plant_id, month_id) VALUES ('76294', 5);
INSERT INTO plant_month (plant_id, month_id) VALUES ('76294', 12);
INSERT INTO plant_month (plant_id, month_id) VALUES ('97224', 5);
INSERT INTO plant_month (plant_id, month_id) VALUES ('97224', 8);
INSERT INTO plant_month (plant_id, month_id) VALUES ('97811', 4);
INSERT INTO plant_month (plant_id, month_id) VALUES ('97811', 6);
INSERT INTO plant_month (plant_id, month_id) VALUES ('100980', 5);
INSERT INTO plant_month (plant_id, month_id) VALUES ('100980', 8);
INSERT INTO plant_month (plant_id, month_id) VALUES ('288795', 1);
INSERT INTO plant_month (plant_id, month_id) VALUES ('288795', 10);
INSERT INTO plant_month (plant_id, month_id) VALUES ('311173', 6);
INSERT INTO plant_month (plant_id, month_id) VALUES ('311173', 12);