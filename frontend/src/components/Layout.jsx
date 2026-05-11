import React from "react";
import { Link } from "react-router-dom";

export default function Layout({ children }) {
  return (
    <div className="flex min-h-screen bg-[#0B0F19] text-white">

      {/* SIDEBAR */}
      <aside className="w-64 bg-[#111827] border-r border-gray-800 p-4">

        <h1 className="text-cyan-400 text-2xl font-bold mb-6">
          PesaMatrix
        </h1>

        <nav className="flex flex-col gap-3 text-gray-300">

          <Link to="/dashboard">Dashboard</Link>
          <Link to="/signals">Signals</Link>
          <Link to="/vip-signals">VIP Signals</Link>
          <Link to="/upload">Upload Content</Link>
          <Link to="/admin">Admin</Link>
          <Link to="/about">About</Link>

        </nav>

      </aside>

      {/* MAIN */}
      <main className="flex-1">

        {/* TOPBAR */}
        <div className="p-4 border-b border-gray-800 bg-[#111827]">
          <h2 className="text-lg font-semibold">
            Trading SaaS Dashboard
          </h2>
        </div>

        {/* CONTENT */}
        <div className="p-6">
          {children}
        </div>

      </main>

    </div>
  );
}
