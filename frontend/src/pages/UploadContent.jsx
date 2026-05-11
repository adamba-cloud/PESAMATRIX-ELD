export default function UploadContent() {
  return (
    <div>

      <h1 className="text-2xl font-bold mb-6">Upload Content</h1>

      <div className="bg-[#111827] p-6 rounded-xl border border-gray-800 space-y-4">

        <input
          placeholder="Paste Image/Video Link"
          className="w-full p-3 bg-[#0B0F19] border border-gray-700 rounded"
        />

        <textarea
          placeholder="Description"
          className="w-full p-3 bg-[#0B0F19] border border-gray-700 rounded"
        />

        <button className="bg-cyan-500 text-black px-6 py-2 rounded">
          Upload
        </button>

      </div>

    </div>
  );
}
