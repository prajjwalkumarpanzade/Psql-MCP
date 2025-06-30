from langchain_anthropic import ChatAnthropic
from prompts import sql_prompt_template, format_mcp_prompt
from dotenv import load_dotenv

load_dotenv()

sql_generator = ChatAnthropic(model="claude-3-5-haiku-20241022", temperature=0.1)
cloaude_mcp = ChatAnthropic(model="claude-3-5-haiku-20241022", temperature=0.2)

def generate_sql_with_claude(question: str, schema: str) -> str:
    prompt = sql_prompt_template(question, schema)
    response = sql_generator.invoke(prompt)
    return response.content.strip().split(";")[0]  # Remove junk if needed


def ask_claude_mcp(records: list[dict], question: str, sql: str) -> str:
    prompt = format_mcp_prompt(records, question, sql)
    response = cloaude_mcp.invoke(prompt)
    return response.content
