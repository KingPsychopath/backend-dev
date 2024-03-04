# SQL Murder Mystery

![Schema of Database](schema.png)

This was my intuition in solving the murder mystery detailed here: https://github.com/NUKnightLab/sql-mysteries

# Find the Crime by Sorting By Murder in the City

```sql
SELECT * from crime_scene_report WHERE city = 'SQL City' and type = 'murder';

```

|          |        |                                                                                                                                                                                           |          |
| -------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| 20180115 | murder | Security footage shows that there were 2 witnesses. The first witness lives at the last house on "Northwestern Dr". The second witness, named Annabel, lives somewhere on "Franklin Ave". | SQL City |

# Find the Witnesses

```sql
SELECT id, name from person WHERE address_street_name LIKE '%Franklin Ave%' and name LIKE '%Annabel%';

```

| id    | name           |
| ----- | -------------- |
| 16371 | Annabel Miller |

```sql
SELECT id, name, address_street_name, max(address_number) As max_address_number
from person
WHERE address_street_name LIKE '%Northwestern Dr%';

```

| id    | name           | address_street_name | max_address_number |
| ----- | -------------- | ------------------- | ------------------ |
| 14887 | Morty Schapiro | Northwestern Dr     | 4919               |

My two witnesses are Annabel Miller(16371) and Morty Schapiro(14887)

# Find the Witness Testimonies

```SQL
SELECT * from interview
WHERE person_id in (16371, 14887);
```

| person_id | transcript                                                                                                                                                                                                                      |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 14887     | I heard a gunshot and then saw a man run out. He had a "Get Fit Now Gym" bag. The membership number on the bag started with "48Z". Only gold members have those bags. The man got into a car with a plate that included "H42W". |
| 16371     | I saw the murder happen, and I recognized the killer from my gym when I was working out last week on January the 9th.                                                                                                           |

Suspect is potentially a ==Gold Gym Member==
Car had a plate that included ==H42W==
Had a Get Fit Now Gym bag so ==he's a member of Get Fit Now Gym==.

Second witness corroborates that the suspect is a member of the gym and went there **after** the murder took place as they recognised them on the week of ==January the 9th==

# First Check the Car Plate

```SQL
SELECT * from drivers_license
WHERE plate_number LIKE '%H42W%';
```

| id     | age | height | eye_color | hair_color | gender | plate_number | car_make  | car_model |
| ------ | --- | ------ | --------- | ---------- | ------ | ------------ | --------- | --------- |
| 183779 | 21  | 65     | blue      | blonde     | female | H42W0X       | Toyota    | Prius     |
| 423327 | 30  | 70     | brown     | brown      | male   | 0H42W2       | Chevrolet | Spark LS  |
| 664760 | 21  | 71     | black     | black      | male   | 4H42WR       | Nissan    | Altima    |

Witnesses say it was a man; so it can't be id 183779.

Suspects are 423327 and 664760.

# Check the Gym Members By ID

```sql
SELECT * FROM get_fit_now_member
WHERE person_id IN (
  SELECT id from drivers_license
WHERE plate_number LIKE '%H42W%'
AND gender = 'male');

SELECT * FROM get_fit_now_member
WHERE person_id IN (423329, 664760);
```

No data returned

Hrmm... the suspects don't have memberships under their id, maybe we can try searching by name

Oops I made a mistake. Was using license id

**Let me get the person id first**

```sql
SELECT * FROM person
WHERE license_id IN (SELECT id from drivers_license
WHERE plate_number LIKE '%H42W%'
AND gender = 'male');
```

| id    | name           | license_id | address_number | address_street_name   | ssn       |
| ----- | -------------- | ---------- | -------------- | --------------------- | --------- |
| 51739 | Tushar Chandra | 664760     | 312            | Phi St                | 137882671 |
| 67318 | Jeremy Bowers  | 423327     | 530            | Washington Pl, Apt 3A | 871539279 |

Hrmm.. Tuschar or Jeremy

Okay let's try this again and get **their gym memberships** -

```sql
SELECT * FROM get_fit_now_member
WHERE person_id IN
(SELECT id FROM person
WHERE license_id IN (SELECT id from drivers_license
WHERE plate_number LIKE '%H42W%'
AND gender = 'male'));

-->
SELECT * FROM get_fit_now_member
WHERE person_id IN
(51739, 67318);
```

| id    | person_id | name          | membership_start_date | membership_status |
| ----- | --------- | ------------- | --------------------- | ----------------- |
| 48Z55 | 67318     | Jeremy Bowers | 20160101              | gold              |

Jeremy is our guy, he has a gold membership but let's confirm some times and dates

**GYM ID**: 48Z5S
**PERSON ID:** 67318

2018-01-15 is the Murder Date
2018-01-09 is when Annabel says she saw him at the gym
(made a mistake earlier murder was after gym sesh)

# Let's Check If He was at the Gym on that Date

```SQL
SELECT * FROM get_fit_now_check_in
WHERE membership_id = '48Z55';
```

| membership_id | check_in_date | check_in_time | check_out_time |
| ------------- | ------------- | ------------- | -------------- |
| 48Z55         | 20180109      | 1530          | 1700           |

Jeremy was there 2018-01-09 like Annabel says

Going to double check their times over lap though

```sql
SELECT * FROM get_fit_now_member
WHERE person_id IN
(16371);
```

| id    | person_id | name           | membership_start_date | membership_status |
| ----- | --------- | -------------- | --------------------- | ----------------- |
| 90081 | 16371     | Annabel Miller | 20160208              | gold              |

```sql
SELECT * FROM get_fit_now_check_in
WHERE membership_id = '90081';
```

| membership_id | check_in_date | check_in_time | check_out_time |
| ------------- | ------------- | ------------- | -------------- |
| 90081         | 20180109      | 1600          | 1700           |

Annabel and Jeremy were both at the Gym on 2018-01-09 between the times of 16:00 and 17:00, Jeremy got there earlier at 15:30.

# Last Checks FaceBook Activity.

```SQL
SELECT * FROM facebook_event_checkin
WHERE person_id in (51739, 67318);
```

| person_id | event_id | event_name             | date     |
| --------- | -------- | ---------------------- | -------- |
| 67318     | 4719     | The Funky Grooves Tour | 20180115 |
| 67318     | 1143     | SQL Symphony Concert   | 20171206 |

Only updates from Jeremy, and he was active online on the date of the murder 2018-01-15.

Pretty sure we've found our guy.

```SQL
INSERT INTO solution VALUES (1, 'Jeremy Bowers');

        SELECT value FROM solution;
```

| value                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Congrats, you found the murderer! But wait, there's more... If you think you're up for a challenge, try querying the interview transcript of the murderer to find the real villain behind this crime. If you feel especially confident in your SQL skills, try to complete this final step with no more than 2 queries. Use this same INSERT statement with your new suspect to check your answer. |

```SQL
SELECT * FROM interview
WHERE person_id = 67318;
```

| person_id | transcript                                                                                                                                                                                                                                       |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 67318     | I was hired by a woman with a lot of money. I don't know her name but I know she's around 5'5" (65") or 5'7" (67"). She has red hair and she drives a Tesla Model S. I know that she attended the SQL Symphony Concert 3 times in December 2017. |

**Find the girl by car and description**

```sql
SELECT * FROM drivers_license
WHERE (height BETWEEN 65 and 67)
AND hair_color = 'red'
AND car_make = 'Tesla';
```

| id     | age | height | eye_color | hair_color | gender | plate_number | car_make | car_model |
| ------ | --- | ------ | --------- | ---------- | ------ | ------------ | -------- | --------- |
| 202298 | 68  | 66     | green     | red        | female | 500123       | Tesla    | Model S   |
| 291182 | 65  | 66     | blue      | red        | female | 08CM64       | Tesla    | Model S   |
| 918773 | 48  | 65     | black     | red        | female | 917UU3       | Tesla    | Model S   |

**Find the People's ID's**

```SQL
SELECT * FROM person
WHERE license_id in (
SELECT id FROM drivers_license
WHERE (height BETWEEN 65 and 67)
AND hair_color = 'red'
AND car_make = 'Tesla');
```

| id    | name             | license_id | address_number | address_street_name | ssn       |
| ----- | ---------------- | ---------- | -------------- | ------------------- | --------- |
| 78881 | Red Korb         | 918773     | 107            | Camerata Dr         | 961388910 |
| 90700 | Regina George    | 291182     | 332            | Maple Ave           | 337169072 |
| 99716 | Miranda Priestly | 202298     | 1883           | Golden Ave          | 987756388 |

**Sort by income to narrow down the folks**

```SQL
SELECT max(SSN) As Highest_Earner, annual_income FROM income
WHERE SSN in (
SELECT ssn FROM person
WHERE license_id in (
SELECT id FROM drivers_license
WHERE (height BETWEEN 65 and 67)
AND hair_color = 'red'
AND car_make = 'Tesla'));
```

987756388 = Miranda Priestly

```sql
SELECT * FROM person
WHERE ssn = 987756388;
```

| id    | name             | license_id | address_number | address_street_name | ssn       |
| ----- | ---------------- | ---------- | -------------- | ------------------- | --------- |
| 99716 | Miranda Priestly | 202298     | 1883           | Golden Ave          | 987756388 |

**Check whether she's been to concerts**

```sql
SELECT * FROM facebook_event_checkin
WHERE person_id = 99716;

```

| person_id | event_id | event_name           | date     |
| --------- | -------- | -------------------- | -------- |
| 99716     | 1143     | SQL Symphony Concert | 20171206 |
| 99716     | 1143     | SQL Symphony Concert | 20171212 |
| 99716     | 1143     | SQL Symphony Concert | 20171229 |

**Ladies and Gentlemen, we got em.**

```sql
INSERT INTO solution VALUES (1, 'Miranda Priestly');

        SELECT value FROM solution;
```

| value                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Congrats, you found the brains behind the murder! Everyone in SQL City hails you as the greatest SQL detective of all time. Time to break out the champagne! |

Took me about an hour to solve:
![[Stop Watch Timer Showing How Long It Took Me To Solve the Murder Mystery]](./time_taken_to_solve.png)
