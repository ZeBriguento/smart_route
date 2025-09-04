import { apiFetch } from "./api";
import { Transport } from "@/types/transport";

export async function listTransports(): Promise<Transport[]> {
  return apiFetch<Transport[]>("/itineraries/transports/");
}
