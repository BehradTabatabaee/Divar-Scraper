# Divar Scraper

This project is a web scraper designed to extract advertisement data from the Divar website, which is a popular platform in Iran for people to buy and sell various items, including real estate, vehicles, electronics, and more. The scraper allows you to specify a city and category to scrape ads from and retrieves the ad details such as the title, time of posting, and contact phone number.

## Features

- Select from a list of predefined cities.
- Choose a category to scrape ads from.
- Specify the number of ads to scrape.
- Collects ad details including title, time of posting, and contact phone number (find price and description yourself using the provided link).
- Handles user authentication by prompting for phone number and SMS code.
- Outputs the scraped data to a text file.

## Prerequisites

- Python 3.x
- Google Chrome
- ChromeDriver
- Required Python packages:
  - selenium
  - arabic_reshaper
  - python-bidi

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/divar-scraper.git
    cd divar-scraper
    ```

2. **Install the required packages:**
    ```bash
    pip install selenium arabic_reshaper python-bidi
    ```

3. **Download ChromeDriver:**
    - Ensure you have Google Chrome installed.
    - Download the ChromeDriver that matches your Chrome version from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
    - Extract the downloaded file and place `chromedriver` in a directory included in your system's `PATH`.

## Usage

1. **Run the script:**
    ```bash
    python divar_scraper.py
    ```

2. **Follow the prompts:**
    - Select a city from the displayed list.
    - Choose a category to scrape ads from.
    - Specify the number of ads you want to scrape.
    - Enter your phone number when prompted.
    - Enter the SMS code received on your phone.

3. **Output:**
    - The script will scrape the specified number of ads and save the data to a text file named after the chosen city and the number of scraped ads.

## Example

```bash
Enter The Cities:
1: تهران
2: مشهد
3: کرج
4: شیراز
5: اصفهان
6: اهواز
7: تبریز
8: کرمانشاه
9: قم
10: رشت
2
Select a Category:
1: خرید و فروش وسایل نقلیه
2: خرید و فروش املاک
3: استخدام و کاریابی
4: خدمات
1
How many?
10
Enter your phone number: 9123456789
Enter the sms sent to your phone: 123456
```
## Notes

- The script uses Selenium to interact with the Divar website.
- The script handles dynamic loading of ads by scrolling and clicking the "load more" button as necessary.
- The scraper includes error handling to manage potential issues such as stale elements or network delays.
- Ensure you have a stable internet connection while running the scraper.
