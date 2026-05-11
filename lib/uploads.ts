import { db, storage } from "./firebase";
import { ref, uploadBytesResumable, getDownloadURL } from "firebase/storage";
import { collection, addDoc, serverTimestamp } from "firebase/firestore";

export const uploadFile = (file: File, onProgress: (p: number) => void) => {
  return new Promise<string>((resolve, reject) => {
    const storageRef = ref(storage, `uploads/${file.name}`);

    const uploadTask = uploadBytesResumable(storageRef, file);

    uploadTask.on(
      "state_changed",
      (snapshot) => {
        const progress =
          (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
        onProgress(progress);
      },
      reject,
      async () => {
        const url = await getDownloadURL(uploadTask.snapshot.ref);
        resolve(url);
      }
    );
  });
};

export const saveContent = async (data: {
  type: "video" | "image" | "link";
  url: string;
  title?: string;
}) => {
  await addDoc(collection(db, "content"), {
    ...data,
    createdAt: serverTimestamp(),
  });
};
