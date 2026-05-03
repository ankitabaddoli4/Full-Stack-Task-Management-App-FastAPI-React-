import { useEffect, useState } from "react";
import { getTasks } from "../services/api";

export default function Dashboard() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    getTasks().then(res => setTasks(res.data));
  }, []);

  return (
    <div>
      <h2>📊 Dashboard</h2>
      {tasks.map((t: any) => (
        <p key={t.id}>{t.title}</p>
      ))}
    </div>
  );
}
