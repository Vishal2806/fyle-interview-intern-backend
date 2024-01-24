-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
-- SELECT
--     teacher_id,
--     COUNT(*) AS grade_A_count
-- FROM
--     assignments
-- WHERE
--     grade = 'A'
-- GROUP BY
--     teacher_id
-- ORDER BY
--     grade_A_count DESC
-- LIMIT 1;

SELECT
    -- a.teacher_id,
    -- COUNT(*) AS num_assignments_graded,
    COUNT(CASE WHEN a.grade = 'A' THEN 1 END) AS num_a_grades
FROM
    assignments a
WHERE
    a.state = 'GRADED'
    AND a.teacher_id = (
        SELECT
            teacher_id
        FROM
            assignments
        WHERE
            state = 'GRADED'
        GROUP BY
            teacher_id
        ORDER BY
            COUNT(*) DESC
        LIMIT 1
    )
GROUP BY
    a.teacher_id;