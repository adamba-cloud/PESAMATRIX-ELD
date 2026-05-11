import "./globals.css";

export const metadata = {
  title: "PMX Signals",
  description: "Forex Signals Platform"
};

export default function RootLayout({
  children
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="bg-bg text-white">{children}</body>
    </html>
  );
}
