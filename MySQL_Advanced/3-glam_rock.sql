-- All bands with Glam rock as their main style, ranked by their longevity

SELECT band_name, IFNULL(split, 2024) - IFNULL(formed, 0) AS lifespan 
FROM metal_bands 
WHERE style like '%Glam rock%';
