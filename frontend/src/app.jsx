import { BrowserRouter, Routes, Route } from "react-router-dom";

import Landing from "./pages/landing";
import Auth from "./pages/auth";
import Dashboard from "./pages/dashboard";
import Signals from "./pages/signals";
import Payments from "./pages/payments";
import Profile from "./pages/profile";
import Admin from "./pages/admin";

function App() {
  return (
    <BrowserRouter>

      <Routes>

        {/* LANDING PAGE */}
        <Route path="/" element={<Landing />} />

        {/* AUTH PAGE */}
        <Route path="/auth" element={<Auth />} />

        {/* MAIN APP PAGES */}
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/signals" element={<Signals />} />
        <Route path="/payments" element={<Payments />} />
        <Route path="/profile" element={<Profile />} />

        {/* ADMIN */}
        <Route path="/admin" element={<Admin />} />

      </Routes>

    </BrowserRouter>
  );
}

export default App;
