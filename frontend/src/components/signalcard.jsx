export default function SignalCard({ pair, type, entry, tp, sl }) {
  return (
    <div
      className={`p-4 rounded border text-white ${
        type === "BUY"
          ? "border-green-500 bg-green-900/20"
          : "border-red-500 bg-red-900/20"
      }`}
    >

      <h2 className="font-bold">
        {type} {pair}
      </h2>

      <p>Entry: {entry}</p>
      <p>TP: {tp}</p>
      <p>SL: {sl}</p>

    </div>
  );
}
