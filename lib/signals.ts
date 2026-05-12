// lib/signals.ts

/**
 * PMX SIGNALS SYSTEM
 * Hybrid version:
 * ✅ Works now with mock/static data
 * ✅ Ready for Firebase later
 */

// import { db } from "./firebase";
// import {
//   collection,
//   addDoc,
//   getDocs,
//   doc,
//   updateDoc,
//   serverTimestamp,
// } from "firebase/firestore";

/* ===================================
   TYPES
=================================== */

export type SignalDirection = "BUY" | "SELL";

export type SignalStatus =
  | "upcoming"
  | "running"
  | "expired"
  | "active";

export type Signal = {
  id?: string;
  pair: string;
  direction: SignalDirection;
  entry: number;
  sl: number;
  tp: number;
  status?: SignalStatus;
};

/* ===================================
   MOCK DATA (TEMPORARY LIVE MODE)
=================================== */

let mockSignals: Signal[] = [
  {
    id: "1",
    pair: "EURUSD",
    direction: "BUY",
    entry: 1.0820,
    sl: 1.0790,
    tp: 1.0880,
    status: "running",
  },
  {
    id: "2",
    pair: "XAUUSD",
    direction: "SELL",
    entry: 3240,
    sl: 3255,
    tp: 3200,
    status: "upcoming",
  },
];

/* ===================================
   CREATE SIGNAL
=================================== */

export const createSignal = async (data: Signal) => {
  try {
    // 🔥 MOCK MODE
    mockSignals.unshift({
      ...data,
      id: Date.now().toString(),
      status: data.status || "active",
    });

    return true;

    // 🔐 FIREBASE MODE (UNCOMMENT LATER)
    /*
    await addDoc(collection(db, "signals"), {
      ...data,
      status: data.status || "active",
      createdAt: serverTimestamp(),
    });
    */
  } catch (error) {
    console.error("Create signal failed:", error);
    return false;
  }
};

/* ===================================
   GET SIGNALS
=================================== */

export const getSignals = async () => {
  try {
    // 🔥 MOCK MODE
    return mockSignals;

    // 🔐 FIREBASE MODE (UNCOMMENT LATER)
    /*
    const snapshot = await getDocs(collection(db, "signals"));

    return snapshot.docs.map((docSnap) => ({
      id: docSnap.id,
      ...docSnap.data(),
    }));
    */
  } catch (error) {
    console.error("Fetch signals failed:", error);
    return [];
  }
};

/* ===================================
   UPDATE STATUS
=================================== */

export const updateSignalStatus = async (
  signalId: string,
  status: SignalStatus
) => {
  try {
    // 🔥 MOCK MODE
    mockSignals = mockSignals.map((signal) =>
      signal.id === signalId
        ? { ...signal, status }
        : signal
    );

    return true;

    // 🔐 FIREBASE MODE (UNCOMMENT LATER)
    /*
    await updateDoc(doc(db, "signals", signalId), {
      status,
      updatedAt: serverTimestamp(),
    });
    */
  } catch (error) {
    console.error("Update failed:", error);
    return false;
  }
};
