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
  const [transport_type, setTransportType] = useState("Autocarro");

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
    <form
      onSubmit={handleSubmit}
      className="max-w-lg mx-auto space-y-6 p-6 bg-white rounded-2xl shadow-lg"
    >
      <div className="text-center">
        <h2 className="text-2xl font-bold text-gray-800">
          Planeje a sua viagem ✈️
        </h2>
        <p className="text-gray-500 mt-1">
          Preencha os detalhes abaixo para gerar seu roteiro personalizado.
        </p>
      </div>

      {/* Dias e Orçamento */}
      <div className="grid grid-cols-2 gap-4">
        <div>
          <label className="block text-gray-700 font-medium mb-1">
            Dias disponíveis
          </label>
          <input
            type="number"
            value={days}
            onChange={(e) => setDays(Number(e.target.value))}
            className="w-full border rounded-xl p-3 focus:ring-2 focus:ring-blue-400 outline-none shadow-sm"
          />
        </div>
        <div>
          <label className="block text-gray-700 font-medium mb-1">
            Orçamento (Kz)
          </label>
          <input
            type="number"
            value={budget}
            onChange={(e) => setBudget(Number(e.target.value))}
            className="w-full border rounded-xl p-3 focus:ring-2 focus:ring-blue-400 outline-none shadow-sm"
          />
        </div>
      </div>

      {/* Preferências */}
      <div>
        <label className="block text-gray-700 font-medium mb-1">
          Preferências
        </label>
        <select
          multiple
          value={preferences}
          onChange={(e) =>
            setPreferences(Array.from(e.target.selectedOptions, (opt) => opt.value))
          }
          className="w-full border rounded-xl p-3 h-32 focus:ring-2 focus:ring-blue-400 outline-none shadow-sm"
        >
          {availablePreferences.map((pref) => (
            <option key={pref.id} value={pref.preference_type}>
              {pref.preference_type}
            </option>
          ))}
        </select>
        <p className="text-xs text-gray-500 mt-1">
          Segure <kbd className="px-1 py-0.5 bg-gray-200 rounded">Ctrl</kbd> para selecionar várias opções
        </p>
      </div>

      {/* Transporte */}
      <div>
        <label className="block text-gray-700 font-medium mb-1">Transporte</label>
        <select
          value={transport_type}
          onChange={(e) => setTransportType(e.target.value)}
          className="w-full border rounded-xl p-3 focus:ring-2 focus:ring-blue-400 outline-none shadow-sm"
        >
          {availableTransports.map((t) => (
            <option key={t.id} value={t.name}>
              {t.name}
            </option>
          ))}
        </select>
      </div>

      {/* Botão */}
      <button
        type="submit"
        className="w-full bg-blue-500 hover:bg-blue-600 text-white font-semibold py-3 rounded-xl transition duration-300 shadow-md"
      >
        Gerar Roteiro 🚀
      </button>
    </form>
  );
}
