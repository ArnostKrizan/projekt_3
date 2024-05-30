"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Arnošt Križan
email: KrizanA@seznam.cz
discord: arnost0782
"""
import sys
import csv
import os
from bs4 import BeautifulSoup as bs
from requests import get


def main(url_district, file_name):
    """
    This function is executed first when the code is run.
    Executes the functions in the correct order from downloading, processing and writing the data to a CSV file.
    As an optional extra, the function will provide the path to the created file and its size in bits.
    """
    print("WELCOME TO THE APP ELECTION SCRAPER")
    print(f"DATA ARE DOWNLOADING FROM SELECTED URL: {url_district}")
    prefix = "https://volby.cz/pls/ps2017nss/"
    unique_urls = get_unique_links(url_district, prefix)
    response = get(unique_urls[0])
    election_parties = extract_party_names(response)

    town_codes = []
    for url in unique_urls:
        town_codes.extend(extract_codes_from_url(url))

    final_data = scrape_data(unique_urls, town_codes)
    write_to_csv(final_data, file_name, election_parties)

    working_directory = os.getcwd()
    file_path = (working_directory + "/" + file_name)
    print(f"THE DATA WAS DOWNLOADED TO A FILE:\n{file_path}")
    print(f"FILE SIZE:\n{os.path.getsize(file_path)} bytes")


def get_unique_links(url_district, prefix):
    """
    This function downloads and filters the URLs of each town and their codes.
    """
    districts_mix = get(url_district)
    districts_bs = bs(districts_mix.content, "html.parser")
    unique_urls = set()
    for url in districts_bs.find_all("a", href=True):
        if "ps311" in url["href"]:
            full_url = prefix + url["href"]
            unique_urls.add(full_url)
    return list(unique_urls)


def extract_party_names(response):
    """
    This function extracts party names from URL adress
    """
    soup = bs(response.content, "html.parser")
    element_names = soup.find_all('td', class_='overflow_name')
    return [element.get_text(strip=True) for element in element_names]


def extract_codes_from_url(text):
    """
    The function gets codes from URLs.
    This ensures that the codes are correct.
    """
    codes = []
    for i in range(len(text) - 5):
        substring = text[i:i + 6]
        if substring.isdigit():
            codes.append(substring)
    return codes


def clean_text(text):
    """
    This function clears the content from BeautifulSoup for subsequent use in functions.
    """
    return text.strip().replace("\xa0", "").replace("&nbsp;", "")


def find_and_append(soup, headers, data_list):
    """
    This function has been prepared for filtering and appending the required data.
    """
    td = soup.find("td", {"class": "cislo", "headers": headers})
    if td:
        data_list.append(clean_text(td.text))
    else:
        data_list.append("N/A")


def scrape_data(town_urls, town_codes):
    """
    This function downloads, filters and aggregates data into a form usable for the following functions.
    """
    final_data = []
    for index, town_link in enumerate(town_urls):
        towns_data = []
        response = get(town_link)

        if response.status_code == 200:
            soup = bs(response.content, "html.parser")
            town_code = town_codes[index] if index < len(town_codes) else "N/A"
            towns_data.append(town_code)
            town_tag = soup.find('h3', string=lambda x: x and 'Obec:' in x)
            town_name = town_tag.text.split(': ')[1].strip() if town_tag else "N/A"
            towns_data.append(town_name)
            find_and_append(soup, "sa2", towns_data)  # registered data
            find_and_append(soup, "sa3", towns_data)  # enveloped data
            find_and_append(soup, "sa6", towns_data)  # valid data

            for headers in ["t1sa2 t1sb3", "t2sa2 t2sb3"]:
                numbers_td = soup.find_all("td", {"class": "cislo", "headers": headers})
                for cislo_td in numbers_td:
                    towns_data.append(clean_text(cislo_td.text))
            final_data.append(towns_data)
        else:
            print("Error loading page:", response.status_code)
    return final_data


def write_to_csv(final_data, file_name, election_parties):
    """
    This function writes data to a .csv file.
    """
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['code', 'location', 'registered', 'enveloped', 'valid'] + election_parties)
        writer.writerows(final_data)


def validate_arguments(url_district, file_name):
    """
    This function validates putted arguments to run this script.
    If the conditions are not met, the user is notified in terminal.
    """
    url_prefix = "https://volby.cz/pls/ps2017nss/"
    suffix = ".csv"
    if url_district.startswith(url_prefix) and file_name.endswith(suffix):
        return True
    elif file_name.startswith(url_prefix) and url_district.endswith(suffix):
        print("WRONG ORDER OF ARGUMENT/S !.")
        return False
    else:
        print("WRONG FORMATE OF ARGUMENT/S !")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Enter to a Terminal: python scriptname.py <url_district> <file_name>")
        print("url_district must be taken from selected single district (Výběr obce) of URL: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ")
        sys.exit(1)
    url_district = sys.argv[1]
    file_name = sys.argv[2]
    if not validate_arguments(url_district, file_name):
        sys.exit(1)
    main(url_district, file_name)