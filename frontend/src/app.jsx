import React from "react"
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"

import Landing from "./pages/landing"
import Auth from "./pages/auth"

import Dashboard from "./pages/dashboard"
import Signals from "./pages/signals"
import Payments from "./pages/payments"
import Profile from "./pages/profile"
import Admin from "./pages/admin"

import { getUser } from "./auth"

import ProtectedRoute from "./components/protectedroute"
import RoleProtectedRoute from "./components/roleprotectedroute"

//
// 🔐 SIMPLE AUTH GUARD (fixes your earlier version)
//
function AuthGuard({ children }) {
  const [user, setUser] = React.useState(null)
  const [loading, setLoading] = React.useState(true)

  React.useEffect(() => {
    async function checkUser() {
      const u = await getUser()
      setUser(u)
      setLoading(false)
    }
    checkUser()
  }, [])

  if (loading) return <p>Loading...</p>

  return user ? children : <Navigate to="/auth" />
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>

        {/* 🌐 PUBLIC ROUTES */}
        <Route path="/" element={<Landing />} />
        <Route path="/auth" element={<Auth />} />

        {/* 📊 PROTECTED USER ROUTES */}
        <Route
          path="/dashboard"
          element={
            <AuthGuard>
              <Dashboard />
            </AuthGuard>
          }
        />

        <Route
          path="/signals"
          element={
            <AuthGuard>
              <Signals />
            </AuthGuard>
          }
        />

        <Route
          path="/payments"
          element={
            <AuthGuard>
              <Payments />
            </AuthGuard>
          }
        />

        <Route
          path="/profile"
          element={
            <AuthGuard>
              <Profile />
            </AuthGuard>
          }
        />

        {/* 💎 VIP ROUTE */}
        <Route
          path="/vip-signals"
          element={
            <RoleProtectedRoute allowedRole="VIP">
              <Signals />
            </RoleProtectedRoute>
          }
        />

        {/* 🛡️ ADMIN ROUTE */}
        <Route
          path="/admin"
          element={
            <RoleProtectedRoute allowedRole="ADMIN">
              <Admin />
            </RoleProtectedRoute>
          }
        />

      </Routes>
    </BrowserRouter>
  )
}
