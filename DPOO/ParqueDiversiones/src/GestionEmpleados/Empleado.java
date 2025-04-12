package GestionEmpleados;

import java.util.List;

public class Empleado extends Usuario{
	
	protected List<Turno> turnosAsignados;

	public Empleado(String nombre, String id, String password, String login) {
		super(nombre, id, password, login);
	}
	
}
