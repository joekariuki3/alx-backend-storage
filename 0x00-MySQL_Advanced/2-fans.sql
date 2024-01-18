-- script that ranks country origins of bands, ordered by the number of (non-unique) fans
-- Column names are origin and nb_fans

-- Createing a temporary table to store the total number of fans for each origin(country)
CREATE TEMPORARY TABLE temp_origin_fans AS
SELECT origin, SUM(fans) AS total_fans
FROM metal_bands
GROUP BY origin;

-- Rank the origins(countries) based on the total number of fans in descending order
SELECT origin, total_fans AS nb_fans
FROM temp_origin_fans
ORDER BY total_fans DESC;
