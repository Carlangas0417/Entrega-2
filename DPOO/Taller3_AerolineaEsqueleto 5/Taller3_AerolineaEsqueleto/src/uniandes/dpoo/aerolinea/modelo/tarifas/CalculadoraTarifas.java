package uniandes.dpoo.aerolinea.modelo.tarifas;

import uniandes.dpoo.aerolinea.modelo.Aeropuerto;
import uniandes.dpoo.aerolinea.modelo.Ruta;
import uniandes.dpoo.aerolinea.modelo.Vuelo;
import uniandes.dpoo.aerolinea.modelo.cliente.Cliente;

public abstract class CalculadoraTarifas {
	
	private static final double IMPUESTO = 0.28; 
	
	public int calcularTarifa(Vuelo vuelo, Cliente cliente) {
		double desc = calcularPorcentajeDescuento(cliente);
		int base = calcularCostoBase(vuelo, cliente);
		int imp = calcularValorImpuestos(base);
		return (int)((base-desc)+imp);
	}
	
	protected abstract int calcularCostoBase(Vuelo vuelo, Cliente cliente);
	
	protected abstract double calcularPorcentajeDescuento(Cliente cliente);
	
	protected int calcularDistanciaVuelo(Ruta ruta) {
		Aeropuerto origen = ruta.getOrigen();
		Aeropuerto destino = ruta.getDestino();
		int distance = Aeropuerto.calcularDistancia(origen, destino);
		return distance;
	}
	
	protected int calcularValorImpuestos(int CostoBase) {
		return (int) (CostoBase*IMPUESTO);
	}
	
}
