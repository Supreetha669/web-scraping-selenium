from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.utils.driver_factory import get_driver
from src.scraper.job_scraper import extract_jobs
from src.utils.csv_writer import save_to_csv

def run_job_scraper():
    driver = get_driver(headless=True)
    driver.get("https://realpython.github.io/fake-jobs/")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "card-content")))

    jobs = driver.find_elements(By.CLASS_NAME, "card-content")
    rows = extract_jobs(jobs)

    save_to_csv(
        "data/jobs.csv",
        ["Title", "Company", "Location", "Link"],
        rows
    )

    driver.quit()
