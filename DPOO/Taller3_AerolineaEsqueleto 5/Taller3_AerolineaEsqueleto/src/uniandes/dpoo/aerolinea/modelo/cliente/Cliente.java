package uniandes.dpoo.aerolinea.modelo.cliente;

import java.util.ArrayList;

import uniandes.dpoo.aerolinea.modelo.Vuelo;
import uniandes.dpoo.aerolinea.tiquetes.Tiquete;

public abstract class Cliente {
	private ArrayList<Tiquete> tiquetesUsados;
	
	private ArrayList<Tiquete> tiquetesSinUsar;

	public Cliente() {
		this.tiquetesUsados = new ArrayList<Tiquete>();
		this.tiquetesSinUsar = new ArrayList<Tiquete>();
	}
	
	public abstract String getTipoCliente();
	public abstract String getIdentificador();
	public void agregarTiquete(Tiquete tiquete) {
		tiquetesSinUsar.add(tiquete);
	}
	
	public void usarTiquetes(Vuelo vuelo) {
		for (Tiquete tiquete : tiquetesSinUsar) {
			if (tiquete.getVuelo().equals(vuelo)){
				tiquete.marcarComoUsado();
				tiquetesUsados.add(tiquete);
				tiquetesSinUsar.remove(tiquete);
				
			}
		}
	}
	
	public int calcularValorTotalTiquetes() {
		int total = 0;
		for (Tiquete tiquete : tiquetesSinUsar) {
			total=tiquete.getTarifa() + total;
			}
		return total;
		}
	
}
