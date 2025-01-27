# CodeChef Automation using Selenium

This project demonstrates the automation of CodeChef problem submissions using Selenium WebDriver. The script logs in to CodeChef, navigates to a problem page, uploads a solution file, runs the code, and submits it automatically.

---

## Features
- **Automated Login**: Retrieves username and password from a `login.txt` file for a seamless login experience.
- **Navigation**: Automatically navigates to the problem page on CodeChef.
- **Code Upload**: Uploads a pre-written solution file (`code.cpp`).
- **Execution and Submission**: Compiles and submits the code after uploading.

---

## Requirements
- Python 3.7 or higher
- Google Chrome browser
- ChromeDriver compatible with your browser version

### Libraries
Install the following Python libraries:
```bash
pip install selenium pynput
```

---

## Setup and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/SamarthKuchya/Codechef_Automation.git
cd codechef-automation
```

### 2. Create a `login.txt` File
Create a `login.txt` file in the project directory with the following format:
```
username = 'your_codechef_username'
password = 'your_codechef_password'
```

### 3. Update the Code File Path
Replace the file path in the script (`D:\Skills\Project Automating Codechef\code.cpp`) with the path to your solution file.

### 4. Run the Script
Run the Python script:
```bash
python automate_codechef.py
```

---

## How It Works
1. **Login**: 
   - Reads username and password from `login.txt`.
   - Logs in to CodeChef using Selenium.

2. **Problem Navigation**:
   - Navigates to the desired problem page (`FOODCOST` in this example).

3. **Code Upload and Submission**:
   - Opens the code upload dialog using Selenium.
   - Types the file path using `pynput.keyboard`.
   - Clicks the "Compile" and "Submit" buttons to execute and submit the code.

---

## Customization
- **Problem Page**: Update the URL in the script to navigate to a different problem.
- **Solution File**: Replace the file path with your solution's path.
- **Browser Settings**: If using a different browser, update the WebDriver initialization accordingly.

---

## Limitations
- **CodeChef UI Changes**: Any changes to the CodeChef website might break the script.
- **File Path**: Ensure the file path is valid and accessible.
- **WebDriver Compatibility**: Ensure ChromeDriver matches the installed Chrome browser version.

---

## Disclaimer
This script is for educational purposes only. Ensure compliance with CodeChef's terms of service and avoid using it for any unethical activities.

---

## License
This project is licensed under the MIT License.

---

## Acknowledgments
Special thanks to the Selenium and Python communities for their support and documentation.
