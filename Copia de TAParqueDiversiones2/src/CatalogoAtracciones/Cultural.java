package CatalogoAtracciones;

import java.io.Serializable;
import java.util.List;

import GestionEmpleados.Empleado;

public class Cultural extends Atraccion implements Serializable{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	public Cultural(String nombre, String ubicacion, int cupoMax, int empleadosMin, String nivelExclusividad,
			List<String> disponibleClima, List<Empleado> empleados) {
		super(nombre, ubicacion, cupoMax, empleadosMin, nivelExclusividad, disponibleClima, empleados);
	}
	@Override
	public void mostrarAtraccion() {
	    System.out.println("Detalles de la atracción Mecánica:");
	    System.out.println("Nombre: " + getNombre());
	    System.out.println("Ubicación: " + getUbicacion());
	    System.out.println("Cupo Máximo: " + getCupoMax());
	    System.out.println("Empleados Mínimos: " + getEmpleadosMin());
	    System.out.println("Nivel de Exclusividad: " + getNivelExclusividad());
	    System.out.println("Clima Disponible: " + getDisponibleClima());
	    if (getDisponibleClima() != null && !getDisponibleClima().isEmpty()) {
	        System.out.println("Climas: ");
	        for (String contraindicacion : getDisponibleClima()) {
	            System.out.println("- " + contraindicacion);
	        }
	    } else {
	        System.out.println("No hay contraindicaciones.");
	    }
	}
	
	public void mostrarAtraccionEmpleados() {
	    mostrarAtraccion();
	    if (getEmpleados() != null && !getEmpleados().isEmpty()) {
	        System.out.println("Empleados asginados: ");
	        for (Empleado empleado : getEmpleados()) {
	            System.out.println("- " + empleado);
	        }
	    } else {
	        System.out.println("No hay empleados asignados a esta atracción.");
	    }
	}
}
