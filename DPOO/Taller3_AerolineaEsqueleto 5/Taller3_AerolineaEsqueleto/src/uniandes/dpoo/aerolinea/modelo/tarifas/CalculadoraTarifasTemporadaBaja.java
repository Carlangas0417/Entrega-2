package uniandes.dpoo.aerolinea.modelo.tarifas;

import uniandes.dpoo.aerolinea.modelo.Ruta;
import uniandes.dpoo.aerolinea.modelo.Vuelo;
import uniandes.dpoo.aerolinea.modelo.cliente.Cliente;
import uniandes.dpoo.aerolinea.modelo.cliente.ClienteCorporativo;

public class CalculadoraTarifasTemporadaBaja extends CalculadoraTarifas
{

	protected final int COSTO_POR_KM_NATURAL = 600;
	protected final int COSTO_POR_KM_CORPORATIVO = 900;
	protected final double DESCUENTO_PEQ = 0.02;
	protected final double DESCUENTO_MEDIANAS = 0.1;
	protected final double DESCUENTO_GRANDES = 0.2;
	
	public int calcularCostoBase(Vuelo vuelo, Cliente cliente) {
		Ruta ruta = vuelo.getRuta();
		int distance = calcularDistanciaVuelo(ruta);
		int total = 0;
		if (cliente.getTipoCliente().equals("Natural") ){
			total = this.COSTO_POR_KM_NATURAL * distance;
			}
		else if(cliente.getTipoCliente().equals("Corporativo")){
			total = this.COSTO_POR_KM_CORPORATIVO * distance;
		}
		
		return total;
		}
	public double calcularPorcentajeDescuento(Cliente cliente) {
		ClienteCorporativo cC = (ClienteCorporativo) cliente; 
		double el_retorno = 0.000;
		if (cliente.getTipoCliente().equals("Corporativo")) {
			int tamano = cC.getTamanoEmpresa();
			if (tamano == 1) {
				el_retorno = this.DESCUENTO_GRANDES;
			}
			else if (tamano == 2){
				el_retorno = this.DESCUENTO_MEDIANAS;
			}
			else {
				el_retorno = this.DESCUENTO_PEQ;
			}
		}
		return el_retorno;
	}
}

