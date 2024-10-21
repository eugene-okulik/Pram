SET NAMES 'utf8mb4' COLLATE 'utf8mb4_0900_ai_ci';
-- 1. Создайте студента (student)
SET @student_name = 'Anton';
SET @student_second_name = 'Silov';

INSERT INTO `students` (name, second_name) values (@student_name, @student_second_name);

SET @student_id := (SELECT id FROM students WHERE name=@student_name AND second_name=@student_second_name);

-- 2. Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
INSERT INTO `books` (title, taken_by_student_id) VALUES ('Book number 1', @student_id),
                                                        ('Book number 2', @student_id),
                                                        ('Book number 3', @student_id),
                                                        ('Book number 4', @student_id),
                                                        ('Book number 5', @student_id);

-- 3. Создайте группу (group) и определите своего студента туда
SET @group_name = 'Group 11111';
insert INTO `groups` (title, start_date, end_date) VALUE (@group_name, '01.09.2024', '30.05.2025');

SET @group_id := (SELECT id from `groups` WHERE title=@group_name);
UPDATE `students` SET group_id=@group_id WHERE id=@student_id;

-- 4. Создайте несколько учебных предметов (subjects)
SET @subjet1 := 'Предмет 1';
SET @subjet2 := 'Предмет 2';
SET @subjet3 := 'Предмет 3';
INSERT  INTO `subjets` (title) VALUES (@subjet1),
                                      (@subjet2),
                                      (@subjet3);
SET @subjet1_id := (SELECT id from `subjets` WHERE title=@subjet1);
SET @subjet2_id := (SELECT id from `subjets` WHERE title=@subjet2);
SET @subjet3_id := (SELECT id from `subjets` WHERE title=@subjet3);

-- 5. Создайте по два занятия для каждого предмета (lessons)
SET @lesson1 := 'Занятие 1';
SET @lesson2 := 'Занятие 2';
INSERT INTO `lessons` (title, subject_id) VALUES ((CONCAT(@subjet1, ' ', @lesson2)), @subjet1_id),
                                                 ((CONCAT(@subjet2, ' ', @lesson1)), @subjet1_id),
                                                 ((CONCAT(@subjet1, ' ', @lesson1)), @subjet2_id),
                                                 ((CONCAT(@subjet2, ' ', @lesson2)), @subjet2_id),
                                                 ((CONCAT(@subjet3, ' ', @lesson1)), @subjet3_id),
                                                 ((CONCAT(@subjet3, ' ', @lesson2)), @subjet3_id);

-- 6. Поставьте своему студенту оценки (marks) для всех созданных вами занятий
INSERT  INTO `marks` (value, lesson_id, student_id) VALUES (5, 6441, @student_id),
                                                           (5, 6442, @student_id),
                                                           (4, 6443, @student_id),
                                                           (2, 6444, @student_id),
                                                           (5, 6445, @student_id),
                                                           (4, 6446, @student_id);

-- Получите информацию из базы данных:
-- 1. Все оценки студента
SELECT * from marks WHERE student_id = @student_id;

-- 2. Все книги студента
SELECT * from books WHERE taken_by_student_id = @student_id;

-- 3. Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
--   (всё одним запросом с использованием Join)

SELECT s.name, s.second_name, g.title AS GROUP_, b.title AS BOOK, l.title AS LESSON_TITLE, m.value AS MARK, s2.title AS LESSON
FROM students s JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets s2 ON l.subject_id = s2.id
WHERE s.id=@student_id;

