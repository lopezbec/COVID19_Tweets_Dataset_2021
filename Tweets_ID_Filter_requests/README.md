## This directory contains the Tweets’ ID obtained from performing a specific filter/search requested.

If you are interested identifying and filtering Tweets given a specific feature that is not currently on the dataset due to Twitter Policies (i.e., geolocation) or you do not have enoguth computational resources to filter over the entire dataset, pls send me an email explaining the request, its purpose and the rational as to why you are not able to perform it. 

In addition to that information, pls also share a R or python script to perform the search.

This directory contains the Tweets’ ID obtained from performing a specific filter/search requested.
If you are interested in identifying and filtering Tweets based a specific feature that is not currently on the dataset due to Twitter Policies (i.e., geolocation) or due to the lack of computational resources to filter over the entire dataset, pls send me an email explaining the request, its purpose, and the rational as to why you are not able to perform it yourself (please use official institutional email). 
In addition to that information, pls also share a R or python script to perform the filter given the conditions you want (e.g., filter based on geolocation, on langue, on country, etc.). The script need to have clear comments to help evaluate it, and it should take as input:  a path of a directory in which subdirectories following the name standard “#YEAR_#month” (like “2020_01” as in this repo) are contained. These subdirectories have a series of CSV files like the example here. As output, the code should generate   a directory, containing a series of subdirectories per month/year and inside these subdirectories csv files per day and hour in which the tweets ID are stored (see code example, and filters already performed)

## Filters Performed

1.	The directory “EN_US_GEO_US” contains all the tweets ID of tweets in English, in which the country of the user was identified as “US” or the geolocation was within the US.
