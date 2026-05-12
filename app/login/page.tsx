"use client";

import { useState } from "react";
import { signInWithEmailAndPassword } from "firebase/auth";
import { useRouter } from "next/navigation";
import { auth } from "../../lib/firebase"; // ✅ FIXED IMPORT

export default function LoginPage() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const login = async () => {
    try {
      await signInWithEmailAndPassword(auth, email, password);
      router.push("/dashboard");
    } catch (error) {
      console.error(error);
      alert("Login Failed");
    }
  };

  return (
    <main className="min-h-screen flex items-center justify-center">
      <div className="bg-card p-6 rounded-2xl w-full max-w-md border border-line">

        <h1 className="text-2xl mb-4 font-bold">Login</h1>

        <input
          className="w-full p-3 mb-3 bg-bg border border-line rounded-xl"
          placeholder="Email"
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          className="w-full p-3 mb-3 bg-bg border border-line rounded-xl"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
        />

        <button onClick={login} className="w-full bg-primary p-3 rounded-xl">
          Login
        </button>
      </div>
    </main>
  );
}
