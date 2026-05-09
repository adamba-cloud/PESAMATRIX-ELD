import { Link } from "react-router-dom";

export default function Landing() {
  return (
    <div className="min-h-screen bg-[#0B0F19] text-white">

      {/* NAVBAR */}
      <div className="flex items-center justify-between px-6 py-4 border-b border-gray-800">

        <h1 className="text-2xl font-bold text-cyan-400">
          TradePro SaaS
        </h1>

        <div className="flex gap-4">
          <Link to="/dashboard" className="text-gray-300 hover:text-cyan-400">
            Dashboard
          </Link>
          <Link to="/signals" className="text-gray-300 hover:text-cyan-400">
            Signals
          </Link>
          <Link to="/payments" className="text-gray-300 hover:text-cyan-400">
            Pricing
          </Link>
        </div>

      </div>

      {/* HERO SECTION */}
      <div className="flex flex-col items-center justify-center text-center px-6 py-24">

        <h2 className="text-5xl font-bold leading-tight">
          Win Smarter with <span className="text-cyan-400">AI Trading Signals</span>
        </h2>

        <p className="text-gray-400 mt-4 max-w-xl">
          Get real-time BUY & SELL signals for Gold, Forex, and Crypto.
          Upgrade to VIP for full access and higher accuracy insights.
        </p>

        <div className="flex gap-4 mt-8">

          <Link
            to="/dashboard"
            className="px-6 py-3 bg-cyan-500 text-black font-semibold rounded hover:bg-cyan-600"
          >
            Get Started
          </Link>

          <Link
            to="/payments"
            className="px-6 py-3 border border-cyan-500 text-cyan-400 rounded hover:bg-cyan-500/10"
          >
            View Pricing
          </Link>

        </div>

      </div>

      {/* FEATURES */}
      <div className="grid md:grid-cols-3 gap-6 px-10 py-10">

        <div className="bg-[#111827] p-6 rounded border border-gray-800">
          <h3 className="text-cyan-400 font-bold">Live Signals</h3>
          <p className="text-gray-400 mt-2 text-sm">
            Real-time trading alerts for Forex, Gold, and Crypto.
          </p>
        </div>

        <div className="bg-[#111827] p-6 rounded border border-gray-800">
          <h3 className="text-cyan-400 font-bold">VIP Access</h3>
          <p className="text-gray-400 mt-2 text-sm">
            Unlock premium signals with higher accuracy.
          </p>
        </div>

        <div className="bg-[#111827] p-6 rounded border border-gray-800">
          <h3 className="text-cyan-400 font-bold">Secure Payments</h3>
          <p className="text-gray-400 mt-2 text-sm">
            Pay via M-Pesa or Stripe with instant activation.
          </p>
        </div>

      </div>

      {/* CALL TO ACTION */}
      <div className="text-center py-16">

        <h3 className="text-2xl font-bold">
          Start Trading Smarter Today
        </h3>

        <p className="text-gray-400 mt-2">
          Join thousands using TradePro SaaS signals
        </p>

        <Link
          to="/dashboard"
          className="inline-block mt-6 px-8 py-3 bg-green-500 text-black font-semibold rounded hover:bg-green-600"
        >
          Enter Dashboard
        </Link>

      </div>

      {/* FOOTER */}
      <div className="border-t border-gray-800 text-center py-6 text-gray-500 text-sm">
        © {new Date().getFullYear()} TradePro SaaS. All rights reserved.
      </div>

    </div>
  );
}
