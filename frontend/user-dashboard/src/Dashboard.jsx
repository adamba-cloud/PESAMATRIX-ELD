import React, { useEffect, useState } from "react";

const API = "http://localhost:5000/api/user";

export default function Dashboard() {

  const [data, setData] = useState(null);

  useEffect(() => {
    fetch(API + "/dashboard")
      .then(res => res.json())
      .then(setData);
  }, []);

  if (!data) return <p>Loading...</p>;

  return (
    <div>
      <h1>User Dashboard</h1>

      <h2>{data.user.name}</h2>
      <p>Plan: {data.user.plan}</p>

      <p>Signals: {data.stats.signals}</p>
      <p>Content: {data.stats.content}</p>

    </div>
  );
}
