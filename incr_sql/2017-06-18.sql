ALTER TABLE `game_close_bill_history_game` ADD `player_id` varchar(255) NOT NULL;
ALTER TABLE `game_close_bill_history_game` ADD `final_money` double(16,2) NOT NULL;
ALTER TABLE `game_close_bill_history_game` ADD `money` double(16,2) NOT NULL;
ALTER TABLE `game_close_bill_history_game` ADD `fee` double(16,2) NOT NULL;
ALTER TABLE `game_close_bill_history_game` ADD `player_score` double(16,2) NOT NULL;
ALTER TABLE `game_close_bill_history_game` ADD INDEX `idx_player_id` (`history_pkid`, `player_id`);
ALTER TABLE `game_close_bill_history_game` ADD `game_id` VARCHAR(255) NOT NULL AFTER `player_score`;