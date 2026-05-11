import Link from "next/link";

export default function Home() {
  return (
    <main className="min-h-screen flex items-center justify-center text-center p-6">
      <div>
        <h1 className="text-4xl font-bold mb-4">PMX SIGNALS</h1>
        <p className="text-gray-400 mb-6">
          Premium Forex Signals Platform
        </p>

        <div className="space-x-4">
          <Link className="bg-primary px-6 py-3 rounded-xl" href="/login">
            Login
          </Link>

          <Link className="bg-card px-6 py-3 rounded-xl" href="/about">
            About Us
          </Link>
        </div>
      </div>
    </main>
  );
}
