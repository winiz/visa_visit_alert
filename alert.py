from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time
from playsound import playsound

# Function to play a sound
def play_alert_sound():
    # Path to your sound file
    sound_file = "siren.wav"
    playsound(sound_file)

# Aug 1 is fly to Portugal date
trip_date = datetime(2024, 7, 25)  # What is the latest appointment you want? 
sessions_token = "https://www.ch-edoc-reservation.admin.ch/#/session?token=XXXXXXXXXXXXXXX" # Obtain this link from the email directly

while True:
    try:
        # Initialize the WebDriver (assuming I have Firefox installed)
        driver = webdriver.Firefox()

        # Open a webpage
        driver.get(sessions_token)

        # Find the button element and click it
        button = driver.find_element(By.ID, "bookingListBtn")
        button.click()


        current_datetime = datetime.now()
        print("Checking Earlist appointment.............", current_datetime)

        # Wait for table to load
        time.sleep(3)

        # Find the content of the cell
        earliest_date_string = driver.find_element(By.XPATH, '//table[@class="mat-table cdk-table"]/tbody/tr[1]/td[1]').text
        earliest_datetime = datetime.strptime(earliest_date_string[4:].strip(), '%d.%m.%Y')  # input: Tu. 01.10.2024
        is_earlier = earliest_datetime < trip_date

        # Print the content of the first row
        print("Earliest appointment is", earliest_datetime)
        print("Is the date earlier than what I want :", is_earlier)

        while is_earlier:
            play_alert_sound()

        print(".........Done Checking Earliest appointment")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        if 'driver' in locals():
            driver.quit()
        time.sleep(30)
