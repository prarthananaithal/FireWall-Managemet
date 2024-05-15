import subprocess
from flask import Flask, request

# Initialize Flask app
app = Flask(__name__)

# Define firewall rule names for blocking and unblocking
http_rule_name = "Block HTTP"
imap_rule_name = "Block IMAP"
pop3_rule_name = "Block POP3"
smtp_rule_name = "Block SMTP"

# Define firewall rules for blocking and unblocking HTTP
firewall_rules_with_HTTP_blocked = [
    """netsh advfirewall firewall add rule name="Block HTTP" dir=out action=block protocol=TCP remoteport=80""",
]

firewall_rules_with_HTTP_allowed = [
    """netsh advfirewall firewall delete rule name="Block HTTP" """,
]

# Define firewall rules for blocking and unblocking IMAP
firewall_rules_with_IMAP_blocked = [
    """netsh advfirewall firewall add rule name="Block IMAP" dir=in action=block protocol=TCP localport=143""",
]

firewall_rules_with_IMAP_allowed = [
    """netsh advfirewall firewall delete rule name="Block IMAP" """,
]

# Define firewall rules for blocking and unblocking POP3
firewall_rules_with_POP3_blocked = [
    """netsh advfirewall firewall add rule name="Block POP3" dir=in action=block protocol=TCP localport=110""",
]

firewall_rules_with_POP3_allowed = [
    """netsh advfirewall firewall delete rule name="Block POP3" """,
]

# Define firewall rules for blocking and unblocking SMTP
firewall_rules_with_SMTP_blocked = [
    """netsh advfirewall firewall add rule name="Block SMTP" dir=out action=block protocol=TCP remoteport=25""",
]

firewall_rules_with_SMTP_allowed = [
    """netsh advfirewall firewall delete rule name="Block SMTP" """,
]

# Function to apply firewall rules
def apply_firewall_rules(rules):
    for rule in rules:
        subprocess.run(rule, shell=True)

# Function to show firewall rules for a specific service
def show_firewall_rule(rule_name):
    try:
        result = subprocess.run(f"""netsh advfirewall firewall show rule name="{rule_name}" """, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Firewall rule {rule_name}: Doesn't exist"
    except Exception as e:
        return str(e)

# Flask route to prompt user to choose firewall rules
@app.route('/')
def choose_firewall():
    html = "<html><body>"
    html += "<h2>Choose Firewall Rules:</h2>"
    html += "<form action='/apply_firewall' method='post' onsubmit='return showPopup()'>"
    html += "<label for='http_blocked'>Block HTTP traffic:</label>"
    html += "<input type='radio' name='firewall' id='http_blocked' value='http_blocked'><br>"
    html += "<label for='http_allowed'>Allow HTTP traffic:</label>"
    html += "<input type='radio' name='firewall' id='http_allowed' value='http_allowed'><br>"
    html += "<label for='imap_blocked'>Block IMAP traffic:</label>"
    html += "<input type='radio' name='firewall' id='imap_blocked' value='imap_blocked'><br>"
    html += "<label for='imap_allowed'>Allow IMAP traffic:</label>"
    html += "<input type='radio' name='firewall' id='imap_allowed' value='imap_allowed'><br>"
    html += "<label for='pop3_blocked'>Block POP3 traffic:</label>"
    html += "<input type='radio' name='firewall' id='pop3_blocked' value='pop3_blocked'><br>"
    html += "<label for='pop3_allowed'>Allow POP3 traffic:</label>"
    html += "<input type='radio' name='firewall' id='pop3_allowed' value='pop3_allowed'><br>"
    html += "<label for='smtp_blocked'>Block SMTP traffic:</label>"
    html += "<input type='radio' name='firewall' id='smtp_blocked' value='smtp_blocked'><br>"
    html += "<label for='smtp_allowed'>Allow SMTP traffic:</label>"
    html += "<input type='radio' name='firewall' id='smtp_allowed' value='smtp_allowed'><br>"
    html += "<input type='submit' value='Apply Firewall Rules'></form><br>"
    html += "<h2>Test Connectivity:</h2>"
    html += "<form action='/test_HTTP' method='get'>"
    html += "<input type='submit' value='Test HTTP Connectivity'></form>"
    html += "<form action='/test_IMAP' method='get'>"
    html += "<input type='submit' value='Test IMAP Connectivity'></form>"
    html += "<form action='/test_POP3' method='get'>"
    html += "<input type='submit' value='Test POP3 Connectivity'></form>"
    html += "<form action='/test_SMTP' method='get'>"
    html += "<input type='submit' value='Test SMTP Connectivity'></form></body></html>"
    html += "<script>"
    html += "function showPopup() { alert('Firewall rules applied successfully.'); return true; }"
    html += "</script>"
    return html

# Flask route to apply firewall rules based on user choice
@app.route('/apply_firewall', methods=['POST'])
def apply_firewall():
    firewall = request.form.get('firewall')
    if firewall == 'http_blocked':
        apply_firewall_rules(firewall_rules_with_HTTP_blocked)
    elif firewall == 'http_allowed':
        apply_firewall_rules(firewall_rules_with_HTTP_allowed)
    elif firewall == 'imap_blocked':
        apply_firewall_rules(firewall_rules_with_IMAP_blocked)
    elif firewall == 'imap_allowed':
        apply_firewall_rules(firewall_rules_with_IMAP_allowed)
    elif firewall == 'pop3_blocked':
        apply_firewall_rules(firewall_rules_with_POP3_blocked)
    elif firewall == 'pop3_allowed':
        apply_firewall_rules(firewall_rules_with_POP3_allowed)
    elif firewall == 'smtp_blocked':
        apply_firewall_rules(firewall_rules_with_SMTP_blocked)
    elif firewall == 'smtp_allowed':
        apply_firewall_rules(firewall_rules_with_SMTP_allowed)
    return choose_firewall()

# Flask route to test HTTP connectivity and display the status of the HTTP firewall rule
@app.route('/test_HTTP')
def test_HTTP():
    result = show_firewall_rule(http_rule_name)
    if isinstance(result, str):
        return generate_table(result, http_rule_name)
    else:
        return result

# Flask route to test IMAP connectivity and display the status of the IMAP firewall rule
@app.route('/test_IMAP')
def test_IMAP():
    result = show_firewall_rule(imap_rule_name)
    if isinstance(result, str):
        return generate_table(result, imap_rule_name)
    else:
        return result

# Flask route to test POP3 connectivity and display the status of the POP3 firewall rule
@app.route('/test_POP3')
def test_POP3():
    result = show_firewall_rule(pop3_rule_name)
    if isinstance(result, str):
        return generate_table(result, pop3_rule_name)
    else:
        return result
    
# Flask route to test SMTP connectivity and display the status of the SMTP firewall rule
@app.route('/test_SMTP')
def test_SMTP():
    result = show_firewall_rule(smtp_rule_name)
    if isinstance(result, str):
        return generate_table(result, smtp_rule_name)
    else:
        return result

# Function to generate HTML table from firewall rule information
def generate_table(rule_info, rule_name):
    table = "<h2>Status of {}:</h2>".format(rule_name)
    table += "<table border='1'>"
    for line in rule_info.splitlines():
        if ":" in line:
            key, value = [item.strip() for item in line.split(":", 1)]
            table += "<tr><td>{}</td><td>{}</td></tr>".format(key, value)
    table += "</table>"
    table += "<br><a href='/'>Back to Home</a>"
    return table

if __name__ == "__main__":
    # Run Flask app
    app.run(host='0.0.0.0', port=80, threaded=True)
