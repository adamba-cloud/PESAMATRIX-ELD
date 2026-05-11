import { supabase } from "./supabaseClient"

// 🔐 SIGN UP
export async function signUp(email, password) {
  const { data, error } = await supabase.auth.signUp({
    email,
    password,
  })

  return { data, error }
}

// 🔐 LOGIN
export async function signIn(email, password) {
  const { data, error } = await supabase.auth.signInWithPassword({
    email,
    password,
  })

  return { data, error }
}

// 🔐 LOGOUT
export async function signOut() {
  const { error } = await supabase.auth.signOut()
  return { error }
}

// 👤 GET CURRENT USER
export async function getUser() {
  const { data } = await supabase.auth.getUser()
  return data?.user
}

// 🔁 AUTH STATE LISTENER
export function onAuthChange(callback) {
  return supabase.auth.onAuthStateChange((event, session) => {
    callback(session?.user || null)
  })
}
