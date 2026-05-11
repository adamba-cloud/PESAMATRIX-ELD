import React, { useState } from "react";
import { Link } from "react-router-dom";

import { signOut } from "../auth";

export default function Layout({ children }) {
  const [mobileMenu, setMobileMenu] = useState(false);

  async function handleLogout() {
    await signOut();
    window.location.href = "/auth";
  }

  return (
    <div className="flex min-h-screen bg-[#0B0F19] text-white">

      {/* MOBILE OVERLAY */}
      {mobileMenu && (
        <div
          className="fixed inset-0 bg-black/50 z-40 lg:hidden"
          onClick={() => setMobileMenu(false)}
        />
      )}

      {/* SIDEBAR */}
      <aside
        className={`
          fixed lg:static z-50 top-0 left-0 h-full
          w-64 bg-[#111827]/95 backdrop-blur-xl
          border-r border-gray-800
          transform transition-transform duration-300
          ${mobileMenu ? "translate-x-0" : "-translate-x-full"}
          lg:translate-x-0
        `}
      >

        {/* LOGO */}
        <div className="p-6 border-b border-gray-800">

          <h1 className="text-2xl font-bold text-cyan-400">
            Adamba Cloud
          </h1>

          <p className="text-gray-400 text-sm mt-1">
            Modern Trading SaaS Platform
          </p>

        </div>

        {/* NAVIGATION */}
        <nav className="p-4 flex flex-col gap-2">

          <NavItem to="/dashboard" label="Dashboard" />
          <NavItem to="/signals" label="Signals" />
          <NavItem to="/vip-signals" label="VIP Signals" />
          <NavItem to="/payments" label="Payments" />
          <NavItem to="/profile" label="Profile" />
          <NavItem to="/admin" label="Admin" />

        </nav>

        {/* USER SECTION */}
        <div className="absolute bottom-0 left-0 w-full p-4 border-t border-gray-800 bg-[#111827]">

          <div className="flex items-center gap-3 mb-4">

            <div className="w-10 h-10 rounded-full bg-cyan-500 flex items-center justify-center font-bold">
              A
            </div>

            <div>
              <p className="font-medium text-white">
                Admin User
              </p>

              <p className="text-gray-400 text-sm">
                VIP Trader
              </p>
            </div>

          </div>

          <button
            onClick={handleLogout}
            className="
              w-full py-2 rounded-lg
              bg-red-500 hover:bg-red-600
              transition-colors duration-200
            "
          >
            Logout
          </button>

        </div>

      </aside>

      {/* MAIN CONTENT */}
      <div className="flex-1 flex flex-col lg:ml-0">

        {/* TOPBAR */}
        <header
          className="
            sticky top-0 z-30
            bg-[#111827]/80 backdrop-blur-xl
            border-b border-gray-800
          "
        >

          <div className="flex items-center justify-between px-6 py-4">

            {/* MOBILE MENU BUTTON */}
            <button
              onClick={() => setMobileMenu(true)}
              className="
                lg:hidden text-white text-2xl
                hover:text-cyan-400 transition-colors
              "
            >
              ☰
            </button>

            {/* TITLE */}
            <div>

              <h2 className="text-lg font-semibold text-white">
                Modern SaaS Dashboard
              </h2>

              <p className="text-sm text-gray-400">
                Trading Control Center
              </p>

            </div>

            {/* STATUS */}
            <div className="flex items-center gap-3">

              <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />

              <span className="text-sm text-gray-300">
                Live Market Active
              </span>

            </div>

          </div>

        </header>

        {/* PAGE CONTENT */}
        <main className="flex-1 p-6 overflow-y-auto">

          {children}

        </main>

      </div>

    </div>
  );
}

/* NAVIGATION ITEM */
function NavItem({ to, label }) {
  return (
    <Link
      to={to}
      className="
        block px-4 py-3 rounded-lg
