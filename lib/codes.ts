import { db } from "./firebase";
import { doc, setDoc, getDoc } from "firebase/firestore";

export const generateCode = async (userId: string) => {
  const code = "PMX-" + Math.random().toString(36).substring(2, 10).toUpperCase();

  await setDoc(doc(db, "accessCodes", userId), {
    code,
    active: true,
  });

  return code;
};

export const verifyCode = async (userId: string, code: string) => {
  const snap = await getDoc(doc(db, "accessCodes", userId));

  if (!snap.exists()) return false;

  return snap.data().code === code && snap.data().active;
};
