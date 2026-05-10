import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../api/api";

export default function Auth() {
  const navigate = useNavigate();

  const [isLogin, setIsLogin] = useState(true);

  const [form, setForm] = useState({
    name: "",
    email: "",
    password: ""
  });

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {

      // LOGIN
      if (isLogin) {

        const res = await API.post("/auth/login", {
          email: form.email,
          password: form.password
        });

        localStorage.setItem("token", res.data.token);

        alert("Login successful");

        navigate("/dashboard");

      } else {

        // REGISTER
        await API.post("/auth/register", {
          name: form.name,
          email: form.email,
          password: form.password
        });

        alert("Registration successful");

        setIsLogin(true);
      }

    } catch (err) {
      console.log(err);

      alert(
        err.response?.data?.message ||
        "Authentication failed"
      );
    }
  };

  return (
    <div className="min-h-screen bg-[#0B0F19] flex items-center justify-center px-4">

      <div className="w-full max-w-md bg-[#111827] border border-gray-800 rounded-xl p-8">

        {/* TITLE */}
        <h1 className="text-3xl font-bold text-cyan-400 text-center mb-2">
          TradePro SaaS
        </h1>

        <p className="text-gray-400 text-center mb-8">
          {isLogin ? "Login to your account" : "Create a new account"}
        </p>

        {/* FORM */}
        <form onSubmit={handleSubmit} className="space-y-4">

          {/* NAME */}
          {!isLogin && (
            <div>
              <label className="text-sm text-gray-400">
                Name
              </label>

              <input
                type="text"
                name="name"
                placeholder="John Doe"
                value={form.name}
                onChange={handleChange}
                className="w-full mt-1 p-3 rounded bg-[#0B0F19] border border-gray-700 text-white outline-none focus:border-cyan-400"
                required
              />
            </div>
          )}

          {/* EMAIL */}
          <div>
            <label className="text-sm text-gray-400">
              Email
            </label>

            <input
              type="email"
              name="email"
              placeholder="you@example.com"
              value={form.email}
              onChange={handleChange}
              className="w-full mt-1 p-3 rounded bg-[#0B0F19] border border-gray-700 text-white outline-none focus:border-cyan-400"
              required
            />
          </div>

          {/* PASSWORD */}
          <div>
            <label className="text-sm text-gray-400">
              Password
            </label>

            <input
              type="password"
              name="password"
              placeholder="••••••••"
              value={form.password}
              onChange={handleChange}
              className="w-full mt-1 p-3 rounded bg-[#0B0F19] border border-gray-700 text-white outline-none focus:border-cyan-400"
              required
            />
          </div>

          {/* BUTTON */}
          <button
            type="submit"
            className="w-full bg-cyan-500 hover:bg-cyan-600 text-black font-semibold py-3 rounded transition"
          >
            {isLogin ? "Login" : "Register"}
          </button>

        </form>

        {/* TOGGLE */}
        <div className="text-center mt-6">

          <button
            onClick={() => setIsLogin(!isLogin)}
            className="text-cyan-400 hover:underline text-sm"
          >
            {isLogin
              ? "Don't have an account? Register"
              : "Already have an account? Login"}
          </button>

        </div>

      </div>

    </div>
  );
}
