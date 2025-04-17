package GestionEmpleados;

import java.util.ArrayList;
import java.util.List;


public class Operador extends Empleado{
	
	private boolean riesgoAlto;
	private List<Integer> atraccionesEntrenado;
	private int atraccionAsignada;
	
	public Operador(String nombre, String id, String password, String login, List<Turno> turnosAsignados,
			boolean riesgoAlto, List<Integer> atraccionesEntrenado, int atraccionAsignada) {
		super(nombre, id, password, login, turnosAsignados);
		this.atraccionAsignada = atraccionAsignada;
		this.riesgoAlto = riesgoAlto;
		this.atraccionesEntrenado = new ArrayList<>();
	}

	public void setRiesgoAlto(boolean riesgoAlto) {
		this.riesgoAlto = riesgoAlto;
	}

	public void setAtraccionesEntrenado(List<Integer> atraccionesEntrenado) {
		this.atraccionesEntrenado = atraccionesEntrenado;
	}

	public void setAtraccionAsignada(int atraccionAsignada) {
		this.atraccionAsignada = atraccionAsignada;
	}

	public boolean isRiesgoAlto() {
		return riesgoAlto;
	}

	public List<Integer> getAtraccionesEntrenado() {
		return atraccionesEntrenado;
	}
	
	public void anadirAtraccionEntrenado(int idAtraccion) {
		atraccionesEntrenado.add(idAtraccion);
	}

	public int getAtraccionAsignada() {
		return atraccionAsignada;
	}
	
	
	
}
