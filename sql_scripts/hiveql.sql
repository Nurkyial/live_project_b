create database if not exists live_project_b location '/user/live_project_b';
show databases;

use live_project_b;

CREATE EXTERNAL TABLE IF NOT EXISTS clients (
    client_id INT,
    client_name STRING,
    client_email STRING,
    client_phone STRING,
    client_address STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    "separatorChar" = ",",
    "quoteChar" = "\"",
    "escapeChar" = "\\"
)
STORED AS TEXTFILE
LOCATION '/user/live_project_b';

select * from clients;

drop table if exists clients;