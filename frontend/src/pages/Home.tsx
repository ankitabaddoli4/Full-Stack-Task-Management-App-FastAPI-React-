export default function Home() {
  return (
    <div style={styles.container}>
      <h1 style={styles.title}>🚀 TaskFlow Frontend</h1>

      <p style={styles.subtitle}>
        FastAPI + React Full Stack Project is Running Successfully
      </p>

      <div style={styles.card}>
        <h2>📊 API Status</h2>
        <ul>
          <li>✔ Backend Connected (if running)</li>
          <li>✔ Frontend Working</li>
          <li>✔ Vite React Setup OK</li>
        </ul>
      </div>

      <div style={styles.card}>
        <h2>🔗 Next Steps</h2>
        <ul>
          <li>Connect Login Page</li>
          <li>Connect Register API</li>
          <li>Fetch Tasks from FastAPI</li>
        </ul>
      </div>
    </div>
  );
}

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    padding: "40px",
    fontFamily: "Arial",
    backgroundColor: "#f5f5f5",
    minHeight: "100vh",
  },
  title: {
    fontSize: "32px",
    marginBottom: "10px",
  },
  subtitle: {
    fontSize: "16px",
    marginBottom: "20px",
    color: "#555",
  },
  card: {
    background: "#fff",
    padding: "20px",
    marginBottom: "20px",
    borderRadius: "10px",
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
  },
};