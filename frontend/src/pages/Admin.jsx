export default function Admin() {
  return (
    <div>

      <h1 className="text-2xl font-bold mb-6">Admin Panel</h1>

      <div className="bg-[#111827] p-6 rounded-xl border border-gray-800 space-y-4">

        <input
          placeholder="Signal Title"
          className="w-full p-3 bg-[#0B0F19] border border-gray-700 rounded"
        />

        <input
          placeholder="Entry Price"
          className="w-full p-3 bg-[#0B0F19] border border-gray-700 rounded"
        />

        <input
          placeholder="TP / SL"
          className="w-full p-3 bg-[#0B0F19] border border-gray-700 rounded"
        />

        <button className="bg-cyan-500 text-black px-6 py-2 rounded">
          Publish Signal
        </button>

      </div>

    </div>
  );
}
