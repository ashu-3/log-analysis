## Description
	
    	log-analysis is project which analysis the log of news articles, like which artilces viewed most times or which day more number of error is occured. Python is used to code the project with psql as database.
    
## Pre Requirements
	run `vagrant ssh` in terminal after `vagrant up`
	extract **newsdata** zip file
	To load data cd into vagrant directory use the coomand `psql -d news -f newsdata.sql`

## To run the code 
	use  `python log-analysis.py` from terminal.

##output 
	Most popular three articles of all time

	Candidate is jerk, alleges rival - 338647
	Bears love berries, alleges bear - 253801
	Bad things gone, say good people - 170098


	Most Popular article authors of all time

	Ursula La Multa - 507594
	Rudolf von Treppenwitz - 423457
	Anonymous Contributor - 170098
	Markoff Chaney - 84557


	Day on which more than one leads to error 

	2016-07-17 - 2.2626862468