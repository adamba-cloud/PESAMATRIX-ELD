import React, { useState } from "react"
import { signIn, signUp } from "../auth"

export default function AuthPage() {
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [loading, setLoading] = useState(false)
  const [message, setMessage] = useState("")

  async function handleLogin() {
    setLoading(true)
    const { error } = await signIn(email, password)
    setLoading(false)

    if (error) setMessage(error.message)
    else setMessage("Login successful")
  }

  async function handleSignup() {
    setLoading(true)
    const { error } = await signUp(email, password)
    setLoading(false)

    if (error) setMessage(error.message)
    else setMessage("Account created! Check your email if confirmation is enabled.")
  }

  return (
    <div style={{ maxWidth: "400px", margin: "auto", padding: "40px" }}>
      <h2>Login / Signup</h2>

      <input
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        style={{ width: "100%", marginBottom: "10px", padding: "10px" }}
      />

      <input
        placeholder="Password"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        style={{ width: "100%", marginBottom: "10px", padding: "10px" }}
      />

      <button onClick={handleLogin} disabled={loading}>
        Login
      </button>

      <button onClick={handleSignup} disabled={loading} style={{ marginLeft: "10px" }}>
        Sign Up
      </button>

      <p>{message}</p>
    </div>
  )
}
