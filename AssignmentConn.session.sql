/*-----------Unique submissions for each day------------*/

WITH daily_subs AS (
    SELECT sub.submission_date, COUNT(submission_date) AS 'Subs_per_hacker',
    h.name AS 'Hacker_with_Max_Submissions', h.hacker_id
    FROM Hackers h JOIN Submissions sub ON h.hacker_id = sub.hacker_id
    GROUP BY sub.submission_date, h.Name, h.hacker_id
    ORDER BY sub.submission_date)
SELECT submission_date, count(Subs_per_hacker) AS 'top_unique_submissions'
FROM daily_subs
GROUP BY submission_date
ORDER BY submission_date




