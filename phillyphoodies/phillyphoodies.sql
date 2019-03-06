CREATE DATABASE PhillyPhoodies;
Use PhillyPhoodies;
CREATE TABLE Users (UserID varchar(15) not null, UserName varchar(30) not null, UserPassword varchar(30) not null, Email varchar(30), Location varchar(30) not null, primary key(UserId) );

CREATE TABLE TypeFood (FoodTypeID varchar(30) not null, FoodType varchar(30) not null, primary key(FoodTypeID));

CREATE TABLE Food (FoodID varchar(20) not null, FoodName varchar(30) not null, FoodPrice float not null, primary key(FoodID));

create table Restaurant(RestaurantID varchar(30) not null,RestaurantName varchar(40) not null, FoodTypeID varchar(30) not null, Address varchar(30) not null, State varchar(10) not null, PricePoint float, primary key(RestaurantID));
CREATE TABLE Food_Restaurant (Food_ID varchar(20) not null,Restaurant_ID varchar(30) not null, primary key(Food_ID,Restaurant_ID), foreign key(Food_ID) references Food(FoodID), foreign key(Restaurant_ID) references Restaurant(RestaurantID));
CREATE TABLE Restaurant_TypeFood (FoodTypeID varchar(30) not null, RestaurantID varchar(30) not null,primary key(FoodTypeID,RestaurantID),foreign key(FoodTypeID) references TypeFood(FoodTypeID), foreign key(RestaurantID) references Restaurant(RestaurantID));


INSERT INTO `phillyphoodies`.`restaurant` (`RestaurantID`, `RestaurantName`, `FoodTypeID`, `Address`, `State`, `PricePoint`) VALUES ('R1', 'Joe\'s Bar', '1', '3141 Market st', 'PA', '1000');
INSERT INTO `phillyphoodies`.`restaurant` (`RestaurantID`, `RestaurantName`, `FoodTypeID`, `Address`, `State`, `PricePoint`) VALUES ('R2', 'Falone Hoagies', '2', '7100 Elmwood Ave', 'PA', '500');
INSERT INTO `phillyphoodies`.`restaurant` (`RestaurantID`, `RestaurantName`, `FoodTypeID`, `Address`, `State`, `PricePoint`) VALUES ('R3', 'Pete Pizza', '3', '7120 Buist Ave', 'PA', '100');

INSERT INTO `phillyphoodies`.`typefood` (`FoodTypeID`, `FoodType`) VALUES ('FT1', 'AMERICAN');
INSERT INTO `phillyphoodies`.`typefood` (`FoodTypeID`, `FoodType`) VALUES ('FT2', 'CHINESE');
INSERT INTO `phillyphoodies`.`typefood` (`FoodTypeID`, `FoodType`) VALUES ('FT3', 'BRAZILLIAN');
INSERT INTO `phillyphoodies`.`typefood` (`FoodTypeID`, `FoodType`) VALUES ('FT4', 'SPANISH');
INSERT INTO `phillyphoodies`.`typefood` (`FoodTypeID`, `FoodType`) VALUES ('FT5', 'JAPANESE');

INSERT INTO `phillyphoodies`.`food` (`FoodID`, `FoodName`, `FoodPrice`) VALUES ('F1', 'Pizza', '6.5');
INSERT INTO `phillyphoodies`.`food` (`FoodID`, `FoodName`, `FoodPrice`) VALUES ('F2', 'Cheese Steak', '5');
INSERT INTO `phillyphoodies`.`food` (`FoodID`, `FoodName`, `FoodPrice`) VALUES ('F3', 'Chicken Nugget', '4.5');
INSERT INTO `phillyphoodies`.`food` (`FoodID`, `FoodName`, `FoodPrice`) VALUES ('F4', 'French Fried', '4.0');



INSERT INTO `phillyphoodies`.`users` (`UserID`, `UserName`, `UserPassword`, `Email`, `Location`) VALUES ('US1', 'THH29', 'THH29', 'thh29@drexel.edu', 'Philadelphia');
INSERT INTO `phillyphoodies`.`users` (`UserID`, `UserName`, `UserPassword`, `Email`, `Location`) VALUES ('US2', 'MRD336', 'MRD336', 'MRD36@DREXEL.EDU', 'PHILADELPHIA');
INSERT INTO `phillyphoodies`.`users` (`UserID`, `UserName`, `UserPassword`, `Email`, `Location`) VALUES ('US3', 'JF945', 'JF945', 'JF945@DREXEL.EDU', 'PHILADELPHIA');
INSERT INTO `phillyphoodies`.`users` (`UserID`, `UserName`, `UserPassword`, `Email`, `Location`) VALUES ('US4', 'KMR711', 'KMR711', 'KMR711@DREXEL.EDU', 'PHILADELPHIA');

INSERT INTO `phillyphoodies`.`food_restaurant` (`Food_ID`, `Restaurant_ID`) VALUES ('F1', 'R1');
INSERT INTO `phillyphoodies`.`food_restaurant` (`Food_ID`, `Restaurant_ID`) VALUES ('F1', 'R2');
INSERT INTO `phillyphoodies`.`food_restaurant` (`Food_ID`, `Restaurant_ID`) VALUES ('F1', 'R3');
INSERT INTO `phillyphoodies`.`food_restaurant` (`Food_ID`, `Restaurant_ID`) VALUES ('F2', 'R2');
INSERT INTO `phillyphoodies`.`food_restaurant` (`Food_ID`, `Restaurant_ID`) VALUES ('F3', 'R1');
INSERT INTO `phillyphoodies`.`food_restaurant` (`Food_ID`, `Restaurant_ID`) VALUES ('F4', 'R3');
INSERT INTO `phillyphoodies`.`food_restaurant` (`Food_ID`, `Restaurant_ID`) VALUES ('F4', 'R2');

INSERT INTO `phillyphoodies`.`restaurant_typefood` (`FoodTypeID`, `RestaurantID`) VALUES ('FT1', 'R1');
INSERT INTO `phillyphoodies`.`restaurant_typefood` (`FoodTypeID`, `RestaurantID`) VALUES ('FT2', 'R1');
INSERT INTO `phillyphoodies`.`restaurant_typefood` (`FoodTypeID`, `RestaurantID`) VALUES ('FT1', 'R2');
INSERT INTO `phillyphoodies`.`restaurant_typefood` (`FoodTypeID`, `RestaurantID`) VALUES ('FT3', 'R2');
INSERT INTO `phillyphoodies`.`restaurant_typefood` (`FoodTypeID`, `RestaurantID`) VALUES ('FT4', 'R3');
INSERT INTO `phillyphoodies`.`restaurant_typefood` (`FoodTypeID`, `RestaurantID`) VALUES ('FT5', 'R3');

select * from users;

select RestaurantName,FoodType 
from restaurant_typefood as rt,restaurant as r,typefood as t 
where rt.FoodTypeID = t.FoodTypeID and rt.RestaurantID = r.RestaurantID;


select r.RestaurantName, tf.FoodType
from restaurant r 
inner join restaurant_typefood rt on r.RestaurantID = rt.RestaurantID 
inner join typefood tf on rt.FoodTypeID = tf.FoodTypeID;
