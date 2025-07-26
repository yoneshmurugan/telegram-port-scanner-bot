# Telegram Port Scanner Bot
The Telegram Bot-Based Open Port Vulnerability Scanner project simplifies 
cybersecurity by using Telegram to perform real-time vulnerability assessments. 
It identifies open ports, analyzes risks, and delivers results via an accessible bot 
interface.

Purpose: To provide network administrators with a convenient tool for vulnerability 
scanning using the Telegram platform. This approach enhances proactive threat 
management by automating open port detection and risk classification. 

Methodology: The system uses the Nmap module for port scanning, the OS module 
for system information, and the Telegram Bot API for user interaction. Encrypted 
communication ensures data security while results are delivered in real-time. 

## Features
- `/start`: Welcome message and commands list.
- `/provideip`: Prompt for IP address. Get ip address by using command 'ipconfig' in cmd
- `/scan`: Scan the IP for open ports (1-1024).
- `/close <port>`: Block a port using Windows firewall.

## Function
- Accept and validate user-provided IP addresses. o Scan for open ports using the Nmap library. 
- List open ports with details (port number, state, protocol). 
- Close specified ports on Windows using netsh. 

## Installation
1. Clone the repo: `git clone https://github.com/yoneshmurugan/telegram-port-scanner-bot.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set your Telegram Bot Token as an environment variable (see Security note below).
4. Run: `python bot.py`

## Requirements
- Python 3.10+
- python-telegram-bot
- python-nmap
- install nmap for windows if needed

## Usage
Replace `BOT_TOKEN` in the code with your actual token or use env vars (bot username @Oiioii_bot). Start the bot and interact via Telegram.

## Security Notes
- **Bot Token**: Never hardcode this in your code. Use environment variables (e.g., `os.getenv('BOT_TOKEN')`). If you dont know how to create bot token, use our token to access @Oiioii_bot
- **Port Scanning**: Ensure you have permission to scan IPs to avoid legal issues.
- **Firewall Changes**: The `/close` command modifies Windows firewall—use with caution. It wont affect the essential ports

## License
MIT License (see LICENSE file).

The integration of a Telegram bot with scanning tools offers a user-
friendly, cost-effective solution for network security. Testing showed accurate detection of open ports, efficient vulnerability classification, and improved response 
times, making it scalable and practical. 
This project demonstrates an innovative approach to real-time vulnerability 
assessment, combining accessibility, functionality, and security. 
