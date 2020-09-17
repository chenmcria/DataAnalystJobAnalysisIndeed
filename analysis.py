
import numpy as np
from collections import Counter
from nltk import word_tokenize
from nltk.corpus import stopwords
import pandas as pd

import matplotlib.pyplot as plt
df = pd.read_csv("dataanalyst.csv", encoding="utf-8")
#print(df.shape)
counts = df.groupby("Company").count()["Title"].sort_values(ascending=False)[:20]

jobs = []
for i in df['Title']:
    jobs.append(i)
#print(jobs)
title_list = ['data analyst', 'business analyst', 'health analyst' 'research analyst',
              'information analyst', 'quantitative analyst', 'social media analyst'
              'operation analyst', 'marketing analyst', 'data scientist', 'research analyst',
              'intelligence analyst', 'database analyst', 'administrator', 'systems analyst']
title_list = np.array(title_list)
def rename(x):
    index = [i in x for i in title_list]
    if sum(index) > 0:
        return title_list[index][0]
    else:
        return x

df['Title'] = df['Title'].str.lower()
df['Title'] = df['Title'].apply(rename)
index = [df["Title"].str.count(i) for i in title_list]
index = np.array(index).sum(axis=0) > 0
df = df[index]
#print(df)
#print(df["Title"].value_counts())
df["Title"].value_counts()[:10].plot.bar(figsize=(12,8),fontsize=7,color="g")
plt.xticks(rotation=45,ha='right')
plt.title("Data Analyst Career Path",fontsize=22)
plt.ylabel("Number of Positions",fontsize=15,rotation=90)
plt.xlabel("Roles",fontsize=5)
plt.show()

#df.insert(2, 'province', provinces)

counts = df.groupby("Location").count()["Title"].sort_values(ascending=False)[:20]
print(counts)
geodf = df.groupby("Location").count()["Title"].to_csv('geo.csv')
print(type(counts))

#counts.index.name = " "
#counts.name = " "
#fig = plt.figure(111)
#ax = fig.add_subplot(111)
#ax.set_title("", fontsize=15)
#counts.plot(kind="pie", cmap=plt.cm.rainbow, autopct="%3.1f%%", fontsize=12)
#plt.show()


stop_words = stopwords.words('english')
def cleanData(desc):
    desc = word_tokenize(desc)
    desc = [word.lower() for word in desc if word.isalpha() and len(word) > 2]
    desc = [word for word in desc if word not in stop_words]
    return desc

tags_df = df["Description"].apply(cleanData)

result = tags_df.apply(Counter).sum().items()
result = sorted(result, key=lambda kv: kv[1],reverse=True)
result_series = pd.Series({k: v for k, v in result})

skills= ["tableau", "looker", "powerpoint", "powerbi", "google sheets", "alteryx",
             "sas","spaa","minitab", "matlab", "vertica", "adobe analytics", "google analytics",
             "unix", "oracle", "hadoop", "spark", "hive", "kafka", "airflow", "cognos", "big query",
         "data mining", "big data",
             ]

qualifications = [ "statistics", "applied statistics", "computer",
             "mathematics", "applied mathematics", "economics", "artificial intelligence",
             "data science", "marketing", "risk management", "operation management", "commerce"]

programming_languages = ["java", "golong", "c++", "python", "r", "sql", "c#", "scala", "javascript",
                         "jsp", ".net", "html", "typescript","go", "github","swift", "mysql"]

must_have_skils = {'analysis', 'visualization', 'statistical programming', 'modelling', 'data collection',
                   "data mining", "machine learning", "presentation", "critical thinking", "data cleaning",
                   "algorithms", "big data", "communication", "problem solving"}



#filter the software used



software_rankings = result_series.filter(items=skills)
sorted_software_rankings = software_rankings.sort_values(ascending=False)
##plot the top softwares used for data analyst
fig = plt.figure(111)
ax = fig.add_subplot(111)
sorted_software_rankings.plot(kind="bar",figsize=(12,8), fontsize=14)
plt.title('Top Softwares Used for Data Analyst',fontsize=15)
plt.xticks(rotation=50,ha='right')
plt.ylabel('Frequency')
plt.show()



#filter the qualification
qualification_rankings = result_series.filter(items=qualifications)
sorted_qualification_rankings = qualification_rankings.sort_values(ascending=False)[:5]
#print(qualification_rankings)
#plot the top qualification for data analyst
sorted_qualification_rankings.index.name = " "
sorted_qualification_rankings.name = " "
sorted_qualification_rankings.plot.pie(figsize=(12,8),startangle=50,autopct='%1.1f%%',fontsize=15)
plt.title("Top Qualifications for Data Analyst",fontsize=25)
centre_circle = plt.Circle((0,0),0.72,color='gray', fc='white',linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')
plt.show()

details = {"roles" :[],
           "qualifications": [],
           "software": [],
           "language": []}
details_df = pd.DataFrame(details)
details_df.to_csv('cleaneddata.csv')


programming_languages_rankings = result_series.filter(items=programming_languages)
sorted_rankings= programming_languages_rankings.sort_values(ascending=False)[:10]
print(software_rankings)
sorted_rankings.index.name = " "
sorted_rankings.name = " "
#print(programming_languages_rankings)
sorted_rankings.plot.pie(cmap=plt.cm.rainbow, autopct="%2.1f%%", figsize=(12,8), fontsize=12,)
plt.xticks(rotation=80,fontsize=15)
plt.title("Programming Language Requirements",fontsize=20)
plt.show()





#filter must have skills
must_have = result_series.filter(items=must_have_skils)
must_have.sort_values(ascending=True).plot(kind='barh',color='y', figsize=(12,8))
plt.title("Must Have Skills for Data Analyst", fontsize=20)
plt.xlabel('Frequency')
plt.show()




new = df["Location"].str.split(",", n = 1, expand = True)
#print(new)
print(new[0].value_counts())
print(new[1])

df["Location"].str.split(",", n = 1, expand = True).value_counts()[:10].plot.bar(figsize=(12,8),fontsize=8,color="g")
plt.xticks(rotation=45,ha='right')
plt.title("Data Analyst Job Distribution in Canada",fontsize=22)
plt.ylabel("Number of Job Postings",fontsize=15,rotation=90)
plt.xlabel("Locations",fontsize=15)
plt.show()

