export default function StatCard({ title, value }) {
  return (
    <div className="bg-[#111827] border border-gray-800 rounded-lg p-5 hover:border-cyan-500 transition duration-200">

      <p className="text-gray-400 text-sm">
        {title}
      </p>

      <h2 className="text-2xl font-bold text-white mt-2">
        {value}
      </h2>

    </div>
  );
}
