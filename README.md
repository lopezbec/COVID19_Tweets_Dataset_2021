##   This repo only contatins the data  from **2021**. For the data  and statistics of other years please visit:<a href="https://github.com/lopezbec/COVID19_Tweets_Dataset" class="uri">https://github.com/lopezbec/COVID19_Tweets_Dataset</a>
-----------------
-   [Data Organization](#data-organization)
-   [Data Statistics](#data-statistics)
    -   [General Statistics](#general-statistics)
    -   [Language Statistics](#language-statistics)
    -   [English Sentiment Analaysis](#english-sentiment-analaysis)
    -   [English Named Entity Recognition, Mentions, and
        Hashtags](#english-named-entity-recognition-mentions-and-hashtags)
    -   [Spanish Sentiment Analaysis](#spanish-sentiment-analaysis)
    -   [Spanish Named Entity
        Recognition](#spanish-named-entity-recognition)
    -   [Data Collection Process
        Inconsistencies](#data-collection-process-inconsistencies)
-   [Hydrating Tweets](#hydrating-tweets)
    -   [Using our TWARC Notebook](#using-our-twarc-notebook)
        -   [Using Hydrator](#using-hydrator)
        -   [Using Twarc](#using-twarc)
-   [Inquiries & Requests](#inquiries-requests)
-   [Licensing](#licensing)
-   [References](#references)


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

The repository contains an ongoing collection of tweets associated with
the novel coronavirus COVID-19 since January 22nd, 2020.

As of 12/31/2021 there were a total of **2,497,294,716** tweets
collected. The tweets are collected using Twitter’s trending topics and
selected keywords. Moreover, the tweets from [Chen et
al. (2020)](https://github.com/echen102/COVID-19-TweetIDs) was used to
supplement the dataset by hydrating non-duplicated tweets. These tweets
are just a sample of all the tweets generated that are provided by
Twitter, and it does not represent the whole population of tweets at any
given point.

**Citation**

Christian Lopez, and Caleb Gallemore (2020) An Augmented Multilingual
Twitter Dataset for Studying the COVID-19 Infodemic. DOI:
10.21203/rs.3.rs-95721/v1
<a href="https://www.researchsquare.com/article/rs-95721/v1" class="uri">https://www.researchsquare.com/article/rs-95721/v1</a>

Data Organization
-----------------

The dataset is organized by hour (UTC) , month, and by tables. The
description of all the features in all five tables is provided below.
For example, the path
“./Summary\_Details/2020\_01/2020\_01\_22\_00\_Summary\_Details.csv”
contains all the summary details of the tweets collection on January
22nd at 00:00 UTC time.

<table class="table table" style="margin-left: auto; margin-right: auto; font-size: 9px; margin-left: auto; margin-right: auto;">
<caption style="font-size: initial !important;">
Features Description
</caption>
<thead>
<tr>
<th style="text-align:left;font-weight: bold;">
Table
</th>
<th style="text-align:left;font-weight: bold;">
Feature Name
</th>
<th style="text-align:left;font-weight: bold;">
Description
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
Primary key
</td>
<td style="text-align:left;">
Tweet\_ID
</td>
<td style="text-align:left;">
Integer representation of the tweets unique identifier
</td>
</tr>
<tr>
<td style="text-align:left;">
1.Summary\_Details
</td>
<td style="text-align:left;">
Language
</td>
<td style="text-align:left;">
When present, indicates a BCP47 language identifier corresponding to the
machine-detected language of the Tweet text
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
Geolocation\_cordinate
</td>
<td style="text-align:left;">
Indicates whether or not the geographic location of the tweet was
reported
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
RT
</td>
<td style="text-align:left;">
Indicates if the tweet is a retweet (YES) or original tweet (NO)
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
Likes
</td>
<td style="text-align:left;">
Number of likes for the tweet
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
Retweets
</td>
<td style="text-align:left;">
Number of times the tweet was retweeted
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
Country
</td>
<td style="text-align:left;">
When present, indicates a list of uppercaseÂ two-letter country
codesÂ from which the tweet comes
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
Date\_Created
</td>
<td style="text-align:left;">
UTC date and time the tweet was created
</td>
</tr>
<tr>
<td style="text-align:left;">
2.Summary\_Hastag
</td>
<td style="text-align:left;">
Hashtag
</td>
<td style="text-align:left;">
Hashtag (\#) present in the tweet
</td>
</tr>
<tr>
<td style="text-align:left;">
3.Summary\_Mentions
</td>
<td style="text-align:left;">
Mentions
</td>
<td style="text-align:left;">
Mention (@) present in the tweet
</td>
</tr>
<tr>
<td style="text-align:left;">
4.Summary\_Sentiment
</td>
<td style="text-align:left;">
Sentiment\_Label
</td>
<td style="text-align:left;">
Most probable tweet sentiment (neutral, positive, negative)
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
Logits\_Neutral
</td>
<td style="text-align:left;">
Non-normalized prediction for neutral sentiment
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
Logits\_Positive
</td>
<td style="text-align:left;">
Non-normalized prediction for positive sentiment
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
Logits\_Negative
</td>
<td style="text-align:left;">
Non-normalized prediction for negative sentiment
</td>
</tr>
<tr>
<td style="text-align:left;">
5.Summary\_NER
</td>
<td style="text-align:left;">
NER\_text
</td>
<td style="text-align:left;">
Text stating a named entity recognized by the NER algorithm
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
Start\_Pos
</td>
<td style="text-align:left;">
Initial character position within the tweet of the NER\_text
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
End\_Pos
</td>
<td style="text-align:left;">
End character position within the tweet of the NER\_text
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
NER\_Label Prob
</td>
<td style="text-align:left;">
Label and probability of the named entity recognized by the NER
algorithm
</td>
</tr>
<tr>
<td style="text-align:left;">
6.Summary\_Sentiment\_ES
</td>
<td style="text-align:left;">
Sentiment\_Label
</td>
<td style="text-align:left;">
Most probable tweet sentiment (neutral, positive, negative)
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
Probability\_pos
</td>
<td style="text-align:left;">
Probability of the tweets sentiment being positive (\<=0.33 is negative,
\>0.33 OR \<0.66 is neutral, else positve)
</td>
</tr>
<tr>
<td style="text-align:left;">
7.Summary\_NER\_ES
</td>
<td style="text-align:left;">
NER\_text
</td>
<td style="text-align:left;">
Text stating a named entity recognized by the NER algorithm
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
Start\_Pos
</td>
<td style="text-align:left;">
Initial character position within the tweet of the NER\_text
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
End\_Pos
</td>
<td style="text-align:left;">
End character position within the tweet of the NER\_text
</td>
</tr>
<tr>
<td style="text-align:left;">
</td>
<td style="text-align:left;">
NER\_Label Prob
</td>
<td style="text-align:left;">
Label and probability of the named entity recognized by the NER
algorithm
</td>
</tr>
</tbody>
</table>

For more information visit: [Twitter
API](https://developer.twitter.com/en/docs) and the [Documentation for
API
Tweet-object](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview/tweet-object)

Data Statistics
===============

General Statistics
------------------

As of 12/31/2021:

Total Number of tweets: **2,497,294,716**

Average daily number of tweets: **145,831**

<table class="table table" style="margin-left: auto; margin-right: auto; font-size: 12px; margin-left: auto; margin-right: auto;">
<caption style="font-size: initial !important;">
Summary Statistics per Month
</caption>
<thead>
<tr>
<th style="text-align:right;font-weight: bold;">
Year
</th>
<th style="text-align:left;font-weight: bold;">
Month
</th>
<th style="text-align:left;font-weight: bold;">
Daily Avg. Original
</th>
<th style="text-align:left;font-weight: bold;">
Daily Avg. Retweets
</th>
<th style="text-align:left;font-weight: bold;">
Daily Avg. Tweets
</th>
<th style="text-align:left;font-weight: bold;">
Total of Orignal
</th>
<th style="text-align:left;font-weight: bold;">
Total of Retweets
</th>
<th style="text-align:left;font-weight: bold;">
Total of Tweets
</th>
<th style="text-align:left;font-weight: bold;">
Total with Geolocation
</th>
<th style="text-align:left;font-weight: bold;">
Max No. Retweets
</th>
<th style="text-align:left;font-weight: bold;">
Max No. Likes
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:right;">
2020
</td>
<td style="text-align:left;">
1
</td>
<td style="text-align:left;">
5,947
</td>
<td style="text-align:left;">
30,576
</td>
<td style="text-align:left;">
35,501
</td>
<td style="text-align:left;">
1,958,346
</td>
<td style="text-align:left;">
7,852,504
</td>
<td style="text-align:left;">
9,810,850
</td>
<td style="text-align:left;">
1,773
</td>
<td style="text-align:left;">
674,151
</td>
<td style="text-align:left;">
334,802
</td>
</tr>
<tr>
<td style="text-align:right;">
2020
</td>
<td style="text-align:left;">
2
</td>
<td style="text-align:left;">
10,978
</td>
<td style="text-align:left;">
29,918
</td>
<td style="text-align:left;">
40,604
</td>
<td style="text-align:left;">
7,624,648
</td>
<td style="text-align:left;">
21,944,443
</td>
<td style="text-align:left;">
29,568,948
</td>
<td style="text-align:left;">
8,103
</td>
<td style="text-align:left;">
469,739
</td>
<td style="text-align:left;">
637,589
</td>
</tr>
<tr>
<td style="text-align:right;">
2020
</td>
<td style="text-align:left;">
3
</td>
<td style="text-align:left;">
13,095
</td>
<td style="text-align:left;">
44,714
</td>
<td style="text-align:left;">
56,283
</td>
<td style="text-align:left;">
12,610,824
</td>
<td style="text-align:left;">
46,659,589
</td>
<td style="text-align:left;">
59,270,412
</td>
<td style="text-align:left;">
19,952
</td>
<td style="text-align:left;">
1,064,693
</td>
<td style="text-align:left;">
1,255,858
</td>
</tr>
<tr>
<td style="text-align:right;">
2020
</td>
<td style="text-align:left;">
4
</td>
<td style="text-align:left;">
30,091
</td>
<td style="text-align:left;">
89,513
</td>
<td style="text-align:left;">
119,859
</td>
<td style="text-align:left;">
20,591,357
</td>
<td style="text-align:left;">
60,301,889
</td>
<td style="text-align:left;">
80,893,244
</td>
<td style="text-align:left;">
38,213
</td>
<td style="text-align:left;">
649,823
</td>
<td style="text-align:left;">
662,005
</td>
</tr>
<tr>
<td style="text-align:right;">
2020
</td>
<td style="text-align:left;">
5
</td>
<td style="text-align:left;">
35,163
</td>
<td style="text-align:left;">
99,928
</td>
<td style="text-align:left;">
135,709
</td>
<td style="text-align:left;">
26,258,213
</td>
<td style="text-align:left;">
73,618,083
</td>
<td style="text-align:left;">
99,876,289
</td>
<td style="text-align:left;">
47,684
</td>
<td style="text-align:left;">
1,007,616
</td>
<td style="text-align:left;">
929,811
</td>
</tr>
<tr>
<td style="text-align:right;">
2020
</td>
<td style="text-align:left;">
6
</td>
<td style="text-align:left;">
51,033
</td>
<td style="text-align:left;">
142,569
</td>
<td style="text-align:left;">
193,096
</td>
<td style="text-align:left;">
34,786,076
</td>
<td style="text-align:left;">
95,171,388
</td>
<td style="text-align:left;">
129,957,461
</td>
<td style="text-align:left;">
58,138
</td>
<td style="text-align:left;">
790,652
</td>
<td style="text-align:left;">
882,693
</td>
</tr>
<tr>
<td style="text-align:right;">
2020
</td>
<td style="text-align:left;">
7
</td>
<td style="text-align:left;">
53,720
</td>
<td style="text-align:left;">
155,042
</td>
<td style="text-align:left;">
209,738
</td>
<td style="text-align:left;">
39,611,015
</td>
<td style="text-align:left;">
111,876,344
</td>
<td style="text-align:left;">
151,487,359
</td>
<td style="text-align:left;">
56,808
</td>
<td style="text-align:left;">
615,768
</td>
<td style="text-align:left;">
1,287,117
</td>
</tr>
<tr>
<td style="text-align:right;">
2020
</td>
<td style="text-align:left;">
8
</td>
<td style="text-align:left;">
51,330
</td>
<td style="text-align:left;">
143,291
</td>
<td style="text-align:left;">
195,037
</td>
<td style="text-align:left;">
37,549,475
</td>
<td style="text-align:left;">
102,834,375
</td>
<td style="text-align:left;">
140,383,850
</td>
<td style="text-align:left;">
55,912
</td>
<td style="text-align:left;">
2,183,434
</td>
<td style="text-align:left;">
860,162
</td>
</tr>
<tr>
<td style="text-align:right;">
2020
</td>
<td style="text-align:left;">
9
</td>
<td style="text-align:left;">
50,068
</td>
<td style="text-align:left;">
132,040
</td>
<td style="text-align:left;">
182,947
</td>
<td style="text-align:left;">
35,861,979
</td>
<td style="text-align:left;">
92,957,247
</td>
<td style="text-align:left;">
128,819,226
</td>
<td style="text-align:left;">
32,381
</td>
<td style="text-align:left;">
1,925,489
</td>
<td style="text-align:left;">
839,689
</td>
</tr>
<tr>
<td style="text-align:right;">
2020
</td>
<td style="text-align:left;">
10
</td>
<td style="text-align:left;">
54,489
</td>
<td style="text-align:left;">
137,225
</td>
<td style="text-align:left;">
198,708
</td>
<td style="text-align:left;">
41,062,885
</td>
<td style="text-align:left;">
104,195,279
</td>
<td style="text-align:left;">
144,962,625
</td>
<td style="text-align:left;">
319,101
</td>
<td style="text-align:left;">
946,810
</td>
<td style="text-align:left;">
785,385
</td>
</tr>
<tr>
<td style="text-align:right;">
2020
</td>
<td style="text-align:left;">
11
</td>
<td style="text-align:left;">
64,125
</td>
<td style="text-align:left;">
111,686
</td>
<td style="text-align:left;">
177,062
</td>
<td style="text-align:left;">
45,096,171
</td>
<td style="text-align:left;">
77,885,575
</td>
<td style="text-align:left;">
122,981,746
</td>
<td style="text-align:left;">
26,488
</td>
<td style="text-align:left;">
1,187,438
</td>
<td style="text-align:left;">
619,643
</td>
</tr>
<tr>
<td style="text-align:right;">
2020
</td>
<td style="text-align:left;">
12
</td>
<td style="text-align:left;">
64,840
</td>
<td style="text-align:left;">
121,149
</td>
<td style="text-align:left;">
186,852
</td>
<td style="text-align:left;">
49,065,436
</td>
<td style="text-align:left;">
87,366,002
</td>
<td style="text-align:left;">
133,179,589
</td>
<td style="text-align:left;">
3,277,244
</td>
<td style="text-align:left;">
1,402,911
</td>
<td style="text-align:left;">
1,038,164
</td>
</tr>
<tr>
<td style="text-align:right;">
2021
</td>
<td style="text-align:left;">
1
</td>
<td style="text-align:left;">
58,225
</td>
<td style="text-align:left;">
134,387
</td>
<td style="text-align:left;">
192,272
</td>
<td style="text-align:left;">
40,878,618
</td>
<td style="text-align:left;">
92,341,359
</td>
<td style="text-align:left;">
133,219,977
</td>
<td style="text-align:left;">
24,293
</td>
<td style="text-align:left;">
1,437,164
</td>
<td style="text-align:left;">
867,275
</td>
</tr>
<tr>
<td style="text-align:right;">
2021
</td>
<td style="text-align:left;">
2
</td>
<td style="text-align:left;">
47,789
</td>
<td style="text-align:left;">
104,467
</td>
<td style="text-align:left;">
152,780
</td>
<td style="text-align:left;">
30,916,912
</td>
<td style="text-align:left;">
65,130,838
</td>
<td style="text-align:left;">
96,047,732
</td>
<td style="text-align:left;">
23,977
</td>
<td style="text-align:left;">
971,119
</td>
<td style="text-align:left;">
644,697
</td>
</tr>
<tr>
<td style="text-align:right;">
2021
</td>
<td style="text-align:left;">
3
</td>
<td style="text-align:left;">
51,889
</td>
<td style="text-align:left;">
117,776
</td>
<td style="text-align:left;">
168,768
</td>
<td style="text-align:left;">
37,803,773
</td>
<td style="text-align:left;">
83,103,448
</td>
<td style="text-align:left;">
120,907,221
</td>
<td style="text-align:left;">
28,788
</td>
<td style="text-align:left;">
1,083,628
</td>
<td style="text-align:left;">
599,385
</td>
</tr>
<tr>
<td style="text-align:right;">
2021
</td>
<td style="text-align:left;">
4
</td>
<td style="text-align:left;">
47,350
</td>
<td style="text-align:left;">
128,902
</td>
<td style="text-align:left;">
176,534
</td>
<td style="text-align:left;">
34,252,762
</td>
<td style="text-align:left;">
90,730,535
</td>
<td style="text-align:left;">
124,983,296
</td>
<td style="text-align:left;">
24,117
</td>
<td style="text-align:left;">
1,111,306
</td>
<td style="text-align:left;">
653,537
</td>
</tr>
<tr>
<td style="text-align:right;">
2021
</td>
<td style="text-align:left;">
5
</td>
<td style="text-align:left;">
45,779
</td>
<td style="text-align:left;">
120,864
</td>
<td style="text-align:left;">
166,235
</td>
<td style="text-align:left;">
34,427,222
</td>
<td style="text-align:left;">
89,269,622
</td>
<td style="text-align:left;">
123,696,843
</td>
<td style="text-align:left;">
22,669
</td>
<td style="text-align:left;">
3,194,460
</td>
<td style="text-align:left;">
697,980
</td>
</tr>
<tr>
<td style="text-align:right;">
2021
</td>
<td style="text-align:left;">
6
</td>
<td style="text-align:left;">
37,931
</td>
<td style="text-align:left;">
84,426
</td>
<td style="text-align:left;">
122,204
</td>
<td style="text-align:left;">
28,310,536
</td>
<td style="text-align:left;">
63,462,978
</td>
<td style="text-align:left;">
91,773,014
</td>
<td style="text-align:left;">
17,693
</td>
<td style="text-align:left;">
824,584
</td>
<td style="text-align:left;">
413,875
</td>
</tr>
<tr>
<td style="text-align:right;">
2021
</td>
<td style="text-align:left;">
7
</td>
<td style="text-align:left;">
47,221
</td>
<td style="text-align:left;">
107,089
</td>
<td style="text-align:left;">
155,522
</td>
<td style="text-align:left;">
35,904,375
</td>
<td style="text-align:left;">
79,718,595
</td>
<td style="text-align:left;">
115,621,765
</td>
<td style="text-align:left;">
16,713
</td>
<td style="text-align:left;">
1,108,703
</td>
<td style="text-align:left;">
633,347
</td>
</tr>
<tr>
<td style="text-align:right;">
2021
</td>
<td style="text-align:left;">
8
</td>
<td style="text-align:left;">
47,626
</td>
<td style="text-align:left;">
109,563
</td>
<td style="text-align:left;">
157,721
</td>
<td style="text-align:left;">
35,681,168
</td>
<td style="text-align:left;">
81,535,924
</td>
<td style="text-align:left;">
117,217,091
</td>
<td style="text-align:left;">
13,943
</td>
<td style="text-align:left;">
1,271,696
</td>
<td style="text-align:left;">
732,266
</td>
</tr>
<tr>
<td style="text-align:right;">
2021
</td>
<td style="text-align:left;">
9
</td>
<td style="text-align:left;">
39,218
</td>
<td style="text-align:left;">
87,191
</td>
<td style="text-align:left;">
126,668
</td>
<td style="text-align:left;">
29,197,317
</td>
<td style="text-align:left;">
63,649,539
</td>
<td style="text-align:left;">
92,846,856
</td>
<td style="text-align:left;">
11,824
</td>
<td style="text-align:left;">
1,107,188
</td>
<td style="text-align:left;">
378,328
</td>
</tr>
<tr>
<td style="text-align:right;">
2021
</td>
<td style="text-align:left;">
10
</td>
<td style="text-align:left;">
26,842
</td>
<td style="text-align:left;">
57,674
</td>
<td style="text-align:left;">
84,225
</td>
<td style="text-align:left;">
19,285,745
</td>
<td style="text-align:left;">
40,307,175
</td>
<td style="text-align:left;">
59,592,920
</td>
<td style="text-align:left;">
9,102
</td>
<td style="text-align:left;">
785,621
</td>
<td style="text-align:left;">
611,358
</td>
</tr>
<tr>
<td style="text-align:right;">
2021
</td>
<td style="text-align:left;">
11
</td>
<td style="text-align:left;">
34,121
</td>
<td style="text-align:left;">
71,347
</td>
<td style="text-align:left;">
105,270
</td>
<td style="text-align:left;">
25,501,791
</td>
<td style="text-align:left;">
52,456,045
</td>
<td style="text-align:left;">
77,957,836
</td>
<td style="text-align:left;">
12,826
</td>
<td style="text-align:left;">
922,430
</td>
<td style="text-align:left;">
493,516
</td>
</tr>
<tr>
<td style="text-align:right;">
2021
</td>
<td style="text-align:left;">
12
</td>
<td style="text-align:left;">
50,803
</td>
<td style="text-align:left;">
111,712
</td>
<td style="text-align:left;">
160,360
</td>
<td style="text-align:left;">
36,715,840
</td>
<td style="text-align:left;">
77,993,852
</td>
<td style="text-align:left;">
112,238,566
</td>
<td style="text-align:left;">
2,499,610
</td>
<td style="text-align:left;">
2,120,230
</td>
<td style="text-align:left;">
708,690
</td>
</tr>
</tbody>
</table>

![](https://github.com/lopezbec/COVID19_Tweets_Dataset/blob/main/Summary_Details/Tweets%20per%20Day.png)

There is a total of 6,647,352 tweets with geolocation information, which
are shown on a map below:

![](https://github.com/lopezbec/COVID19_Tweets_Dataset/blob/main/Summary_Details/GeoTweets.png)

Language Statistics
-------------------

<table class="table table" style="margin-left: auto; margin-right: auto; font-size: 12px; margin-left: auto; margin-right: auto;">
<caption style="font-size: initial !important;">
Tweets Language Summary
</caption>
<thead>
<tr>
<th style="text-align:left;font-weight: bold;">
Languages
</th>
<th style="text-align:left;font-weight: bold;">
Total No. Tweets
</th>
<th style="text-align:right;font-weight: bold;">
Percentage of Tweets
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
English
</td>
<td style="text-align:left;">
1,617,146,501
</td>
<td style="text-align:right;">
64.91
</td>
</tr>
<tr>
<td style="text-align:left;">
Spanish; Castilian
</td>
<td style="text-align:left;">
296,690,430
</td>
<td style="text-align:right;">
11.91
</td>
</tr>
<tr>
<td style="text-align:left;">
Portuguese
</td>
<td style="text-align:left;">
104,303,870
</td>
<td style="text-align:right;">
4.19
</td>
</tr>
<tr>
<td style="text-align:left;">
French
</td>
<td style="text-align:left;">
81,247,218
</td>
<td style="text-align:right;">
3.26
</td>
</tr>
<tr>
<td style="text-align:left;">
Bahasa
</td>
<td style="text-align:left;">
74,369,368
</td>
<td style="text-align:right;">
2.99
</td>
</tr>
<tr>
<td style="text-align:left;">
Others
</td>
<td style="text-align:left;">
317,516,933
</td>
<td style="text-align:right;">
12.75
</td>
</tr>
</tbody>
</table>

![](https://github.com/lopezbec/COVID19_Tweets_Dataset/blob/main/Summary_Details/Tweets%20by%20Language%20Line%20plot.png)

English Sentiment Analaysis
---------------------------

The sentiment of all the English tweets was estimated using a
state-or-the-art Twitter Sentiment algorithm
[BB\_twtr](https://arxiv.org/abs/1704.06125). [(See code
here)](https://github.com/leelaylay/TweetSemEval) .

![](https://github.com/lopezbec/COVID19_Tweets_Dataset/blob/main/Summary_Sentiment/Tweets%20Sentiment.png)

![](https://github.com/lopezbec/COVID19_Tweets_Dataset/blob/main/Summary_Sentiment/Tweets%20Sentiment%20Percentage.png)

English Named Entity Recognition, Mentions, and Hashtags
--------------------------------------------------------

The Named Entity Recognition algorithm of
[flairNLP](https://github.com/flairNLP/flair) was used to extract topics
of conversation about PERSON, LOCATION, ORGANIZATION, and others. Below
are the top 5 NER, Mentions (@) and Hastags (\#)

<table class="table table" style="margin-left: auto; margin-right: auto; font-size: 12px; margin-left: auto; margin-right: auto;">
<caption style="font-size: initial !important;">
Top 5 Mentions, Hashtags, and NER
</caption>
<thead>
<tr>
<th style="text-align:left;font-weight: bold;">
Mentions
</th>
<th style="text-align:left;font-weight: bold;">
Hashtags
</th>
<th style="text-align:left;font-weight: bold;">
NER Person
</th>
<th style="text-align:left;font-weight: bold;">
NER Location
</th>
<th style="text-align:left;font-weight: bold;">
NER Organization
</th>
<th style="text-align:left;font-weight: bold;">
NER Miscellaneous
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
@realDonaldTrump
</td>
<td style="text-align:left;">
\#covid19
</td>
<td style="text-align:left;">
covid
</td>
<td style="text-align:left;">
us
</td>
<td style="text-align:left;">
cdc
</td>
<td style="text-align:left;">
covid
</td>
</tr>
<tr>
<td style="text-align:left;">
14,106,218
</td>
<td style="text-align:left;">
127,743,107
</td>
<td style="text-align:left;">
12,908,264
</td>
<td style="text-align:left;">
14,395,901
</td>
<td style="text-align:left;">
12,150,440
</td>
<td style="text-align:left;">
21,363,481
</td>
</tr>
<tr>
<td style="text-align:left;">
@realdonaldtrump
</td>
<td style="text-align:left;">
\#coronavirus
</td>
<td style="text-align:left;">
biden
</td>
<td style="text-align:left;">
uk
</td>
<td style="text-align:left;">
covid
</td>
<td style="text-align:left;">
covid-19
</td>
</tr>
<tr>
<td style="text-align:left;">
7,159,966
</td>
<td style="text-align:left;">
43,902,064
</td>
<td style="text-align:left;">
11,060,219
</td>
<td style="text-align:left;">
11,669,435
</td>
<td style="text-align:left;">
9,875,511
</td>
<td style="text-align:left;">
20,260,487
</td>
</tr>
<tr>
<td style="text-align:left;">
@mippcivzla
</td>
<td style="text-align:left;">
\#covid
</td>
<td style="text-align:left;">
trump
</td>
<td style="text-align:left;">
india
</td>
<td style="text-align:left;">
pfizer
</td>
<td style="text-align:left;">
americans
</td>
</tr>
<tr>
<td style="text-align:left;">
4,217,090
</td>
<td style="text-align:left;">
16,348,619
</td>
<td style="text-align:left;">
5,904,393
</td>
<td style="text-align:left;">
11,289,600
</td>
<td style="text-align:left;">
3,856,722
</td>
<td style="text-align:left;">
6,741,840
</td>
</tr>
<tr>
<td style="text-align:left;">
@joebiden
</td>
<td style="text-align:left;">
\#whatshappeninginmyanmar
</td>
<td style="text-align:left;">
fauci
</td>
<td style="text-align:left;">
china
</td>
<td style="text-align:left;">
omicron
</td>
<td style="text-align:left;">
covid19
</td>
</tr>
<tr>
<td style="text-align:left;">
3,486,876
</td>
<td style="text-align:left;">
3,552,497
</td>
<td style="text-align:left;">
3,197,458
</td>
<td style="text-align:left;">
5,206,687
</td>
<td style="text-align:left;">
2,158,951
</td>
<td style="text-align:left;">
5,753,622
</td>
</tr>
<tr>
<td style="text-align:left;">
@narendramodi
</td>
<td style="text-align:left;">
\#covid\<u+30fc\>19
</td>
<td style="text-align:left;">
joe biden
</td>
<td style="text-align:left;">
covid
</td>
<td style="text-align:left;">
fda
</td>
<td style="text-align:left;">
republicans
</td>
</tr>
<tr>
<td style="text-align:left;">
3,232,193
</td>
<td style="text-align:left;">
2,252,353
</td>
<td style="text-align:left;">
1,111,640
</td>
<td style="text-align:left;">
4,989,840
</td>
<td style="text-align:left;">
1,733,394
</td>
<td style="text-align:left;">
1,792,146
</td>
</tr>
</tbody>
</table>

Spanish Sentiment Analaysis
---------------------------

The sentiment of all the Spanish tweets was estimated using sentiment
analysis in spanish based on neural networks model of the the python
library [sentiment-analysis-spanish
0.0.25](https://pypi.org/project/sentiment-analysis-spanish/).

![](https://github.com/lopezbec/COVID19_Tweets_Dataset/blob/main/Summary_Sentiment_ES/Tweets%20Sentiment%20ES.png)

![](https://github.com/lopezbec/COVID19_Tweets_Dataset/blob/main/Summary_Sentiment_ES/Tweets%20Sentiment%20Percentage%20ES.png)

Spanish Named Entity Recognition
--------------------------------

The Spanish Named Entity Recognition algorithm of
[flairNLP](https://github.com/flairNLP/flair) was used to extract topics
of conversation about PERSON, LOCATION, ORGANIZATION, and others. Below
are the top 5 NER of all the Spanish tweets (\* some special character
in Spanish are not correctly represented in the readme file, like
character with accent mark)

<table class="table table" style="margin-left: auto; margin-right: auto; font-size: 12px; margin-left: auto; margin-right: auto;">
<caption style="font-size: initial !important;">
Top 5 Mentions, Hashtags, and NER
</caption>
<thead>
<tr>
<th style="text-align:left;font-weight: bold;">
NER Person
</th>
<th style="text-align:left;font-weight: bold;">
NER Location
</th>
<th style="text-align:left;font-weight: bold;">
NER Organization
</th>
<th style="text-align:left;font-weight: bold;">
NER Miscellaneous
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
covid
</td>
<td style="text-align:left;">
venezuela
</td>
<td style="text-align:left;">
mippcivzla
</td>
<td style="text-align:left;">
covid-19
</td>
</tr>
<tr>
<td style="text-align:left;">
3,435,740
</td>
<td style="text-align:left;">
3,484,718
</td>
<td style="text-align:left;">
3,255,403
</td>
<td style="text-align:left;">
21,059,216
</td>
</tr>
<tr>
<td style="text-align:left;">
nicolasmaduro
</td>
<td style="text-align:left;">
mÃ©xico
</td>
<td style="text-align:left;">
vtvcanal8
</td>
<td style="text-align:left;">
covid
</td>
</tr>
<tr>
<td style="text-align:left;">
1,936,533
</td>
<td style="text-align:left;">
2,814,077
</td>
<td style="text-align:left;">
1,877,732
</td>
<td style="text-align:left;">
13,937,466
</td>
</tr>
<tr>
<td style="text-align:left;">
mippcivzla
</td>
<td style="text-align:left;">
espaÃ±a
</td>
<td style="text-align:left;">
covid
</td>
<td style="text-align:left;">
covid19
</td>
</tr>
<tr>
<td style="text-align:left;">
1,077,693
</td>
<td style="text-align:left;">
1,323,803
</td>
<td style="text-align:left;">
1,466,091
</td>
<td style="text-align:left;">
12,253,204
</td>
</tr>
<tr>
<td style="text-align:left;">
lopezobrador
</td>
<td style="text-align:left;">
cuba
</td>
<td style="text-align:left;">
gobierno
</td>
<td style="text-align:left;">
coronavirus
</td>
</tr>
<tr>
<td style="text-align:left;">
280,120
</td>
<td style="text-align:left;">
867,503
</td>
<td style="text-align:left;">
679,713
</td>
<td style="text-align:left;">
3,324,150
</td>
</tr>
<tr>
<td style="text-align:left;">
amlo
</td>
<td style="text-align:left;">
argentina
</td>
<td style="text-align:left;">
oms
</td>
<td style="text-align:left;">
delta
</td>
</tr>
<tr>
<td style="text-align:left;">
117,502
</td>
<td style="text-align:left;">
572,376
</td>
<td style="text-align:left;">
624,907
</td>
<td style="text-align:left;">
297,178
</td>
</tr>
</tbody>
</table>

Data Collection Process Inconsistencies
---------------------------------------

Only tweets in English were collected from 22 January to 31 January
2020, after this time the algorithm collected tweets in all languages.
There are also some known gaps of data shown below:

<table class="table table" style="margin-left: auto; margin-right: auto; font-size: 12px; margin-left: auto; margin-right: auto;">
<caption style="font-size: initial !important;">
Known gaps
</caption>
<thead>
<tr>
<th style="text-align:left;font-weight: bold;">
Date
</th>
<th style="text-align:left;font-weight: bold;">
Time
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
2020-08-06
</td>
<td style="text-align:left;">
07:00 UTC
</td>
</tr>
<tr>
<td style="text-align:left;">
2020-08-08
</td>
<td style="text-align:left;">
07:00 UTC
</td>
</tr>
<tr>
<td style="text-align:left;">
2020-08-09
</td>
<td style="text-align:left;">
07:00 UTC
</td>
</tr>
<tr>
<td style="text-align:left;">
2020-08-14
</td>
<td style="text-align:left;">
07:00 UTC
</td>
</tr>
<tr>
<td style="text-align:left;">
2021-05-06
</td>
<td style="text-align:left;">
16:00 UTC
</td>
</tr>
</tbody>
</table>

Hydrating Tweets
================

Using our TWARC Notebook
------------------------

The notebook
[Automatically\_Hydrate\_TweetsIDs\_COVID190\_v2.ipynb](https://github.com/lopezbec/COVID19_Tweets_Dataset/blob/main/Automatically_Hydrate_TweetsIDs_COVID19_v2.ipynb)
will allow you to automatically hydrate the tweets-ID from our
[COVID19\_Tweets\_dataset GitHub
repository](https://github.com/lopezbec/COVID19_Tweets_Dataset).

You can run this notebook directly on the cloud using Google Colab [(see
how to
tutorials)](https://colab.research.google.com/notebooks/welcome.ipynb#scrollTo=xitplqMNk_Hc)
and Google Drive.

In order to hydrate the tweet-IDs using
[TWARC](https://github.com/DocNow/twarc) you need to create a [Twitter
Developer Account](https://developer.twitter.com/en/apply-for-access).

The Twitter API’s rate limits pose an issue to fetch data from
tweed-IDs. So, we recommended using Hydrator to convert the list of
tweed-IDs, into a CSV file containing all data and meta-data relating to
the tweets. Hydrator also manages Twitter API Rate Limits for you.

For those who prefer a command-line interface over a GUI, we recommend
using Twarc.

### Using Hydrator

Follow the instructions on the [Hydrator github
repository](https://github.com/DocNow/hydrator).

### Using Twarc

Follow the instructions on the [Twarc github
repository](https://github.com/DocNow/twarc).

Inquiries & Requests
====================

If you would like to filter the tweets’ ID based on some metadata not
provided on the repo (e.g., geolocation), if you would like to run some
additional analyses on the full tweet text data (e.g., sentiment
analysis using another language model, topic modeling, etc.), or if you
have any questions about the dataset, please contact Dr. Christian Lopez
at
**<a href="mailto:lopezbec@lafayette.edu" class="email">lopezbec@lafayette.edu</a>**

Existing filters performed are located in ‘Tweets\_ID\_Filter\_requests’
directory

Licensing
=========

This dataset is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International Public License
([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)).
By using this dataset, you agree to abide by the stipulations in the
license, remain in compliance with Twitter’s [Terms of
Service](https://developer.twitter.com/en/developer-terms/agreement-and-policy),
and cite the following manuscript:

Christian Lopez, and Caleb Gallemore (2020) An Augmented Multilingual
Twitter Dataset for Studying the COVID-19 Infodemic. DOI:
10.21203/rs.3.rs-95721/v1
<a href="https://www.researchsquare.com/article/rs-95721/v1" class="uri">https://www.researchsquare.com/article/rs-95721/v1</a>

References
==========

<a name="chen"></a> Emily Chen, Kristina Lerman, and Emilio Ferrara.
2020. \#COVID-19: The First Public Coronavirus Twitter Dataset.
arXiv:cs.SI/2003.07372, 2020

<a href="https://github.com/echen102/COVID-19-TweetIDs" class="uri">https://github.com/echen102/COVID-19-TweetIDs</a>
