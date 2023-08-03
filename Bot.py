import openai

class ChatGPTBotAPI:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        openai.api_key = openai_api_key
        self.prompts = []  # List to store user-provided prompts

    def create_prompt(self, prompt):
        """
        Takes a user-provided prompt as input and stores it for later interactions with the ChatGPT bot.
        """
        self.prompts.append(prompt)

    def get_response(self, prompt_index):
        """
        Takes the index of a previously stored prompt and returns the ChatGPT bot's response to that prompt.
        """
        if prompt_index < 0 or prompt_index >= len(self.prompts):
            raise ValueError("Invalid prompt index. Prompt index out of range.")

        prompt = self.prompts[prompt_index]

        # Call the OpenAI API to get the ChatGPT response
        response = openai.Completion.create(
            engine="text-davinci-002",  # You can use other engines as well
            prompt=prompt,
            max_tokens=100  # Adjust this value as needed for response length
        )

        return response.choices[0].text.strip()

    def update_prompt(self, prompt_index, new_prompt):
        """
        Updates an existing prompt at the given index with a new prompt provided by the user.
        """
        if prompt_index < 0 or prompt_index >= len(self.prompts):
            raise ValueError("Invalid prompt index. Prompt index out of range.")

        self.prompts[prompt_index] = new_prompt
