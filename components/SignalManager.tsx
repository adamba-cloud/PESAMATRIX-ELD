"use client";

import { updateSignalStatus } from "@/lib/signals";

export default function SignalManager({ signalId }: { signalId: string }) {
  return (
    <div className="space-x-2">
      <button onClick={() => updateSignalStatus(signalId, "upcoming")}>
        Upcoming
      </button>

      <button onClick={() => updateSignalStatus(signalId, "running")}>
        Running
      </button>

      <button onClick={() => updateSignalStatus(signalId, "expired")}>
        Expired
      </button>
    </div>
  );
}
