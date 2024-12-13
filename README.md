# HEADLESS_GOBUSTER

A programm to find directories of dynamic web applications, like OWASP Juice Shop.  
This is a lightweight version of the known <a href="https://github.com/OJ/gobuster">**gobuster**</a> - tool.  

The program was created as part of my training at the Developer Academy and is used exclusively for teaching purposes.  

## Table of Contents
1. <a href="#technologies">Technologies</a>  
2. <a href="#features">Features</a>  
3. <a href="#getting-started">Getting Started</a>  
4. <a href="#usage">Usage</a>  
5. <a href="#additional-notes">Additional Notes</a>  

## Technologies
* **Python** 3.12.2
    * **argparse, time** (modules from standard library)
    * **Selenium** 4.9.0 (module to install, <a href="https://selenium-python.readthedocs.io/">More Information</a>)
        * **GeckoDriver for Firefox browser** v0.35.0 (driver to install, <a href="https://github.com/mozilla/geckodriver">More Information</a>)

## Features
The following table shows which functions **Headless_Gobuster** supports:  

| Flag | Choices | Description | Required |
| ---- | ------- | ----------- | -------- |
| --help |  | Get a list of the available options | no
| -u <br> --url |  | Target URL | yes |
| -w <br> --wordlist |  | Path to wordlist file | yes |

**Flow of the Program**
- Parsing th given arguments (URL and wordlist).
- Configuring the Selenium WebDriver in headless mode.
- Loading the wordlist from a file and returning it as a list of strings for later use.
- Performing directory scanning by iterating through this list of directories and checking each one for existence on the given web server by comparing the content of the base URL with the target URL.
- Printing the existing directories.
>i: The path to the WebDriver is hard coded. If desired, the code can be customized to pass it as an argument to the run command.

## Getting Started
0) <a href="https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo">Fork</a> the project to your namespace, if you want to make changes or open a <a href="https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests">Pull Request</a>.
1) <a href="https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository">Clone</a> the project to your platform if you just want to use the program.
    - <ins>Example</ins>: Clone the repo e.g. using an SSH-Key:  
    ```
    git clone git@github.com:SarahZimmermann-Schmutzler/headless_gobuster.git
    ```
2) There are dependencies to install, the other modules are part of the standard library:
    - Selenium, you can install it across platforms with **Pip**:  
    ```
    pip install selenium==4.9.0
    ```
    - The WebDriver for Selenium, in this case **GeckoDriver** for the Firefox browser:
        - Linux / Ubuntu:
            - <a href="https://github.com/mozilla/geckodriver/releases">Downloading from GitHub</a>  
                `geckodriver-v0.35.0-linux64.tar.gz`
            - Open a terminal in the Download directory:
                - Unzip file:  
                ```
                tar -xvzf geckodriver-v0.35.0-linux64.tar.gz
                ```
                - Move the driver to a directory in which executable programs are stored and can be used system-wide:  
                ```
                sudo mv geckodriver /usr/local/bin/geckodriver
                ```
        - <a href="https://github.com/mozilla/geckodriver/releases">Versions for other operating systems</a>


## Usage
- Make sure you are in the folder where you cloned **Headless_Gobuster** into.  

- Help! What options does the program support!?    
    ```bash
    python headless_gobuster.py -h
    # or
    python headless_gobuster.py --help
    ```  

- To find the directories of a dynamic web application use the following command in your terminal:
    ```bash
    python headless_gobuster.py -u [URL] -w [path/to/wordlist]
    ```
    - <ins>Example</ins>: Find the directories of the OWASP Juice Shop:  
        ```bash
        python headless_gobuster.py -u "http://127.0.0.1:3000/#" -w "wordlist.txt"
        ```
- What you see after ... a while in the terminal:
    >i: If it takes so long, why no multithreading? Multithreading can lead to unexpected errors in Selenium, especially when a single WebDriver instance is used for multiple threads.  
    ```
    [+] Directory found: 0 --> http://127.0.0.1:3000/#/0
	[+] Directory found: about --> http://127.0.0.1:3000/#/about
	[+] Directory found: accounting --> http://127.0.0.1:3000/#/accounting
	[+] Directory found: administration --> http://127.0.0.1:3000/#/administration
	[+] Directory found: basket --> http://127.0.0.1:3000/#/basket
	[+] Directory found: chatbot --> http://127.0.0.1:3000/#/chatbot
	[+] Directory found: contact --> http://127.0.0.1:3000/#/contact
	[+] Directory found: login --> http://127.0.0.1:3000/#/login
	[+] Directory found: register --> http://127.0.0.1:3000/#/register
	[+] Directory found: score-board --> http://127.0.0.1:3000/#/score-board
	[+] Directory found: search --> http://127.0.0.1:3000/#/search
    ```

## Additional Notes
In Python, **Selenium** is a library (open-source) that allows developers to automate web applications by writing a script that performs certain actions in a web browser as if it were controlled by a human user.  

To use Selenium, a WebDriver must be installed for the respective browser (e.g. **GeckoDriver** for Firefox).  

The **argparse** module is used to parse (read) command line arguments in Python programs. It allows to define arguments and options that can be passed to the program when starting it from the command line. These are then processed and are available in the program as variables.  

The **time** module in Python is a module from the standard library that provides functions to work with time. It provides basic tools to deal with time measurements, time zones and sleep functions.  
   
**Pip** is the default package manager for Python. It allows you to install, manage, and uninstall third-party Python libraries and modules. It simplifies the process of adding functionality to your Python projects by letting you download and install libraries from the Python Package Index (PyPI), a repository of Python packages.
