import Link from "next/link";

export default function UpgradePage() {
  return (
    <main className="min-h-screen flex items-center justify-center p-6">

      <div className="bg-card border border-line p-6 rounded-3xl w-full max-w-2xl">

        <h1 className="text-3xl font-bold text-center mb-2">
          Upgrade to VIP
        </h1>

        <p className="text-center text-gray-400 mb-6">
          Pay via M-Pesa to activate VIP access
        </p>

        {/* MPESA BOX */}
        <div className="bg-bg border border-line p-5 rounded-2xl mb-6">

          <h2 className="font-bold mb-3">M-Pesa Payment Details</h2>

          <p>📌 Paybill Number: <b>322372</b></p>

          <p className="mt-2">
            📌 Account Number: <b>Your unique PMX account number</b>
          </p>

          <p className="text-gray-400 mt-3 text-sm">
            After payment, contact admin for activation.
          </p>

        </div>

        <div className="grid md:grid-cols-2 gap-4">

          <div className="bg-bg p-5 rounded-2xl border border-line">
            <h3 className="font-bold">Monthly</h3>
            <p className="text-3xl font-bold my-3">$29</p>
            <button className="w-full bg-primary p-3 rounded-xl">
              Pay Monthly
            </button>
          </div>

          <div className="bg-bg p-5 rounded-2xl border border-goldx">
            <h3 className="font-bold text-goldx">Yearly VIP</h3>
            <p className="text-3xl font-bold my-3">$199</p>
            <button className="w-full bg-goldx text-black p-3 rounded-xl">
              Best Value
            </button>
          </div>

        </div>

        <Link href="/dashboard" className="block text-center mt-6 text-primary">
          Back Dashboard
        </Link>

      </div>
    </main>
  );
}
