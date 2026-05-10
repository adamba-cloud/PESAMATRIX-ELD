import Layout from "../layouts/Layout";

export default function Dashboard() {
  return (
    <Layout>
      <div className="space-y-6">
        
        <h1 className="text-3xl font-bold tracking-wide">
          Dashboard Overview
        </h1>

        {/* STATS GRID */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <Card title="Total Profit" value="$12,430" />
          <Card title="Win Rate" value="78%" />
          <Card title="Active Signals" value="14" />
          <Card title="Subscribers" value="1,240" />
        </div>

      </div>
    </Layout>
  );
}

/* CARD COMPONENT (local for now) */
function Card({ title, value }) {
  return (
    <div className="p-5 rounded-2xl bg-[#111827] border border-gray-800 shadow-lg hover:scale-[1.02] transition">
      <div className="text-gray-400 text-sm">{title}</div>
      <div className="text-2xl font-bold mt-2">{value}</div>
    </div>
  );
}
