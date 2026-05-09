import React, { useEffect, useState } from "react";

const API = "http://localhost:5000/api/admin";

export default function AdminDashboard() {

  const [data, setData] = useState(null);

  useEffect(() => {
    fetch(API + "/dashboard")
      .then(res => res.json())
      .then(setData);
  }, []);

  if (!data) return <p>Loading...</p>;

  return (
    <div>
      <h1>Admin Dashboard</h1>

      <p>Users: {data.users}</p>
      <p>Payments: {data.payments}</p>
      <p>Signals: {data.signals}</p>
      <p>Content: {data.content}</p>
      <p>Licenses: {data.licenses}</p>
      <p>Logs: {data.logs}</p>

    </div>
  );
}
