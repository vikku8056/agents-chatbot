import os

import chainlit as cl
from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun
from langchain.utilities import WikipediaAPIWrapper

load_dotenv()

# OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")