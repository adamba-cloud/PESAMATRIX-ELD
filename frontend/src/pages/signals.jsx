import { useEffect, useState } from "react";
import Sidebar from "../components/sidebar";
import API from "../api/api";

export default function Signals() {
  const [signals, setSignals] = useState([]);

  useEffect(() => {
    const fetchSignals = async () => {
      try {
        const res = await API.get("/signals");
        setSignals(res.data.signals);
      } catch (err) {
        console.log(err);
      }
    };

    fetchSignals();
  }, []);

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

          {signals.map((s, index) => (
            <div
              key={index}
              className={`bg-[#111827] border rounded-lg p-5 hover:scale-[1.02] transition ${
                s.type === "BUY" ? "border-green-600" : "border-red-600"
              }`}
            >

              <h2
                className={
                  s.type === "BUY"
                    ? "text-green-400 font-bold text-lg"
                    : "text-red-400 font-bold text-lg"
                }
              >
                {s.type} - {s.pair}
              </h2>

              <p className="text-gray-400 mt-2 text-sm">
                Entry: {s.entry}
              </p>

              <p className="text-gray-400 text-sm">
                TP: {s.tp}
              </p>

              <p className="text-gray-400 text-sm">
                SL: {s.sl}
              </p>

            </div>
          ))}

        </div>

      </div>
    </div>
  );
}
