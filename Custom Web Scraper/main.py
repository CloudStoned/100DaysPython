from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

def setup_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    return driver


def scrape_mostplayed():
    driver = setup_driver()

    try:
        driver.get('https://steamdb.info')
        wait = WebDriverWait(driver,10)

        games_data = []

        rows = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div.body-wrap table tbody tr")
        ))

        for row in rows:
            try:
                game_name = row.find_element(By.CSS_SELECTOR, "td a").text
                current_players = row.find_element(By.CSS_SELECTOR, "td[class='text-right']").text
                peak_24h = row.find_element(By.CSS_SELECTOR, "td[class='text-right']")[1].text


                current_players = int(current_players.replace(',', ''))
                peak_24h = int(peak_24h.replace(',', ''))

                games_data.append([
                    {
                        'Game' :game_name,
                        'Current Players':current_players,
                        '24h Peak': peak_24h
                    }
                ])

            except Exception as e:
                print(f"Error processing row: {e}")
                continue
        
        df = pd.DataFrame(games_data)
        return df
    
    except Exception as e:
        print(f'Error during scrapings: {e}')
        return None

def main():
    df = scrape_mostplayed()

    if df is not None and not df.empty:
        print('\n Most Played Games on Steam')
        print(df)



if __name__ == "__main__":
    main()


