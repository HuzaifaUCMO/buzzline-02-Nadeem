afka Buzzline Project
Table of Contents
Overview
Features
Project Structure
Prerequisites
Setup & Installation
How to Run
Windows
MacLinux
Logging & Real-Time Analytics
Troubleshooting
Contributing
License
Overview
This project demonstrates how to use Kafka for sending and receiving messages in real time. The Producer publishes messages to a Kafka topic, and the Consumer processes (and optionally analyzes) those messages.

Features
Custom Kafka Producer: Sends custom messages to a specified Kafka topic.
Custom Kafka Consumer: Reads messages from the same Kafka topic, logs them in real time, and highlights important patterns or alerts (e.g., messages containing the word "error").
Real-Time Analytics: Simple alerting mechanism for messages matching certain keywords or patterns.
Logging: Uses Python’s built-in logging module for structured, time-stamped logs.
Project Structure
lua
Copy
Edit
.
├── consumers
│   ├── kafka_consumer_example.py
│   └── kafka_consumer_yourname.py   <-- Your unique consumer
├── producers
│   ├── kafka_producer_example.py
│   └── kafka_producer_yourname.py   <-- Your unique producer
├── logs
│   └── [log files]
├── README.md                        <-- This file
├── requirements.txt
└── ...
consumers/: Contains Python scripts for Kafka consumers.
producers/: Contains Python scripts for Kafka producers.
logs/: Log files output by producer or consumer scripts.
requirements.txt: Lists Python dependencies.
README.md: Documentation (this file).
Prerequisites
Kafka: Ensure you have a running Kafka broker.
Typically, this means having Kafka and Zookeeper installed and started on localhost:9092.
Python 3.7+: Required for running the scripts.
Virtual Environment (Recommended): For managing dependencies.
Setup & Installation
Clone the Repository

bash
Copy
Edit
git clone https://github.com/your-username/buzzline-02-case.git
cd buzzline-02-case
Create & Activate Virtual Environment
Windows:

bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate
Mac/Linux:

bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
How to Run
Windows
Activate virtual environment:
bash
Copy
Edit
.venv\Scripts\activate
Run the producer:
bash
Copy
Edit
py -m producers.kafka_producer_yourname
Run the consumer:
bash
Copy
Edit
py -m consumers.kafka_consumer_yourname
Mac/Linux
Activate virtual environment:
bash
Copy
Edit
source .venv/bin/activate
Run the producer:
bash
Copy
Edit
python3 -m producers.kafka_producer_yourname
Run the consumer:
bash
Copy
Edit
python3 -m consumers.kafka_consumer_yourname
Note: Make sure your Kafka broker is running on localhost:9092 (or adjust the scripts accordingly if it’s different).

Logging & Real-Time Analytics
Logging:
Both the producer and consumer scripts use Python’s logging module. By default, logs may be directed to:

The console (standard out), and/or
A log file in the logs/ directory.
Real-Time Analytics:
The consumer script demonstrates a simple mechanism for detecting the keyword "error". You can customize this logic to detect any pattern (e.g., "alert", "critical", or specific JSON values).

python
Copy
Edit
if "error" in msg.lower():
    logger.warning(f"ALERT: Found an error in message: {msg}")
Troubleshooting
Kafka Connection Errors:
Verify you can connect to Kafka on localhost:9092. If not, update bootstrap_servers in the Python scripts.
Module Not Found:
Double-check your virtual environment is active and you have installed all packages from requirements.txt.
Permissions:
On Mac/Linux, you might need to run chmod +x on certain scripts if you receive permission errors.
Contributing
Fork the repository on GitHub.
Create a feature branch:
bash
Copy
Edit
git checkout -b feature/my-new-feature
Commit your changes:
bash
Copy
Edit
git add .
git commit -m "Add cool new feature"
git push origin feature/my-new-feature
Open a Pull Request on GitHub.
License
This project is open source. See the LICENSE file for details (if included), or choose a license that best fits your needs.

Commit History
You can review your commit history in GitHub by clicking on the commits link in your repository home page. Make sure your commits are small, frequent, and have meaningful messages.

Example:

git add .
git commit -m "Add unique producer script"
git push