import React, { useState } from "react";

import Layout from "../components/Layout";
import API from "../api/api";

export default function Admin() {

  const [form, setForm] = useState({
    pair: "",
    type: "BUY",
    entry: "",
    tp: "",
    sl: ""
  });

  const [announcement, setAnnouncement] = useState("");

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  async function createSignal() {

    try {

      const res = await API.post("/signals/create", {
        pair: form.pair,
        type: form.type,
        entry: Number(form.entry),
        tp: Number(form.tp),
        sl: Number(form.sl)
      });

      alert(res.data.message || "Signal created successfully!");

      setForm({
        pair: "",
        type: "BUY",
        entry: "",
        tp: "",
        sl: ""
      });

    } catch (err) {

      console.log(err);
      alert("Failed to create signal");

    }
  }

  function publishAnnouncement() {
    alert("Announcement published!");
    setAnnouncement("");
  }

  return (
    <Layout>

      {/* HEADER */}
      <div className="mb-8">

        <h1 className="text-3xl font-bold text-cyan-400">
          Admin Panel
        </h1>

        <p className="text-gray-400 mt-2">
          Manage your trading SaaS platform
        </p>

      </div>

      {/* STATS */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-5 mb-8">

        <div className="
          bg-[#111827]
          border border-gray-800
          rounded-xl
          p-5
        ">

          <p className="text-gray-400 text-sm">
            Total Users
          </p>

          <h2 className="text-3xl font-bold text-cyan-400 mt-2">
            120
          </h2>

        </div>

        <div className="
          bg-[#111827]
          border border-gray-800
          rounded-xl
          p-5
        ">

          <p className="text-gray-400 text-sm">
            Total Signals
          </p>

          <h2 className="text-3xl font-bold text-green-400 mt-2">
            45
          </h2>

        </div>

        <div className="
          bg-[#111827]
          border border-gray-800
          rounded-xl
          p-5
        ">

          <p className="text-gray-400 text-sm">
            Revenue
          </p>

          <h2 className="text-3xl font-bold text-yellow-400 mt-2">
            KES 32,000
          </h2>

        </div>

      </div>

      {/* ADMIN TOOLS GRID */}
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5 mb-8">

        {/* USER MANAGEMENT */}
        <div className="
          bg-[#111827]
          border border-gray-800
          rounded-xl
          p-5
        ">

          <h2 className="text-xl font-semibold text-white mb-2">
            User Management
          </h2>

          <p className="text-gray-400 text-sm">
            Upgrade users to VIP or ADMIN roles.
          </p>

          <div className="mt-4 flex gap-2">

            <button className="
              px-4 py-2 rounded-lg
              bg-cyan-500 hover:bg-cyan-600
              transition-colors
            ">
              View Users
            </button>

            <button className="
              px-4 py-2 rounded-lg
              bg-yellow-500 hover:bg-yellow-600
              transition-colors
            ">
              VIP Access
            </button>

          </div>

        </div>

        {/* SIGNAL CONTROL */}
        <div className="
          bg-[#111827]
          border border-gray-800
          rounded-xl
          p-5
        ">

          <h2 className="text-xl font-semibold text-white mb-2">
            Signal Control
          </h2>

          <p className="text-gray-400 text-sm">
            Publish, edit, or remove trading signals.
          </p>

          <div className="mt-4 flex gap-2">

            <button className="
              px-4 py-2 rounded-lg
              bg-green-500 hover:bg-green-600
              transition-colors
            ">
              New Signal
            </button>

            <button className="
              px-4 py-2 rounded-lg
              bg-red-500 hover:bg-red-600
              transition-colors
            ">
              Delete
            </button>

          </div>

        </div>

        {/* ANNOUNCEMENTS */}
        <div className="
          bg-[#111827]
          border border-gray-800
          rounded-xl
          p-5
        ">

          <h2 className="text-xl font-semibold text-white mb-2">
            Announcements
          </h2>

          <p className="text-gray-400 text-sm">
            Send updates to all platform users.
          </p>

          <textarea
            value={announcement}
            onChange={(e) => setAnnouncement(e.target.value)}
            placeholder="Write announcement..."
            className="
              mt-4 w-full h-24
              bg-[#0B0F19]
              border border-gray-700
              rounded-lg p-3
              text-white
              outline-none
            "
          />

          <button
            onClick={publishAnnouncement}
            className="
              mt-4 px-4 py-2 rounded-lg
              bg-cyan-500 hover:bg-cyan-600
              transition-colors
            "
          >
            Publish Announcement
          </button>

        </div>

      </div>

      {/* CREATE SIGNAL FORM */}
      <div className="
        bg-[#111827]
        border border-gray-800
        rounded-xl
        p-6
      ">

        <h2 className="text-2xl font-bold text-white mb-5">
          Create Trading Signal
        </h2>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">

          <input
            name="pair"
            value={form.pair}
            onChange={handleChange}
            placeholder="Pair (e.g XAUUSD)"
            className="
              p-3 rounded-lg
              bg-[#0B0F19]
              border border-gray-700
              text-white
              outline-none
            "
          />

          <select
            name="type"
            value={form.type}
            onChange={handleChange}
            className="
              p-3 rounded-lg
              bg-[#0B0F19]
              border border-gray-700
              text-white
              outline-none
            "
          >
            <option value="BUY">BUY</option>
            <option value="SELL">SELL</option>
          </select>

          <input
            name="entry"
            value={form.entry}
            onChange={handleChange}
            placeholder="Entry Price"
            className="
              p-3 rounded-lg
              bg-[#0B0F19]
              border border-gray-700
              text-white
              outline-none
            "
          />

          <input
            name="tp"
            value={form.tp}
            onChange={handleChange}
            placeholder="Take Profit"
            className="
              p-3 rounded-lg
              bg-[#0B0F19]
              border border-gray-700
              text-white
              outline-none
            "
          />

          <input
            name="sl"
            value={form.sl}
            onChange={handleChange}
            placeholder="Stop Loss"
            className="
              p-3 rounded-lg
              bg-[#0B0F19]
              border border-gray-700
              text-white
              outline-none
            "
          />

        </div>

        <button
          onClick={createSignal}
          className="
            mt-6 px-6 py-3 rounded-lg
            bg-cyan-500 hover:bg-cyan-600
            text-black font-bold
            transition-colors
          "
        >
          Create Signal
        </button>

      </div>

    </Layout>
  );
}
