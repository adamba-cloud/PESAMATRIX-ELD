import { db } from "./firebase";
import { doc, setDoc } from "firebase/firestore";

export const createUserProfile = async (user: any) => {
  const accountNumber = "PMX-" + user.uid.slice(0, 8).toUpperCase();

  await setDoc(doc(db, "users", user.uid), {
    email: user.email,
    accountNumber,
    vip: false,
    createdAt: new Date()
  });
};
