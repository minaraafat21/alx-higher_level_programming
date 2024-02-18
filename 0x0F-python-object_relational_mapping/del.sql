DELETE FROM states
WHERE id NOT IN (
    SELECT id FROM (
        SELECT MIN(id) AS id
        FROM states
        GROUP BY name
    ) AS temp
);
