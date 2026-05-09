import React, { useEffect, useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

export default function AdminDashboard() {

  // =========================
  // STATE
  // =========================
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
  const [error, setError] = useState(null);

  // =========================
  // API BASE (CHANGE IN PROD)
  // =========================
  const API = "http://localhost:5000/superadmin";

  // =========================
  // FETCH DATA
  // =========================
  useEffect(() => {
    loadDashboard();
  }, []);

  async function loadDashboard() {
    setLoading(true);
    setError(null);

    try {
      const res = await fetch(`${API}/dashboard-data`, {
        method: "GET",
        credentials: "include",
      });

      if (!res.ok) {
        throw new Error("Failed to fetch dashboard data");
      }

      const data = await res.json();

      setStats(data.stats || {});
      setUsers(data.users || []);
      setPayments(data.payments || []);
      setSignals(data.signals || []);
      setContent(data.content || []);
      setLogs(data.logs || []);
      setLicenses(data.licenses || []);

    } catch (err) {
      console.error(err);
      setError("⚠️ Failed to load dashboard");
    }

    setLoading(false);
  }

  // =========================
  // LOADING STATE
  // =========================
  if (loading) {
    return (
      <div className="p-6 text-white bg-gray-950 min-h-screen">
        <h2>Loading dashboard...</h2>
      </div>
    );
  }

  // =========================
  // ERROR STATE
  // =========================
  if (error) {
    return (
      <div className="p-6 text-red-500 bg-gray-950 min-h-screen">
        <h2>{error}</h2>
        <Button onClick={loadDashboard}>Retry</Button>
      </div>
    );
  }

  // =========================
  // UI
  // =========================
  return (
    <div className="min-h-screen bg-gray-950 text-white p-6">

      {/* HEADER */}
      <h1 className="text-2xl font-bold mb-6">
        🛠 Super Admin SaaS Dashboard
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
          <Button
            key={tab}
            onClick={() => setActiveTab(tab)}
            className={activeTab === tab ? "bg-blue-600" : ""}
          >
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
        <div>
          <h2 className="text-xl mb-3">👥 Users</h2>

          <div className="space-y-3">
            {users.map((u) => (
              <Card key={u.id}>
                <CardContent className="p-3 flex justify-between">
                  <div>
                    <p className="font-bold">{u.name}</p>
                    <p>{u.email}</p>
                    <p className="text-gray-400 text-sm">{u.role}</p>
                  </div>
                  <Button>Manage</Button>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      )}

      {/* ================= PAYMENTS ================= */}
      {activeTab === "payments" && (
        <div>
          <h2 className="text-xl mb-3">💳 M-Pesa Payments</h2>

          <div className="space-y-3">
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
        </div>
      )}

      {/* ================= SIGNALS ================= */}
      {activeTab === "signals" && (
        <div>
          <h2 className="text-xl mb-3">📊 Trading Signals</h2>

          <div className="space-y-3">
            {signals.map((s) => (
              <Card key={s.id}>
                <CardContent className="p-3">
                  <p>📈 {s.asset}</p>
                  <p>Entry: {s.entry}</p>
                  <p>TP: {s.tp}</p>
                  <p>SL: {s.sl}</p>
                  <p>Status: {s.status}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      )}

      {/* ================= CONTENT ================= */}
      {activeTab === "content" && (
        <div>
          <h2 className="text-xl mb-3">📁 Content Library</h2>

          <div className="space-y-3">
            {content.map((c) => (
              <Card key={c.id}>
                <CardContent className="p-3">
                  <p>{c.title}</p>
                  <p className="text-gray-400">{c.type}</p>
                  <a href={c.link} className="text-blue-400">
                    Open
                  </a>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      )}

      {/* ================= LICENSES ================= */}
      {activeTab === "licenses" && (
        <div>
          <h2 className="text-xl mb-3">🔐 Access Licenses</h2>

          <div className="space-y-3">
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
        </div>
      )}

      {/* ================= LOGS ================= */}
      {activeTab === "logs" && (
        <div>
          <h2 className="text-xl mb-3">📡 System Logs</h2>

          <div className="space-y-3">
            {logs.map((l, i) => (
              <Card key={i}>
                <CardContent className="p-3">
                  <p>{l.method} {l.path}</p>
                  <p>{l.ip_address}</p>
                  <p className="text-gray-400">{l.timestamp}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      )}

    </div>
  );
}
