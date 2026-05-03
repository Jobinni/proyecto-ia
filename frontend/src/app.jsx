import { useState } from 'react';

const TIPOS = [
  {
    value: 'procedimiento',
    label: '📋 Procedimiento',
    descripcion: 'Cómo realizar una tarea paso a paso',
    placeholder: 'Ej: ¿Cómo hago una unión a inglete correctamente?',
    color: 'green',
  },
  {
    value: 'seguridad',
    label: '🦺 Seguridad',
    descripcion: 'Normas y equipos de protección antes de una tarea',
    placeholder: 'Ej: ¿Qué protección necesito para usar la sierra circular?',
    color: 'yellow',
  },
  {
    value: 'material',
    label: '🪵 Material / Herramienta',
    descripcion: 'Identificar y entender materiales o herramientas del taller',
    placeholder: 'Ej: ¿Para qué sirve la cola PVA y cuándo se usa?',
    color: 'orange',
  },
];

function App() {
  const [consulta, setConsulta] = useState('');
  const [tipo, setTipo] = useState('procedimiento');
  const [resultado, setResultado] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const tipoActual = TIPOS.find(t => t.value === tipo);

  const handleConsultar = async () => {
    if (!consulta.trim()) return;

    setLoading(true);
    setError('');
    setResultado('');

    try {
      const response = await fetch('http://localhost:8000/api/v1/consultar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ consulta, tipo })
      });

      if (!response.ok) throw new Error('Error de conexión con el Backend de IA');

      const data = await response.json();
      setResultado(data.respuesta);
    } catch (err) {
      setError('Ocurrió un error al procesar la consulta. Asegúrate de que FastAPI y Ollama estén corriendo.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-amber-50 flex flex-col items-center p-6">

      {/* Header */}
      <header className="w-full max-w-3xl bg-green-900 text-white rounded-lg shadow-md p-6 mb-8 text-center">
        <h1 className="text-3xl font-bold flex justify-center items-center gap-3">
          🪵 Asistente de Capacitación — Carpintería IA
        </h1>
        <p className="mt-2 text-green-200">
          Consulta procedimientos, normas de seguridad y materiales del taller usando RAG
        </p>
      </header>

      <main className="w-full max-w-3xl bg-white rounded-lg shadow-md p-6 space-y-6">

        {/* Selector de tipo de consulta */}
        <div>
          <label className="block text-gray-700 font-bold mb-3">
            ¿Qué tipo de consulta es?
          </label>
          <div className="grid grid-cols-3 gap-3">
            {TIPOS.map(t => (
              <button
                key={t.value}
                onClick={() => { setTipo(t.value); setResultado(''); setError(''); }}
                className={`p-3 rounded-lg border-2 text-left transition text-sm ${
                  tipo === t.value
                    ? 'border-green-600 bg-green-50 font-bold'
                    : 'border-gray-200 hover:border-green-300'
                }`}
              >
                <div className="font-semibold">{t.label}</div>
                <div className="text-gray-500 text-xs mt-1">{t.descripcion}</div>
              </button>
            ))}
          </div>
        </div>

        {/* Área de consulta */}
        <div>
          <label className="block text-gray-700 font-bold mb-2">
            Ingresa tu consulta:
          </label>
          <textarea
            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none"
            rows="4"
            placeholder={tipoActual?.placeholder}
            value={consulta}
            onChange={(e) => setConsulta(e.target.value)}
          ></textarea>
        </div>

        {/* Botón */}
        <button
          onClick={handleConsultar}
          disabled={loading || !consulta}
          className={`w-full font-bold py-3 px-4 rounded-lg transition ${
            loading || !consulta
              ? 'bg-gray-400 cursor-not-allowed text-white'
              : 'bg-green-700 hover:bg-green-800 text-white shadow-lg'
          }`}
        >
          {loading ? 'Consultando documentos del taller...' : 'Consultar Asistente IA'}
        </button>

        {/* Error */}
        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative">
            {error}
          </div>
        )}

        {/* Resultado */}
        {resultado && (
          <div className="mt-4">
            <h2 className="text-xl font-bold text-gray-800 border-b-2 border-green-600 pb-2 mb-4">
              {tipoActual?.label} — Respuesta del Asistente:
            </h2>
            <div className="bg-green-50 p-5 rounded-lg border border-green-100 text-gray-800 leading-relaxed text-base whitespace-pre-line">
              {resultado}
            </div>
          </div>
        )}
      </main>

      <footer className="mt-6 text-gray-400 text-sm text-center">
        Sistema de Capacitación con IA y RAG — Empresa de Carpintería
      </footer>
    </div>
  );
}

export default App;
