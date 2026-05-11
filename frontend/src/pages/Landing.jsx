import { Link } from "react-router-dom";

export default function Landing() {
  return (
    <div className="min-h-screen bg-[#0B0F19] text-white">

      {/* HERO */}
      <div className="flex flex-col items-center justify-center text-center px-6 py-24">

        <h1 className="text-5xl font-bold text-cyan-400 mb-4">
          PesaMatrix Trading SaaS
        </h1>

        <p className="text-gray-400 max-w-xl mb-8">
          Real-time Forex signals, VIP trading insights, and automated
          content delivery — all in one clean dashboard.
        </p>

        <div className="flex gap-4">
          <Link
            to="/dashboard"
            className="bg-cyan-500 px-6 py-3 rounded-lg text-black font-semibold"
          >
            Enter Dashboard
          </Link>

          <Link
            to="/signals"
            className="border border-cyan-500 px-6 py-3 rounded-lg"
          >
            View Signals
          </Link>
        </div>

      </div>

      {/* FEATURES */}
      <div className="grid md:grid-cols-3 gap-6 px-10 pb-20">

        {[
          "Live Trading Signals",
          "VIP Locked Access",
          "Admin Content Control"
        ].map((f, i) => (
          <div key={i} className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <h3 className="text-cyan-400 text-lg mb-2">{f}</h3>
            <p className="text-gray-400 text-sm">
              Professional SaaS-grade system designed for traders.
            </p>
          </div>
        ))}

      </div>

    </div>
  );
}
