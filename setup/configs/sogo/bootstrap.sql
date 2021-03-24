DROP VIEW IF EXISTS sogo_view;

CREATE VIEW `sogo_view` 
    AS SELECT 
        `user`.`email` AS `c_uid`, 
        `user`.`domain_name` AS `domain`, 
        `user`.`email` AS `c_name`, 
        `user`.`password` AS `c_password`, 
        `user`.`displayed_name` AS `c_cn`, 
        `user`.`email` AS `mail` 
    FROM `user` ;