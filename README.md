
# Firewall Rules Management with Flask

## Introduction
This project implements a web application using Flask, a Python web framework, to manage firewall rules on a Windows system. It allows users to block or unblock specific types of network traffic (HTTP, IMAP, POP3, SMTP) through a user-friendly web interface.

## Code Overview
1. **Importing Libraries:**
   - The code begins by importing necessary libraries: `subprocess` for executing shell commands and `Flask` for creating the web application.

2. **Initialization:**
   - Flask application is initialized.

3. **Defining Firewall Rules:**
   - Firewall rule names and corresponding commands to block or unblock traffic are defined.

4. **Functions:**
   - `apply_firewall_rules()`: Function to execute firewall rules.
   - `show_firewall_rule()`: Function to display the status of firewall rules.
   - `choose_firewall()`: Flask route to display a form for choosing firewall rules.
   - `apply_firewall()`: Flask route to apply firewall rules based on user choice.
   - Routes for testing connectivity and displaying firewall status for HTTP, IMAP, POP3, and SMTP.

5. **HTML Templates:**
   - HTML templates are generated dynamically within Flask routes using string concatenation. The templates include forms for choosing firewall rules and testing connectivity.

6. **JavaScript:**
   - JavaScript function `showPopup()` is embedded in the HTML to show a pop-up message when applying firewall rules.

7. **Generating HTML Tables:**
   - Function `generate_table()` is used to format the output of firewall status into HTML tables.

8. **Main Block:**
   - Checks if the script is executed directly and starts the Flask application on port 80.

## Notable Features
- Provides a user-friendly web interface for managing firewall rules.
- Utilizes subprocess to execute shell commands for manipulating firewall rules.
- Uses JavaScript to display pop-up messages for better user interaction.

## Recommendations for Improvement
- Enhance error handling to provide more informative messages to users.
- Implement user authentication and authorization for security purposes.
- Add styling to improve the visual appearance of the web interface.

## License
This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.

## Conclusion
This project demonstrates how to create a simple web application for managing firewall rules using Flask. It provides a convenient way for users to control network traffic on a Windows system through a web browser.
