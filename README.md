# Course Data Scraper

## Overview
This Python script automatically scrapes course information from a list of URLs provided in a text file and saves the data into a CSV file. The scraped information includes the course name, duration, time commitment, tags (subject), course description, and the URL of each course.

The repository contains example input `urls.txt` and output `course_data.csv`.

## Prerequisites
Make sure you have [Python](https://www.python.org/downloads/) and [Poetry](https://python-poetry.org/docs/#installation) installed on your system.

## Installation
1. Clone this repository to your local machine.
2. Install the project dependencies using Poetry:

```
poetry install
```

## Usage
1. Prepare Your URL List: Place all the course URLs you want to scrape in the urls.txt file, each URL on a new line.
2. Activate the Poetry Shell: Run the following command to activate the virtual environment managed by Poetry:

```
poetry shell
```

3. Run the Scraper: Execute the script to scrape the data and save it into a CSV file:

```
python3 course_scraper.py
```

## Features
- Scrapes course details such as title, duration, commitment, subject, and description.
- Outputs data in CSV format for easy use in spreadsheets or data analysis tools.
- Manages Python dependencies and virtual environments with Poetry for easy setup and reproducible builds.

## License
This project is released under the MIT License.

## Author
Merve B. Duman

