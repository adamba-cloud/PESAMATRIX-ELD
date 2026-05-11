import React, { useEffect, useState } from "react"
import { supabase } from "../supabaseClient"
import { getUser } from "../auth"

export default function ChatBox() {
  const [messages, setMessages] = useState([])
  const [text, setText] = useState("")
  const [user, setUser] = useState(null)

  // Load user
  useEffect(() => {
    async function loadUser() {
      const u = await getUser()
      setUser(u)
    }
    loadUser()
  }, [])

  // Load messages
  useEffect(() => {
    fetchMessages()

    const channel = supabase
      .channel("realtime chat")
      .on(
        "postgres_changes",
        { event: "*", schema: "public", table: "messages" },
        () => fetchMessages()
      )
      .subscribe()

    return () => supabase.removeChannel(channel)
  }, [])

  async function fetchMessages() {
    const { data } = await supabase
      .from("messages")
      .select("*")
      .order("created_at", { ascending: true })

    setMessages(data || [])
  }

  async function sendMessage() {
    if (!text || !user) return

    await supabase.from("messages").insert([
      {
        user_id: user.id,
        message: text,
      },
    ])

    setText("")
  }

  return (
    <div style={{ border: "1px solid #ccc", padding: "10px" }}>
      <h3>Live Chat</h3>

      <div style={{ height: "200px", overflowY: "auto" }}>
        {messages.map((m) => (
          <div key={m.id}>
            <b>{m.user_id}:</b> {m.message}
          </div>
        ))}
      </div>

      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Type message..."
      />

      <button onClick={sendMessage}>Send</button>
    </div>
  )
}
