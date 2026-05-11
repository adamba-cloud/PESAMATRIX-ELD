"use client";

import { useState } from "react";
import { uploadFile, saveContent } from "@/lib/uploads";

export default function UploadContent() {
  const [progress, setProgress] = useState(0);
  const [file, setFile] = useState<File | null>(null);

  const handleUpload = async () => {
    if (!file) return;

    const url = await uploadFile(file, setProgress);

    await saveContent({
      type: file.type.startsWith("video") ? "video" : "image",
      url,
    });

    alert("Upload complete");
  };

  return (
    <div className="space-y-3">
      <input
        type="file"
        onChange={(e) => setFile(e.target.files?.[0] || null)}
      />

      <button onClick={handleUpload} className="bg-blue-600 px-4 py-2 rounded">
        Upload
      </button>

      {progress > 0 && (
        <div className="w-full bg-gray-700 h-2 rounded">
          <div
            className="bg-green-500 h-2"
            style={{ width: `${progress}%` }}
          />
        </div>
      )}
    </div>
  );
}
