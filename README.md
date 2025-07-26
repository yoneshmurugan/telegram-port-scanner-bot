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

<img width="1712" height="869" alt="diagram-export-10-10-2024-10_00_42-AM" src="https://github.com/user-attachments/assets/282a4e67-562d-4c40-8da7-642a599805c4" />

## Features
- `/start`: Welcome message and commands list.
- `/provideip`: Prompt for IP address. Get ip address by using command 'ipconfig' in cmd
- `/scan`: Scan the IP for open ports (1-1024).
- `/close <port>`: Block a port using Windows firewall.

![Picture1](https://github.com/user-attachments/assets/32b683ea-a6b5-4a66-94a5-90aefc70d515)

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
Replace `BOT_TOKEN` in the code with your actual token or use env vars. Start the bot and interact via Telegram.
Create a .env file with your own bot token, Get your own bot token from BotFather on Telegram

## EXAMPLE .env file 
BOT_TOKEN="YOUR TOKEN"

## Security Notes
- **Bot Token**: Never hardcode this in your code. Use environment variables (e.g., `os.getenv('BOT_TOKEN')`).
- **Port Scanning**: Ensure you have permission to scan IPs to avoid legal issues.
- **Firewall Changes**: The `/close` command modifies Windows firewall—use with caution. It wont affect the essential ports

## License
MIT License (see LICENSE file).

The integration of a Telegram bot with scanning tools offers a user-
friendly, cost-effective solution for network security. Testing showed accurate detection of open ports, efficient vulnerability classification, and improved response 
times, making it scalable and practical. 
This project demonstrates an innovative approach to real-time vulnerability 
assessment, combining accessibility, functionality, and security. 

## Conclusion
The Open Port Scanner Bot is a practical and effective tool for enhancing network security. Its intuitive design makes cybersecurity accessible to non-technical users, while its modular and scalable architecture ensures adaptability. By addressing existing gaps in network security tools, the project demonstrates the potential for technology to simplify complex tasks and empower users. 
The system's limitations highlight areas for future development, ensuring that the project remains relevant and impactful. Overall, the Open Port Scanner Bot is a significant step toward accessible and automated cybersecurity solutions. 


