import Sidebar from "../components/Sidebar";
import StatCard from "../components/StatCard";

export default function Dashboard() {
  return (
    <div className="flex bg-[#0B0F19] text-white min-h-screen">

      <Sidebar />

      <div className="flex-1 p-6">

        <h1 className="text-3xl font-bold mb-6 text-cyan-400">
          User Dashboard
        </h1>

        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">

          <StatCard title="Total Signals" value="12" />
          <StatCard title="VIP Status" value="ACTIVE" color="green" />
          <StatCard title="Plan" value="FREE" color="yellow" />

        </div>

        {/* Signal Preview */}
        <div className="mt-8">
          <h2 className="text-xl mb-4">Latest Signals</h2>

          <div className="grid gap-3">

            <div className="p-4 bg-green-900/20 border border-green-500 rounded">
              BUY EURUSD @ 1.0850
            </div>

            <div className="p-4 bg-red-900/20 border border-red-500 rounded">
              SELL XAUUSD @ 2340
            </div>

          </div>

        </div>

      </div>

    </div>
  );
}
