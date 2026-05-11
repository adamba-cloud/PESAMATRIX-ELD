export default function Dashboard() {
  return (
    <div>

      <h1 className="text-2xl font-bold mb-6">Dashboard Overview</h1>

      {/* STATS */}
      <div className="grid md:grid-cols-3 gap-4">

        <div className="bg-[#111827] p-5 rounded-xl border border-gray-800">
          <h3 className="text-gray-400">Active Signals</h3>
          <p className="text-3xl text-cyan-400 font-bold">12</p>
        </div>

        <div className="bg-[#111827] p-5 rounded-xl border border-gray-800">
          <h3 className="text-gray-400">VIP Users</h3>
          <p className="text-3xl text-cyan-400 font-bold">48</p>
        </div>

        <div className="bg-[#111827] p-5 rounded-xl border border-gray-800">
          <h3 className="text-gray-400">Win Rate</h3>
          <p className="text-3xl text-green-400 font-bold">87%</p>
        </div>

      </div>

      {/* LIVE PANEL */}
      <div className="mt-6 bg-[#111827] p-6 rounded-xl border border-gray-800">
        <h2 className="text-lg font-semibold mb-3">Live Market Feed</h2>
        <p className="text-gray-400">
          Connected systems will display live trade signals here.
        </p>
      </div>

    </div>
  );
}
