package CatalogoAtracciones;

import java.util.List;

import GestionEmpleados.Empleado;

public class Cultural extends Atraccion{
	public Cultural(String nombre, String ubicacion, int cupoMax, int empleadosMin, String nivelExclusividad,
			List<String> disponibleClima, List<Empleado> empleados) {
		super(nombre, ubicacion, cupoMax, empleadosMin, nivelExclusividad, disponibleClima, empleados);
	}
	
	public void mostrarCultural() {
	    System.out.println("Detalles de la atracción Mecánica:");
	    System.out.println("Nombre: " + getNombre());
	    System.out.println("Ubicación: " + getUbicacion());
	    System.out.println("Cupo Máximo: " + getCupoMax());
	    System.out.println("Empleados Mínimos: " + getEmpleadosMin());
	    System.out.println("Nivel de Exclusividad: " + getNivelExclusividad());
	    System.out.println("Clima Disponible: " + getDisponibleClima());
	    System.out.println("Empleados asignados: ");
	    List<Empleado> empleados = getEmpleados();
	    if (empleados != null) {
	    	for (int i = 0; i < empleados.size(); i++) {
		    	Empleado empleado = empleados.get(i);
				System.out.println("Empleado asignado: " + empleado.nombre + ".\n");
				System.out.println("Login del empleado asignado: " + empleado.getLogin() + ".\n");
			}
	    }
	    else {
	    	System.out.println("No hay ningún empleado asignado.");
	    }
	    
	}
}
