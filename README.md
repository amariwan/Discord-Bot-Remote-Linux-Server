# Discord Bot with Command Execution

This Discord bot allows you to execute commands on a server via Discord messages.

## Features

- Executes commands prefixed with `!execute ` securely using `sudo`.
- Sends command output back to the Discord channel in a formatted code block.
- Handles errors and provides feedback on command execution.

## Installation

1. Clone the repository or download the script.
2. Install the required Python packages:

   ```
   pip install discord.py python-dotenv
   ```

3. Create a `.env` file in the project directory and add your Discord bot token and sudo password:

   ```
   DISCORD_TOKEN=your_discord_bot_token_here
   SUDO_PASSWORD=your_sudo_password_here
   ```

4. Run the script:

   ```
   python main.py
   ```

## Usage

- Invite the bot to your Discord server.
- Use the command `!execute [your_command]` in any text channel where the bot is present to execute commands on the server.
- The bot will execute the command using `sudo`, capture the output, and send it back to the channel in a formatted code block.

## Security Note

- **Environment Variables**: Ensure your `.env` file is kept private and not shared or exposed to others.
- **Command Execution**: Use caution with command execution via Discord, as it could potentially be abused. Limit the bot's access and commands to trusted users only.
- **Sudo Usage**: Configure `sudo` securely on your system to minimize risks associated with elevated privileges.

## Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests. Please adhere to the coding standards and ensure your changes are well-tested.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
