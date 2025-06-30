def sql_prompt_template(question: str, schema: str) -> str:
    return f"""
You are an expert SQL assistant.
Given this database schema:
{schema}

Generate a valid SQL query to answer:
"{question}"

- Only return the SQL query.
- No assumptions, no explanations, no prefix, no suffix.
"""

def format_mcp_prompt(records: list[dict], question: str, sql: str = None) -> str:
    context = "\n\n".join(
        f"[Record {i+1}]\n" + "\n".join(f"{k}: {v}" for k, v in r.items())
        for i, r in enumerate(records)
    )
    return f"""
You are a helpful assistant.
Only use the data provided to answer the question.
If the answer is not in the data, reply: "Data is not provided."

SQL: {sql or 'N/A'}

<>
{context}
<>

<>
{question}
""".strip()
