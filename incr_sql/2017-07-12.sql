CREATE TABLE `game_user_priv` (
  `pkid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_pkid` int(10) unsigned NOT NULL,
  `priv_item` varchar(255) NOT NULL,
  `game_type_pkid` int(10) unsigned NOT NULL,
  PRIMARY KEY (`pkid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
CREATE TABLE `game_type` (
  `pkid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `type_name` varchar(255) NOT NULL,
  `type_desc` varchar(255) DEFAULT NULL,
  `most_player_count` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`pkid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
ALTER TABLE game_account.game_user ADD expired_at DATETIME DEFAULT '2199-01-01 00:00:00' NOT NULL ;
INSERT INTO `game_type` (`pkid`, `created_at`, `updated_at`, `type_name`, `type_desc`, `most_player_count`) VALUES (NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'mj-baida', '麻将BD', 4), (NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'pk-pinshi', '扑克PS', 5);;
INSERT INTO `game_user_priv` (`pkid`, `created_at`, `updated_at`, `user_pkid`, `priv_item`, `game_type_pkid`) VALUES (NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, '1', 'all', '1'), (NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, '1', 'all', '2');
ALTER TABLE `game_info` ADD `game_type_pkid` INT(10) UNSIGNED NULL, ADD `user_pkid` INT(10) UNSIGNED NULL AFTER `game_type_pkid`;
ALTER TABLE `game_result` ADD `game_type_pkid` INT(10) UNSIGNED NULL, ADD `user_pkid` INT(10) UNSIGNED NULL AFTER `game_type_pkid`;
ALTER TABLE `game_close_bill_history_game` ADD `game_type_pkid` INT(10) UNSIGNED NULL, ADD `user_pkid` INT(10) UNSIGNED NULL AFTER `game_type_pkid`;
ALTER TABLE `game_close_bill_history_detail` ADD `game_type_pkid` INT(10) UNSIGNED NULL, ADD `user_pkid` INT(10) UNSIGNED NULL AFTER `game_type_pkid`;
ALTER TABLE `game_close_bill_history` ADD `game_type_pkid` INT(10) UNSIGNED NULL, ADD `user_pkid` INT(10) UNSIGNED NULL AFTER `game_type_pkid`;
UPDATE `game_info` SET user_pkid=1,game_type_pkid=1;
UPDATE `game_result` SET user_pkid=1,game_type_pkid=1;
UPDATE `game_close_bill_history_game` SET user_pkid=1,game_type_pkid=1;
UPDATE `game_close_bill_history_detail` SET user_pkid=1,game_type_pkid=1;
UPDATE `game_close_bill_history` SET user_pkid=1,game_type_pkid=1;
INSERT INTO game_account.game_user
(pkid, username, password, created_at, updated_at, expired_at)
VALUES(NULL, 'sample1', 'e10adc3949ba59abbe56e057f20f883e', NOW(), '1970-01-01 00:00:00.000', '2017-07-14 18:00:00');
INSERT INTO game_account.game_user_priv
(pkid, created_at, updated_at, user_pkid, priv_item, game_type_pkid)
VALUES(NULL, NOW(), NOW(), 2, 'all', 2);


