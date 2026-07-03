import { useState } from "react";
import { FaRobot, FaWallet, FaArrowTrendUp, FaCreditCard } from "react-icons/fa6";
import "./App.css";

function App() {
  const [income, setIncome] = useState("");
  const [expense, setExpense] = useState("");
  const [analysis, setAnalysis] = useState("");
  const [loading, setLoading] = useState(false);

  const incomeValue = Number(income || 0);
  const expenseValue = Number(expense || 0);
  const netProfit = incomeValue - expenseValue;

  const analyzeFinance = async () => {
    setLoading(true);
    setAnalysis("");

    try {
      const response = await fetch("http://127.0.0.1:8000/finance/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ income: incomeValue, expense: expenseValue }),
      });

      const data = await response.json();
      setAnalysis(data.analysis || "Analiz sonucu alınamadı.");
    } catch {
      setAnalysis("Backend bağlantısı kurulamadı. FastAPI çalışıyor mu kontrol et.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="page">
      <div className="glow glow-one"></div>
      <div className="glow glow-two"></div>

      <section className="dashboard">
        <header className="hero">
          <div className="logo">
            <FaRobot />
          </div>
          <div>
            <h1>Yapay Zeka Finans SaaS</h1>
            <p>Yapay zeka destekli finans analiz paneli</p>
          </div>
        </header>

        <section className="stats">
          <div className="stat-card">
            <FaWallet />
            <span>Aylık Gelir</span>
            <strong>{incomeValue.toLocaleString("tr-TR")} TL</strong>
          </div>

          <div className="stat-card">
            <FaCreditCard />
            <span>Aylık Gider</span>
            <strong>{expenseValue.toLocaleString("tr-TR")} TL</strong>
          </div>

          <div className="stat-card highlight">
            <FaArrowTrendUp />
            <span>Net Kazanç</span>
            <strong>{netProfit.toLocaleString("tr-TR")} TL</strong>
          </div>
        </section>

        <section className="panel">
          <div className="form">
            <label>
              Aylık Gelir
              <input
                type="number"
                placeholder="Örn: 35000"
                value={income}
                onChange={(e) => setIncome(e.target.value)}
              />
            </label>

            <label>
              Aylık Gider
              <input
                type="number"
                placeholder="Örn: 27000"
                value={expense}
                onChange={(e) => setExpense(e.target.value)}
              />
            </label>

            <button onClick={analyzeFinance} disabled={loading}>
              <FaRobot />
              {loading ? "Analiz ediliyor..." : "AI Analiz Et"}
            </button>
          </div>

          <div className="result">
            <h2>AI Yorumu</h2>
            <p>
              {analysis ||
                "Gelir ve gider bilgilerini girip AI Analiz Et butonuna basın."}
            </p>
          </div>
        </section>
      </section>
    </main>
  );
}

export default App;