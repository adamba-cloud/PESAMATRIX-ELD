import React from "react"
import { Link } from "react-router-dom"
import { signOut } from "../auth"

export default function Layout({ children }) {
  async function handleLogout() {
    await signOut()
    window.location.href = "/auth"
  }

  return (
    <div style={{ display: "flex", minHeight: "100vh" }}>

      {/* SIDEBAR */}
      <aside
        style={{
          width: "240px",
          background: "#111827",
          color: "white",
          padding: "20px",
        }}
      >
        <h2>Adamba Cloud</h2>

        <nav style={{ display: "flex", flexDirection: "column", gap: "12px" }}>
          <Link to="/dashboard" style={linkStyle}>Dashboard</Link>
          <Link to="/signals" style={linkStyle}>Signals</Link>
          <Link to="/vip-signals" style={linkStyle}>VIP</Link>
          <Link to="/payments" style={linkStyle}>Payments</Link>
          <Link to="/profile" style={linkStyle}>Profile</Link>
          <Link to="/admin" style={linkStyle}>Admin</Link>
        </nav>

        <button
          onClick={handleLogout}
          style={{
            marginTop: "30px",
            padding: "10px",
            width: "100%",
            border: "none",
            cursor: "pointer",
          }}
        >
          Logout
        </button>
      </aside>

      {/* MAIN CONTENT */}
      <main style={{ flex: 1, background: "#f3f4f6" }}>

        {/* TOPBAR */}
        <header
          style={{
            background: "white",
            padding: "16px",
            borderBottom: "1px solid #ddd",
          }}
        >
          <h3>Modern SaaS Dashboard</h3>
        </header>

        {/* PAGE CONTENT */}
        <div style={{ padding: "20px" }}>
          {children}
        </div>

      </main>
    </div>
  )
}

const linkStyle = {
  color: "white",
  textDecoration: "none",
}
