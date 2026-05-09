import React, { useEffect, useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

export default function AdminDashboard() {
  const [stats, setStats] = useState({
    users: 0,
    payments: 0,
    signals: 0,
    content: 0,
    logs: 0,
    licenses: 0,
  });

  const [users, setUsers] = useState([]);
  const [payments, setPayments] = useState([]);
  const [signals, setSignals] = useState([]);
  const [content, setContent] = useState([]);
  const [logs, setLogs] = useState([]);
  const [licenses, setLicenses] = useState([]);

  const [activeTab, setActiveTab] = useState("dashboard");
  const [loading, setLoading] = useState(true);

  // 🔥 CHANGE THIS IN PRODUCTION
  const API = "http://localhost:5000/superadmin";

  useEffect(() => {
    fetchAll();
  }, []);

  async function fetchAll() {
    setLoading(true);

    try {
      const res = await fetch(`${API}/dashboard-data`, {
        credentials: "include",
      });

      const data = await res.json();

      setStats(data.stats || {});
      setUsers(data.users || []);
      setPayments(data.payments || []);
      setSignals(data.signals || []);
      setContent(data.content || []);
      setLogs(data.logs || []);
      setLicenses(data.licenses || []);
    } catch (err) {
      console.error("API error:", err);
    }

    setLoading(false);
  }

  return (
    <div className="min-h-screen bg-gray-950 text-white p-6">

      {/* HEADER */}
      <h1 className="text-2xl font-bold mb-6">
        🛠 Super Admin Dashboard
      </h1>

      {/* NAVIGATION */}
      <div className="flex flex-wrap gap-2 mb-6">
        {[
          "dashboard",
          "users",
          "payments",
          "signals",
          "content",
          "licenses",
          "logs",
        ].map((tab) => (
          <Button key={tab} onClick={() => setActiveTab(tab)}>
            {tab.toUpperCase()}
          </Button>
        ))}
      </div>

      {/* ================= DASHBOARD ================= */}
      {activeTab === "dashboard" && (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">

          <Card>
            <CardContent className="p-4">
              <h2>👤 Users</h2>
              <p className="text-3xl">{stats.users}</p>
            </CardContent>
          </Card>

          <Card>
            <CardContent className="p-4">
              <h2>💳 Payments</h2>
              <p className="text-3xl">{stats.payments}</p>
            </CardContent>
          </Card>

          <Card>
            <CardContent className="p-4">
              <h2>📊 Signals</h2>
              <p className="text-3xl">{stats.signals}</p>
            </CardContent>
          </Card>

          <Card>
            <CardContent className="p-4">
              <h2>📁 Content</h2>
              <p className="text-3xl">{stats.content}</p>
            </CardContent>
          </Card>

          <Card>
            <CardContent className="p-4">
              <h2>🔐 Licenses</h2>
              <p className="text-3xl">{stats.licenses}</p>
            </CardContent>
          </Card>

          <Card>
            <CardContent className="p-4">
              <h2>📡 Logs</h2>
              <p className="text-3xl">{stats.logs}</p>
            </CardContent>
          </Card>

        </div>
      )}

      {/* ================= USERS ================= */}
      {activeTab === "users" && (
        <div className="space-y-3">
          <h2 className="text-xl mb-3">👥 Users</h2>

          {users.map((u) => (
            <Card key={u.id}>
              <CardContent className="p-3 flex justify-between">
                <div>
                  <p className="font-bold">{u.name}</p>
                  <p>{u.email}</p>
                  <p className="text-sm text-gray-400">{u.role}</p>
                </div>

                <Button>Manage</Button>
              </CardContent>
            </Card>
          ))}
        </div>
      )}

      {/* ================= PAYMENTS ================= */}
      {activeTab === "payments" && (
        <div className="space-y-3">
          <h2 className="text-xl mb-3">💳 Payments (M-Pesa)</h2>

          {payments.map((p) => (
            <Card key={p.id}>
              <CardContent className="p-3">
                <p>📱 {p.phone}</p>
                <p>💰 {p.amount}</p>
                <p>📦 {p.plan}</p>
                <p>Status: {p.status}</p>
                <p>Ref: {p.mpesa_code}</p>
              </CardContent>
            </Card>
          ))}
        </div>
      )}

      {/* ================= SIGNALS ================= */}
      {activeTab === "signals" && (
        <div className="space-y-3">
          <h2 className="text-xl mb-3">📊 Trading Signals</h2>

          {signals.map((s) => (
            <Card key={s.id}>
              <CardContent className="p-3">
                <p>📈 Asset: {s.asset}</p>
                <p>Entry: {s.entry}</p>
                <p>TP: {s.tp}</p>
                <p>SL: {s.sl}</p>
                <p>Status: {s.status}</p>
              </CardContent>
            </Card>
          ))}
        </div>
      )}

      {/* ================= CONTENT ================= */}
      {activeTab === "content" && (
        <div className="space-y-3">
          <h2 className="text-xl mb-3">📁 Content Library</h2>

          {content.map((c) => (
            <Card key={c.id}>
              <CardContent className="p-3">
                <p>📌 {c.title}</p>
                <p>Type: {c.type}</p>
                <a
                  href={c.link}
                  target="_blank"
                  className="text-blue-400"
                >
                  Open
                </a>
              </CardContent>
            </Card>
          ))}
        </div>
      )}

      {/* ================= LICENSES ================= */}
      {activeTab === "licenses" && (
        <div className="space-y-3">
          <h2 className="text-xl mb-3">🔐 Access Licenses</h2>

          {licenses.map((l) => (
            <Card key={l.id}>
              <CardContent className="p-3">
                <p>Code: {l.code}</p>
                <p>User: {l.user_id}</p>
                <p>Used: {l.used}</p>
                <p>Status: {l.status}</p>
              </CardContent>
            </Card>
          ))}
        </div>
      )}

      {/* ================= LOGS ================= */}
      {activeTab === "logs" && (
        <div className="space-y-3">
          <h2 className="text-xl mb-3">📡 System Logs</h2>

          {logs.map((l, i) => (
            <Card key={i}>
              <CardContent className="p-3">
                <p>{l.method} - {l.path}</p>
                <p>{l.ip_address}</p>
                <p>{l.timestamp}</p>
              </CardContent>
            </Card>
          ))}
        </div>
      )}

    </div>
  );
}
