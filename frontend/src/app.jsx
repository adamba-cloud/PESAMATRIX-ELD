import { BrowserRouter, Routes, Route } from "react-router-dom";

import Dashboard from "./pages/dashboard";
import Signals from "./pages/signals";
import Payments from "./pages/payments";
import Profile from "./pages/profile";
import Admin from "./pages/admin";

function App() {
  return (
    <BrowserRouter>

      <Routes>

        <Route path="/" element={<Dashboard />} />
        <Route path="/dashboard" element={<Dashboard />} />

        <Route path="/signals" element={<Signals />} />
        <Route path="/payments" element={<Payments />} />
        <Route path="/profile" element={<Profile />} />

        {/* ADMIN ROUTE ADDED */}
        <Route path="/admin" element={<Admin />} />

      </Routes>

    </BrowserRouter>
  );
}

export default App;
