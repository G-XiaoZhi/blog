create table `entry` (
    `id` int(11) unsigned not null AUTO_INCREMENT comment 'id',
    `title` VARCHAR(64) not null default '' comment 'title',
    `slug` VARCHAR(64) not null default '' comment 'slug',
    `body` text not null comment 'title',
    `create_time` datetime not null default CURRENT_TIMESTAMP comment 'create_time',
    `modify_time` datetime not null default CURRENT_TIMESTAMP comment 'modify_time',
    `version` int(11) unsigned not null default 1 comment 'version',

    primary key (`id`)
) engine = InnoDB  default charset=utf8 comment 'entry';


create table `tag` (
    `id` int(11) unsigned not null AUTO_INCREMENT comment 'id',
    `name` VARCHAR(64) not null default '' comment 'name',
    `slug` VARCHAR(64) not null default '' comment 'slug',
    `create_time` datetime not null default CURRENT_TIMESTAMP comment 'create_time',
    `modify_time` datetime not null default CURRENT_TIMESTAMP comment 'modify_time',
    `version` int(11) unsigned not null default 1 comment 'version',

    primary key (`id`)
) engine = InnoDB default charset=utf8 comment='tag';


create table `entry_tags` (
    `id` int(11) unsigned not null AUTO_INCREMENT comment 'id',
    `tag_id` int(11) unsigned not null,
    `entry_id` int(11) unsigned not null,

    primary key (`id`),
     key `idx_tag_id` (`tag_id`),
     key `idx_entry_id` (`entry_id`),
     constraint `fk_tag_id` foreign key (`tag_id`) REFERENCES tag(`id`),
     constraint `fk_entry_id` foreign key (`entry_id`) REFERENCES entry(`id`)
) engine=InnoDB default charset=utf8 comment='entry_tags';