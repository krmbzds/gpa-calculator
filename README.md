gpa-calculator
==============

Quick & dirty GPA calculator. Saves data into a local sqlite database. Gives pretty table output.


## Use case scenario

You want to calculate your semester GPA. Shit's messed up because some of your professors didn't enter your grades on time (therefore they're not appearing on your transcript). You know your grades and want to make a quick calculation. You also want to add new grades as they're announced. Then [gpa-calculator](https://github.com/krmbzds/gpa-calculator)'s got you covered.

## Input Sequence
Run the code:
```bash
$ python3 ./gpa-calculator.py
```
Initial execution:
```
No grades database found...

Press any key to intialize the database and start adding grades.

Database initialized.

Created 'grades' table on 'grades.db' database.

Class Name: MATH 101
Semester Hours: 4
Letter Grade: B+

Add another line? (Y/n) 

Class Name: PHYS 101
Semester Hours: 4
Letter Grade: A-

Add another line? (Y/n) 

Class Name: TECH 101
Semester Hours: 4
Letter Grade: A

Add another line? (Y/n) 

Class Name: POLS 101
Semester Hours: 3
Letter Grade: D

Add another line? (Y/n) n
```
## Output
```
+------------+--------+-------+
| Class Name | Credit | Grade |
+------------+--------+-------+
|  MATH 101  |   4    |   B+  |
+------------+--------+-------+
|  PHYS 101  |   4    |   A-  |
+------------+--------+-------+
|  TECH 101  |   4    |   A   |
+------------+--------+-------+
|  POLS 101  |   3    |   D   |
+------------+--------+-------+
+----------------+--------------+----------------+
| Quality Points | Total Credit | Cumulative GPA |
+----------------+--------------+----------------+
|      47.0      |      15      |      3.14      |
+----------------+--------------+----------------+
```
