"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
// import { signInWithEmailAndPassword } from "firebase/auth";
// import { auth } from "../../lib/firebase";

export default function LoginPage() {
  const router = useRouter();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  const login = async () => {
    if (!email || !password) {
      alert("Enter email and password");
      return;
    }

    setLoading(true);

    try {
      // 🔥 TEMP MOCK LOGIN MODE
      localStorage.setItem("pmxUser", email);

      // 🔐 WHEN READY FOR FIREBASE, REPLACE ABOVE WITH:
      /*
      await signInWithEmailAndPassword(auth, email, password);
      */

      router.push("/dashboard");
    } catch (error) {
      console.error(error);
      alert("Login Failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen flex items-center justify-center bg-bg px-4">
      <div className="bg-card p-6 rounded-2xl w-full max-w-md border border-line shadow-lg">

        <h1 className="text-2xl font-bold mb-2 text-center">
          Welcome Back
        </h1>

        <p className="text-sm text-center mb-6 opacity-70">
          Login to access PMX Signals
        </p>

        <input
          type="email"
          placeholder="Email Address"
          className="w-full p-3 mb-3 bg-bg border border-line rounded-xl outline-none"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          className="w-full p-3 mb-4 bg-bg border border-line rounded-xl outline-none"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button
          onClick={login}
          disabled={loading}
          className="w-full bg-primary p-3 rounded-xl font-semibold"
        >
          {loading ? "Logging in..." : "Login"}
        </button>

        <p className="text-center text-sm mt-4 opacity-70">
          Premium access for VIP members
        </p>
      </div>
    </main>
  );
}
