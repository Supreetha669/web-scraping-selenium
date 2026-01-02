# Web Scraping & Crawling Project (Python + Selenium)

This project demonstrates end-to-end **web scraping and automation** using Python.  
It covers **static scraping, dynamic scraping with Selenium, clean project structure, GitHub version control, and local automation (VPS-like setup)**.

---

##  Project Overview

In this project, I built a Python-based scraping framework that can:
- Scrape **static websites** using Requests & BeautifulSoup
- Scrape **dynamic websites** using Selenium
- Handle **pagination, scrolling, and button clicks**
- Run Selenium in **headless mode**
- Export data to **CSV files**
- Follow **clean, modular project structure**
- Be **automated locally** similar to a VPS using Task Scheduler
- Be version-controlled and published on **GitHub**

---

##  Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- Selenium
- WebDriverWait
- Headless Chrome
- CSV module
- Git & GitHub
- Windows Task Scheduler (for automation)

---

##  Project Structure
web-scraping-selenium/
│
├── src/
│ ├── crawler/
│ │ └── selenium_crawler.py
│ ├── scraper/
│ │ └── job_scraper.py
│ ├── utils/
│ │ ├── csv_writer.py
│ │ └── driver_factory.py
│
├── data/
│ └── .gitkeep
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore


Note:
The `data/` folder is intentionally empty on GitHub.  
CSV files are generated locally when the script runs and are excluded using `.gitignore`.

---

# Step-by-Step: What I Did

## 1️ Python Environment Setup
- Installed Python correctly
- Created a virtual environment (`.venv`)
- Installed required libraries using `pip`



## 2️ Static Web Scraping
- Used `requests` to fetch HTML
- Used `BeautifulSoup` to parse pages
- Extracted structured data
- Saved output to CSV



## 3️ Pagination & Crawling
- Identified page URLs with page numbers
- Crawled multiple pages using loops
- Added delays to avoid overloading servers



## 4️ Dynamic Web Scraping with Selenium
- Used Selenium to open real browser
- Handled JavaScript-rendered content
- Implemented:
  - Infinite scrolling
  - Button clicking
  - Dynamic waits using `WebDriverWait`

---

## 5️ Headless Browser Automation
- Ran Chrome in **headless mode**
- Enabled background execution
- Made the scraper server-ready


## 6️ Modular Project Structure
- Separated responsibilities:
  - Crawlers → navigation
  - Scrapers → data extraction
  - Utils → reusable helpers
- Used a single entry point (`main.py`)



## 7️ Logging & Debugging
- Implemented Python logging
- Logged execution steps into `output.log`
- Enabled background execution visibility


## 8️ Git & GitHub Version Control
- Initialized Git repository
- Created proper `.gitignore`
- Excluded:
  - Virtual environment
  - Generated CSV files
- Pushed clean, professional code to GitHub



## 9️ Local Automation (VPS-Like Setup)
Since I didn’t use a paid VPS:
- Ran Selenium in headless mode
- Executed scripts in background
- Automated execution using **Windows Task Scheduler**

## This simulates how scrapers run on a VPS using cron jobs.


##  How to Run the Project

## 1 Clone the repository
```bash
git clone https://github.com/Supreetha669/web-scraping-selenium.git
2️ Create virtual environment
python -m venv .venv
.venv\Scripts\activate

3️ Install dependencies
pip install -r requirements.txt

4️ Run the scraper
python main.py

5️ Output

CSV files will be generated inside the data/ folder

Logs will be written to output.log

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6c3712b7-6eed-401d-b35a-fdf74662c85e" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1ce277b7-a0e4-4dbe-a621-d7c7c8884a73" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4fd3d009-787d-4858-b557-cb3c17e2adf8" />





