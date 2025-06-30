from db import get_connection, get_table_schema_json
from llm import generate_sql_with_claude, ask_claude_mcp

def query_and_answer(question: str) -> str:
    schema = get_table_schema_json()
    sql_query = generate_sql_with_claude(question, schema)
    print("-------------------", sql_query)

    if not sql_query or not sql_query.strip().upper().startswith("SELECT"):
        return f"Blocked non-SELECT query: {sql_query}"

    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(sql_query)
        rows = cur.fetchall()
        if not rows:
            return "No data found for your question."
    except Exception as e:
        return f"SQL Error: {e}"
    finally:
        cur.close()
        conn.close()

    return ask_claude_mcp(rows, question, sql_query)
