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


def check_for_dirs(driver: webdriver.Firefox, base_url: str, directory: str, main_page_keywords: List[str]) -> None:
    """
    Checks if a directory exists on a web server by examining the page content of the target directory.

    The function navigates to the specified directory's URL and checks the page source for the absence of specific keywords
    that indicate the main page. If none of the main page keywords are found, the directory is assumed to exist.

    Args:
        driver (webdriver.Firefox): Selenium WebDriver instance used to load and interact with pages.
        base_url (str): The base URL of the web application.
        directory (str): The specific directory to check.
        main_page_keywords (List[str]): A list of keywords that indicate the main (landing) page content.

    Returns:
        None
    """
    full_url = f"{base_url}/{directory}"
    try:
        driver.get(full_url)
        time.sleep(2)  # Allow page to load
        #WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, "status"), "Loaded"))
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        full_content = driver.page_source
        #print(f"Full_{directory}: {full_content}")

        if not any(keyword in full_content for keyword in main_page_keywords):
            print(f"[+] Directory found: {directory} --> {full_url}")
        #else:
            #print(f"[-] Directory does not exist: {directory} (Navigated back to main page)")

    except Exception as e:
        print(f"An error occurred with {full_url}: {str(e)}")


def scan_directories(driver: webdriver.Firefox, base_url: str, directories: List[str], main_page_keywords: List[str]) -> None:
    """
    Scans a list of directories on a web server and identifies potential existing directories.

    The function iterates through the list of directories, calling `check_for_dirs` to determine if each directory exists.

    Args:
        driver (webdriver.Firefox): Selenium WebDriver instance used to load pages.
        base_url (str): The base URL of the web application to scan.
        directories (List[str]): A list of directory names to test for existence.
        main_page_keywords (List[str]): A list of keywords that indicate the main (landing) page content.

    Returns:
        None
    """
    try:
        # Iterate through directories and compare base content with full_content
        for directory in directories:
            check_for_dirs(driver, base_url, directory, main_page_keywords)

    except Exception as e:
        print(f"An error occurred while loading base URL: {str(e)}")


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
    parser.add_argument("-k", "--keywords", type=str, required=True, help="Comma-seperated keywords that define the base/main page")
    parser.add_argument("-w", "--wordlist", type=str, required=True, help="Path to wordlist file")
    args = parser.parse_args()

    # Extract arguments
    url = args.url
    wordlist_path = args.wordlist
    
    # Convert keywords to list
    main_page_keywords = args.keywords.split(',')

    # Configure WebDriver
    driver = configure_webdriver(headless=True)

    try:
        # Load wordlist
        directories = load_wordlist(wordlist_path)
        if directories is None:
            return

        # Scan directories
        scan_directories(driver, url, directories, main_page_keywords)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
