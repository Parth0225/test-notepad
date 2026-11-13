"use client";
import { useEffect, useState } from "react";
import { api } from "@/lib/api";

export default function Page() {
  const [items, setItems] = useState<{ id: number; title: string }[]>([]);
  useEffect(() => { api<{ id: number; title: string }[]>("/notes/").then(setItems); }, []);
  return <ul>{items.map((i) => <li key={i.id}>{i.title}</li>)}</ul>;
}
