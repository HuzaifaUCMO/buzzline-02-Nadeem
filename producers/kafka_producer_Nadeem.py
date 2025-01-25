# kafka_producer_Nadeem.py
# 
# Produce weather-related streaming messages and send them to a Kafka topic.

# ------------------------------------------------------------------------
# 1. IMPORT STATEMENTS
# ------------------------------------------------------------------------
import os
import sys
import time
import utils
from dotenv import load_dotenv

from utils.utils_producer import (
    verify_services,
    create_kafka_producer,
    create_kafka_topic,
)
from utils.utils_logger import logger

# ------------------------------------------------------------------------
# 2. LOAD ENVIRONMENT VARIABLES
# ------------------------------------------------------------------------
load_dotenv()

# ------------------------------------------------------------------------
# 3. HELPER FUNCTIONS FOR .ENV VARIABLES
# ------------------------------------------------------------------------
def get_kafka_topic() -> str:
    """
    Retrieves the Kafka topic name from the .env file,
    falling back on 'weather_updates' if none is found.
    """
    topic = os.getenv("KAFKA_TOPIC", "weather_updates")
    logger.info(f"Kafka topic: {topic}")
    return topic


def get_message_interval() -> int:
    """
    Retrieves the message interval from the .env file,
    defaulting to 3 seconds if not specified.
    """
    interval = int(os.getenv("MESSAGE_INTERVAL_SECONDS", 3))
    logger.info(f"Message interval: {interval} seconds")
    return interval

# ------------------------------------------------------------------------
# 4. CORE MESSAGE GENERATION LOGIC
# ------------------------------------------------------------------------
def generate_messages(producer, topic, interval_secs):
    """
    Continuously generate weather messages and dispatch
    them to the specified Kafka topic.

    :param producer: KafkaProducer instance
    :param topic: Topic to publish messages to
    :param interval_secs: Delay between messages in seconds
    """
    weather_updates = [
        "Sunny with a high of 72°F",
        "Rainy with chances of thunderstorms",
        "Partly cloudy with mild temperatures",
        "Snow expected later today",
        "Clear skies with a cool breeze",
    ]

    try:
        while True:
            for message in weather_updates:
                logger.info(f"Generated weather update: {message}")
                producer.send(topic, value=message)
                logger.info(f"Sent message to '{topic}': {message}")
                time.sleep(interval_secs)
    except KeyboardInterrupt:
        logger.warning("Producer interrupted by user.")
    except Exception as e:
        logger.error(f"Error in message generation: {e}")
    finally:
        producer.close()
        logger.info("Kafka producer closed.")

# ------------------------------------------------------------------------
# 5. MAIN FUNCTION
# ------------------------------------------------------------------------
def main():
    """
    Entry point for this producer:
     1) Ensures Kafka topic is available.
     2) Creates a Kafka producer.
     3) Streams generated weather messages to the topic.
    """
    logger.info("START producer.")
    verify_services()

    # Get topic and interval
    topic = get_kafka_topic()
    interval_secs = get_message_interval()

    # Create the Kafka producer
    producer = create_kafka_producer()
    if not producer:
        logger.error("Failed to create Kafka producer. Exiting...")
        sys.exit(3)

    # Make sure the topic exists before sending messages
    try:
        create_kafka_topic(topic)
        logger.info(f"Kafka topic '{topic}' is ready.")
    except Exception as e:
        logger.error(f"Failed to create or verify topic '{topic}': {e}")
        sys.exit(1)

    # Start sending messages to the topic
    logger.info(f"Starting message production to '{topic}'...")
    generate_messages(producer, topic, interval_secs)

    logger.info("END producer.")

# ------------------------------------------------------------------------
# 6. IF RUN DIRECTLY, INVOKE MAIN
# ------------------------------------------------------------------------
if __name__ == "__main__":
    main()
