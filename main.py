from bs4 import BeautifulSoup
import requests
import csv
from itertools import zip_longest

num = 0 
job_title = []
company = []
location = []
skills = []
links = []

while True:
    try:
        result = requests.get(f'https://wuzzuf.net/search/jobs/?q=python&start={num}')
        src = result.content
        soup = BeautifulSoup(src , 'lxml')
        page_limit =int(soup.find('strong').text)
        if( num > page_limit // 15 ):
            print("Page Ended")
            break


        jobs_list = soup.find_all('div' , {'class': 'css-1gatmva e1v1l3u10'})

        for job_list in jobs_list:
            job_title.append(job_list.find('h2').text.strip())
            company.append(job_list.find('a' , {'class' : 'css-17s97q8'}).text.strip())
            location.append(job_list.find('span' , {'class' : 'css-5wys0k'}).text.strip())
            skills.append(job_list.find('div' , {'class' : 'css-y4udm8'}).text.strip())
            links.append(job_list.find('a' ,{'class' : 'css-o171kl'}).attrs['href'])

        num +=1
        print("Page Switched")

    except:
        print("Error")
        break

file_list = [job_title , company , location , skills, links]
#import to csv
exported = zip_longest(*file_list)
with open('jobs.csv' , 'w') as f:
    wr = csv.writer(f)
    wr.writerow(["Job Title" , "Company Name" , "Location" ,"Skills" ,"Link"])
    wr.writerows(exported)
    print("File Saved!")
