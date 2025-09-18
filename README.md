# CodeAlpha_WebScraping
Book Store Web Scraping - CodeAlpha Internship Task

This project is developed as part of the CodeAlpha Data Analytics Internship. The goal of this task is to extract structured book data from a public website using Python-based web scraping techniques.

Project Overview

The website used for scraping is:
🔗 Books to Scrape

This is an open-source practice website that provides book listings with:

Title
Price
Rating
Category (optional enhancement)
The scraper collects this data and stores it in a clean .csv format for further analysis.

Objectives

Learn and apply web scraping techniques.
Extract meaningful information from structured HTML pages.
Store data in a format suitable for data analysis.
Prepare for real-world data collection scenarios.
Tools & Libraries Used

Python
requests – for fetching HTML content
BeautifulSoup – for parsing and extracting HTML elements
pandas – for creating and exporting the dataset
How It Works

The script loops through the first 5 pages of the book store.
It extracts:
Book Title
Price
Star Rating
All the data is saved in a books_scraped_data.csv file.
