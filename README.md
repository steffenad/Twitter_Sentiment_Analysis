# Data-Pipeline for Sentiment Analysis 
* Using **Twitter** as a Data Source
* **Sentiment Analysis** on Tweets 
* Visualising  results with **Tableau** Dashboards
* Data-Pipeline  on **Google Cloud** for data collection

## Goal of Project
The general goal of this project was to collect "tweets" from the Social media plattform **Twitter** of topics of current relevance and interest and to use the plain text of these messages to do **Sentiment Analysis** on it.  

In a second step I have build a **Data Pipeline** on **Google Cloud** to automatize the data collection process so that I can see the latest trends refreshed automatically in my specific designed **Tableau** Dashboards. 

**Sentiment Analysis** can show in which general mood Twitter users have been discussing certrain issues. Does their tweets have been written in a positive, negative or neutral sentiment? Are Tweets about politician A are more negative then about politician B on average?

Therefore, I have collected tweets for two example topics. The first one was the controversial movie **"Joker"**.  Journalists and their reviews seem to see the movie more sceptical than the normal audience. I wanted to find out if Sentiment Analysis on Twitter Data can confirm this impression.

The second topic was the **Canadian Election**. I have collected tweets about the two main candidates, Justin Trudeau and Andrew Scheer, to analyse Sentiment towards both of them on Twitter close before Election Day in Canada.

But it general, using different kind of basic data analytics tools combined in one project to build a working **Data Pipeline** was in itself a motivating challenge.

![](https://lh3.googleusercontent.com/lD2WHSILNvjtOBTY_WpfTdfCsZxRAn2a4LuejieCSPeTdfJqj7MTlJT93FkGLsU2uZghg88K98NbjY4DVA4SC2qlR3jd7s5ZO-UjTkNZ1gj-GtEZsAC7u9SOIrER338tKP_Vvw8yJmrikkknhkgpp1co7r6Cw1zYn2OcV6_5lW9lCFyc2HmQaSbKpIc0PJPjkNfYdK_kasMioIYwgB6DLXbNSbl5ykLUoKeXLUdAvSqiAkfzbrUiJIVkMTqRyXiAstkYVfpVZJK2abyrsIgIBYqX_Ug-oysVgSobu4cs0lr_qO3O4XLCsSLSQwUPoni34jHTp1T95vSBUKXHRF3mLInT1qQrEG9LvQZc7qUcXbMPm9hioAxCq4piXF8p1ehWBhi3cC7KL_07ZtWcsawkPGUTl91WELmkGJRZ2JFFax1Lcdc0fJTLOuF50A6nZOQAJUj0eGyZc29kP9FNUqVfyZUtvuTSW3ZpcAN3OdO22jX2nEuuvZOeIk_yzg5m8icygSVcKzelGbrTvL8EZsz6reMmU8c0m7e9GAqbi7tjzKyexJWBpPk3Gmaabpsbuo83baufMtC7Jl_0bripUIdzUD_4R_YBN4hQdx5I8fbU0V9alriSktsXcFxS1qztJ5pqaxJiRIwJOo2ePXwACbwChCPPVHMT5_P1Gvt6VxbsgmDblKpguUm8=w1166-h654-no)


## project development

1. To use Twitter as a Data Source you need to apply for a **Twitter Developer Account** first.  

	After confirmation by Twitter you will have access to the **Twitter APIs** and you can start to collect Tweets with the help of **Python**.
	
	But it is not just the plain text that you can retrieve from Twitter, you can get additional information like the username, location of the user, time when the tweet has been created, number of followers etc.. 
	
	With this information you can build a **Raw Data Frame** of Twitter Data then.






![](https://lh3.googleusercontent.com/oHtGLqLq3u2g7AN8m0Occ7VjraBPOexbFHLi8Gx-DB-kdp1lxsS2OItvtOG84VlmD_isBDKTmg8uA3jnKzRWl4npB_PNvhtXthlALlQB2y7EBYchwK6GnADC8K9bj96yLL3P0n2Z1A4mdhEpkJQzD5YwdrqWqDHHLEms7LWKk8uzxMEeLIWZbtttDl0S_W4-e5k0LBKjV5dhJyP2HXzqtrEit3weK9I0UWFYaOTSmMtsY5bLLvpbEI4NaG-GU5SO_4SCZH0E-BrkI-fqYVrAxN1ukOY-nqLFC2bxeuUsbzQyP7mUV75gUBNsrgR8OzaUb5BgLaWlgOeeJXoa9f3-IrhdUJPtITWiDS4OcM8IUL7tRNJUWqNktl4xSjbuub7NCdxXACAQLObPkF7EymLyl8DLNYCCA0RiksigOK7fAfk-1zh56_NJAZ9uIu9JDnK__XakkTmgP9CL6e0G1S-J9meCEu_hYGZM64lmEapF3tVh7ctOVoGXy5bDNbkOpnYxEQqBPnmGF1arb8hre94g12E0U7NWqEeKmIEBTL3ZxUD3tJkdQopBBg9kiUAEzR5E9t9TuBAJry5BaQ0HUp7XFIt7z2kpkvoxGvJBXwEUBZJj_Egggd5N1ZTckFbwanCPlMEVrUuXhenFX6y4rzQQhX4wwflh_4Tz7toM246dK6CKu7IaUBhA=w1166-h654-no)
2. After collecting the raw data from twitter, I wanted to find out in which mood(sentiment) the text of each tweet had been written. 
**Sentiment Analysis** is simply the process of finding out whether a piece of text is positive, negative or neutral.

There are different types of Sentiment Analyser models.
Vader is a model used especially for **Social Media content**, and it can show the strength of emotions of a text.

It gives a **sentiment score** between minus 1 for extreme negative and plus 1 for extreme postive texts.

![](https://lh3.googleusercontent.com/DgA8AWBuQi29HocfMPnTnCB7B4OTj2n6MyjmcyXOsdkSbQqb-6C-6mDN1_AIrSdp7evtTeGNxbbuukazpli38WOrsuRAmPKx9csWEM-k6-1uDjHRpu-cSCunBwmW7s9j46bzi8ak5WnHP7vkKt7mAAJvTdVzKWesT4ugpq5S4jGbEqwQ9HPocJnYC9eawAMeOYyj2A5Ew9eFQMTg16aGjgXJkbDp1B_YK4akj-ta--KAaUA4H0V4Jv-pmQ6bOcAV8QwGWyCx67OSgnIeLAQQVPWITsz3SlzaiHle9rbzs5FpLy5xcWToRhof7Ad_5c1kxwSyzc805WALHO5tOoN-LPTmGFKAIiAbqoxp5D-HwbK6eYX-Nh-NGd8waN2FxzJ7BOM6B9BNUS4-HcOLdROi7UQvBEQ-HPRTcf5Qimwi_DPbJbmtFPMkGZVqX7vml3m9QCs0wJi_hjxD3qStHztnM3uHzAW8syY6ojQmYeCiBrWD8GKPRJUoKhSZDaXFIXHWddAY16_fPuAw-wtvQYjakPA7Ux707n0s2rRLHQResFU6dvanwqX9CX7panhBvv21fhr4kHK_52dVzEReCwFCcMh0xV0r2TQyLjiGQ-x59gEayA6rdSjcTbCEs2ZWxH915sunzuxVTMShg3i3iFj-ll6W4oOkbOGOUb8_lWlRWFkkO88M82a7=w1172-h654-no)
	But how does the **Vader** Sentiment Analyser actually work? The model  uses a **dictionary** where every word or Word combinations got a certain score. It also takes also care of punctuation, capitalisation, acronyms, emoticions, curse words or conjunctions.
![](https://lh3.googleusercontent.com/-P7o-Rfg--dbjS98CHYc9vLO3DYyTlorZ1RHrlZtcLouWqPvQl5NTT03RFC50INUO4zh8NhYS40R7X8S6Nh6Zmu5NrDu3JoAthWYG586KNNotclduTgy06_OTX7iriFXo6uBcexmlTYOoZ1XjIWsgCrEu1MAwTPXaBaoTK-EFXdOT3m2UYNg2SWUtFt_iATw_DWWVW8WVBCOfI7gdY-JxNAnSL0WmVj6ER7ANynuvQjTBmfCNi501dnEharpZRsP6WukiEj9DnSakG3Se6pFLk55BS1BhOW3EmQa3NLjSmSFsqbWiRMpzB5DbNUxuRQ9K3O_uPTGiNQjz4Nzug7AU4KcdRzKAr1vvq-G0aBLAa9hWP7zJQMrVm06eJDKV3BxHRnclwH_xU6gmc1LOQJe_DXLEzsYhA_PKfERC5kp59MTZRpT00tMow00uuOtnbrQCbzO7YREYw-Ov5S2gEch3OxT0u4jlrTzzWxWBqO4_UNjhnFs-8djNtszeBAUQAj_hB0WlqZb4tzWAo_z1-d2r1so_8aO8_0Gi2K5yzWaI0g2SriB6qPdW-Lwvx4wHdEDldwmuCpd3ZILHjej-ySv6KtbSZF045uOQhVJr-SVcyG_nb3ySgwH7pszTBiQUq5RGbX4gHTwZOY0u0dITPZHOXox8aIicrJrBBiLbz-vD1K5bTiExjhl=w1160-h654-no)
3. Simplified, there are two ways of doing this kind project:

* When you do your **working process** of collecting, coding, analysing, 	storing and visualising data completely locally on your computer, it will be necessary to re-run the process every day again and again **manually** to get the latest Data from Twitter.

![
](https://lh3.googleusercontent.com/lFfHVv2lUmyYR7G0V248mSNEKH-jMrj47-M3ZHMKPuuXtjtxpG2ZJfYb8T4vV5iAEZDzkboOKAZoJEHt3fl3maLmq4wetDfn88_rQJHMvau_RQjFtSUtANKBPQ2EWxWgfF3LheW893xMTFS92SF5c7F5XeN9GoB_Oxo_YSGqTFO7uJfSxcJP1ULJiQuDEACG-mWhz2dpl2e6vXXNXUZzEZgvZwjnv3wKDK915yUJLNDa8IU9AdK2GW66ZPazb09SZNnO_cPBlTMyF3f7hBKTuNhYNUL3Vbtqjt-zZlrvFMLnMAQIAWSWWZvCo75bqnahl6HtRSu96_fXep6rHHRc7cOXO9tfbW8I2aKuJOEWlMyVdkMSKQhjaORf_PewxZe4aE5IGVelKBTWrHUfayW6gZmMJc6ue3CBCGpszXIbPznfhnB6CAJFFZW7E0J-lwmS6qa1ww91nwuWNFDOjvlPnIX57uI-EjNAXpcTxkyNgQ5fAGdkXaZ0mRLNasNZZxHEreU04zxQybvzzfWVMkPMO_U3DYgCgZph6zftkZlSmJJPxiGg7xPLtGDh2UdQxYoxUKQayzPKCOvSIcggvaW3cdHj8bu5F5mmpscg7xtebMgB0DRz9WSwwSKJuMzxjUgloNFb8RKbLQ9YN6cR26hSXaJ2ZXXHdFmKEdrIQpm72tesv-_Jci1d=w1186-h654-no)
* There is a more elegant way to draft the working process, so that at the end it will be possible to just check your **Tableau Dashboard** every day, where you can see the latest Tweets added & analysed **automatically**.

	Putting Coding, Computing and Storage into **Google Cloud** makes it possible to automatize the collection of tweets. 
	
	Therefore you have to define a **Cronjob** for your Coding Script so that the script re-runs frequently inside the cloud, in this case once per day to collect and and analyse the tweets automatized.
	
	The data will has then been stored inside the cloud in a **SQL database**. 
	
	Connecting **Tableau** to **Cloud SQL** enables you to always get the latest data for your Dashboard Visualisations.


![](https://lh3.googleusercontent.com/ZTifa0hyLjltTYnBbNKsrat7tJfW-Z2JfIsx2V5Nj4LEkrN6UfS8Eeope5X5HesjRZ88zPK-pQXjk7xl3Oz_Lpwtf7RPecDXfYAXK2Fda-PqSV7_Ykwycuo0DtpjH182gCaSTrqzZ_yF6Bd3Q_V-4n9l1XaWiZvnHrvq1UCdojfFKm2Y50tRsLcGeVaM4vT0eXBJurqQrMWB28p-Jl2NZ_pRCh7isPlxo5WetKib0uOE5xf1TBxkQXjAmueuJh1WNUlU7wartYNgwcRKyeKRSW0qsB4aGTfYJ_zVx0DfzvBsn-zomIKr7UB1jDfGAzmNxQisek7ljB4W3RLmoJxt5UANHMLD-hnWIC3FqvJOVoXEmwsh1hrd6kklWTTZhSumHwCg10lgDNS_rDAhVW6hbBNJN0IAOp9ap4WMwzGhnZOE1MIXMcWPJvIBmvyxakhYPkgk_d-AXHfDtIRzqqVjEcQwcZHWzpedQrlCBxJhAnREep9i-DAiAjXKHLRxkzKNyspxjN5d4fe4S-3W6eSDL5pdyH1NOdE03jkZHnq_idY87iRF_m9TWDEQoOvJ2_LXzG-LcLgjDG9WgpURoYz6dHMdf4fX_g8ousoam4Bc-NHGX2MT24tB1wCxioCaIPHuBKwFq0rJ_UkMXEPuLuenC0_vqsgrt1WuosqV5IxRrpPV19-VT59o=w1180-h654-no)


