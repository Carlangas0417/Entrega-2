package CatalogoAtracciones;

import java.io.Serializable;
import java.util.List;

import GestionEmpleados.Empleado;

public class Cultural extends Atraccion implements Serializable {
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
	    System.out.println("ID: " + getID());
	    System.out.println("Cupo Máximo: " + getCupoMax());
	    System.out.println("Empleados Mínimos: " + getEmpleadosMin());
	    System.out.println("Nivel de Exclusividad: " + getNivelExclusividad());
	    if (getDisponibleClima() != null && !getDisponibleClima().isEmpty()) {
	        System.out.println("Climas disponibles: ");
	        for (String clima : getDisponibleClima()) {
	            System.out.println("- " + clima);
	        }
	    } else {
	        System.out.println("No hay climas en los que la atracción esté disponible.");
	    }
	    
	    
	}
}
