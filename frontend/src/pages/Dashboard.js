import React, { useEffect, useState } from "react"
import { supabase } from "../supabaseClient"
import { signOut, getUser } from "../auth"

export default function Dashboard() {
  const [user, setUser] = useState(null)

  useEffect(() => {
    async function loadUser() {
      const currentUser = await getUser()
      setUser(currentUser)
    }

    loadUser()
  }, [])

  async function handleLogout() {
    await signOut()
    window.location.href = "/"
  }

  if (!user) {
    return <h3>Loading dashboard...</h3>
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>Dashboard</h1>

      <p>Welcome: {user.email}</p>

      <button onClick={handleLogout}>
        Logout
      </button>

      <hr />

      <h3>Your SaaS is now connected 🚀</h3>
      <p>This is your protected dashboard area.</p>
    </div>
  )
}
