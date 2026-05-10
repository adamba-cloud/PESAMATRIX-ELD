import { BrowserRouter, Routes, Route } from "react-router-dom";

import Landing from "./pages/landing";
import Auth from "./pages/auth";

import Dashboard from "./pages/dashboard";
import Signals from "./pages/signals";
import Payments from "./pages/payments";
import Profile from "./pages/profile";
import Admin from "./pages/admin";

import ProtectedRoute from "./components/protectedroute";

function App() {
  return (
    <BrowserRouter>

      <Routes>

        {/* PUBLIC ROUTES */}
        <Route path="/" element={<Landing />} />
        <Route path="/auth" element={<Auth />} />

        {/* PROTECTED ROUTES */}
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />

        <Route
          path="/signals"
          element={
            <ProtectedRoute>
              <Signals />
            </ProtectedRoute>
          }
        />

        <Route
          path="/payments"
          element={
            <ProtectedRoute>
              <Payments />
            </ProtectedRoute>
          }
        />

        <Route
          path="/profile"
          element={
            <ProtectedRoute>
              <Profile />
            </ProtectedRoute>
          }
        />

        <Route
          path="/admin"
          element={
            <ProtectedRoute>
              <Admin />
            </ProtectedRoute>
          }
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;
