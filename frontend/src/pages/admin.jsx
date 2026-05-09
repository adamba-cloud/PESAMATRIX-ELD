import { useState } from "react";
import Sidebar from "../components/sidebar";
import API from "../api/api";

export default function Admin() {

  const [form, setForm] = useState({
    pair: "",
    type: "BUY",
    entry: "",
    tp: "",
    sl: ""
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const createSignal = async () => {
    try {
      const res = await API.post("/admin/create-signal", form);
      alert(res.data.message);
      setForm({ pair: "", type: "BUY", entry: "", tp: "", sl: "" });
    } catch (err) {
      console.log(err);
      alert("Failed to create signal");
    }
  };

  return (
    <div className="flex min-h-screen bg-[#0B0F19] text-white">

      <Sidebar />

      <div className="flex-1 p-6">

        <h1 className="text-3xl font-bold text-cyan-400 mb-6">
          Admin Panel
        </h1>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">

          <div className="bg-[#111827] p-5 rounded border border-gray-800">
            <p className="text-gray-400">Total Users</p>
            <h2 className="text-2xl text-white">120</h2>
          </div>

          <div className="bg-[#111827] p-5 rounded border border-gray-800">
            <p className="text-gray-400">Total Signals</p>
            <h2 className="text-2xl text-white">45</h2>
          </div>

          <div className="bg-[#111827] p-5 rounded border border-gray-800">
            <p className="text-gray-400">Revenue</p>
            <h2 className="text-2xl text-white">KES 32,000</h2>
          </div>

        </div>

        {/* Create Signal Form */}
        <div className="bg-[#111827] p-6 rounded border border-gray-800">

          <h2 className="text-xl font-bold mb-4 text-white">
            Create Trading Signal
          </h2>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">

            <input
              name="pair"
              value={form.pair}
              onChange={handleChange}
              placeholder="Pair (e.g XAUUSD)"
              className="p-2 bg-black border border-gray-700 rounded"
            />

            <select
              name="type"
              value={form.type}
              onChange={handleChange}
              className="p-2 bg-black border border-gray-700 rounded"
            >
              <option value="BUY">BUY</option>
              <option value="SELL">SELL</option>
            </select>

            <input
              name="entry"
              value={form.entry}
              onChange={handleChange}
              placeholder="Entry Price"
              className="p-2 bg-black border border-gray-700 rounded"
            />

            <input
              name="tp"
              value={form.tp}
              onChange={handleChange}
              placeholder="Take Profit"
              className="p-2 bg-black border border-gray-700 rounded"
            />

            <input
              name="sl"
              value={form.sl}
              onChange={handleChange}
              placeholder="Stop Loss"
              className="p-2 bg-black border border-gray-700 rounded"
            />

          </div>

          <button
            onClick={createSignal}
            className="mt-5 bg-cyan-500 hover:bg-cyan-600 text-black font-bold px-6 py-2 rounded"
          >
            Create Signal
          </button>

        </div>

      </div>
    </div>
  );
}
