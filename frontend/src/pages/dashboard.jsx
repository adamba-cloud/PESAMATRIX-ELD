import Sidebar from "../components/sidebar";
import StatCard from "../components/statcard";

export default function Dashboard() {
  return (
    <div className="flex min-h-screen bg-[#0B0F19] text-white">

      {/* Sidebar */}
      <Sidebar />

      {/* Main Content */}
      <div className="flex-1 p-6">

        {/* Header */}
        <div className="mb-6">
          <h1 className="text-3xl font-bold text-cyan-400">
            Dashboard
          </h1>
          <p className="text-gray-400 mt-1">
            Welcome back to your trading control center
          </p>
        </div>

        {/* Stats Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">

          <StatCard title="Total Signals" value="128" />
          <StatCard title="Win Rate" value="82%" />
          <StatCard title="Active Plan" value="VIP" />

        </div>

        {/* Live Activity Panel */}
        <div className="mt-8 bg-[#111827] border border-gray-800 rounded-lg p-5">

          <h2 className="text-xl font-semibold text-white mb-3">
            Live Market Overview
          </h2>

          <div className="space-y-2 text-gray-400 text-sm">

            <p>• EUR/USD BUY signal updated</p>
            <p>• XAUUSD volatility increasing</p>
            <p>• BTCUSDT trend bullish continuation</p>

          </div>

        </div>

        {/* Quick Info Cards */}
        <div className="mt-8 grid grid-cols-1 md:grid-cols-2 gap-4">

          <div className="bg-[#111827] p-5 rounded-lg border border-gray-800">
            <h3 className="text-cyan-400 font-semibold">Performance</h3>
            <p className="text-gray-400 mt-2">
              Your account is performing above average this week.
            </p>
          </div>

          <div className="bg-[#111827] p-5 rounded-lg border border-gray-800">
            <h3 className="text-cyan-400 font-semibold">Subscription</h3>
            <p className="text-gray-400 mt-2">
              VIP access active with full signal privileges.
            </p>
          </div>

        </div>

      </div>
    </div>
  );
}
