# Election_Analysis

## Overview of Election Audit 

### Purpose 

The purpose of this analysis was to aid a Colorado Board of Elections employee named Tom in a election audit of a U.S. congressional precinct in Colorado. Using the raw data from the election, we will determine the total votes cast, total votes for each candidate, the percentages for each candidate and the winner of the election based on popular vote. Python was used so that the code can be used to automate the process for other elections. 

## Election-Audit Results 
-	There were 369,711 total votes cast in this election. In order to obtain this number, a for loop was written in which a variable total_votes was set to zero (prior to the for loop), and then for each row in the csv file, a one was added to the initial zero (total_votes) variable. 
-	In Jefferson county, there were a total of 38,855 votes cast. The percentage of total votes in Jefferson county was 10.5%.
In Arapahoe county, there were a total of 24,801 votes cast. The percentage of total votes in Arapahoe county was 6.7%. 
In Denver county there were a total of 306,055 votes cast. The percentage of total votes in Denver county was 82.8%.
Lines 96-107 of PyPoll_Challenge.py show the code for calculating the percentage of total votes for each county. Lines 71-80 show the code for calculating the total votes cast for the three different counties. 
-	Denver was the county with the largest number of votes. Lines 109 to 120 show the code that was written to determine the country with the largest turnout.
-	Charles Casper Stockham received 85,213 votes, which consisted of 23.0% of the total votes. Diana DeGette received 272,892 votes, which consisted of 73.8% of the total votes. Raymon Anthony Doane received 11,606 votes, which consisted of 3.1% of the total votes. The code for the percentages can be found in lines 129-138. The code for determining the total votes for each candidate can be found in lines 51-66
-	Diana DeGette won the election with a winning vote count of 272, 892 and a winning percentage (of the total votes) of 73.8%. The lines of code that determined this outcome are 142-148. 

## Election-Audit Summary 

Through the utilization of Python, the code can be utilized to audit other congressional districts and local elections. In order to analyze any other election, a different csv file would have to be loaded. This can be modified in the line 12 of code which specifies what file to load. Additionally, the files that are being loaded may have different headers, or the data may be in different rows than those that are referenced in the code. For example, line 56 may have to be altered in which 1 is the index referenced. 
