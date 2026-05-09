import Sidebar from "../components/sidebar";
import API from "../api/api";

export default function Payments() {

  // PAYMENT LOGIC
  const upgrade = async () => {
    try {
      const res = await API.post("/payments/subscribe-vip");
      alert(res.data.message);
    } catch (err) {
      alert("Upgrade failed");
      console.log(err);
    }
  };

  return (
    <div className="flex min-h-screen bg-[#0B0F19] text-white">

      {/* Sidebar */}
      <Sidebar />

      {/* Main Content */}
      <div className="flex-1 p-6">

        {/* Header */}
        <h1 className="text-3xl font-bold text-cyan-400 mb-2">
          Subscription & Payments
        </h1>

        <p className="text-gray-400 mb-6">
          Upgrade your account to unlock VIP trading signals
        </p>

        {/* Current Status */}
        <div className="bg-[#111827] border border-gray-800 rounded-lg p-5 mb-6">

          <h2 className="text-lg font-semibold text-white mb-2">
            Current Plan
          </h2>

          <div className="flex items-center justify-between">

            <p className="text-gray-400">
              You are currently on:
            </p>

            <span className="px-3 py-1 rounded bg-yellow-500/20 text-yellow-400 text-sm">
              FREE PLAN
            </span>

          </div>

        </div>

        {/* Upgrade Options */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">

          {/* VIP Plan */}
          <div className="bg-[#111827] border border-cyan-500 rounded-lg p-5 hover:scale-[1.02] transition">

            <h2 className="text-cyan-400 font-bold text-xl">
              VIP PLAN
            </h2>

            <p className="text-gray-400 mt-2 text-sm">
              Access full trading signals, VIP alerts, and priority updates.
            </p>

            <p className="text-white mt-4 text-2xl font-bold">
              KES 999 / month
            </p>

            <button
              onClick={upgrade}
              className="mt-4 w-full bg-cyan-500 hover:bg-cyan-600 text-black font-semibold py-2 rounded"
            >
              Upgrade with M-Pesa
            </button>

          </div>

          {/* PRO Plan */}
          <div className="bg-[#111827] border border-purple-500 rounded-lg p-5 hover:scale-[1.02] transition">

            <h2 className="text-purple-400 font-bold text-xl">
              PRO PLAN
            </h2>

            <p className="text-gray-400 mt-2 text-sm">
              VIP + advanced analytics + institutional signals.
            </p>

            <p className="text-white mt-4 text-2xl font-bold">
              $29 / month
            </p>

            <button className="mt-4 w-full bg-purple-500 hover:bg-purple-600 text-black font-semibold py-2 rounded">
              Pay with Stripe
            </button>

          </div>

        </div>

        {/* Payment Instructions */}
        <div className="mt-8 bg-[#111827] border border-gray-800 rounded-lg p-5">

          <h3 className="text-white font-semibold mb-2">
            Payment Methods
          </h3>

          <ul className="text-gray-400 text-sm space-y-1">
            <li>• M-Pesa (Safaricom) instant activation</li>
            <li>• Stripe (Card payments worldwide)</li>
            <li>• Auto subscription renewal supported</li>
          </ul>

        </div>

      </div>
    </div>
  );
}
