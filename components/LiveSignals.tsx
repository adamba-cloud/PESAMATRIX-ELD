"use client";

import { useEffect, useState } from "react";
import { getSignals } from "@/lib/signals";

export default function LiveSignals() {
  const [signals, setSignals] = useState<any[]>([]);

  useEffect(() => {
    const load = async () => {
      const data = await getSignals();
      setSignals(data);
    };

    load();
  }, []);

  return (
    <div className="space-y-4">
      {signals.map((s: any) => (
        <div
          key={s.id}
          className="p-4 rounded-xl bg-gray-900 border border-gray-700"
        >
          <h2 className="text-lg font-bold">{s.pair}</h2>
          <p>Direction: {s.direction}</p>
          <p>Entry: {s.entry}</p>
          <p>SL: {s.sl}</p>
          <p>TP: {s.tp}</p>
        </div>
      ))}
    </div>
  );
}
