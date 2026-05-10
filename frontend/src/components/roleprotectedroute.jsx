import { Navigate } from "react-router-dom";

export default function RoleProtectedRoute({
  children,
  allowedRole
}) {

  // GET TOKEN
  const token = localStorage.getItem("token");

  // GET USER ROLE
  const role = localStorage.getItem("role");

  // NOT LOGGED IN
  if (!token) {
    return <Navigate to="/auth" />;
  }

  // ADMIN ONLY ROUTE
  if (allowedRole === "ADMIN" && role !== "ADMIN") {
    return (
      <div className="min-h-screen flex items-center justify-center bg-[#0B0F19] text-red-400 text-2xl font-bold">
        Access denied
      </div>
    );
  }

  // VIP ONLY ROUTE
  if (allowedRole === "VIP" && role !== "VIP") {
    return (
      <div className="min-h-screen flex items-center justify-center bg-[#0B0F19] text-yellow-400 text-2xl font-bold">
        Upgrade required
      </div>
    );
  }

  return children;
}
