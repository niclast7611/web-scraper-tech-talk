# Job Listing Web Scraper 

## Set Up Steps 
1. Download Python [here](https://www.python.org/downloads/)
2. If you have Python check what version you have

        $ python3 -V
3. If you download Python then you will pip (Python package manager), so just check the version

        $ pip3 -V
4. Now that you have the those, clone the repo to your local and cd into it
5. You may need to download two a libraries called 
    1. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Python library for pulling data out of HTML and XMl files 
    
        `$ pip3 install bs4`

    2. [Requests](https://pypi.org/project/requests/) - Python Library for easily making HTTP request 
    
        `$ pip3 install requests`
6. Open the code

## Code Look Over
Step by step starting from the top 

<img src="images/Screen Shot 2022-07-27 at 11.00.24 AM.png">

Above are all the needed imports to get this file working including the two libraries we downloaded above. 

<img src="images/Screen Shot 2022-07-27 at 11.06.12 AM.png">
On line 14 I am grabbing of the page I want to scrape.

*Important is to check the syntax and structure of the url. As you can see the original url is on line 13. 

I deleted some of the url and allowed for string interpolation so I can change the url search results in VScode instead of doing it normally on the website. 

The first curly bracket on line 14 is for the job the user is search for while the second curly bracket is for the location of the job. 

<img src='images/Screen Shot 2022-07-27 at 11.01.00 AM.png'/>

This method is what we use to scrape all the information from the webpage, because it is a job listing I was looking for a couple specific pieces of data. By using the Chrome inspector tool I found all the corresponding div and classnames that contained the information I wanted. I searched for a specific one using the .find() method and saved them each to corresponding variables.

From line 29-32 there is a try and except block seeing if the posts have a salary listed if not it will say 'Not Listed'. 

Line 33 is saving all those variables into a variable called record. and finally we are returning that variable.

<img src='images/Screen Shot 2022-07-27 at 11.01.19 AM.png'/>

This main method is what actually does the heavy lifting. 

So for the while loop is true it is going to continue making requests to the url, parse through the HTML, and search for the job listing card which contains all the information we found in the above section. You can find the container using the inspector in Chrome. 

It is going to append the card information to a new array called records on line 38.

Line 51-55 is ensuring that the scraper will go over to the next page of listings until there is no more pages left. Instead of just scraping the first page.

The coolest part is line 57-61 which is saving all the records data to a csv file, allowing for easy viewing of all the information in a column and row format. We name the rows on line 60. 

And finally we call the main method with the url search parameters we talked about in the second section. You can change the location and job title to anything and it will scrape that corresponding Indeed page as long as the url is valid and you don't get a 403 error. 

## Trouble Shooting

If you scrape a specific page to many times you will get a 403 response which means the page is forbidding you from doing this action. 

Also double check if you allowed to scrape a specific page some companies do not allow it but Indeed does so that is why I chose to scrape that page in this example. 

If you are not getting any information in the csv file   

    print(len(cards))
    print(response)

To see what the information you are getting. 

To run a python file in VScode travel to the top of the file and look for a play button this will run the current python file in your terminal. 

<img src='images/Screen Shot 2022-07-27 at 11.29.10 AM.png'/>

The csv file can be hard to look at if theres a lot of information in it like you see below. 

<img src='images/Screen Shot 2022-07-27 at 11.31.15 AM.png'/>

To help with that you can actually import a csv file into Google Sheets or Excel if you have that. [here](https://support.google.com/docs/answer/40608?hl=en&co=GENIE.Platform%3DDesktop) 

And you can then format it like so and if you are using this scraper to find jobs you can add other rows to keep track of your application and response process. 

<img src='images/Screen Shot 2022-07-27 at 11.37.42 AM.png'/>

This simple project can be made in under 75 lines of code but can be easily expanded to include a filter to only show specific jobs with a certain salary, or only if they include Full Stack in the title, etc. It was super fun working on this and learning Python for the first time. Theres plenty of helpful resources out there if you get stuck. Have fun with this repo options are almost endless with the different sites you could scrape just do your research before hand!
