import { listTransports } from "@/services/transportService";
import { Transport } from "@/types/transport";

export async function listTransportsController(): Promise<Transport[]> {
  return listTransports();
}
