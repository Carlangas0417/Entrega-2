package uniandes.dpoo.aerolinea.modelo;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import uniandes.dpoo.aerolinea.exceptions.VueloSobrevendidoException;
import uniandes.dpoo.aerolinea.modelo.cliente.Cliente;
import uniandes.dpoo.aerolinea.tarifas.CalculadoraTarifas;
import uniandes.dpoo.aerolinea.tiquetes.GeneradorTiquetes;
import uniandes.dpoo.aerolinea.tiquetes.Tiquete;

public class Vuelo {

	private String fecha;
	private Ruta ruta;
	private Avion avion;
	private Map<String,Tiquete> tiquetes;
	
	public Vuelo( Ruta ruta, String fecha, Avion avion) {
		this.fecha = fecha;
		this.ruta = ruta;
		this.avion = avion;
		this.tiquetes = new HashMap<String,Tiquete>();
	}
	public String getFecha() {
		return fecha;
	}
	public Ruta getRuta() {
		return ruta;
	}
	public Avion getAvion() {
		return avion;
	}
	public ArrayList<Tiquete> getTiquetes() {
		ArrayList<Tiquete>listaTiquetes= new ArrayList<Tiquete>();
		for (String elemento: this.tiquetes.keySet()) {
			listaTiquetes.addLast(this.tiquetes.get(elemento));
		}
		return listaTiquetes;
	}
	
	public int venderTiquetes(Cliente cliente, CalculadoraTarifas calculadora, int cantidad) throws VueloSobrevendidoException {
		int tarifa = calculadora.calcularTarifa(this, cliente);
		int precioTotal = 0;
		for (int i=0; i<cantidad; i++ ) {
			Tiquete tiquete =GeneradorTiquetes.generarTiquete(this, cliente, tarifa);
			boolean valido = false;
			while (valido ==false){
			if (GeneradorTiquetes.validarTiquete(tiquete.getCodigo())!= true) {
				GeneradorTiquetes.registrarTiquete(tiquete);
				tiquetes.put(tiquete.getCodigo(), tiquete);
				cliente.agregarTiquete(tiquete);
				valido=true;
				}
			else {
				 tiquete = GeneradorTiquetes.generarTiquete(this, cliente, tarifa);
				}
			}
			precioTotal += tiquete.getTarifa();
		}
		if (tiquetes.size()>=avion.getCapacidad()) {
			throw new VueloSobrevendidoException(this);
		}
		else {
			return precioTotal;
		}
	}
	
	// TODO: Hacer VenderTiquetes y equals
}
