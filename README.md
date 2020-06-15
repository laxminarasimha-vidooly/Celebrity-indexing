Project Name:   Celebrity indexing

Scope: To grade a celebrity based on various factors and derived metrics collected across platforms and methodologies listed in strategy in order to index them for brand affiliation.

Business Problem:
To grade celebrities based on social presence and audience traction
To suggest a new celebrity to brand for endorsement
To run a comparative analysis of celebrity endorsements

Usability:
Inorder to achieve the above business problem, the system needs to be build such that celebrities are suggested according to the category of a brand and listed based on their grades calculated through various statistics and their performance in social profiles. 

Strategy:
Model needs to be built for indexing celebrities based on their social presence and various other factors contributing to indexing such as audience engagement, sentiment analysis and brand affinity

Platforms considered for collecting relevant stats: Instagram, YouTube, Facebook, Twitter, Tiktok

Celebrity Features considered for calculating social presence:
Profile statistics (Public): Lifetime statistics of different social media handles (followers, following, uploads, views, subscribers, joining date etc.,)
Video level statistics (Public): Engagement (comments, views, likes, shares, video duration etc.,).
Text statistics (Public): video metadata analysis and comments analysis for sentiment
Audience level statistics: audience engagement of celebrity (YouTube), demographics and TG of audience (Audience engagement and recognition through thumbnail/face of user id of audience) 

Metrics considered for celebrity profiling:
Segmentation of the celebrity (broader level) – Categorization of celebrity based on the presence of a celebrity in various industries such as Cinema/Television/Sports/Internet
Language of the celebrity
Geography of the celebrity - Identifying geography based on regional (language) of the celebrity
Region of the audience – region identification of audience based on languages such as South/North/East/West India locations
Engagement of the celebrity (In platforms) – Recent Celebrity engagement in terms of likes, dislikes and  comments across platforms and in global based on post/video frequency and their respective engagement
Demographics of celebrity: Gender, Age of the celebrity, Celebrity features - height, weight, complexion
Content-type of celebrity across platforms – Detailed breakdown of content types posted by celebrities in various platforms of the content type published by celebrity across platforms (Genre of content published by a celebrity)
Historical associations (of brands) Any past affiliations of brands with Celebrity associations of brands in the past are labeled will be labeled
Active Endorsements - Celebrity endorsements of brands currently are labeled of brands by celebrities at present will be identified
The political influence of the celebrity both in the past and present
Brand safe content around celebrity published by the celebrity in the past
Weightage of the upcoming content release of a celebrity - It can be an upcoming movie/ series/ event that gained popularity recently and has weightage towards the index
Celebrity Cross-platform share - the share of celebrity presence across platforms - Celebrity presence across platforms in terms of posts, videos, and static.
Grading of the celebrity – Grading of the celebrity is based on various factors  from social platform presence, celebrity profiling and other derived metrics calculated from these two and these scores are further used to calculate popularity index of celebrity 
Audience metrics:  audience tg and demography is identified with the help of thumbnail/face recognition and with the use of audience engagement tracking.

Methodology:
I. Celebrity:
1.       Fetch the exhaustive list of all celebrities and influencers
2.       Social mapping of celebrities and influencers across platforms
3.       Relevant stats collection through fetching (automated and manual)
4.       Parameters labelling (Genre, TG, Demographics, features etc.,)
5.       Sentiment analysis of comments across platforms (Non UGC)
6.       Metrics calculation and parameters estimation
7.       Data cleaning and feature selection
II. Brands:
1.       Brands identification and exhaustive list preparation
2.       Brands labelling (categorization)
3.       Historical and active analysis of brands with celebrities
III. Brands affinity, celebrity social score and audience score calculation based on statistics 
IV. Modelling and recommendation


Solution:
Model’s output will be the popularity measure of each celebrity industry wise, audience score along with affinity towards brand and overall scoring

Data Quantity Required:
~15000 celebrities were identified (all potential celebrities from movie, tv, sports, social media industries, and influencers). This is not exhaustive and may increase or decrease.

Sources:
Platform wise profile statistics and video statistics fetched through crawling. a limited number of comments are fetched for  sentiment analysis. labelling of various parameters done through manual tagging.  Audience demographics and tg are to be identified with face recognition (gender, tg) and audience engagement

List Of Algorithms used:
Custom recommendation engine with multiple scoring and normalization methodologies

API Endpoints:
Calculated value of celebrity index (popularity and performance) in social media along with affinity score towards industry, audience score and overall ranking of celebrity

QA Strategy:
Testing needs to be done of given celebrities for identification of popularity and performance based on their statistics (Qualitative) 

Input Parameters:
brand category(mandatory): Category of brands for which celebrity indexing required
gender of celebrity (optional)
age group of celebrity(optional)
Language of celebrity (optional)
Audience tg (optional)
Audience demographics(optional)
Audience geographical location(optional)

Output parameters:
Top_celebrities(top 5): celebrities’ suggestion from model
celebrity_score_social: Rank of celebrity for social media popularity(out of 5)
brand _affinity: weightage of celebrity towards selected brand category(out of 5)
Audience scoring: weightage of audience towards respective celebrity
final ranking: overall weighted ranking of celebrity in selected category (0-1)

File description:
celeb_data_clean.ipynb: contains necessary files for cleaning raw input.
Celeb_model: contains feature extraction, score caluclation and ranking.
Modeling: Final rankking for brand category provided.
Celebrity_indexing_part-I (2): Input raw file for scores calculation.
