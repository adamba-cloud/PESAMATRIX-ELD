export default function Signals() {
  return (
    <div>

      <h1 className="text-2xl font-bold mb-6">Market Signals</h1>

      <div className="space-y-4">

        {[1,2,3].map((s) => (
          <div key={s} className="bg-[#111827] p-5 rounded-xl border border-gray-800">

            <h3 className="text-cyan-400 font-semibold">
              GOLD BUY SIGNAL #{s}
            </h3>

            <p className="text-gray-400 text-sm mt-1">
              Entry: 2025.xx | SL: 2010 | TP: 2040
            </p>

          </div>
        ))}

      </div>

    </div>
  );
}
