# failed_login.py

This tool will return all failed logins to Splunk Enterprise for the past 7 days.

## Installation

**For safety, install to a python virtual environment**

1. Clone the repository ```git clone https://github.com/philskents/tr_challenge.git```
2. Install the prerequisites ```pip install -r requirements.txt```

## Usage

python failed_login.py [OPTIONS]

Options:
  
  --host TEXT                     Splunk hostname  [required]
  
  --port INTEGER                  Splunk REST API port  [default: 8089]
  
  --username TEXT                 Splunk username  [required]
  
  --password TEXT                 Splunk password  [required]
  
  --help			  Display help 

[![asciicast](https://asciinema.org/a/jx8FWcJfdwTFXGrDHo32wZRQ6.svg)](https://asciinema.org/a/jx8FWcJfdwTFXGrDHo32wZRQ6)
