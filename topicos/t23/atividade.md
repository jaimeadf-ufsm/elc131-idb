## Sem índice

```sql
CREATE TABLE `project`(
    `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
    `duration` INTEGER,
    `cost` INTEGER
);
```

```sql
INSERT INTO `project` (`duration`, `cost`) VALUES (1, 1);
INSERT INTO `project` (`duration`, `cost`) VALUES (2, 2);
INSERT INTO `project` (`duration`, `cost`) VALUES (2, 3);
INSERT INTO `project` (`duration`, `cost`) VALUES (10, 4);
INSERT INTO `project` (`duration`, `cost`) VALUES (12, 5);
INSERT INTO `project` (`duration`, `cost`) VALUES (15, 6);
```

```sql
    START TRANSACTION;

    UPDATE project SET cost = 10 WHERE duration > 10; 

    COMMIT;
```

```sql
    START TRANSACTION;

    UPDATE project SET cost = 10 WHERE duration < 10; 

    COMMIT;
```

# Com índice

```sql
CREATE TABLE `project`(
    `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
    `duration` INTEGER,
    `cost` INTEGER,
    INDEX (`duration`)
);
```

```sql
INSERT INTO `project` (`duration`, `cost`) VALUES (1, 1);
INSERT INTO `project` (`duration`, `cost`) VALUES (2, 2);
INSERT INTO `project` (`duration`, `cost`) VALUES (2, 3);
INSERT INTO `project` (`duration`, `cost`) VALUES (10, 4);
INSERT INTO `project` (`duration`, `cost`) VALUES (12, 5);
INSERT INTO `project` (`duration`, `cost`) VALUES (15, 6);
```

```sql
    START TRANSACTION;

    UPDATE project SET cost = 10 WHERE duration > 10; 

    COMMIT;
```

```sql
    START TRANSACTION;

    UPDATE project SET cost = 10 WHERE duration < 10; 

    COMMIT;
```