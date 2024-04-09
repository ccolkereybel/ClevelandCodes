GARDENING 

SEEDS
name	varchar(100)
monthToPlant char(3)	fk to months
source	varchar(100)
environment		varchar(255)	(sun shade water amt etc.)
daysToHarvest int
picture  varchar(100)	link to image

MONTHS
month_id char(3) pk
month_name varchar(25)

-------------------------------------------------------------

REGISTRATION

STUDENTS

PAYMENT

COURSES
crn pk 13231	int
Name	JavaScript	varchar
Course Number	2320 varchar or int
Department_id	int
Description		varchar
credits			int
staff_id	int fk to staff
semester_id int fk to semester
building_id int fk
room number	varchar 131
time	time
days	varchar
book_id 	int fk
pre-reqs fk COURSES int
max_students int

REGISTERED
course_id
student_id 

STAFF
staff_id	pk
role or title 
name
office number
phone number

BUILDINGS
building_id
name	ATTC
address
campus_id	metro

CAMPUS
campus_id
name
address

DEPARTMENT IT Math Chemistry
department_id
name
office
department_head fk staff
coordinator fk staff 

SEMESTERS
semester_id 
name
dates 
session 8 14 16 weeks