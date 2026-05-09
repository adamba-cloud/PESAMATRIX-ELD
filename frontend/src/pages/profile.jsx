import Sidebar from "../components/sidebar";

export default function Profile() {

  // temporary mock (later replace with API/JWT data)
  const user = {
    name: "Demo User",
    email: "user@gmail.com",
    role: "FREE",
    subscription: "Inactive"
  };

  const handleLogout = () => {
    localStorage.removeItem("token");
    window.location.href = "/login";
  };

  return (
    <div className="flex min-h-screen bg-[#0B0F19] text-white">

      {/* Sidebar */}
      <Sidebar />

      {/* Main Content */}
      <div className="flex-1 p-6">

        {/* Header */}
        <h1 className="text-3xl font-bold text-cyan-400 mb-6">
          My Profile
        </h1>

        {/* User Info Card */}
        <div className="bg-[#111827] border border-gray-800 rounded-lg p-6">

          <h2 className="text-xl font-semibold text-white mb-4">
            Account Information
          </h2>

          <div className="space-y-3 text-gray-300 text-sm">

            <p>
              <span className="text-gray-400">Name:</span> {user.name}
            </p>

            <p>
              <span className="text-gray-400">Email:</span> {user.email}
            </p>

            <p>
              <span className="text-gray-400">Role:</span>{" "}
              <span className={user.role === "VIP" ? "text-green-400" : "text-yellow-400"}>
                {user.role}
              </span>
            </p>

            <p>
              <span className="text-gray-400">Subscription:</span>{" "}
              <span className={user.subscription === "Active" ? "text-green-400" : "text-red-400"}>
                {user.subscription}
              </span>
            </p>

          </div>

        </div>

        {/* JWT / Token Display */}
        <div className="mt-6 bg-[#111827] border border-gray-800 rounded-lg p-6">

          <h2 className="text-xl font-semibold text-white mb-4">
            Session (JWT)
          </h2>

          <p className="text-gray-400 text-sm break-all">
            {localStorage.getItem("token") || "No active session"}
          </p>

        </div>

        {/* Actions */}
        <div className="mt-6">

          <button
            onClick={handleLogout}
            className="bg-red-500 hover:bg-red-600 text-white px-6 py-2 rounded"
          >
            Logout
          </button>

        </div>

      </div>
    </div>
  );
}
