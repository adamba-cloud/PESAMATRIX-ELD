import { Navigate } from "react-router-dom";

export default function RoleProtectedRoute({
  children,
  allowedRole
}) {

  const token = localStorage.getItem("token");

  // user role saved after login
  const role = localStorage.getItem("role");

  // not logged in
  if (!token) {
    return <Navigate to="/auth" />;
  }

  // wrong role
  if (role !== allowedRole) {
    return <Navigate to="/dashboard" />;
  }

  return children;
}
