# ux-persona-generator
A command-line tool built with Python that leverages the Groq API and Llama 3 to automatically generate detailed user personas for UX design projects based on simple user prompts.

# UX Persona Generator with Groq

This is a command-line tool that helps UX designers, product managers, and developers quickly generate detailed user personas. By providing a brief description of your product and target audience, the script uses the Groq API to call the Llama 3 model and create a well-structured persona, saving you time and effort in the initial stages of your UX research.

The generated persona is displayed in the console and automatically saved to a `PersonaGenerator.txt` file for future reference.

## Features

-   **Interactive CLI:** A simple and straightforward command-line interface.
-   **AI-Powered:** Leverages the speed and power of the Groq API with the Llama 3 model.
-   **Customized Personas:** Generates personas tailored to your specific project and target audience.
-   **Structured Output:** Provides a detailed persona including a name, photo description, bio, goals, frustrations, and more.
-   **Automatic Saving:** Appends each new persona to a local `.txt` file for easy access.

## Getting Started

To run this script, you need to set up your environment first.

### Prerequisites

-   Python 3 installed.
-   An API key from [Groq](https://console.groq.com/keys).

### Setup

1.  **Clone or Download:**
    Get a copy of the `ux_persona_creator.py` script on your local machine.

2.  **Install Dependencies:**
    You will need the `groq` Python library. You can install it using pip:
    ```bash
    pip install groq
    ```

3.  **Add Your API Key:**
    Open the `ux_persona_creator.py` file in a text editor and replace `"YOUR API KEY HERE"` with your actual Groq API key.

    ```python
    # Change this line
    MY_API_KEY = "YOUR API KEY HERE"
    ```
    **Important:** Do not share your code publicly with the API key inside it.

## How to Run

1.  Navigate to the script's directory in your terminal.
2.  Run the following command:
    ```bash
    python ux_persona_creator.py
    ```
3.  The script will then prompt you to enter the project description and the target audience.

## Usage Example

Here is an example of how the interaction in the terminal will look:

```text
Welcome to the UX Persona Generator with Groq!
--------------------------------------------------
What kind of product or website do you need a persona for? (e.g., meditation app, plant e-commerce)
> A mobile app for tracking personal finances and setting budgets

Who is the main target audience for this project? (e.g., young adults, seniors, new parents)
> University students and recent graduates

 Understood! Thinking of a persona for you... Please wait a moment.

--------------------------------------------------
Persona Generated Successfully!

**Fictional Name:** Alex Mendes

**Photo:** A profile picture of a smiling young man in his early 20s, wearing a university hoodie, sitting in a campus library with a laptop open in front of him.

**Age:** 22

**Profession:** Recent Computer Science Graduate / Freelance Web Developer

**Short Bio:** Alex just graduated and is navigating the transition from student life to a full-time career. He's passionate about technology and is starting to earn his own money through freelance gigs. While excited about his financial independence, he finds managing money overwhelming and is looking for a simple tool to help him stay on top of his expenses and save for the future, like buying a new high-end laptop.

**Goals:**
-   To save up for a new MacBook Pro within the next 6 months.
-   To clearly understand where his money is going each month.
-   To avoid getting into debt from small, unnecessary purchases.
-   To build a small emergency fund.

**Frustrations and Pain Points:**
-   "I lose track of my subscriptions and small daily expenses."
-   "Most budgeting apps I've tried are too complex and have too many features I don't need."
-   "I feel anxious when I look at my bank account at the end of the month because I don't know where all my money went."
-   "It's hard to balance paying off my student loan with my personal savings goals."

**Behaviors and Habits:**
Alex is tech-savvy and spends a lot of time on his phone and laptop. He uses apps for everything from ordering food to managing his study schedule. He prefers clean, intuitive interfaces and gets frustrated with clunky or slow applications. He checks his social media and emails frequently throughout the day.

**Quote:** "I want to be smart with my money, but I need a tool that's as simple and fast as checking my social media."
--------------------------------------------------
```
After this is displayed, the same text will be added to your `PersonaGenerator.txt` file.
