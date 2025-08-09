# UX Persona creator
import os
from groq import Groq

MY_API_KEY = "YOUR API KEY HERE"

def create_ux_persona():
    
    print("Welcome to the UX Persona Generator with Groq!")
    print("-" * 50)

    # Collect information from the user
    project_description = input("What kind of product or website do you need a persona for? (e.g., meditation app, plant e-commerce)\n> ")
    target_audience = input("Who is the main target audience for this project? (e.g., young adults, seniors, new parents)\n> ")

    print("\n Understood! Thinking of a persona for you... Please wait a moment.\n")

    # Preparing to call the Groq API
    try:
        # Initializes the Groq "client" with your key
        groq_client = Groq(api_key=MY_API_KEY)

        # Create the prompt
        
        prompt_for_ai = f"""
        Act as a UX Design expert.
        Create a detailed user persona for a UX project.

        **Project Description:** {project_description}
        **Target Audience:** {target_audience}

        The persona must include the following fields:
        - Fictional Name and Photo (describe a profile picture)
        - Age
        - Profession
        - Short Bio (one paragraph)
        - Goals (3 to 4 goals related to the product)
        - Frustrations and Pain Points (3 to 4 frustrations the product can solve)
        - Behaviors and Habits (how they behave in their daily life)
        - A quote that summarizes the persona's attitude.

        Format the response clearly and in an organized manner.
        """

        # Make the call to the Groq API
        
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt_for_ai,
                }
            ],
            model="llama3-8b-8192",
        )

        # Show the AI's response to the user
        generated_persona = chat_completion.choices[0].message.content
        print("-" * 50)
        print("Persona Generated Successfully! \n")
        print(generated_persona)
        print("-" * 50)
        with open("PersonaGenerator.txt", "a") as savefile:
        	savefile.write("\n")
        	savefile.write(generated_persona)
        	savefile.write("\n" + "="*50)
        	savefile.write("\n")

    except Exception as e:
        # Handling errors
        print(f"\n An error occurred: {e}")
        print("Please check if your API key is correct and if you have an internet connection.")


# Start the program
if __name__ == "__main__":
    create_ux_persona()