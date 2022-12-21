DESCRIBE tutorial;
DESCRIBE passo;

SELECT * FROM tutorial;
SELECT * FROM passo;

INSERT INTO tutorial (titulo)
VALUES ('Tutorial x'),
('Tutorial y'),
('Tutorial z');

INSERT INTO passo (descriçao, Tutorial_idTutorial)
VALUES ('Descrição do tutorial x', 1),
('Descrição do tutorial y', 2),
('Descrição do tutorial z', 3);