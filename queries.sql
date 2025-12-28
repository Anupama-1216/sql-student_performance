


-- Base dataset for analysis
SELECT
    s.student_id,
    s.name,
    s.department,
    m.subject_id,
    m.score,
    m.semester
FROM Marks m
JOIN Students s ON m.student_id = s.student_id;
