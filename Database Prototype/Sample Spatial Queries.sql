USE wisley_pt;

/* Query to find closet flower bed containing plant 76294*/
SELECT pb.bed_id, ST_Distance(ST_PointFromText('POINT(480060.6195600935 155300.5319708603)'), fb.polygon) 
AS dist FROM plant_bed pb 
JOIN flower_bed fb ON pb.bed_id = fb.id 
WHERE pb.plant_id =76294 ORDER BY dist LIMIT 1;

/* Query to find places, sorted by distance from a location */
SELECT id, ST_AsText(coordinates), name, description, ST_Distance(ST_PointFromText('POINT(480060.6195600935 155300.5319708603)'), proj_coord) AS dist FROM place ORDER BY dist;
              
/* Query to find the mathematical centroid of flower bed 2 */
SELECT ST_AsText(ST_Centroid(polygon)) FROM flower_bed WHERE id = 2;
