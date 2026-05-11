export default function VIPSignals() {
  const isUnlocked = false; // later we connect code system

  return (
    <div>

      <h1 className="text-2xl font-bold mb-6">VIP Signals</h1>

      {!isUnlocked ? (
        <div className="bg-red-500/10 border border-red-500 p-6 rounded-xl">
          🔒 Access Denied — VIP Code Required
        </div>
      ) : (
        <div className="text-green-400">
          VIP content unlocked
        </div>
      )}

    </div>
  );
}
