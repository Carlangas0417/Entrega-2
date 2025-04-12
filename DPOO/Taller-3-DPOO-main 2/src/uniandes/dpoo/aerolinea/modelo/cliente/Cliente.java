package uniandes.dpoo.aerolinea.modelo.cliente;

import java.util.ArrayList;

import uniandes.dpoo.aerolinea.modelo.Vuelo;
import uniandes.dpoo.aerolinea.tiquetes.Tiquete;

public abstract class Cliente {
	protected ArrayList<Tiquete> tiquetesSinUsar;
	protected ArrayList<Tiquete> tiquetesUsados;
	public Cliente() {
		this.tiquetesSinUsar= new ArrayList<Tiquete>();
		this.tiquetesUsados = new ArrayList<Tiquete>();
	}	
	public abstract String getTipoCliente();
	public abstract String getIdentificador();
	public void agregarTiquete(Tiquete tiquete) {
		tiquetesSinUsar.add(tiquete);
	}
	public int calcularValorTiquetes() {
		int valorTotal =0;
		for (Tiquete tiquete : tiquetesSinUsar) {
			valorTotal=tiquete.getTarifa() + valorTotal;
		}
		//for (Tiquete tiquete : tiquetesUsados) {
		//	valorTotal+=tiquete.getTarifa();
		//}
		return valorTotal;
	}
	public void usarTiquetes(Vuelo vuelo) {
		for (Tiquete tiquete : tiquetesSinUsar) {
			if (tiquete.getVuelo().equals(vuelo)){
				tiquete.marcarComoUsado();
				tiquetesSinUsar.remove(tiquete);
				tiquetesUsados.add(tiquete);
			}
		}
	}
}
