"use client";

import { useState } from "react";
import { addNews } from "@/lib/news";

export default function NewsForm() {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  return (
    <div className="space-y-2">
      <input
        placeholder="News title"
        className="input"
        onChange={(e) => setTitle(e.target.value)}
      />

      <textarea
        placeholder="News content"
        className="input"
        onChange={(e) => setContent(e.target.value)}
      />

      <button
        onClick={() => addNews(title, content)}
        className="bg-green-600 px-4 py-2 rounded"
      >
        Publish News
      </button>
    </div>
  );
}
