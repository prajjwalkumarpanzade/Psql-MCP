import QuestionForm from "./components/QuestionForm";

export default function Home() {
  return (
    <main style={{ padding: "40px", fontFamily: "sans-serif", textAlign: "center" }}>
      <h1 style={{ fontSize: "28px", marginBottom: "20px" }}>Ask Your Database</h1>
      <QuestionForm />
    </main>
  );
}
