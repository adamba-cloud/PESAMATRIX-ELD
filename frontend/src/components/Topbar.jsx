import { Bell, Search } from "lucide-react";

export default function Topbar() {
  return (
    <header className="flex items-center justify-between px-6 py-4 border-b border-gray-800 bg-[#0B1220]">
      
      {/* SEARCH BAR */}
      <div className="flex items-center gap-2 bg-gray-900 px-4 py-2 rounded-xl w-1/3">
        <Search size={18} className="text-gray-400" />
        <input
          placeholder="Search..."
          className="bg-transparent outline-none w-full text-sm"
        />
      </div>

      {/* RIGHT ICONS */}
      <div className="flex items-center gap-4">
        <Bell className="text-gray-300" />
        <div className="w-9 h-9 rounded-full bg-gradient-to-r from-purple-500 to-cyan-500" />
      </div>

    </header>
  );
}
