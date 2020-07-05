# Write your MySQL query statement below
#21:23AC
Select u.FirstName,u.LastName,r.City,r.State from Person as u Left join Address as r on u.PersonID = r.PersonID
