# Identity Bot
A Discord bot to help new users introduce themselves to current and future users and also help them get familiar with other users in the channel. It can help to avoid cluttering text channels with repeated questions about another user's location, age etc. Users can ask this bot for other users' introductions.

This bot isn't a substitute for actual introductions when joining a server but it can help to have some basic information about others available with a single command.

### Installation
Go to this [link](https://discordapp.com/oauth2/authorize?&client_id=352971068232695810&scope=bot&permissions=0) to install onto your server. You need 'manage server' permissions on the server you want to install the bot to.

### Usage
The bot prefix is `!id`. Bot commands are `iam`, `whois`, `list` and `delete`. Each command is described below

=======Command======= | =======Description=======
-------------- | ---
`!id iam [introduction]` | This command will save your whatever you set as `[introduction]` with the bot. Your introduction can be as long as you want. Other users can get your introduction using the command below.
`!id whois @user1 @user2` | This command will get introductions for the users you mention in the message and DM them to you. Note that it sends a DM and does not reply on the same channel.
`!id list` | This command lists all users who have saved introductions with Identity Bot on your server.
`!id delete` | This command will delete your introduction. Other users won't be able to get your introduction any more after using this command.

### Suggested Setup
Set up a channel where @everyone cannot read messages. User's can use `whois` and other commands in that channel and then receive DMs from the bot. User's will probably be less hesitant to use `whois` if others don't know when they are using it.

### FAQ
#### Can I host this bot myself?
Feel free. I'm currently using an EC2 instance and RDS instance. I will share instructions for hosting on AWS soon along with the database schema.

#### This bot needs feature X/bug fix Y/etc.
Please open an issue (or even better, fix it and submit a PR).
