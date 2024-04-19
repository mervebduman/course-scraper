import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def scrape_course_data(url):
    # Set up soup
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract course title
    title = soup.find('h1').text if soup.find('h1') else "Title not found"
    
    # Extract course description
    description_element = soup.find(string=re.compile("Course description"))
    description = description_element.find_next('p').text.strip() if description_element and description_element.find_next('p') else "Description not found"
    
    # Extract duration
    duration_element = soup.find('div', class_='group-details-inner').find('div', class_='field--name-extra-field-pll-extra-field-duration')
    duration = duration_element.find('div', class_='field__item').text.strip() if duration_element else "Duration not found"
    
    # Extract time commitment
    time_commitment_element = soup.find(string=re.compile("Time Commitment"))
    time_commitment = time_commitment_element.find_next().text.strip() if time_commitment_element else "Time commitment not found"
    
    # Extract tags (Subject)
    subject_element = soup.find('div', class_='group-details-inner').find('div', class_='field--name-extra-field-pll-extra-field-subject')
    subject = subject_element.find('div', class_='field__item').text.strip() if subject_element else "Subject not found"

    return {
        "Name": title,
        "Duration": duration,
        "Time commitment": time_commitment,
        "Tags": subject,
        "Course description": description,
        "Link": url
    }

def main():
    # List to store each course's data
    courses_data = []

    # Read URLs from the file
    with open("urls.txt", 'r') as file:
        urls = file.readlines()

    # Loop through each URL, strip newline characters and scrape data
    for url in urls:
        url = url.strip()  # Remove any extra newline or spaces
        if url:  # Check if the URL is not empty
            course_data = scrape_course_data(url)
            courses_data.append(course_data)

    # Create a DataFrame
    df = pd.DataFrame(courses_data)

    # Save the DataFrame as csv
    df.to_csv('course_data.csv', index=False)

if __name__ == "__main__":
    main()