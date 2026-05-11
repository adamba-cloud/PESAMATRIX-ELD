import { db } from "./firebase";
import { collection, addDoc, serverTimestamp, getDocs } from "firebase/firestore";

export type Signal = {
  pair: string;
  direction: "BUY" | "SELL";
  entry: number;
  sl: number;
  tp: number;
  status?: "active" | "closed";
};

export const createSignal = async (data: Signal) => {
  await addDoc(collection(db, "signals"), {
    ...data,
    status: "active",
    createdAt: serverTimestamp(),
  });
};

export const getSignals = async () => {
  const snapshot = await getDocs(collection(db, "signals"));
  return snapshot.docs.map((doc) => ({
    id: doc.id,
    ...doc.data(),
  }));
};
