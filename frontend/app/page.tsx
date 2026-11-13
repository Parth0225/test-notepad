import Link from "next/link";

const pages = [{"route": "notes", "label": "Notes"}];

export default function Home() {
  return (
    <div>
      <h1 className="mb-4 text-2xl font-semibold">Notes Test</h1>
      <ul className="space-y-2">
        {pages.map((p) => (
          <li key={p.route}>
            <Link className="text-blue-700 underline" href={`/${p.route}`}>{p.label}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
