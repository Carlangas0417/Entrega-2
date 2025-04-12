package CatalogoAtracciones;

import java.util.List;

import GestionEmpleados.Empleado;

public class Cultural extends Atraccion{
	public Cultural(String nombre, String ubicacion, int cupoMax, int empleadosMin, String nivelExclusividad,
			List<String> disponibleClima, List<Empleado> empleados) {
		super(nombre, ubicacion, cupoMax, empleadosMin, nivelExclusividad, disponibleClima, empleados);
	}
}
