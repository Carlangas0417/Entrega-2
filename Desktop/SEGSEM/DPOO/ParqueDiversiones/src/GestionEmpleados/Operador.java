package GestionEmpleados;

import java.util.List;

import CatalogoAtracciones.Mecanica;

public class Operador extends Empleado{
	
	private boolean riesgoAlto;
	private List<Integer> atraccionesEntrenado;
	private Mecanica atraccionAsignada;
	
	public Operador(String nombre, String id, String password, String login, List<Turno> turnosAsignados,
			boolean riesgoAlto, List<Integer> atraccionesEntrenado, Mecanica atraccionAsignada) {
		super(nombre, id, password, login, turnosAsignados);
		this.atraccionAsignada = atraccionAsignada;
		this.riesgoAlto = riesgoAlto;
		this.atraccionesEntrenado = atraccionesEntrenado;
	}

	public void setRiesgoAlto(boolean riesgoAlto) {
		this.riesgoAlto = riesgoAlto;
	}

	public void setAtraccionesEntrenado(List<Integer> atraccionesEntrenado) {
		this.atraccionesEntrenado = atraccionesEntrenado;
	}

	public void setAtraccionAsignada(Mecanica atraccionAsignada) {
		this.atraccionAsignada = atraccionAsignada;
	}

	public boolean isRiesgoAlto() {
		return riesgoAlto;
	}

	public List<Integer> getAtraccionesEntrenado() {
		return atraccionesEntrenado;
	}

	public Mecanica getAtraccionAsignada() {
		return atraccionAsignada;
	}
	
	
	
}
