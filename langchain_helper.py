from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def generate_pet_name():
  # temperature defines the level of creativity
  llm = OpenAI(temperature=0.7,  openai_api_key=openai_api_key)

  # using a prompt template that accepts different parameters
  prompt_template_name = PromptTemplate(
        input_variables = ['animal_type','pet_color'],
        template = "I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet."
    )

  # LLMChain allows to use llm and prompt templates together
  name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="pet_name")

  response = name_chain({'animal_type': animal_type, 'pet_color': pet_color})

  return response

if __name__ == "__main__":
    print(generate_pet_name("Dog", "Black"))