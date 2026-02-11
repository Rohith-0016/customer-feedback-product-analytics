SELECT AVG(Rating) FROM feedback;

SELECT Category, COUNT(*) 
FROM feedback 
GROUP BY Category 
ORDER BY COUNT(*) DESC;

SELECT COUNT(*) 
FROM feedback
WHERE Rating <= 2;
