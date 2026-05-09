export default function StatCard({ title, value }) {
  return (
    <div className="p-4 bg-[#111827] border border-gray-800 rounded text-white">

      <h3 className="text-gray-400">{title}</h3>

      <p className="text-2xl font-bold text-cyan-400 mt-2">
        {value}
      </p>

    </div>
  );
}
