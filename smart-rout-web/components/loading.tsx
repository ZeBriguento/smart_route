// components/Loading.tsx
export default function Loading() {
  return (
   <div className="fixed inset-0 flex items-center justify-center bg-blue-500/90 animate-pulse z-50">
  <div className="flex flex-col items-center">
    <div className="w-12 h-12 border-4 border-white border-dashed rounded-full animate-spin"></div>
    <p className="mt-4 text-white font-medium">Carregando opções...</p>
  </div>
</div>

  );
}
