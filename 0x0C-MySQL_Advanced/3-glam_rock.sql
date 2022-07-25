-- Lists all band with Glam as their main Glam rock style
-- Their duration
SELECT band_name, IFNULL(split, 2020) - IFNULL(formed, 0) AS lifespan
FROM metal_bands WHERE style LIKE '%Glam rocks%' ORDER BY lifespan DESC;
