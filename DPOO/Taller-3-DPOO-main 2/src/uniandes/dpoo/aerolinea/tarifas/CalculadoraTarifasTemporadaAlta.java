package uniandes.dpoo.aerolinea.tarifas;

import uniandes.dpoo.aerolinea.modelo.Aeropuerto;
import uniandes.dpoo.aerolinea.modelo.Vuelo;
import uniandes.dpoo.aerolinea.modelo.cliente.Cliente;

public class CalculadoraTarifasTemporadaAlta extends CalculadoraTarifas {
	public final int COSTO_POR_KM = 1000;
	public CalculadoraTarifasTemporadaAlta() {
		super();
	}
	
	@Override
	public int calcularCostoBase(Vuelo vuelo, Cliente cliente) {
		// TODO Auto-generated method stub
		Aeropuerto origen = vuelo.getRuta().getOrigen();
		Aeropuerto destino = vuelo.getRuta().getDestino();
		return Aeropuerto.calcularDistancia(origen, destino)*COSTO_POR_KM;
		
	}

	@Override
	public double calcularPorcentajeDescuento(Cliente cliente) {
		return 0;
	}
	

}
