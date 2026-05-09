import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <div className="w-64 h-screen bg-[#0B0F19] text-white p-5 border-r border-gray-800">
      
      <h1 className="text-2xl font-bold text-cyan-400 mb-10">
        TradePro SaaS
      </h1>

      <nav className="flex flex-col gap-4">
        <Link className="hover:text-cyan-400" to="/dashboard">Dashboard</Link>
        <Link className="hover:text-cyan-400" to="/signals">Signals</Link>
        <Link className="hover:text-cyan-400" to="/payments">Payments</Link>
        <Link className="hover:text-cyan-400" to="/profile">Profile</Link>
      </nav>

      <div className="mt-10 p-3 bg-green-900/30 rounded text-green-400 text-sm">
        VIP system active
      </div>
    </div>
  );
}
