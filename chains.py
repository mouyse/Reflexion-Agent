import datetime
from dotenv import load_dotenv

from schemas import AnswerQuestion

load_dotenv()

from langchain_core.output_parsers.openai_tools import (
    JsonOutputToolsParser,
    PydanticToolsParser
)

from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from schemas import AnswerQuestion

llm = ChatOpenAI(model="gpt4-turbo-preview")
parser = JsonOutputToolsParser(return_id=True)
parser_pydentic = PydanticToolsParser(tools=[AnswerQuestion])

actor_prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
                You are expert researcher.
                Current Time: {time}
                
                1. {first_instruction}
                2. Reflect and critique your answer. Be severe to maximize improvement.
                3. Recommend search queries to research information and improve your answer 
            """
        ),
        MessagesPlaceholder(variable_name="messages"),
        ("system", "Answer the user's question above using the required format")
    ]
).partial(
    time=lambda: datetime.datetime.now().isoformat(),
)

first_responder_prompt_template = actor_prompt_template.partial(
    first_instruction = "Provide a detailed ~250 word answer"
)

first_responder = first_responder_prompt_template | llm.bind_tools(
    tools = [AnswerQuestion], tool_choice="AnswerQuestion"
)

if __name__ == "__main__":
    human_message = HumanMessage(
        content="Write about how the India sensex will behave in upcoming a week or a month's time based on the trending geopolitical and economical matters. List down the possible ranges that it can move and the provide the suggestions on some of the stocks that could provide enormous returns in a week or a month's time."
    )
    chain = (
        first_responder_prompt_template
        | llm.bind_tools(tools = [AnswerQuestion], tool_choice="AnswerQuestion")
        | parser_pydentic
    )
    res = chain.invoke(input = {"messages": [human_message]})
    print(res)