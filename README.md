# Gaia AI Node Guide

In this guide, we will go through setting up and running a Gaia AI node using the lightweight LLM model **Qwen2 0.5B Instruct** to earn **GaiaPoints** for future Gaia token airdrop!

---

# Gaia Dashboard
In Gaia XP program, we accumulate points by interacting with Gaia AI Agents and running Gaia nodes.
1. Connect your wallet to [Gaia Dashboard](https://gaianet.ai/reward?invite_code=ReV7iv) and complete registration.
2. Use this invite code to boost up your XP: `ReV7iv`
3. Complete social tasks in [Rewards Summary](https://www.gaianet.ai/reward-summary)

---

# Gaia Node
I will go through the complete process of earning **Node Points** and **User Points** in the dashboard by:
* Setting up a node.
* Keeping node online and processing requests.
* Joining a Domain.
* Chatting with the AI agent tied to the domain you've joined.

## 1. System Requirements
To run a Gaia node with the **Llama-3.2-3B-Instruct** model, ensure your system meets the following minimum requirements:

- **CPU**: 4 cores
- **RAM**: 8GB
- **Storage**: 10GB

**For Windows users**:
* You need to install Ubuntu by enabaling wsl on your windows, or run ubuntu/linux distro through VM like Virtualbox or VMware.

**For Linux/VPS users**:
* You are good to go and keep going through the following guide.

> If you are a VPS user, I recommend to install it on your Windows too, so you farm more **GaiaPoints**. The more your node is online, connected to a domain and chat with AI, the more you receive **Node Points** & **User Points**
---

## 2. Install dependecies
1. Update packages
     ```bash
   sudo apt update && sudo apt upgrade -y
     ```

2. Install Python
     ```bash
     ## Python 3.8 Pip, Python3 Install
     sudo apt install -y python3-pip
     sudo apt install pip
     sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
     ```

---

## 3. Install Gaia Node CLI
To install the Gaia Node CLI, run the following command:

```bash
curl -sSfL 'https://github.com/GaiaNet-AI/gaianet-node/releases/latest/download/install.sh' | bash
```

After installation, run this `source /root/.bashrc` or simply restart your terminal to make the gaianet CLI working.

---

## 4. Config Gaia Node
By running this command, by default you will download default **Llama-3.2-3B-Instruct** model and initialize your Node:

  ```bash
gaianet init
  ```

---

## 5. Start Gaia Node
By running a Gaia Node, we are actually deploying an AI Agent with a specific AI Model that we can chat with it.

- **Start the Node**
  ```bash
  gaianet start
  ```

- **Optional: Stop the Node**
  ```bash
  gaianet stop
  ```

---

## 6. Register Your Node on Gaia Dashboard
1. Run this command to get your **Node ID** and **Device ID**:
     ```bash
     gaianet info
     ```
2. Visit [Node Settings](https://www.gaianet.ai/setting/nodes) and click **Connect New Node**.
3. Copy and paste the IDs into the website and click **Join**.

---

## 7. Joining a Domain
* You must join a domain and chat with the domain to earn **Node Points**
* Chatting with your own node without a domain makes no sense
1. Enter the following command in your terminal
   ```bash
   gaianet stop
   gaianet config --domain gaia.domains
   gaianet init
   gaianet start
   ```
2. Go to [Node Settings](https://www.gaianet.ai/setting/nodes).
3. Click the three dots next to your active node and select **Join Domain**.
4. Click on Next **Step**
5. Search for the domain `llama.gaia.domains`

![image](https://github.com/user-attachments/assets/b96f4bf2-33af-4b8c-8491-96306371aae6)

6. Click on the domain and complete the next steps.

---

## 8. Chat with Your Node
To interact with your node and earn XP, visit: [llama Gaia Domain](https://llama.gaia.domains)

* You need **Credit Balance** to be able to chat with your node.
* Everyday, Convert your **Gaiapoints** to **Credit Balance**.
* Your Gaiapoints will remain same after converting and You can convert 1000 gaiapoints everyday.

![image](https://github.com/user-attachments/assets/ba7e9d4c-70b7-4621-97ae-7f0633303154)


---

## 9. Run AutoChat Bot 
1. **Create an API Key**:
   - Go to [Gaia API Keys](https://www.gaianet.ai/setting/gaia-api-keys) and create a new key. Save the API key somewhere since you won't be able to access it again.

2. **Download the Python Script**:
   - Run:
     ```bash
     curl -L -o gaiabot.py https://github.com/Shiro-Kuro/Gaianet-AI/raw/main/gaiabot.py
     ```

3. **Run the Script**:
   - Open a screen to run the bot in the background, so if you closed the terminal, it won't stop:
     ```bash
     screen -S gaiabot
     ```
   - Now run this command to start the bot:
     ```bash
     python3 gaiabot.py
     ```
   - Enter your Gaia API key when prompted.

* To minmize the screen, press `Ctrl+A+D`
* To return the screen, enter command: `screen -r gaiabot`
* To stop and kill the bot, press `CTRL+C` inside the screen & run this command: `screen -XS gaiabot quit`

It might gives you failed attempts which is because of networks floods, if all connections are stable it will generate the result after few failed attempts.


---

## 10. Earn Points
You are now earning points by following this guide. Points will be updated after 24h or more.
* `User Points`: Chat with your domain or other domains
* `Node Points`: Keep your node uptime and chat with the domain you have joined.

![image](https://github.com/user-attachments/assets/3b1c85cb-80a4-4cdc-b769-7b22282bd268)

If you are a Local PC user (windows or linux), you simply can rerun your Node + ChatBot everyday at your start
