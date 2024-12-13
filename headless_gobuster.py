import argparse
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from typing import List, Optional

# Path to the Gecko WebDriver
driver_path = "/usr/local/bin/geckodriver"

def configure_webdriver(headless: bool = True) -> webdriver.Firefox:
    """
    Configures the Selenium WebDriver with the specified options.

    Args:
        headless (bool): If True, runs the WebDriver in headless mode. Defaults to True.

    Returns:
        webdriver.Firefox: Configured Firefox WebDriver instance.
    """
    options = Options()
    if headless:
        options.add_argument("--headless")
    service = Service(executable_path=driver_path)
    driver = webdriver.Firefox(service=service, options=options)
    return driver


def load_wordlist(wordlist_path: str) -> Optional[List[str]]:
    """
    Loads a wordlist from a file and returns it as a list of strings.

    Args:
        wordlist_path (str): Path to the wordlist file.

    Returns:
        Optional[List[str]]: A list of directories from the wordlist, or None if the file is not found.
    """
    try:
        with open(wordlist_path, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Wordlist not found under {wordlist_path}.")
        return None


def check_for_dirs(driver: webdriver.Firefox, base_url: str, directory: str) -> None:
    """
    Checks if a directory exists on a web server by comparing the content of the base URL with the target URL.

    Args:
        driver (webdriver.Firefox): Selenium WebDriver instance.
        base_url (str): The base URL of the web application.
        directory (str): The directory to check for existence.

    Returns:
        None
    """
    full_url = f"{base_url}/{directory}"
    try:
        driver.get(base_url)
        time.sleep(2)  # Allow page to load
        #WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, "status"), "Loaded"))
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        base_content = driver.page_source

        driver.get(full_url)
        time.sleep(2)  # Allow page to load
        #WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, "status"), "Loaded"))
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        full_content = driver.page_source

        if base_content != full_content:
            print(f"[+] Directory found: {directory} --> {full_url}")
            #print(f"Found dir: {full_url}")
    except Exception as e:
        print(f"An error occurred with {full_url}: {str(e)}")


def scan_directories(driver: webdriver.Firefox, base_url: str, directories: List[str]) -> None:
    """
    Iterates through a list of directories and checks each one for existence.

    Args:
        driver (webdriver.Firefox): Selenium WebDriver instance.
        base_url (str): The base URL of the web application.
        directories (List[str]): A list of directories to scan.

    Returns:
        None
    """
    for directory in directories:
        check_for_dirs(driver, base_url, directory)


def main() -> None:
    """
    Main function to orchestrate the scanning of directories on a web application.

    This function parses command-line arguments, configures the WebDriver, loads the wordlist,
    and performs directory scanning using Selenium.

    Args:
        None

    Returns:
        None
    """
    # Parse arguments
    parser = argparse.ArgumentParser(description="My Gobuster version for dynamic web applications")
    parser.add_argument("-u", "--url", type=str, required=True, help="Target URL (e.g., http://127.0.0.1:3000/)")
    parser.add_argument("-w", "--wordlist", type=str, required=True, help="Path to wordlist file")
    args = parser.parse_args()

    url = args.url
    wordlist_path = args.wordlist

    # Configure WebDriver
    driver = configure_webdriver(headless=True)

    try:
        # Load wordlist
        directories = load_wordlist(wordlist_path)
        if directories is None:
            return

        # Scan directories
        scan_directories(driver, url, directories)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
