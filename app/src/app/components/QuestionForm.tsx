"use client";

import { useState } from "react";

const QuestionForm = () => {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const askQuestion = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setAnswer("");

    try {
      const res = await fetch(`http://localhost:8000/ask?question=${encodeURIComponent(question)}`);
      const data = await res.json();
      setAnswer(data.answer);
    } catch (err) {
      setAnswer("Failed to fetch answer.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={askQuestion} style={{ maxWidth: "500px", margin: "0 auto" }}>
      <input
        type="text"
        value={question}
        placeholder="Ask a question..."
        onChange={(e) => setQuestion(e.target.value)}
        required
        style={{
          width: "100%",
          padding: "10px",
          fontSize: "16px",
          marginBottom: "10px",
        }}
      />
      <button
        type="submit"
        disabled={loading}
        style={{
          padding: "10px 20px",
          fontSize: "16px",
          backgroundColor: "#0070f3",
          color: "#fff",
          border: "none",
          cursor: "pointer",
        }}
      >
        {loading ? "Asking..." : "Ask"}
      </button>

      {answer && (
        <div style={{ marginTop: "20px", padding: "10px", background: "#f1f1f1" }}>
          <strong>Answer:</strong>
          <p>{answer}</p>
        </div>
      )}
    </form>
  );
};

export default QuestionForm;
