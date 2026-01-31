
insert into teams (team_name, base_country, championships) values
('Redbull racing','Austria',6),
('Ferrari','Italy',16),
('Mercedes','Germany',8);

insert into drivers (driver_name, nationality, team_id, wins, podiums, championships) values
('Max verstappen','Nerthlands',1,60,100,3),
('Lewis Hamilton','UK',2,103,197,7),
('Charles leleric','Monoco',3,6,30,0);

insert into circuits (circuit_name, country, length_km, laps) values
('Silverstone','UK',5.89,52),
('Monza','Italy',5.79,53);

insert into races (season, circuit_id, race_date) values
(2024, 1, '2024-07-07');

insert into race_results (race_id, driver_id, position, points) values
(1, 1, 1, 25),
(1, 2, 2, 18),
(1, 3, 3, 15);

# in progress
