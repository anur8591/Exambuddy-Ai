export default function Home() {
  const handleTest = async () => {
    const res = await fetch("http://127.0.0.1:8000/plan", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ syllabus: ["Chapter 1", "Chapter 2"] })
    });
    const data = await res.json();
    console.log(data);
    alert("Check console for plan output!");
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h1>ExamBuddy.AI</h1>
      <p>Welcome to your study copilot!</p>
      <button
        style={{ padding: "10px 20px", background: "#0070f3", color: "#fff", border: "none" }}
        onClick={handleTest}
      >
        Test Plan API
      </button>
    </div>
  );
}
