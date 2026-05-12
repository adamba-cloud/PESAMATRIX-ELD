// lib/uploads.ts

/**
 * HYBRID CONTENT UPLOAD SYSTEM
 * ✅ Works now without Firebase
 * ✅ Ready for real Firebase later
 * ✅ Supports image / video / link uploads
 */

// import { db, storage } from "./firebase";
// import {
//   ref,
//   uploadBytesResumable,
//   getDownloadURL,
// } from "firebase/storage";

// import {
//   collection,
//   addDoc,
//   serverTimestamp,
// } from "firebase/firestore";

/* ===================================
   TYPES
=================================== */

export type ContentType = "video" | "image" | "link";

export type ContentItem = {
  type: ContentType;
  url: string;
  title?: string;
};

/* ===================================
   MOCK STORAGE
=================================== */

let mockContent: ContentItem[] = [];

/* ===================================
   UPLOAD FILE
=================================== */

export const uploadFile = async (
  file?: File,
  onProgress?: (p: number) => void
): Promise<string> => {
  try {
    /* 🔥 MOCK MODE */

    if (onProgress) {
      let progress = 0;

      const timer = setInterval(() => {
        progress += 20;
        onProgress(progress);

        if (progress >= 100) {
          clearInterval(timer);
        }
      }, 300);
    }

    await new Promise((r) => setTimeout(r, 1800));

    return "https://placehold.co/600x400?text=PMX+Upload";

    /* 🔐 FIREBASE MODE (UNCOMMENT LATER)

    return new Promise<string>((resolve, reject) => {
      const storageRef = ref(storage, `uploads/${file!.name}`);
      const uploadTask = uploadBytesResumable(storageRef, file!);

      uploadTask.on(
        "state_changed",
        (snapshot) => {
          const progress =
            (snapshot.bytesTransferred /
              snapshot.totalBytes) *
            100;

          onProgress?.(progress);
        },
        reject,
        async () => {
          const url = await getDownloadURL(
            uploadTask.snapshot.ref
          );

          resolve(url);
        }
      );
    });

    */
  } catch (error) {
    console.error("Upload failed:", error);
    return "";
  }
};

/* ===================================
   SAVE CONTENT
=================================== */

export const saveContent = async (
  data: ContentItem
) => {
  try {
    /* 🔥 MOCK MODE */
    mockContent.unshift(data);

    return true;

    /* 🔐 FIREBASE MODE (UNCOMMENT LATER)

    await addDoc(collection(db, "content"), {
      ...data,
      createdAt: serverTimestamp(),
    });

    return true;

    */
  } catch (error) {
    console.error("Save failed:", error);
    return false;
  }
};

/* ===================================
   GET CONTENT (OPTIONAL)
=================================== */

export const getContent = async () => {
  return mockContent;
};
