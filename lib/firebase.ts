// lib/firebase.ts

/**
 * HYBRID FIREBASE FILE
 * ✅ Works in mock mode now
 * ✅ Ready for real Firebase later
 */

import { initializeApp, getApps, getApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";

/* ===================================
   CHECK IF FIREBASE ENV EXISTS
=================================== */

const hasFirebaseConfig =
  !!process.env.NEXT_PUBLIC_FIREBASE_API_KEY &&
  !!process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID &&
  !!process.env.NEXT_PUBLIC_FIREBASE_APP_ID;

/* ===================================
   MOCK FALLBACK
=================================== */

let auth: any = {};
let db: any = {};
let storage: any = {};

/* ===================================
   REAL FIREBASE MODE
=================================== */

if (hasFirebaseConfig) {
  const firebaseConfig = {
    apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY!,
    authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN!,
    projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID!,
    storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET!,
    messagingSenderId:
      process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID!,
    appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID!,
  };

  const app = getApps().length ? getApp() : initializeApp(firebaseConfig);

  auth = getAuth(app);
  db = getFirestore(app);
  storage = getStorage(app);
}

/* ===================================
   EXPORTS
=================================== */

export { auth, db, storage };
