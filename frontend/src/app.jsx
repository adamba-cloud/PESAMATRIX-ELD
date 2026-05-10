import { BrowserRouter, Routes, Route } from "react-router-dom";

import Landing from "./pages/landing";
import Auth from "./pages/auth";

import Dashboard from "./pages/dashboard";
import Signals from "./pages/signals";
import Payments from "./pages/payments";
import Profile from "./pages/profile";
import Admin from "./pages/admin";

import ProtectedRoute from "./components/protectedroute";
import RoleProtectedRoute from "./components/roleprotectedroute";

function App() {
  return (
    <BrowserRouter>

      <Routes>

        {/* PUBLIC ROUTES */}
        <Route path="/" element={<Landing />} />
        <Route path="/auth" element={<Auth />} />

        {/* USER DASHBOARD */}
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />

        {/* FREE SIGNALS */}
        <Route
          path="/signals"
          element={
            <ProtectedRoute>
              <Signals />
            </ProtectedRoute>
          }
        />

        {/* VIP SIGNALS */}
        <Route
          path="/vip-signals"
          element={
            <RoleProtectedRoute allowedRole="VIP">
              <Signals />
            </RoleProtectedRoute>
          }
        />

        {/* PAYMENTS */}
        <Route
          path="/payments"
          element={
            <ProtectedRoute>
              <Payments />
            </ProtectedRoute>
          }
        />

        {/* PROFILE */}
        <Route
          path="/profile"
          element={
            <ProtectedRoute>
              <Profile />
            </ProtectedRoute>
          }
        />

        {/* ADMIN PANEL */}
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
  );
}

export default App;
