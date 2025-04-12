package uniandes.dpoo.aerolinea.modelo;

import java.util.Collection;

import uniandes.dpoo.aerolinea.exceptions.VueloSobrevendidoException;
import uniandes.dpoo.aerolinea.modelo.cliente.Cliente;
import uniandes.dpoo.aerolinea.modelo.tarifas.CalculadoraTarifas;
import uniandes.dpoo.aerolinea.tiquetes.GeneradorTiquetes;
import uniandes.dpoo.aerolinea.tiquetes.Tiquete;

public class Vuelo {

		private String fecha;
		private Avion avion;
		private Ruta ruta;
		private Collection<Tiquete> tiquetes;
		
		public Vuelo(String fecha, Avion avion, Ruta ruta) {
			super();
			this.fecha = fecha;
			this.avion = avion;
			this.ruta = ruta;
		}


		public String getFecha() {
			return fecha;
		}


		public Avion getAvion() {
			return avion;
		}


		public Ruta getRuta() {
			return ruta;
		}
		
		public Collection<Tiquete> getTiquetes(){
			return this.tiquetes;
		}
		
		public int venderTiquetes(Cliente pasajero, CalculadoraTarifas calculadora, int cantidadTiquetes) 
		        throws VueloSobrevendidoException {
		    
		    int tarifaAplicada = calculadora.calcularTarifa(this, pasajero);
		    int total = 0;

		    for (int i = 0; i < cantidadTiquetes; i++) {
		        Tiquete nuevoTiquete = GeneradorTiquetes.generarTiquete(this, pasajero, tarifaAplicada);
		        boolean esValido = false;

		        while (!esValido) {
		            if (!GeneradorTiquetes.validarTiquete(nuevoTiquete.getCodigo())) {
		                GeneradorTiquetes.registrarTiquete(nuevoTiquete);
		                tiquetes.add(nuevoTiquete);
		                pasajero.agregarTiquete(nuevoTiquete);
		                esValido = true;
		            } else {
		                nuevoTiquete = GeneradorTiquetes.generarTiquete(this, pasajero, tarifaAplicada);
		            }
		        }
		        total += nuevoTiquete.getTarifa();
		    }

		    if (tiquetes.size() >= avion.getCapacidad()) {
		        throw new VueloSobrevendidoException(this);
		    }

		    return total;
		}

		
		
		@Override
		public boolean equals(Object obj) {
			return this == obj;
		}
		
		
}
