from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()  # copies .env api key (dict) to os.environ


def main():
    print("Hello from langchain-hello-world!")
    information = """
    Elon Reeve Musk (/ˈiːlɒn/ ⓘ EE-lon; born June 28, 1971) is a businessman and former public official who is the CEO and largest shareholder of Tesla and SpaceX. Musk has been the wealthiest person in the world since 2025, and became the only trillionaire in terms of US dollars in June 2026; as of July 23, 2026, Forbes estimates his net worth to be US$744 billion.
    """
    summary_template = """
    given the information {information} about a person i want you to create:
    1. A short summary
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0,model="gpt-5")  # chatopenAi is a wrapper around the openai api//api inside the class
    #llm = ChatOllama(temperature=0,model="gemma3:270m") # ollama model
    chain = summary_prompt_template | llm  #conects component /pass result to llm /llm is runnable component
    response = chain.invoke(input={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
