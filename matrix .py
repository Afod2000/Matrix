import requests
import time
from huggingface_hub import InferenceApi

# Hugging Face API Token (replace with your actual token)
HF_API_TOKEN = "your_huggingface_api_token "  # Replace with your API token

# Create an instance of the Hugging Face Inference API for the Dolphin Mistral model
model_name = "mistralai/Mistral-7B-v0.1"  # The Mistral model hosted on Hugging Face
inference = InferenceApi(repo_id=model_name, token=HF_API_TOKEN)

# Function to print in dot-matrix style
def dot_matrix_print(message):
    for char in message:
        if char == " ":
            print(" ", end="", flush=True)
        else:
            print(char, end=" ", flush=True)  # Add space between characters
        time.sleep(0.03)  # Delay for dot-matrix effect
    print("\n")

# Define the Hidden Wiki URL (example)
hidden_wiki_url = "http://3g2upl4pq6kufc4m.onion"

# Function to connect to the Hidden Wiki using Tor
def access_hidden_wiki(url):
    dot_matrix_print("Connecting to the dark web...")

    # Using the Tor proxy to make a request
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',  # Tor default port for SOCKS proxy
        'https': 'socks5h://127.0.0.1:9050'
    }

    try:
        # Send a request through Tor to the .onion URL
        response = requests.get(url, proxies=proxies, timeout=30)

        # Check if the connection was successful
        if response.status_code == 200:
            dot_matrix_print("Successfully connected to the Hidden Wiki!")
            return response.text  # Return the full response for analysis
        else:
            dot_matrix_print(f"Failed to connect: Status code {response.status_code}")
            return None
    except requests.RequestException as e:
        dot_matrix_print(f"Error: Could not connect to {url}.")
        dot_matrix_print(f"Details: {e}")
        return None

# Function to use Dolphin Mistral LLM via Hugging Face API to analyze the Hidden Wiki content and generate code
def generate_code(content, language):
    dot_matrix_print("Generating code or scripts based on hidden knowledge...")

    try:
        # Use Hugging Face Inference API to query the Dolphin Mistral model with the content and target language
        prompt = (
            f"Analyze the following content and generate a {language} code snippet or script:\n\n{content}\n\n"
            "Make sure the code is functional and well-commented."
        )
        response = inference(prompt)

        # Extract the LLM's response
        code = response.get('generated_text', "No response from the model.")
        return code.strip()
    except Exception as e:
        dot_matrix_print(f"Error consulting the LLM: {e}")
        return "Sorry, I could not process your request at this time."

# Main Program Flow
def mr_matrix():
    dot_matrix_print("Mr. Matrix delves into the shadowy depths...")

    # Access the Hidden Wiki
    hidden_wiki_content = access_hidden_wiki(hidden_wiki_url)
    
    if hidden_wiki_content:
        dot_matrix_print("Accessing forbidden knowledge...")

        # Ask the user for the desired programming language
        language = input("Enter the programming language for the code generation (e.g., Python, JavaScript, Bash): ").strip()

        # Validate the user input for programming language
        if not language:
            dot_matrix_print("No programming language specified. Exiting...")
            return

        # Generate code based on the Hidden Wiki content for the specified language
        generated_code = generate_code(hidden_wiki_content, language)

        # Display the generated code in dot-matrix style
        dot_matrix_print("Generated Code:")
        dot_matrix_print(generated_code)
    else:
        dot_matrix_print("Unable to retrieve hidden knowledge at this time.")

# Run the program
if __name__ == "__main__":
    mr_matrix()
