import React, { useState } from "react";
import { PieChart, Pie, Cell, Tooltip, Legend, ResponsiveContainer } from 'recharts';


function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const COLORS = ["#0088FE", "#00C49F", "#FFBB28", "#FF8042", "#AA336A", "#8884D8"];


  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
  if (!file) {
    alert("Please select a file first!");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await fetch("http://127.0.0.1:5000/upload", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    setResult(data);
  } catch (error) {
    console.error("Error uploading file:", error);
  }
};
const chartData = result && result.analysis
  ? Object.entries(result.analysis.summary).map(([key, value]) => ({
      name: key,
      value: Math.abs(value)  // use absolute value for chart
    }))
  : [];


  return (
    <div style={{ padding: "20px" }}>
  <h2>AI-FinAdvisor: Upload Your Bank Statement</h2>
  <input type="file" onChange={(e) => setFile(e.target.files[0])} />
  <button onClick={handleUpload}>Upload</button>

  {result && (
    <div style={{ marginTop: "20px" }}>
      <h3>Transactions:</h3>
      {result.transactions.map((t, i) => (
        <div key={i}>
          <strong>{t.date}</strong> - {t.description} - ₹{t.amount} - {t.category}
        </div>
      ))}

      {result.analysis && (
        <div style={{ marginTop: "20px" }}>
          <h3>Summary:</h3>
          <pre>{JSON.stringify(result.analysis.summary, null, 2)}</pre>
          {chartData.length > 0 && (
  <div style={{ width: "100%", height: 300, marginTop: "20px" }}>
    <h3>Spending by Category:</h3>
    <ResponsiveContainer>
      <PieChart>
        <Pie
          data={chartData}
          dataKey="value"
          nameKey="name"
          cx="50%"
          cy="50%"
          outerRadius={100}
          fill="#8884d8"
          label
        >
          {chartData.map((entry, index) => (
            <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
          ))}
        </Pie>
        <Tooltip />
        <Legend />
      </PieChart>
    </ResponsiveContainer>
  </div>
)}


          <h3>Advice:</h3>
          <ul>
            {result.analysis.advice.map((a, i) => (
              <li key={i}>{a}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  )}
</div>

  );
}

export default App;
