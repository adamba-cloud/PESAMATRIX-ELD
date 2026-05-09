import Sidebar from "../components/sidebar";

export default function Signals() {
  return (
    <div className="flex min-h-screen bg-[#0B0F19] text-white">

      {/* Sidebar */}
      <Sidebar />

      {/* Main Content */}
      <div className="flex-1 p-6">

        <h1 className="text-3xl font-bold text-cyan-400 mb-2">
          Trading Signals
        </h1>

        <p className="text-gray-400 mb-6">
          Live BUY / SELL signals from the system
        </p>

        {/* Signals List */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">

          {/* BUY Signal */}
          <div className="bg-[#111827] border border-green-600 rounded-lg p-5 hover:scale-[1.02] transition">

            <h2 className="text-green-400 font-bold text-lg">
              BUY - XAUUSD
            </h2>

            <p className="text-gray-400 mt-2 text-sm">
              Entry: 3320
            </p>
            <p className="text-gray-400 text-sm">
              TP: 3350
            </p>
            <p className="text-gray-400 text-sm">
              SL: 3300
            </p>

          </div>

          {/* SELL Signal */}
          <div className="bg-[#111827] border border-red-600 rounded-lg p-5 hover:scale-[1.02] transition">

            <h2 className="text-red-400 font-bold text-lg">
              SELL - EURUSD
            </h2>

            <p className="text-gray-400 mt-2 text-sm">
              Entry: 1.1200
            </p>
            <p className="text-gray-400 text-sm">
              TP: 1.1100
            </p>
            <p className="text-gray-400 text-sm">
              SL: 1.1250
            </p>

          </div>

          {/* BUY Signal */}
          <div className="bg-[#111827] border border-green-600 rounded-lg p-5 hover:scale-[1.02] transition">

            <h2 className="text-green-400 font-bold text-lg">
              BUY - BTCUSDT
            </h2>

            <p className="text-gray-400 mt-2 text-sm">
              Entry: 95000
            </p>
            <p className="text-gray-400 text-sm">
              TP: 98000
            </p>
            <p className="text-gray-400 text-sm">
              SL: 93000
            </p>

          </div>

        </div>

      </div>
    </div>
  );
}
