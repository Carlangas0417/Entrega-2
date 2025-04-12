package uniandes.dpoo.aerolinea.modelo.tarifas;

import uniandes.dpoo.aerolinea.modelo.Ruta;
import uniandes.dpoo.aerolinea.modelo.Vuelo;
import uniandes.dpoo.aerolinea.modelo.cliente.Cliente;

public class CalculadoraTarifasTemporadaAlta extends CalculadoraTarifas{

	protected final int COSTO_POR_KM = 1000;
	
	public int calcularCostoBase(Vuelo vuelo, Cliente cliente) {
		Ruta ruta = vuelo.getRuta();
		int distance = calcularDistanciaVuelo(ruta);
		int total = 0;
		total = this.COSTO_POR_KM * distance;
		return total;
	}
	public double calcularPorcentajeDescuento(Cliente cliente) {
		return 0;
	}
}
