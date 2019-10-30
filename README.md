# Data-Pipeline for Sentiment Analysis 


* Using **Twitter** as a Data Source
* **Sentiment Analysis** on Tweets 
* Visualising  results with **Tableau** Dashboards
* Data-Pipeline  on **Google Cloud** for data collection

<br>

## Goal of Project
The general goal of this project was to collect "tweets" from the Social media plattform **Twitter** of topics of current relevance and interest and to use the plain text of these messages to do **Sentiment Analysis** on it.  

In a second step I have build a **Data Pipeline** on **Google Cloud** to automatize the data collection process so that I can see the latest trends refreshed automatically in my specific designed **Tableau** Dashboards. 

**Sentiment Analysis** can show in which general mood Twitter users have been discussing certrain issues. Does their tweets have been written in a positive, negative or neutral sentiment? Are Tweets about politician A are more negative then about politician B on average?

Therefore, I have collected tweets for two example topics. The first one was the controversial movie **"Joker"**.  Journalists and their reviews seem to see the movie more sceptical than the normal audience. I wanted to find out if Sentiment Analysis on Twitter Data can confirm this impression.

The second topic was the **Canadian Election**. I have collected tweets about the two main candidates, Justin Trudeau and Andrew Scheer, to analyse Sentiment towards both of them on Twitter close before Election Day in Canada.

But it general, using different kind of basic data analytics tools combined in one project to build a working **Data Pipeline** was in itself a motivating challenge.

<br>

![](https://imagizer.imageshack.com/img923/6929/99IFyS.jpg)

<br>

## Project Developement
<br>
1. To use Twitter as a Data Source you need to apply for a **Twitter Developer Account** first.  

After confirmation by Twitter you will have access to the **Twitter APIs** and you can start to collect Tweets with the help of **Python**.
	
But it is not just the plain text that you can retrieve from Twitter, you can get additional information like the username, location of the user, time when the tweet has been created, number of followers etc.. 
	
With this information you can build a **Raw Data Frame** of Twitter Data then.
<br>


![](https://imagizer.imageshack.com/img921/2094/uQM514.jpg)
<br>
<br>
2. After collecting the raw data from twitter, I wanted to find out in which mood(sentiment) the text of each tweet had been written. 
**Sentiment Analysis** is simply the process of finding out whether a piece of text is positive, negative or neutral.

There are different types of Sentiment Analyser models.
Vader is a model used especially for **Social Media content**, and it can show the strength of emotions of a text.

It gives a **sentiment score** between minus 1 for extreme negative and plus 1 for extreme postive texts.
<br>


![](https://imagizer.imageshack.com/img922/2299/jhOU5V.jpg)<br>
<br>
	But how does the **Vader** Sentiment Analyser actually work? The model  uses a **dictionary** where every word or Word combinations got a certain score. It also takes also care of punctuation, capitalisation, acronyms, emoticions, curse words or conjunctions.
<br>
![](https://imagizer.imageshack.com/img923/4034/rcfLDW.jpg)<br>
<br>
3. Simplified, there are two ways of doing this kind project:

When you do your **working process** of collecting, coding, analysing, 	storing and visualising data completely locally on your computer, it will be necessary to re-run the process every day again and again **manually** to get the latest Data from Twitter.
<br>
![](https://imagizer.imageshack.com/img924/9764/w3NB9p.jpg)<br>
<br>

There is a more elegant way to draft the working process, so that at the end it will be possible to just check your **Tableau Dashboard** every day, where you can see the latest Tweets added & analysed **automatically**.

Putting Coding, Computing and Storage into **Google Cloud** makes it possible to automatize the collection of tweets. 
	
Therefore you have to define a **Cronjob** for your Coding Script so that the script re-runs frequently inside the cloud, in this case once per day to collect and and analyse the tweets automatized.
	
The data will has then been stored inside the cloud in a **SQL database**. 
	
Connecting **Tableau** to **Cloud SQL** enables you to always get the latest data for your Dashboard Visualisations.
<br>


![](https://imagizer.imageshack.com/img922/5461/yybmiN.jpg)<br>
<br>
## Results

For the two example topics that I have collected Tweets of, **"Joker"** and **Canadian Election** , I have created Dashboards on Tableau to summarize the retrieved insights in a vivid form.
On the **Tableau Dashboard** for the movie "Joker" you can see on top a block that summarizes the most important numbers of the analysis as an eye-catcher.

Below on the left there are two graphs that show the **number of collected tweets** over time and a **map** for the locations of twitter users. 
	
On the right there is graph of the **average sentiment** per day, that users have been written their tweets about this movie in. 
	
It shows that the sentiment towards the movie went up significantly when the movie came to the movie theaters on the 4th of October in the US and the UK. Now the normal audience had the chance to see the movie themselves and did not longer only rely on the critical reports in the media about it.

It is also interesting to see that the sentiment is always higher during 	the weekend, when more people visit the cinemas.

Below on the right there is also a **Wordcloud**, that shows in an illustrative way the most used words in tweets about the movie "Joker".

In general the **Vader** model seems to work quite well for this topic by confirming the public mood and discussions on other social media plattforms with its scoring results.
 <br>
 
![](https://imagizer.imageshack.com/img921/9093/MIUut9.jpg)

On the Dashboard for the **Canadian Election** you can see on top on the left the total number of retrieved tweets, the collected tweets from yesterday and the percentage change compared to the day before.

Below there is a comparison of sentiment towards both main candidates and a graph that shows the total number of tweets, that spiked extremely during the TV debate.
	
It is interesting to see that **Andrew Scheer**, the conservative candidate, had a higher sentiment score until a few days before the election. Then there was a turnaround and on election day the sentiment towards the winner **Justin Trudeau** spiked.
	
However the **sentiment score** for both candidates was moving in a **relative small range** so that interpretations of the data should be treated with caution.

On the right of the dashboard there is also a summary of sentiment towards the candidates for the last three days to see the **latest trends** and not just an average score for the complete time frame.

Below on the right I have included a graph showing the average sentiment of **Canada's main media outlets**, when they have tweeted about one of the candidates. It is fascinating to see how a tabloid like the **"Toronto Sun"** has been using a more negative language for their posts compared to a more serious newspaper like the **"Toronto Star"**

**Media Bias** towards one of those candidates can also be found by this kind of analysis. I discovered differences up to 0.4 points (on a scale from -1 to +1 !) only for this very short time frame of 2 weeks, which are clearly significant. Further analysis on this point could be an exciting project too.
<br>
![](https://imagizer.imageshack.com/img924/6060/n6tTU9.jpg)










