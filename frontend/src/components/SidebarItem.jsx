export default function SidebarItem({ label }) {
  return (
    <div className="px-4 py-3 rounded-xl text-gray-300 hover:bg-gray-800 hover:text-white cursor-pointer transition">
      {label}
    </div>
  );
}
