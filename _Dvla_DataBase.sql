use master
go 
create database cars
go
use cars
go
create table MakeModel
(
    CARID int identity,
    MAKE varchar(20),
    MODEL varchar(20),
    year int not null

)
go
create table regPartLists
(
    DvlaIDs blob,
    yearIDS blob,
    randomID varchar(3) identity
)
go
create table carreg
(
    CARID
)