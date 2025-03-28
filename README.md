# HEADLESS_GOBUSTER

A programm to **find directories of dynamic web applications**, like the [OWASP Juice Shop](https://github.com/juice-shop/juice-shop).  
This is a lightweight version of the known [gobuster](https://github.com/OJ/gobuster) - tool.  

The program was created as part of my training at the Developer Academy and is used exclusively for teaching purposes.  

## Table of Contents

1. [Technologies](#technologies)
1. [Getting Started](#getting-started)
1. [Usage](#usage)
   * [Program Options](#program-options)
   * [Program Flow](#program-flow)
   * [Example Run](#example-run) 

## Technologies

* **Python** 3.12.2
  * **argparse, time, typing**
  * **Selenium** [More Information](https://selenium-python.readthedocs.io/)
    * In Python, it is a library (open-source) that allows developers to automate web applications by writing a script that performs certain actions in a web browser as if it were controlled by a human user.
    * To use it, a **WebDriver** must be installed for the respective browser, in this case:
      * **GeckoDriver for Firefox browser** v0.35.0 [More Information](https://github.com/mozilla/geckodriver)

## Getting Started

0) [Fork](https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) the project to your namespace, if you want to make changes or open a [Pull Request](https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).

1. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the project to your platform if you just want to use it:

    ```bash
    git clone git@github.com:SarahZimmermann-Schmutzler/headless_gobuster.git
    ```

1. Install the **dependencies**:
   * Create a **Virtual Environment (Venv)** in the project folder:

      ```bash
      python -m venv env
      ```

   * **Activate** the Venv:

      ```bash
      source venv/bin/activate #Linux
      env\Scripts\activate #Windows
      ```

   * Install the **dependencies** from [requirements.txt](./requirements.txt):

      ```bash
      pip install -r requirements.txt
      ```

1. Install the **GeckoDriver** for the Firefox browser:
     * [Download v0.35.0 from GitHub](https://github.com/mozilla/geckodriver/releases) and follow the instrcutions given there.


## Usage

* For the further commands navigate to the directory you cloned **XSStrike** into.

### Program Options

* To see all available **program options** have a look in the `help-section`:

    ```bash
    python headless_gobuster.py -h
    # or
    python headless_gobuster.py --help
    ```

    | Option (Long) | Short | Description | Required? |
    | ------------- | ----- | ----------- | --------- |
    | --help | -h | Get a list of the **available options** | no |
    | --url | -u | **Target URL** | yes |
    | --keywords | -k | Comma-seperated keywords that **define the base/main page** | yes |
    | --wordlist | -w | Path to **wordlist file** | yes |

### Program Flow

* **Parsing** the given arguments (URL, main page keywords and wordlist).
* Configuring the **Selenium WebDriver** in headless mode.
* Loading the **wordlist** from a file and returning it as a list of strings for later use.
* Performing **directory scanning** by iterating through this list of directories and **checking each one for existence** on the given web server by comparing the content of the base URL with the target URL.
* Printing the existing directories in the terminal.

> [!NOTE]  
> The path to the WebDriver is hard coded. If desired, the code can be customized to pass it as an argument to the run command.

### Example Run

* To find the directories of a dynamic web application like the OWASP Juice Shop use the following command:

    ```bash
    python headless_gobuster.py -u "http://127.0.0.1:3000/#" -k "Apple Juice,Apple Pomace,Banana Juice" -w "wordlist.txt"
    ```

* After some time it will yield the following **output**:

> [!NOTE]
> If it takes so long, why no multithreading? Multithreading can lead to unexpected errors in Selenium, especially when a single WebDriver instance is used for multiple threads.

```bash
[+] Directory found: about --> http://127.0.0.1:3000/#/about
[+] Directory found: accounting --> http://127.0.0.1:3000/#/accounting
[+] Directory found: administration --> http://127.0.0.1:3000/#/administration
[+] Directory found: basket --> http://127.0.0.1:3000/#/basket
[+] Directory found: chatbot --> http://127.0.0.1:3000/#/chatbot
[+] Directory found: contact --> http://127.0.0.1:3000/#/contact
[+] Directory found: register --> http://127.0.0.1:3000/#/forgot-password
[+] Directory found: login --> http://127.0.0.1:3000/#/login
[+] Directory found: register --> http://127.0.0.1:3000/#/photo-wall
[+] Directory found: register --> http://127.0.0.1:3000/#/recycle
[+] Directory found: register --> http://127.0.0.1:3000/#/register
[+] Directory found: score-board --> http://127.0.0.1:3000/#/score-board
```
