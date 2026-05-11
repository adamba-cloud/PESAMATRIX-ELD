import { db } from "./firebase";
import {
  collection,
  addDoc,
  getDocs,
  doc,
  updateDoc,
  serverTimestamp,
} from "firebase/firestore";

/**
 * SIGNAL TYPES
 */
export type SignalDirection = "BUY" | "SELL";
export type SignalStatus = "upcoming" | "running" | "expired" | "active";

export type Signal = {
  pair: string;
  direction: SignalDirection;
  entry: number;
  sl: number;
  tp: number;
  status?: SignalStatus;
};

/**
 * CREATE NEW SIGNAL (ADMIN)
 */
export const createSignal = async (data: Signal) => {
  await addDoc(collection(db, "signals"), {
    ...data,
    status: data.status || "active",
    createdAt: serverTimestamp(),
  });
};

/**
 * GET ALL SIGNALS (USER / VIP DASHBOARD)
 */
export const getSignals = async () => {
  const snapshot = await getDocs(collection(db, "signals"));

  return snapshot.docs.map((docSnap) => ({
    id: docSnap.id,
    ...docSnap.data(),
  }));
};

/**
 * UPDATE SIGNAL STATUS (ADMIN CONTROL PANEL)
 */
export const updateSignalStatus = async (
  signalId: string,
  status: SignalStatus
) => {
  await updateDoc(doc(db, "signals", signalId), {
    status,
    updatedAt: serverTimestamp(),
  });
};
