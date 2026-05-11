import { db } from "./firebase";
import { collection, addDoc, getDocs, serverTimestamp } from "firebase/firestore";

export const addNews = async (title: string, content: string) => {
  await addDoc(collection(db, "news"), {
    title,
    content,
    createdAt: serverTimestamp(),
  });
};

export const getNews = async () => {
  const snap = await getDocs(collection(db, "news"));
  return snap.docs.map((d) => ({ id: d.id, ...d.data() }));
};
