import { createClient } from "https://esm.sh/@supabase/supabase-js"

const supabaseUrl = "https://mfqhwwqqgubontkfatyd.supabase.co"

const supabaseAnonKey = "sb_publishable_T7CX34OQYp5H_nvdjKP0-Q_vDeMPCuA"

export const supabase = createClient(supabaseUrl, supabaseAnonKey)
