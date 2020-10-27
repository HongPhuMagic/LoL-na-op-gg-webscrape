from selenium import webdriver                           # Allows to connect browser
from selenium.webdriver.common.keys import Keys          # Allows us to access common keys like enter and esc
import time
import csv

# Showing the path to the webdrive location
PATH = 'C:\Program Files (x86)\chromedriver.exe'
# driver = webdriver.Chrome(PATH)


def search(driver):  

    game_type = driver.find_elements_by_xpath("//div[@class='GameType']")
    game_results = driver.find_elements_by_xpath("//div[@class='GameResult']")
    game_len = driver.find_elements_by_xpath("//div[@class='GameLength']")
    game_champ = driver.find_elements_by_xpath("//div[@class='ChampionName']")

    game_kill =  driver.find_elements_by_xpath("//div[@class='KDA']/span[1]")
    game_death = driver.find_elements_by_xpath("//span[@class='Death']")
    game_assist = driver.find_elements_by_xpath("//span[@class='Assist']")

    champ_lvl = driver.find_elements_by_xpath("//div[@class='Level']")

    stat = text(game_champ, game_results, game_len, game_type, champ_lvl, game_kill, game_death, game_assist)
    return stat
    


def text(game_champ, game_results, game_len, game_type, champ_lvl, game_kill, game_death, game_assist):

    game_champ = game_champ[7:]
    game_death = game_death[8:]
    game_assist = game_assist[8:]
    game_kill = game_kill[1:]

    for i in range(len(game_champ)):
        
        game_champ[i] = game_champ[i].text
        game_results[i] = game_results[i].text
        game_len[i] = game_len[i].text
        game_type[i] = game_type[i].text
        champ_lvl[i] = champ_lvl[i].text
        game_kill[i] = game_kill[i].text
        game_death[i] = game_death[i].text 
        game_assist[i] = game_assist[i].text

    for j in range(len(champ_lvl)):
        champ_lvl[j] = (champ_lvl[j])[5:]

    return game_champ, game_results, game_len, game_type, champ_lvl, game_kill, game_death, game_assist



def scrape(u1):
    driver = webdriver.Chrome(PATH)
    try:
      
        driver.get("https://na.op.gg/")

        driver.maximize_window()
        
        searching = driver.find_element_by_xpath("//input[@class='summoner-search-form__text']")
        searching.send_keys(u1)
        searching.send_keys(Keys.RETURN)
        time.sleep(1)

        for i in range(5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            link = driver.find_element_by_link_text('Show More')
            link.click()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

        champ, result, length, type, lvl, kill, death, assist = search(driver)

        time.sleep(5)
        driver.quit()

        # Creating the column names for the dataframe
        ro0 = ['Username', 'Champion', 'Results', 'Game_Length', 'Game_Type', 'Champ_lvl', 'Kills', 'Deaths', 'Assists']

        user = []
        for use in range(len(champ)):
            user.append(u1)

        # Creating a CSV file by appending the list I've created
        row = zip(user, champ, result, length, type, lvl, kill, death, assist)
        with open(u1 + '_stat.csv','w', encoding='utf-8', newline='') as csvfile:
            links_writer=csv.writer(csvfile)
            links_writer.writerow(ro0)
            for item in row:
                links_writer.writerow(item)

    except:
        print('Username not found.')
        driver.quit()
        return ('unsuccessful.')

    return ("Successful!")



if __name__ == '__main__':
    # Creating a driver object containing the browser selection and linking it to the webdrive executable  
    driver = webdriver.Chrome(PATH)
    username = str(input())
    scrape(username)

    

