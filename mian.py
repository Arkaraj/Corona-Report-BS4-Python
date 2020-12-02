import pync
import requests
from bs4 import BeautifulSoup
import time
from one import all

#Sources:Google-Covid, my.gov.in
URL = 'https://google.com/covid19-map/?hl=en'
URL2='https://webcache.googleusercontent.com/search?q=cache:https://mohfw.gov.in/'

def main():
    response = requests.get(URL)
    resp = requests.get(URL2)

    soup = BeautifulSoup(response.text, 'html.parser')
    soul = BeautifulSoup(resp.text, 'html.parser')
    All = soup.select('td.l3HOY')  #<td class="uMsnNd HAChlc">979</td>
    Ind_all = soul.select('#site-dashboard strong')
    deaths = soup.select('td.l3HOY')
    #dc=[count['td'] for count in deaths]    #req-->.uMsnNd:nth-child(5)
    note=soup.select('div.pym81b')[3]
    print("NOTE: ")
    print(note.text)
    # l=len(deaths)
    # print(l)
    print('\nThe total no. of infected in the world currently is: ',All[0].text)
    print('The total no. of deaths in the world currently is: ',deaths[3].text)
    y=list(All[0].text)
    k=list(deaths[3].text)
    y=all(y)
    k=all(k)
    #print(k)
    def listToString(s):  
         # initialize an empty string 
        str1 = ""  
        
        # traverse in the string   
        for ele in s:  
            str1 += ele   
        # return string   
        return str1
    print("The no. of pepole infected in India is: ",Ind_all[0].text)
    print("The no. of deaths in India is: ",Ind_all[2].text)
    ch=int(listToString(k))
    vh=int(listToString(y))
    dr=(ch/vh)*100
    dri=(int(Ind_all[2].text)/int(Ind_all[0].text))*100
    print("The death rate of the world is: %.2f" %dr+"%")
    print("The death rate of India is: %.2f"%dri+"%")
    n=200000
    #print(vh) or ch
    if(ch>n):
        pync.notify('The deaths has reached 200000 !!', title="Corona alert") #mac notification by terminal
        print('The deaths has reached ',n,' !!')
if __name__ == '__main__':
    main()
