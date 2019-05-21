## Description
	
    	log-analysis is project which analysis the log of news articles, like which artilces viewed most times or which day more number of error is occured. Python is used to code the project with psql as database.
    
## Pre Requirements
	run `vagrant ssh` in terminal after `vagrant up`
	extract **newsdata** zip file
	To load data cd into vagrant directory use the coomand `psql -d news -f newsdata.sql`

## To run the code 
	use  `python log-analysis.py` from terminal.
