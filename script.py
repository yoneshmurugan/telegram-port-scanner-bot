import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes ,MessageHandler, filters
import nmap
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
user_data = {}
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Welcome to the Open Port Scanner Bot! \n"
        "Use the following commands:\n"
        "/provideip - Provide your IP address for scanning\n"
        "/scan - Scan the provided IP address for open ports\n"
        "/close <port> - Close a specific port on your IP"
    )
# Define the /provideip command handler
async def provide_ip(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Please reply with your IP address (e.g., 192.168.1.1 or your public IP). "
        "Make sure you have permission to scan the provided IP."
    )

# Define the IP address handler
async def handle_ip(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_ip = update.message.text

    # Validate the provided IP address
    parts = user_ip.split(".")
    if len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts):
        # Save the IP address for the user
        user_data[update.effective_user.id] = user_ip
        await update.message.reply_text(
            f"IP address {user_ip} has been received. Use /scan to scan this IP address."
        )
    else:
        await update.message.reply_text("Invalid IP address. Please provide a valid IPv4 address.")

# Define the /scan command handler
async def scan_ports(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id

    # Check if the user has provided an IP address
    if user_id not in user_data:
        await update.message.reply_text(
            "You haven't provided an IP address yet. Use /provideip to provide one."
        )
        return

    user_ip = user_data[user_id]
    await update.message.reply_text(
        f"Scanning IP address {user_ip}. Please wait..."
    )

    # Initialize the nmap scanner
    nm = nmap.PortScanner()

    try:
        # Scan the provided IP address for open ports in the range 1-1024
        nm.scan(user_ip, '1-1024')

        open_ports = []
        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                ports = nm[host][proto].keys()
                for port in ports:
                    if nm[host][proto][port]['state'] == 'open':
                        open_ports.append(port)

        # Send the scanning result
        if open_ports:
            await update.message.reply_text(f"Open Ports on {user_ip}: {', '.join(map(str, open_ports))}")
        else:
            await update.message.reply_text(f"No open ports found on {user_ip}.")
    except Exception as e:
        await update.message.reply_text(f"An error occurred while scanning: {e}")

# Define the /close command handler (Windows version using netsh)
async def close_port(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    # Check if the user has provided an IP address
    if user_id not in user_data:
        await update.message.reply_text(
            "You haven't provided an IP address yet. Use /provideip to provide one."
        )
        return

    # Check if a port number was provided
    if len(context.args) != 1 or not context.args[0].isdigit():
        await update.message.reply_text("Please provide a valid port number to close (e.g., /close 22).")
        return

    port = context.args[0]
    user_ip = user_data[user_id]

    # Close the provided port on the user's IP address (using netsh for Windows)
    try:
        # Use netsh to block the port on the Windows firewall
        os.system(f"netsh advfirewall firewall add rule name=BlockPort{port} dir=in action=block protocol=TCP localport={port}")
        
        # Confirm that the port has been blocked
        await update.message.reply_text(f"Port {port} has been closed on IP {user_ip}.")
    except Exception as e:
        await update.message.reply_text(f"An error occurred while closing the port: {e}")

# Initialize the Application
application = Application.builder().token(BOT_TOKEN).build()

# Add command handlers to the application
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('provideip', provide_ip))
application.add_handler(CommandHandler('scan', scan_ports))
application.add_handler(CommandHandler('close', close_port))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_ip))

# Start the bot
if __name__ == "__main__":
    print("Bot is running...")
    application.run_polling()
