# REST-film-rate
Film rating using REST API at http://www.omdbapi.com/

# General Information and pre-settings
### Program Information
Program to read "Rotten Tomatoes" rating for a given film title. The program reads the ratings from http://www.omdbapi.com<br/>
PLEASE NOTE: you need a valid key to acces the sites API, the key can be requested at this link www.omdbapi.com/apikey.aspx

### Operating Environment
The program has been tested on Linux Ubuntu 16.04

### Get a valid KEY
A valid key is required to access http://www.omdbapi.com/ API, the key can be requested for free at www.omdbapi.com/apikey.aspx<br/>
Write the key (without any extra character) in the first line of "key.txt" file using a text editor of choice (gedit, vi, ...)

# Running the program
## OPTION1: Run the program in container
Docker shall be installed in your system for the container building and running

#### Build the container image
From directory with source file "filmRate.py" "key.txt" and "Dockerfile" execute<br/>
`sudo docker build -t film-rating`

#### Run the container
Two modes available to run the container
1) interactive mode (multiple films)<br/>
	`sudo docker run -i --rm film-rating`
  
2) single film evaluation<br/>
	`sudo docker run --rm film-rating "film name"`

## OPTION2: Run the program from command line
Make sure "requests" library is installed with the command<br/>
`pip install requests`

Launch the program, two options available<br/>
1) interactive mode (multiple films)<br/>
		`python3 filmRate.py`
    
2) single film evaluation<br/>
		`python3 filmRate.py "film name"`
