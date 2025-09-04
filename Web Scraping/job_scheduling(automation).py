import schedule
import time

def job():
    print("Running Scraper..")

schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)

    