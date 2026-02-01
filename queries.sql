
select
    d.driver_name,
    t.team_name,
    d.wins,
    d.championships
from drivers d
join teams t on d.team_id = t.team_id
order by d.wins desc;

select
    driver_id,
    avg(lap_times) as avg_lap
from lap_time
group by driver_id;

select
    d.driver_name,
    avg(p.duration_sec) as avg_pit
from pit_stops p
join drivers d on p.driver_id = d.driver_id
group by d.driver_name
order by avg_pit;

select compound, count(*) as usage_count
from tyre_stints
group by compound;

select
    d.driver_name,
    min(l.lap_times) as fastest_lap
from lap_time l
join drivers d on l.driver_id = d.driver_id
group by d.driver_id, d.driver_name;

#in progress
