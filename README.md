# Election_Analysis

## Overview

A Colorado Board of Elections wants an election audit of a recent local congressional election.
Using a database, they want to:

1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes
3. Calculate the total number of votes each candidate received
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular vote
6. The voter turnout for each county
    - The percentage of votes from each county out of the total count
7. The county with the highest turnout

## Resources
- Data Source: elections_results.csv
- Software: Phyton 3.6.7, Visual Studio Code 1.47.1

## Results
The analysis of the election shows that:
- There were 369,711 votes cast in the election
- The county turnout (percentage) and number of votes are:
    - Jefferson: turnout of 10.5% and 38,855 number of votes.
    - Denver: turnout of 82.8% and 306,055 number of votes.
    - Arapahoe: turnout of 6.7% and 27,801 number of votes.
- The county with the highest turnout:
    - **Denver** had the highest turnout: **82.8%**.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
    
## Summary
It is important to notice that this code was written to be versatile, and it can be used in any county, with any number of candidates.
As the database file (CSV) has the same format (Ballot ID, County, Candidate as headers), the code will run flawlessly for any number of counties and/or candidates.
As an example, you can see below that I modified the original CSV file (election_results_mod.csv), where:

1. I added a fourth candidate, "Buffallo Bill"
2. I added a fourth County, "Rockwell". 

After running the code, as it is, here are the results:

1. County of Rockweel shows up on the County Votes list with 0.6% Turnout and 2,285 votes.
2. Candidate Bufallo Bill has 0.0% of votes, and 167 number of votes

Below is a snapshot of the Terminal

![Screen Shot 2020-11-08 at 4 19 54 PM](https://user-images.githubusercontent.com/72593264/98485837-e8f8ae00-21de-11eb-9d82-c84d47c42d1e.png)







    
    
