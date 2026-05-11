import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from "./components/Layout";

import Landing from "./pages/Landing";
import Dashboard from "./pages/Dashboard";
import Admin from "./pages/Admin";
import Signals from "./pages/Signals";
import VIPSignals from "./pages/VIPSignals";
import UploadContent from "./pages/UploadContent";
import About from "./pages/About";

export default function App() {
  return (
    <BrowserRouter>

      <Routes>

        {/* PUBLIC */}
        <Route path="/" element={<Landing />} />
        <Route path="/about" element={<About />} />

        {/* APP (WITH LAYOUT) */}
        <Route
          path="/dashboard"
          element={
            <Layout>
              <Dashboard />
            </Layout>
          }
        />

        <Route
          path="/admin"
          element={
            <Layout>
              <Admin />
            </Layout>
          }
        />

        <Route
          path="/signals"
          element={
            <Layout>
              <Signals />
            </Layout>
          }
        />

        <Route
          path="/vip-signals"
          element={
            <Layout>
              <VIPSignals />
            </Layout>
          }
        />

        <Route
          path="/upload"
          element={
            <Layout>
              <UploadContent />
            </Layout>
          }
        />

      </Routes>

    </BrowserRouter>
  );
}
