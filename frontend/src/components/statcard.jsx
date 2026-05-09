export default function StatCard({ title, value, color }) {
  return (
    <div className="p-4 bg-[#111827] rounded border border-gray-800 shadow">

      <h3 className="text-gray-400">{title}</h3>

      <p className={`text-2xl font-bold mt-2 text-${color || "cyan"}-400`}>
        {value}
      </p>

    </div>
  );
}
