create table users
(
    id       int primary key,
    username varchar(35)
);

create table student_group
(
    id    serial primary key,
    title varchar(10) not null
);

create table student
(
    id         serial primary key,
    user_id    int,
    name       varchar(30) not null,
    surname    varchar(30) not null,
    patronymic varchar(30) not null,
    group_id   int,

    constraint fk_student_user
        foreign key (user_id)
            references users (id),
    constraint fk_student_group
        foreign key (group_id)
            references student_group (id)
);

create table role
(
    id   serial primary key,
    name varchar(20) not null
);

create table user_role
(
    role_id int,
    user_id int,

    constraint fk_user_role
        foreign key (user_id)
            references users (id),
    constraint fk_role
        foreign key (role_id)
            references role (id)
);