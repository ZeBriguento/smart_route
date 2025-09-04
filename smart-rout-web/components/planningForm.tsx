"use client";

import { useState, useEffect } from "react";
import { listPreferencesController } from "@/controllers/preferenceController";
import { listTransportsController } from "@/controllers/transportController";
import Loading from "@/components/loading";

type Props = {
  onSubmit: (
    days: number,
    budget: number,
    preferences: string[],
    transport_type: string
  ) => void;
};

type Preference = {
  id: number;
  preference_type: string;
};

type Transport = {
  id: number;
  name: string;
};

export default function PlanningForm({ onSubmit }: Props) {
  const [days, setDays] = useState(1);
  const [budget, setBudget] = useState(100);
  const [preferences, setPreferences] = useState<string[]>([]);
  const [transport_type, setTransportType] = useState("bus");

  const [availablePreferences, setAvailablePreferences] = useState<Preference[]>([]);
  const [availableTransports, setAvailableTransports] = useState<Transport[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      try {
        const prefs = await listPreferencesController();
        const transports = await listTransportsController();

        setAvailablePreferences(prefs);
        setAvailableTransports(transports);
      } catch (err) {
        console.error("Erro ao carregar dados do backend:", err);
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, []);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(days, budget, preferences, transport_type);
  };
if (loading) return <Loading />;
  return (
    <form onSubmit={handleSubmit} className="space-y-4 p-4 bg-gray-100 rounded-lg">
      <h2 className="text-xl font-bold">Planeje a sua viagem</h2>

      <div>
        <label>Dias disponíveis</label>
        <input
          type="number"
          value={days}
          onChange={(e) => setDays(Number(e.target.value))}
          className="w-full border p-2 rounded"
        />
      </div>

      <div>
        <label>Orçamento (Kz)</label>
        <input
          type="number"
          value={budget}
          onChange={(e) => setBudget(Number(e.target.value))}
          className="w-full border p-2 rounded"
        />
      </div>

      <div>
        <label>Preferências</label>
        <select
          multiple
          value={preferences}
          onChange={(e) =>
            setPreferences(Array.from(e.target.selectedOptions, (opt) => opt.value))
          }
          className="w-full border p-2 rounded"
        >
          {availablePreferences.map((pref) => (
            <option key={pref.id} value={pref.preference_type}>
              {pref.preference_type}
            </option>
          ))}
        </select>
      </div>

      <div>
        <label>Transporte</label>
        <select
          value={transport_type}
          onChange={(e) => setTransportType(e.target.value)}
          className="w-full border p-2 rounded"
        >
          {availableTransports.map((t) => (
            <option key={t.id} value={t.name}>
              {t.name}
            </option>
          ))}
        </select>
      </div>

      <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">
        Gerar Roteiro
      </button>
    </form>
  );
}
