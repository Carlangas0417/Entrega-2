package uniandes.dpoo.aerolinea.persistencia;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;

import org.json.JSONArray;
import org.json.JSONObject;

import uniandes.dpoo.aerolinea.exceptions.InformacionInconsistenteException;
import uniandes.dpoo.aerolinea.modelo.Aerolinea;
import uniandes.dpoo.aerolinea.modelo.Aeropuerto;
import uniandes.dpoo.aerolinea.modelo.Avion;
import uniandes.dpoo.aerolinea.modelo.Ruta;
import uniandes.dpoo.aerolinea.modelo.Vuelo;

/**
 * Esta clase no está implementada - y no debería implementarse como parte del
 * taller.
 * 
 * Su objetivo es sólo ilustrar que podría haber varias implementaciones de la
 * misma interfaz, y que durante la ejecución alguien podría decidir cuál de
 * estas implementaciones
 * usar.
 */
public class PersistenciaAerolineaJson implements IPersistenciaAerolinea {
	private static final String NOMBRE_AVION = "nombre";
	private static final String CAPACIDAD_AVION = "capacidad";

	@Override
	public void cargarAerolinea(String archivo, Aerolinea aerolinea)
			throws IOException, InformacionInconsistenteException {
		String jsonCompleto = new String(Files.readAllBytes(new File(archivo).toPath()));
		JSONObject raiz = new JSONObject(jsonCompleto);
		cargarAvion(aerolinea, raiz.getJSONArray("aviones"));
		cargarAeropuerto(aerolinea, raiz.getJSONArray("aeropuertos"));
		cargarRuta(aerolinea, raiz.getJSONArray("rutas"));
		cargarVuelo(aerolinea, raiz.getJSONArray("vuelos"));
	}

	private void cargarAvion(Aerolinea aerolinea, JSONArray jAvion) {
		int numClientes = jAvion.length();
		for (int i = 0; i < numClientes; i++) {
			JSONObject avion = jAvion.getJSONObject(i);
			String nombreAvion = avion.getString("nombre");
			int capacidad = avion.getInt("capacidad");
			aerolinea.agregarAvion(new Avion(nombreAvion, capacidad));
		}
	}

	private void cargarAeropuerto(Aerolinea aerolinea, JSONArray jAeropuerto) {
		int numAeropuertos = jAeropuerto.length();
		for (int i = 0; i < numAeropuertos; i++) {
			JSONObject aeropuerto = jAeropuerto.getJSONObject(i);
			String nombre = aeropuerto.getString("nombre");
			String codigo = aeropuerto.getString("codigo");
			String nombreCiudad = aeropuerto.getString("nombreCiudad");
			double latitud = aeropuerto.getDouble("latitud");
			double longitud = aeropuerto.getDouble("longitud");
			aerolinea.agregarAeropuerto(new Aeropuerto(nombre, codigo, nombreCiudad, latitud, longitud));
		}
	}

	private void cargarRuta(Aerolinea aerolinea, JSONArray jRuta) {
		int numRutas = jRuta.length();
		for (int i = 0; i < numRutas; i++) {
			JSONObject ruta = jRuta.getJSONObject(i);
			String codigoRuta = ruta.getString("codigoRuta");
			String horaSalida = ruta.getString("horaSalida");
			String horaLlegada = ruta.getString("horaLlegada");
			String origen = ruta.getString("origen");
			String destino = ruta.getString("destino");
			Aeropuerto aeropuertoOrigen = aerolinea.getAeropuerto(origen);
			Aeropuerto aeropuertoDestino = aerolinea.getAeropuerto(destino);
			aerolinea.agregarRuta(new Ruta(aeropuertoOrigen, aeropuertoDestino, horaSalida, horaLlegada, codigoRuta));
		}
	}

	private void cargarVuelo(Aerolinea aerolinea, JSONArray jVuelo) {
		int numVuelos = jVuelo.length();
		for (int i = 0; i < numVuelos; i++) {
			JSONObject vuelo = jVuelo.getJSONObject(i);
			String fecha = vuelo.getString("fecha");
			String codigoRuta = vuelo.getString("codigoRuta");
			String avion = vuelo.getString("avion");
			Ruta ruta = aerolinea.getRuta(codigoRuta);
			try {
				aerolinea.programarVuelo(fecha, codigoRuta, avion);
			} catch (Exception e) {
				System.out.println(e.getMessage());
			}
		}
	}

	@Override
	public void salvarAerolinea(String archivo, Aerolinea aerolinea) throws IOException {

		JSONObject jobject = new JSONObject();
		salvarAeropuerto(jobject, aerolinea);
		salvarAvion(jobject, aerolinea);
		salvarRuta(jobject, aerolinea);
		salvarVuelo(jobject, aerolinea);
		PrintWriter pw = new PrintWriter(archivo);
		jobject.write(pw, 2, 0);
		pw.close();
		// No está implementado (y no es necesario para el taller)
	}

	private void salvarAvion(JSONObject jobject, Aerolinea aerolinea) {
		JSONArray jAviones = new JSONArray();
		for (Avion avion : aerolinea.getAviones()) {
			JSONObject jAvion = new JSONObject();
			jAvion.put(NOMBRE_AVION, avion.getNombre());
			jAvion.put(CAPACIDAD_AVION, avion.getCapacidad());
			jAviones.put(jAvion);
		}
		jobject.put("aviones", jAviones);

	}

	private void salvarVuelo(JSONObject jobject, Aerolinea aerolinea) {
		JSONArray jVuelos = new JSONArray();
		for (Vuelo vuelo : aerolinea.getVuelos()) {
			JSONObject jVuelo = new JSONObject();
			jVuelo.put("fecha", vuelo.getFecha());
			jVuelo.put("codigoRuta", vuelo.getRuta().getCodigoRuta());
			jVuelo.put("avion", vuelo.getAvion().getNombre());
			jVuelos.put(jVuelo);
		}
		jobject.put("vuelos", jVuelos);
	}

	private void salvarRuta(JSONObject jobject, Aerolinea aerolinea) {
		JSONArray jRutas = new JSONArray();
		for (Ruta ruta : aerolinea.getRutas()) {
			JSONObject jRuta = new JSONObject();
			jRuta.put("horaSalida", ruta.getHoraSalida());
			jRuta.put("horaLlegada", ruta.getHoraLlegada());
			jRuta.put("codigoRuta", ruta.getCodigoRuta());
			jRuta.put("origen", ruta.getOrigen().getCodigo());
			jRuta.put("destino", ruta.getDestino().getCodigo());
			jRutas.put(jRuta);
		}
		jobject.put("rutas", jRutas);
	}

	private void salvarAeropuerto(JSONObject jobject, Aerolinea aerolinea) {
		JSONArray jAeropuertos = new JSONArray();
		for (Aeropuerto aeropuerto : aerolinea.getAeropuertos()) {
			JSONObject jAeropuerto = new JSONObject();
			jAeropuerto.put("nombre", aeropuerto.getNombre());
			jAeropuerto.put("codigo", aeropuerto.getCodigo());
			jAeropuerto.put("nombreCiudad", aeropuerto.getNombreCiudad());
			jAeropuerto.put("latitud", aeropuerto.getLatitud());
			jAeropuerto.put("longitud", aeropuerto.getLongitud());
			jAeropuertos.put(jAeropuerto);
		}
		jobject.put("aeropuertos", jAeropuertos);
	}
}
