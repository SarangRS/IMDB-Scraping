# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 00:10:48 2019

@author: Sarang
"""

import requests
import re

from bs4 import BeautifulSoup
page=requests.get("http://www.imdb.com/chart/top")
soup=BeautifulSoup(page.content,'html.parser')
movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]
imdb=[]
for index in range(0, len(movies)):
    # Seperate movie into: 'place', 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"movie_title": movie_title,
            "year": year,
            "place": place,
            "rating": ratings[index],
            "vote": votes[index],
"link": links[index]}
    imdb.append(data)
    
    
for j in range(0,len(links)):
    
    url1=links[j]
    page2=requests.get("https://www.imdb.com/"+url1)
    soup2=BeautifulSoup(page2.content,'html.parser')
#reviewer   
    rev=soup2.find(class_="ratings_wrapper")
    reviewer=rev.find(class_="small").get_text()
#censor_rating    
    C=soup2.find('div',class_="subtext").get_text()
    censor=(''.join(C.split()))
    data=censor.split("|")
    censor_rating=data[0]
#length of movie    
    length_of_movie=data[1]
    G=data[2].split(',')
    try:
        generes1=G[0]
    except:
        generes1='NA'
        
    try:
        generes2=G[1]
    except:
        generes2='NA'
    
    try:
        generes3=G[2]
    except:
        generes3='NA'
    
    try:
        generes4=G[3]
    except:
        generes4='NA'
#year of release 
    try:
        YR=data[3].split('(')
        year_release=YR[0]
    except:
        continue
        
#story summary    
    summary=soup2.find(class_='summary_text').get_text()
    story_summary=(' '.join(summary.split()).replace('.', ''))
#director    
    direc=soup2.find_all('div',class_="credit_summary_item")
    D=(direc[0].get_text()).split(':')
    director=(' '.join(D[1].split()).replace('.', ''))
#writers    
    W=(direc[1].get_text()).split(':')
    writer=(' '.join(W[1].split()).replace('.', ''))
    writers=writer.split(',')
    try:
        writer1=writers[0]
    except:
        writer1='NA'
        
    try:
        writer2=writers[1]
    except:
        writer2='NA'
    
    try:
        writer3=writers[2]
    except:
        writer3='NA'
#stars   
    table=soup2.find('table')
    table_row=table.find_all('tr')
    stars=[c.get_text() for c in table_row[1:6]]
    
    star1=(' '.join(stars[0].split()).replace('.', ''))
    s1=star1.split("  ")
    s1[0]
    
    star2=(' '.join(stars[1].split()).replace('.', ''))
    s2=star2.split("  ")
    s2[0]
    
    star3=(' '.join(stars[2].split()).replace('.', ''))
    s3=star3.split("  ")
    s3[0]
    
    star4=(' '.join(stars[3].split()).replace('.', ''))
    s4=star4.split("  ")
    s4[0]
    
    star5=(' '.join(stars[4].split()).replace('.', ''))
    s5=star5.split("  ")
    s5[0]
    keyword_=[]
#keywords    
    keyword=soup2.find(class_='see-more inline canwrap')
    keywords=keyword.find_all('a')
    count=len(keywords)
    for i in keywords:
        count = count-1;
        if count>0:
            a=i.get_text()
            keyword_.append(a)
#budget    
    budget=soup2.find(id='titleDetails')
    budget0=budget.find_all(class_='txt-block')
    budget1=budget.find_all('h4')
    budget2=[i.get_text() for i in budget1]
    for i in range(len(budget2)) :
        if budget2[i]=='Budget:':
            s=i
    b=budget0[s].get_text()
    bud=(' '.join(b.split()).replace('.', ''))
    a1=bud.split(':')
    a2=a1[1].split('(')
    a2[0]
#usa gross    
    for i in range(len(budget2)) :
        if budget2[i]=='Gross USA:':
            s=i
    gross=budget0[s].get_text()
    USA_gross=(' '.join(gross.split()).replace('.', ''))
    u1=USA_gross.split(':')
    u2=a1[1].split('(')
    u2[0] 
            
#world_wide        
    for i in range(len(budget2)) :
        if budget2[i]=='Cumulative Worldwide Gross:':
            s=i
    cumulative=budget0[s].get_text()
    CWG=(' '.join(cumulative.split()).replace('.', ''))
    e1=CWG.split(':')
    e2=a1[1].split('(')
    e2[0] 
    
    
    for i in range(len(budget2)) :
        if budget2[i]=='Production Co:':
            s=i
    production=budget0[s].get_text()
    P=(' '.join(production.split()).replace('.', ''))
    p1=P.split(':')
    p2=a1[1]
    p2[0:len(a2)-11]
#pandas
    data = {"slno":j,"reviewer": reviewer,
            "censor_rating":censor_rating,
            "length_of_movie": length_of_movie,
            "generes1": generes1,"generes2": generes2,"generes3": generes3,"generes4": generes4,
            " year_release":  year_release," story_summary":  story_summary," director": director,
"writer1": writer1,"writer2": writer2,"writer3": writer3,"star1": star1,"star2": star2,"star3": star3,"star4": star4,"star5": star5,"keyword_":keyword_,"budget":a2[0],"USA Gross":u2[0],"Cumulative World Gross ":e2[0],"Production Co":p2[0:len(a2)-11]}
    imdb.append(data)



    
    


    
  
    
    
    

    
    
    

