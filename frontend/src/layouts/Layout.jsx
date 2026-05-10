import Topbar from "../components/Topbar";
import SidebarItem from "../components/SidebarItem";

export default function Layout({ children }) {
  return (
    <div className="flex min-h-screen bg-[#0B1220] text-white">
      
      {/* SIDEBAR */}
      <aside className="w-64 hidden md:flex flex-col border-r border-gray-800 bg-[#0F172A]">
        
        <div className="p-6 text-xl font-bold tracking-wide">
          TradeDash
        </div>

        <nav className="flex-1 px-4 space-y-2">
          <SidebarItem label="Dashboard" />
          <SidebarItem label="Signals" />
          <SidebarItem label="Analytics" />
          <SidebarItem label="Payments" />
          <SidebarItem label="Settings" />
        </nav>

        <div className="p-4 border-t border-gray-800">
          <div className="p-4 rounded-xl bg-gradient-to-r from-purple-600 to-cyan-500 text-sm">
            Upgrade to Pro 🚀
          </div>
        </div>

      </aside>

      {/* MAIN AREA */}
      <div className="flex-1 flex flex-col">
        <Topbar />

        <main className="flex-1 p-6 md:p-10 overflow-y-auto">
          {children}
        </main>
      </div>

    </div>
  );
}
