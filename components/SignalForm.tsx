"use client";

import { useState } from "react";
import { createSignal } from "@/lib/signals";

export default function SignalForm() {
  const [form, setForm] = useState({
    pair: "",
    direction: "BUY",
    entry: 0,
    sl: 0,
    tp: 0,
  });

  const submit = async () => {
    await createSignal(form as any);
    alert("Signal posted");
  };

  return (
    <div className="space-y-2">
      <input
        placeholder="Pair (EURUSD)"
        className="input"
        onChange={(e) => setForm({ ...form, pair: e.target.value })}
      />

      <input
        placeholder="Entry"
        type="number"
        className="input"
        onChange={(e) => setForm({ ...form, entry: Number(e.target.value) })}
      />

      <input
        placeholder="SL"
        type="number"
        className="input"
        onChange={(e) => setForm({ ...form, sl: Number(e.target.value) })}
      />

      <input
        placeholder="TP"
        type="number"
        className="input"
        onChange={(e) => setForm({ ...form, tp: Number(e.target.value) })}
      />

      <button
        onClick={submit}
        className="bg-blue-600 px-4 py-2 rounded"
      >
        Send Signal
      </button>
    </div>
  );
}
