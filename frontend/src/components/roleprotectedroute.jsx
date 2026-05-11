import React, { useEffect, useState } from "react"
import { Navigate } from "react-router-dom"

import { getUser } from "../auth"
import { getUserRole } from "../utils/getUserRole"

export default function RoleProtectedRoute({
  children,
  allowedRole,
}) {
  const [loading, setLoading] = useState(true)
  const [authorized, setAuthorized] = useState(false)

  useEffect(() => {
    async function checkRole() {
      const user = await getUser()

      if (!user) {
        setAuthorized(false)
        setLoading(false)
        return
      }

      const role = await getUserRole(user.id)

      if (role === allowedRole) {
        setAuthorized(true)
      } else {
        setAuthorized(false)
      }

      setLoading(false)
    }

    checkRole()
  }, [allowedRole])

  if (loading) return <p>Checking permissions...</p>

  return authorized ? children : <Navigate to="/dashboard" />
}
