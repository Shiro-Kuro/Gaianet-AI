# Title: GaiaAI Chatbot
# The script will print the credit part and ask for the API key
import requests
import random
import time
import logging
from typing import List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("chatbot.log"),
        logging.StreamHandler()
    ]
)

# Configuration
BASE_URL = "https://llama.gaia.domains"
MODEL = "Llama-3.2-3B-Instruct-Q5_K_M"
MAX_RETRIES = 100  # Essentially infinite retries
RETRY_DELAY = 7  # Seconds between retries
QUESTION_DELAY = 1  # Seconds between successful questions

QUESTIONS = [
    "What is the Turing test, and has any AI passed it?",
    "What are generative adversarial networks (GANs) and how do they work?",
    "How does backpropagation optimize neural networks?",
    "What are transformers in deep learning, and why are they revolutionary?",
    "How does zero-knowledge proof ensure privacy in blockchain?",
    "What is the halting problem in computation?",
    "How does a quantum computer differ from a classical computer?",
    "What is homomorphic encryption, and how does it enable secure computation?",
    "What are the limitations of deep reinforcement learning?",
    "How does emergent behavior arise in complex AI systems?",
    "What is quantum decoherence, and how does it relate to quantum computing?",
    "What is the Einstein-Rosen bridge, and is it theoretically traversable?",
    "How does Hawking radiation work, and what does it imply about black holes?",
    "What is the holographic principle in physics?",
    "How does the Casimir effect demonstrate quantum vacuum energy?",
    "What is the Fermi Paradox, and what are its possible solutions?",
    "How does entropy relate to the arrow of time?",
    "What is the Drake equation, and how does it estimate extraterrestrial life?",
    "How do quantum fluctuations give rise to the universe?",
    "What is the simulation hypothesis, and what are its implications?",
    "How does the Many-Worlds Interpretation differ from the Copenhagen interpretation?",
    "What is a Bose-Einstein condensate, and how does it behave?",
    "How do dark matter and dark energy influence the universe?",
    "What is the weak anthropic principle, and how does it relate to cosmology?",
    "How does quantum tunneling enable nuclear fusion in stars?",
    "What are quarks and gluons, and how do they form matter?",
    "How does the Higgs boson give particles mass?",
    "What is the Ekpyrotic universe theory, and how does it challenge the Big Bang?",
    "How does RNA differ from DNA, and why is it crucial for life?",
    "What is CRISPR-Cas9, and how does it enable gene editing?",
    "How does epigenetics influence gene expression without changing DNA?",
    "What is horizontal gene transfer, and how does it affect evolution?",
    "How does synthetic biology aim to redesign life?",
    "What is mitochondrial DNA, and how is it inherited?",
    "How do telomeres affect aging and cellular lifespan?",
    "What is the role of ribosomes in protein synthesis?",
    "How does the microbiome impact human health and disease?",
    "What is a prion, and how do prion diseases spread?",
    "How does the placebo effect work, and what are its limitations?",
    "What is neuroplasticity, and how does it reshape the brain?",
    "How does the blood-brain barrier protect neural function?",
    "What is the Default Mode Network, and how does it influence consciousness?",
    "How does serotonin impact mood, and what are its neurological effects?",
    "What is the Sapir-Whorf hypothesis, and does language shape thought?",
    "How do psychedelic substances alter perception and cognition?",
    "What is the nature of free will, and is it an illusion?",
    "How does Gödels incompleteness theorem challenge mathematical logic?",
    "What is the Riemann Hypothesis, and why is it unsolved?",
    "How does string theory attempt to unify physics?",
    "What is the AdS/CFT correspondence, and why is it significant?",
]

def chat_with_ai(api_key: str, question: str) -> str:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    messages = [
        {"role": "user", "content": question}
    ]

    data = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.7
    }

    for attempt in range(MAX_RETRIES):
        try:
            logging.info(f"Attempt {attempt+1} for question: {question[:50]}...")
            response = requests.post(
                f"{BASE_URL}/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )

            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]

            logging.warning(f"API Error ({response.status_code}): {response.text}")
            time.sleep(RETRY_DELAY)

        except Exception as e:
            logging.error(f"Request failed: {str(e)}")
            time.sleep(RETRY_DELAY)

    raise Exception("Max retries exceeded")

def run_bot(api_key: str):
    while True:  # Outer loop to repeat the questions indefinitely
        random.shuffle(QUESTIONS)
        logging.info(f"Starting chatbot with {len(QUESTIONS)} questions in random order")

        for i, question in enumerate(QUESTIONS, 1):
            logging.info(f"\nProcessing question {i}/{len(QUESTIONS)}")
            logging.info(f"Question: {question}")

            start_time = time.time()
            try:
                response = chat_with_ai(api_key, question)
                elapsed = time.time() - start_time

                # Print the entire response
                print(f"Answer to '{question[:50]}...':\n{response}")

                logging.info(f"Received full response in {elapsed:.2f}s")
                logging.info(f"Response length: {len(response)} characters")

                # Ensure the script waits for the full response before proceeding
                time.sleep(QUESTION_DELAY)  # Wait before asking next question

            except Exception as e:
                logging.error(f"Failed to process question: {str(e)}")
                continue

def main():
    print("Title: GaiaAI Chatbot")
    print("Created by: Moei, modified by Shiro-Kuro")
    api_key = input("Enter your API key: ")
    run_bot(api_key)

if __name__ == "__main__":
    main()
