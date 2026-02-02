create database f1_analytics;

use f1_analytics;

create table teams (
	team_id int auto_increment primary key,
    team_name varchar(50) unique not null,
    base_country varchar(50),
    championships int default 0
);

CREATE TABLE drivers (
  driver_id INT AUTO_INCREMENT PRIMARY KEY,
  driver_name VARCHAR(50) NOT NULL,
  nationality VARCHAR(40),
  team_id INT,
  wins INT DEFAULT 0,
  podiums INT DEFAULT 0,
  championships INT DEFAULT 0,
  foreign key (team_id) references teams(team_id)
);

create table circuits (
	circuit_id int auto_increment primary key,
    circuit_name varchar(100) ,
    country varchar(100),
    length_km decimal(4,2),
    laps int 
);

create table races(
	race_id int auto_increment primary key,
    season year ,
    circuit_id int ,
    race_date date ,
    foreign key(circuit_id ) references circuits(circuit_id )
);

create table race_results (
	result_id int auto_increment primary key,
    race_id int,
    driver_id int ,
    position int ,
    points decimal(4,1),
    foreign key (race_id) references races(race_id),
    foreign key (driver_id) references drivers(driver_id)
);

create table lap_time(
	lap_id int auto_increment primary key,
    race_id int,
    driver_id int,
    lap_number int,
    lap_times int,
    foreign key (race_id) references races(race_id),
    foreign key(driver_id) references drivers(driver_id)
);

create table pit_stops( 
	pit_if  int auto_increment primary key,
	race_id int,
	driver_id int,
    lap int,
    duration_sec decimal(4,2),
    tyre_compound varchar (20),
     foreign key (race_id) references races(race_id),
    foreign key(driver_id) references drivers(driver_id)
);
#some more will be added in further commits 
