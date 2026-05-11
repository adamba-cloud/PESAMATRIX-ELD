import Link from "next/link";

export default function AboutPage() {
  return (
    <main className="min-h-screen p-6 md:p-12 text-white">
      <div className="max-w-3xl mx-auto bg-card border border-line p-6 rounded-3xl">

        <h1 className="text-3xl font-bold mb-4">About PMX Signals</h1>

        <p className="text-gray-300 mb-4">
          PMX Signals is a premium forex trading signals platform designed to
          help traders make informed decisions using high accuracy market analysis.
        </p>

        <p className="text-gray-300 mb-4">
          We provide daily BUY & SELL signals, risk management guidance,
          and VIP trading insights.
        </p>

        <h2 className="text-xl font-bold mt-6 mb-2">Our Mission</h2>

        <p className="text-gray-300 mb-4">
          To simplify forex trading for beginners and professionals using
          structured, data-driven signals.
        </p>

        <Link href="/dashboard" className="text-primary">
          Go to Dashboard →
        </Link>

      </div>
    </main>
  );
}
